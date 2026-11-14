"""Tests for the dataset catalogue, downloads, archive extraction and registry."""

import hashlib
import zipfile

import pandas as pd
import pytest

from neo import paths
from neo.data import ham10000, registry
from neo.data.cli import main
from neo.data.download import DownloadError, download_file, extract_zip, human_size, is_complete
from neo.data.sources import HAM10000, SOURCES, RemoteFile


@pytest.fixture
def data_dir(monkeypatch, tmp_path):
    """Point NEO_DATA_DIR to an empty temporary folder."""
    monkeypatch.setenv(paths.ENV_VAR, str(tmp_path / "data"))
    return tmp_path / "data"


def local_remote(tmp_path, content: bytes, name: str = "file.bin", md5: str | None = None):
    """A RemoteFile that points to a local file, so tests never touch the network."""
    origin = tmp_path / "origin" / name
    origin.parent.mkdir(parents=True, exist_ok=True)
    origin.write_bytes(content)
    return RemoteFile(name, origin.as_uri(), len(content), md5 or hashlib.md5(content).hexdigest())


def fake_metadata() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "lesion_id": ["HAM_1", "HAM_1", "HAM_2", "HAM_3"],
            "image_id": ["ISIC_1", "ISIC_2", "ISIC_3", "ISIC_4"],
            "dx": ["mel", "mel", "nv", "akiec"],
            "dx_type": ["histo", "histo", "follow_up", "consensus"],
            "age": [80.0, 80.0, None, 45.0],
            "sex": ["male", "male", "unknown", "female"],
            "localization": ["scalp", "scalp", "back", "face"],
            "dataset": ["vidir_modern", "vidir_modern", "rosendahl", "vienna_dias"],
        }
    )


# --- catalogue ---------------------------------------------------------------


def test_catalogue_entries_are_complete():
    for source in SOURCES.values():
        assert source.license and source.doi and source.files
        names = [f.name for f in source.files]
        assert len(names) == len(set(names))
        for remote in source.files:
            assert remote.url.startswith("https://")
            assert remote.size > 0 and len(remote.md5) == 32


def test_default_selection_is_the_core_group():
    assert {f.name for f in HAM10000.select()} == {
        "HAM10000_images_part_1.zip",
        "HAM10000_images_part_2.zip",
        "HAM10000_metadata.csv",
    }
    with pytest.raises(ValueError):
        HAM10000.select(["no-such-group"])


def test_human_size():
    assert human_size(512) == "512 B"
    assert human_size(1366522108) == "1.37 GB"


# --- download ----------------------------------------------------------------


def test_download_verifies_and_skips_second_time(tmp_path, capsys):
    remote = local_remote(tmp_path, b"dermoscopy" * 1000)
    folder = tmp_path / "dest"
    path = download_file(remote, folder)
    assert path.read_bytes() == b"dermoscopy" * 1000
    assert is_complete(remote, folder)
    download_file(remote, folder)
    assert "already there" in capsys.readouterr().out


def test_download_with_wrong_checksum_is_rejected(tmp_path):
    remote = local_remote(tmp_path, b"corrupted", md5="0" * 32)
    folder = tmp_path / "dest"
    with pytest.raises(DownloadError):
        download_file(remote, folder, verbose=False)
    assert list(folder.iterdir()) == []


def test_zip_extraction(tmp_path):
    archive = tmp_path / "ok.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("a.jpg", b"1")
        bundle.writestr("sub/b.jpg", b"2")
    assert extract_zip(archive, tmp_path / "out") == 2
    assert (tmp_path / "out" / "sub" / "b.jpg").read_bytes() == b"2"


def test_zip_with_path_outside_destination_is_rejected(tmp_path):
    archive = tmp_path / "bad.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("../escaped.txt", b"x")
    with pytest.raises(DownloadError):
        extract_zip(archive, tmp_path / "out")
    assert not (tmp_path / "escaped.txt").exists()


def test_dry_run_downloads_nothing(data_dir, monkeypatch, capsys):
    def fail(*args, **kwargs):
        raise AssertionError("a dry run must not download")

    monkeypatch.setattr("neo.data.cli.download_file", fail)
    assert main(["download", "ham10000"]) == 0
    out = capsys.readouterr().out
    assert "Dry run" in out and "CC BY-NC 4.0" in out
    assert not data_dir.exists()


# --- registry ----------------------------------------------------------------


def test_ham10000_conversion():
    frame = ham10000.convert(fake_metadata())
    registry.validate(frame)
    assert list(frame.columns) == list(registry.COLUMNS)
    assert frame["uid"].tolist()[0] == "ham10000/ISIC_1"
    assert frame["file"].tolist()[0] == "raw/ham10000/images/ISIC_1.jpg"
    assert frame["malignant"].tolist() == [True, True, False, True]
    assert frame["label_source"].tolist() == ["histology", "histology", "follow_up", "consensus"]
    assert frame["country"].tolist() == ["AT", "AT", "AU", "AT"]
    assert frame["lesion_id"].nunique() == 3
    assert (frame["license"] == "CC BY-NC 4.0").all()
    assert frame["patient_id"].isna().all() and frame["fitzpatrick"].isna().all()


def test_validation_reports_problems():
    frame = ham10000.convert(fake_metadata())
    broken = frame.copy()
    broken.loc[1, "uid"] = broken.loc[0, "uid"]
    broken.loc[2, "diagnosis"] = "freckle"
    broken.loc[3, "license"] = pd.NA
    with pytest.raises(registry.RegistryError) as error:
        registry.validate(broken)
    message = str(error.value)
    assert "uid" in message and "freckle" in message and "license" in message

    with pytest.raises(registry.RegistryError):
        registry.validate(frame.drop(columns=["license"]))


def test_malignant_must_agree_with_diagnosis():
    frame = ham10000.convert(fake_metadata())
    frame.loc[2, "malignant"] = True  # a nevus marked as malignant
    with pytest.raises(registry.RegistryError):
        registry.validate(frame)


def test_missing_image_files_are_detected(data_dir):
    frame = ham10000.convert(fake_metadata())
    with pytest.raises(registry.RegistryError, match="not found"):
        registry.validate(frame, check_files=True)


def test_build_registry_end_to_end(data_dir):
    """Small fake HAM10000 on disk: archives + metadata -> registry file."""
    folder = data_dir / "raw" / "ham10000"
    folder.mkdir(parents=True)
    metadata = fake_metadata()
    metadata.to_csv(folder / "HAM10000_metadata.csv", index=False)
    halves = (metadata["image_id"][:2], metadata["image_id"][2:])
    for name, ids in zip(ham10000.IMAGE_ARCHIVES, halves, strict=True):
        with zipfile.ZipFile(folder / name, "w") as bundle:
            for image_id in ids:
                bundle.writestr(f"{image_id}.jpg", b"jpeg")

    path = ham10000.build_registry()
    assert path == data_dir / "registry" / "ham10000.csv"
    loaded = registry.load("ham10000")
    assert len(loaded) == 4
    assert loaded["malignant"].tolist() == [True, True, False, True]
    assert len(registry.load()) == 4
