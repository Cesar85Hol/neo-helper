"""Split a dataset into train / validation / test **by lesion**.

All images of one lesion go to the same part, so the model is never tested on
a lesion it has seen in training (CLEAR Derm items 10-12). The split is
stratified by diagnosis: each part keeps the class proportions.

The split is made once, saved in the repository (``ml/splits/``) and then only
read: results stay comparable across machines and library versions.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split

PARTS = ("train", "val", "test")
DEFAULT_FRACTIONS = (0.70, 0.15, 0.15)
DEFAULT_SEED = 2026
SPLIT_COLUMNS = ["uid", "lesion_id", "split"]

# ml/splits/, next to the package.
SPLITS_DIR = Path(__file__).resolve().parents[2] / "splits"


class SplitError(ValueError):
    """The split breaks one of its rules."""


def split_by_lesion(
    frame: pd.DataFrame,
    fractions: tuple[float, float, float] = DEFAULT_FRACTIONS,
    seed: int = DEFAULT_SEED,
) -> pd.DataFrame:
    """Assign every image of ``frame`` (a registry) to train, val or test."""
    if abs(sum(fractions) - 1.0) > 1e-9 or min(fractions) <= 0:
        raise SplitError(f"Fractions must be positive and sum to 1, got {fractions}")
    if frame["lesion_id"].isna().any():
        raise SplitError("Every image needs a lesion_id to be split by lesion")

    lesions = frame.groupby("lesion_id")["diagnosis"].agg(lambda s: s.mode().iloc[0])
    if (frame.groupby("lesion_id")["diagnosis"].nunique() > 1).any():
        raise SplitError("Some lesions have more than one diagnosis")

    _, val_fraction, test_fraction = fractions
    train_ids, rest_ids = train_test_split(
        lesions.index.to_numpy(),
        test_size=val_fraction + test_fraction,
        stratify=lesions.to_numpy(),
        random_state=seed,
    )
    rest = lesions.loc[rest_ids]
    val_ids, test_ids = train_test_split(
        rest.index.to_numpy(),
        test_size=test_fraction / (val_fraction + test_fraction),
        stratify=rest.to_numpy(),
        random_state=seed,
    )
    part_of = {lesion: "train" for lesion in train_ids}
    part_of.update({lesion: "val" for lesion in val_ids})
    part_of.update({lesion: "test" for lesion in test_ids})

    out = frame[["uid", "lesion_id"]].copy()
    out["split"] = out["lesion_id"].map(part_of)
    check(out, frame)
    return out.reset_index(drop=True)


def check(split: pd.DataFrame, frame: pd.DataFrame) -> None:
    """Raise ``SplitError`` if ``split`` is not a valid lesion-level split of ``frame``."""
    problems = []
    if list(split.columns) != SPLIT_COLUMNS:
        raise SplitError(f"Split columns must be {SPLIT_COLUMNS}, got {list(split.columns)}")
    if set(split["uid"]) != set(frame["uid"]) or split["uid"].duplicated().any():
        problems.append("the split does not contain every image exactly once")
    unknown = sorted(set(split["split"].dropna()) - set(PARTS))
    if unknown or split["split"].isna().any():
        problems.append(f"unknown or missing part names {unknown}")
    leaked = int((split.groupby("lesion_id")["split"].nunique() > 1).sum())
    if leaked:
        problems.append(f"{leaked} lesion(s) appear in more than one part")
    merged = split.merge(frame[["uid", "diagnosis"]], on="uid", how="left")
    for part in PARTS:
        missing = set(frame["diagnosis"]) - set(merged.loc[merged["split"] == part, "diagnosis"])
        if missing:
            problems.append(f"part '{part}' has no image of {sorted(missing)}")
    if problems:
        raise SplitError("; ".join(problems))


def split_path(source: str, version: str = "v1") -> Path:
    return SPLITS_DIR / f"{source}_lesion_{version}.csv"


def save(split: pd.DataFrame, source: str, version: str = "v1", overwrite: bool = False) -> Path:
    """Write the split to ``ml/splits/``. An existing split is never replaced by accident."""
    path = split_path(source, version)
    if path.exists() and not overwrite:
        raise SplitError(
            f"{path} already exists. A published split must not change: "
            "use a new version name, or pass overwrite=True on purpose."
        )
    path.parent.mkdir(parents=True, exist_ok=True)
    split.to_csv(path, index=False)
    return path


def load(source: str, version: str = "v1") -> pd.DataFrame:
    path = split_path(source, version)
    if not path.is_file():
        raise FileNotFoundError(f"{path} not found. Create it with: neo-data split {source}")
    return pd.read_csv(path)


def summary(split: pd.DataFrame, frame: pd.DataFrame) -> pd.DataFrame:
    """Images per diagnosis and part, with lesion and image totals."""
    merged = split.merge(frame[["uid", "diagnosis"]], on="uid")
    table = pd.crosstab(merged["diagnosis"], merged["split"])[list(PARTS)]
    table.loc["images"] = table.sum()
    table.loc["lesions"] = [merged.loc[merged["split"] == p, "lesion_id"].nunique() for p in PARTS]
    return table
