"""Tests for the lesion-level split, the duplicate search and the chart helpers."""

import numpy as np
import pandas as pd
import pytest
from PIL import Image

from neo import plots
from neo.data import duplicates, ham10000, registry, split


def fake_registry(n_lesions: int = 400, seed: int = 0) -> pd.DataFrame:
    """A registry with 1-3 images per lesion and unbalanced classes."""
    rng = np.random.default_rng(seed)
    classes = rng.choice(["nv", "mel", "bkl", "df"], size=n_lesions, p=[0.6, 0.2, 0.15, 0.05])
    rows = []
    for number, diagnosis in enumerate(classes):
        for copy in range(rng.integers(1, 4)):
            rows.append(
                {
                    "lesion_id": f"L{number}",
                    "image_id": f"I{number}_{copy}",
                    "dx": diagnosis,
                    "dx_type": "histo",
                    "age": 50,
                    "sex": "female",
                    "localization": "back",
                    "dataset": "rosendahl",
                }
            )
    return ham10000.convert(pd.DataFrame(rows))


# --- split ---------------------------------------------------------------------


def test_no_lesion_is_in_two_parts():
    frame = fake_registry()
    parts = split.split_by_lesion(frame)
    assert (parts.groupby("lesion_id")["split"].nunique() == 1).all()
    assert set(parts["uid"]) == set(frame["uid"])


def test_split_fractions_are_close_to_70_15_15():
    parts = split.split_by_lesion(fake_registry())
    lesions = parts.drop_duplicates("lesion_id")["split"].value_counts(normalize=True)
    assert lesions["train"] == pytest.approx(0.70, abs=0.01)
    assert lesions["val"] == pytest.approx(0.15, abs=0.01)
    assert lesions["test"] == pytest.approx(0.15, abs=0.01)


def test_split_keeps_class_proportions():
    frame = fake_registry()
    parts = split.split_by_lesion(frame).merge(frame[["uid", "diagnosis"]], on="uid")
    lesions = parts.drop_duplicates("lesion_id")
    overall = lesions["diagnosis"].value_counts(normalize=True)
    for part in split.PARTS:
        inside = lesions.loc[lesions["split"] == part, "diagnosis"].value_counts(normalize=True)
        assert (inside - overall).abs().max() < 0.03


def test_split_is_reproducible_and_depends_on_the_seed():
    frame = fake_registry()
    first = split.split_by_lesion(frame, seed=1)
    assert first.equals(split.split_by_lesion(frame, seed=1))
    assert not first.equals(split.split_by_lesion(frame, seed=2))


def test_check_detects_a_leaking_lesion():
    frame = fake_registry()
    parts = split.split_by_lesion(frame)
    lesion = parts["lesion_id"].value_counts().index[0]  # a lesion with several images
    row = parts.index[parts["lesion_id"] == lesion][0]
    parts.loc[row, "split"] = "test" if parts.loc[row, "split"] != "test" else "train"
    with pytest.raises(split.SplitError, match="more than one part"):
        split.check(parts, frame)


def test_check_detects_a_missing_image():
    frame = fake_registry()
    parts = split.split_by_lesion(frame)
    with pytest.raises(split.SplitError, match="exactly once"):
        split.check(parts.iloc[1:], frame)


def test_bad_fractions_are_rejected():
    with pytest.raises(split.SplitError):
        split.split_by_lesion(fake_registry(), fractions=(0.7, 0.2, 0.2))


def test_published_split_is_not_overwritten(tmp_path, monkeypatch):
    monkeypatch.setattr(split, "SPLITS_DIR", tmp_path)
    parts = split.split_by_lesion(fake_registry())
    split.save(parts, "demo")
    with pytest.raises(split.SplitError, match="already exists"):
        split.save(parts, "demo")
    assert split.load("demo").equals(parts)


def test_published_ham10000_split_is_valid():
    """The split committed in ml/splits/ respects the rules (skipped until it exists)."""
    path = split.split_path("ham10000")
    if not path.is_file():
        pytest.skip("ml/splits/ham10000_lesion_v1.csv not created yet")
    parts = pd.read_csv(path)
    assert len(parts) == 10015 and parts["lesion_id"].nunique() == 7470
    assert (parts.groupby("lesion_id")["split"].nunique() == 1).all()
    assert set(parts["split"]) == set(split.PARTS)


# --- duplicates ----------------------------------------------------------------


def test_duplicates_are_found_and_classified(tmp_path):
    rng = np.random.default_rng(0)
    folder = tmp_path / "raw" / "ham10000" / "images"
    folder.mkdir(parents=True)
    base = rng.integers(0, 255, size=(90, 120, 3), dtype=np.uint8)
    other = rng.integers(0, 255, size=(90, 120, 3), dtype=np.uint8)
    pictures = {
        "A": base,  # original
        "B": base,  # identical file, same lesion
        "C": np.clip(base.astype(int) + 1, 0, 255).astype(np.uint8),  # re-saved, other lesion
        "D": other,  # unrelated
    }
    for name, pixels in pictures.items():
        Image.fromarray(pixels).save(folder / f"{name}.png")
    frame = registry.empty_frame(4)
    frame["uid"] = [f"ham10000/{n}" for n in pictures]
    frame["file"] = [f"raw/ham10000/images/{n}.png" for n in pictures]
    frame["lesion_id"] = ["L1", "L1", "L2", "L3"]
    frame["diagnosis"] = ["nv", "nv", "mel", "nv"]

    pairs = duplicates.find_pairs(frame, root=tmp_path)
    found = {
        (a.split("/")[1], b.split("/")[1]) for a, b in zip(pairs.uid_a, pairs.uid_b, strict=True)
    }
    assert found == {("A", "B"), ("A", "C"), ("B", "C")}
    counts = duplicates.summarise(pairs)
    assert counts == {
        "pairs": 3,
        "exact": 1,
        "same_lesion": 1,
        "across_lesions": 2,
        "across_diagnoses": 2,
    }


# --- charts --------------------------------------------------------------------


def test_charts_are_drawn_and_saved(tmp_path):
    counts = pd.Series({"nv": 6705, "mel": 1113, "df": 115})
    figure = plots.bar_counts(counts, "Images per class")
    written = plots.save(figure, tmp_path, "classes")
    assert [p.suffix for p in written] == [".svg", ".png"]
    assert all(p.stat().st_size > 1000 for p in written)

    table = pd.DataFrame({"histology": [10, 90], "follow_up": [90, 10]}, index=["nv", "mel"])
    plots.save(plots.stacked_share(table, "Label source"), tmp_path, "sources")
    assert (tmp_path / "sources.svg").is_file()


def test_too_many_series_are_rejected():
    table = pd.DataFrame(np.ones((2, 9)), index=["a", "b"])
    with pytest.raises(ValueError, match="At most"):
        plots.stacked_share(table, "Too many")


def test_share_chart_is_drawn(tmp_path):
    shares = pd.Series({"mel": 0.205, "nv": 0.061})
    sizes = pd.Series({"mel": 1113, "nv": 6705})
    plots.save(plots.bar_shares(shares, sizes, "Dark corners"), tmp_path, "shares")
    assert (tmp_path / "shares.png").stat().st_size > 1000
