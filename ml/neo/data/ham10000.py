"""HAM10000: extract the archives and convert the metadata to the common registry.

Source: Tschandl, Rosendahl and Kittler, Scientific Data 2018,
Harvard Dataverse doi:10.7910/DVN/DBW86T. 10,015 dermoscopic images of
7,470 lesions in 7 classes.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from neo import paths
from neo.data import registry
from neo.data.download import extract_zip
from neo.data.sources import HAM10000

KEY = HAM10000.key
METADATA_FILE = "HAM10000_metadata.csv"
IMAGE_ARCHIVES = ("HAM10000_images_part_1.zip", "HAM10000_images_part_2.zip")
IMAGE_FOLDER = "images"

# 'dx_type' in the source -> 'label_source' in the registry.
LABEL_SOURCE = {
    "histo": "histology",
    "follow_up": "follow_up",
    "consensus": "consensus",
    "confocal": "confocal",
}

# 'dataset' in the source is the sub-collection. Rosendahl is the Queensland
# (Australia) practice; the others come from the Medical University of Vienna.
COUNTRY = {
    "rosendahl": "AU",
    "vidir_modern": "AT",
    "vidir_molemax": "AT",
    "vienna_dias": "AT",
}


def raw_folder() -> Path:
    return paths.subdir("raw") / KEY


def extract_images() -> int:
    """Extract the two image archives. Returns the number of image files."""
    folder = raw_folder()
    total = 0
    for name in IMAGE_ARCHIVES:
        archive = folder / name
        if not archive.is_file():
            raise FileNotFoundError(
                f"{archive} not found. Download it with: neo-data download {KEY} --yes"
            )
        total += extract_zip(archive, folder / IMAGE_FOLDER)
    return total


def convert(metadata: pd.DataFrame) -> pd.DataFrame:
    """Convert the HAM10000 metadata table to the common registry format."""
    out = registry.empty_frame(len(metadata))
    image_id = metadata["image_id"].astype(str).to_numpy()
    diagnosis = metadata["dx"].astype(str).to_numpy()

    out["uid"] = [f"{KEY}/{i}" for i in image_id]
    out["source"] = KEY
    out["image_id"] = image_id
    relative = Path("raw") / KEY / IMAGE_FOLDER
    out["file"] = [(relative / f"{i}.jpg").as_posix() for i in image_id]
    out["modality"] = "dermoscopic"
    out["diagnosis"] = diagnosis
    out["diagnosis_original"] = diagnosis
    out["malignant"] = [d in registry.MALIGNANT for d in diagnosis]
    out["label_source"] = metadata["dx_type"].map(LABEL_SOURCE).fillna("unknown").to_numpy()
    out["lesion_id"] = metadata["lesion_id"].to_numpy()
    # HAM10000 does not publish patient identifiers.
    out["centre"] = metadata["dataset"].to_numpy()
    out["country"] = metadata["dataset"].map(COUNTRY).to_numpy()
    out["age"] = pd.to_numeric(metadata["age"], errors="coerce").to_numpy()
    out["sex"] = metadata["sex"].fillna("unknown").to_numpy()
    out["site"] = metadata["localization"].to_numpy()
    # Skin phototype and ethnicity are not recorded in HAM10000.
    out["fitzpatrick_method"] = "unknown"
    out["license"] = HAM10000.license
    out["license_url"] = HAM10000.license_url
    out["source_doi"] = HAM10000.doi
    return out


def build_registry(check_files: bool = True) -> Path:
    """Extract the images, convert the metadata and save the registry."""
    metadata_path = raw_folder() / METADATA_FILE
    if not metadata_path.is_file():
        raise FileNotFoundError(
            f"{metadata_path} not found. Download it with: neo-data download {KEY} --yes"
        )
    if check_files:
        extract_images()
    frame = convert(pd.read_csv(metadata_path))
    registry.validate(frame, check_files=check_files)
    return registry.save(frame, KEY)
