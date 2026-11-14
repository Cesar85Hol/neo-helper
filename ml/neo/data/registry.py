"""The common data registry: one row per image, the same columns for every dataset.

Each dataset has a small converter that turns its own metadata into this
format (see ``neo/data/ham10000.py``). Everything downstream (EDA, splits,
embeddings, evaluation by subgroup) reads only the registry.

Columns follow docs/05_scelte_e_pipeline.md §4.1, plus ``license`` and
``source`` recorded per image.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from neo import paths

# Column name -> meaning. The order is the order of the CSV file.
COLUMNS: dict[str, str] = {
    "uid": "unique identifier: '<source>/<image_id>'",
    "source": "dataset key, e.g. 'ham10000'",
    "image_id": "identifier given by the dataset authors",
    "file": "image path relative to the data folder (NEO_DATA_DIR)",
    "modality": "dermoscopic | clinical | smartphone",
    "diagnosis": "label in the common vocabulary (see DIAGNOSES)",
    "diagnosis_original": "label exactly as written in the source",
    "malignant": "True / False, derived from 'diagnosis' (see MALIGNANT)",
    "label_source": "histology | follow_up | consensus | confocal | single_expert | unknown",
    "lesion_id": "same value for all images of one lesion",
    "patient_id": "same value for all images of one patient",
    "centre": "acquisition centre or sub-collection",
    "country": "ISO 3166-1 alpha-2 country code of the centre",
    "age": "approximate age in years",
    "sex": "female | male | unknown",
    "site": "anatomical site, as written in the source",
    "fitzpatrick": "skin phototype 1-6",
    "fitzpatrick_method": "in_person | from_image | unknown",
    "ethnicity_self_reported": "self-reported ethnicity, never inferred",
    "artifacts": "comma-separated artifacts, filled by the audit (ink, ruler, ...)",
    "license": "licence of this image",
    "license_url": "link to the licence text",
    "source_doi": "DOI of the dataset release the image was taken from",
}

# Columns that must have a value on every row.
REQUIRED = ("uid", "source", "image_id", "file", "modality", "diagnosis", "license", "source_doi")

MODALITIES = ("dermoscopic", "clinical", "smartphone")

# Common label vocabulary: the seven HAM10000 classes. Datasets added later
# (package P5) extend it, e.g. with squamous cell carcinoma.
DIAGNOSES: dict[str, str] = {
    "akiec": "actinic keratosis / intraepithelial carcinoma (Bowen's disease)",
    "bcc": "basal cell carcinoma",
    "bkl": "benign keratosis (seborrheic keratosis, solar lentigo, lichen-planus-like keratosis)",
    "df": "dermatofibroma",
    "mel": "melanoma",
    "nv": "melanocytic nevus",
    "vasc": "vascular lesion",
}

# Classes counted as malignant for the malignancy score. 'akiec' is included
# as in Tschandl et al. 2020 (actinic keratoses are pre-malignant, Bowen's
# disease is carcinoma in situ).
MALIGNANT = frozenset({"akiec", "bcc", "mel"})

LABEL_SOURCES = ("histology", "follow_up", "consensus", "confocal", "single_expert", "unknown")


class RegistryError(ValueError):
    """The registry does not respect the common format."""


def empty_frame(n_rows: int = 0) -> pd.DataFrame:
    """A registry with all columns and ``n_rows`` empty rows."""
    return pd.DataFrame({name: [pd.NA] * n_rows for name in COLUMNS})


def validate(frame: pd.DataFrame, check_files: bool = False) -> None:
    """Raise ``RegistryError`` listing every problem found in ``frame``."""
    problems: list[str] = []

    if list(frame.columns) != list(COLUMNS):
        missing = [c for c in COLUMNS if c not in frame.columns]
        extra = [c for c in frame.columns if c not in COLUMNS]
        problems.append(f"columns differ from the schema (missing: {missing}, extra: {extra})")
        raise RegistryError("; ".join(problems))

    for name in REQUIRED:
        n_missing = int(frame[name].isna().sum())
        if n_missing:
            problems.append(f"'{name}' is empty on {n_missing} row(s)")

    duplicated = int(frame["uid"].duplicated().sum())
    if duplicated:
        problems.append(f"'uid' is repeated on {duplicated} row(s)")

    for name, allowed in (
        ("modality", MODALITIES),
        ("diagnosis", tuple(DIAGNOSES)),
        ("label_source", LABEL_SOURCES),
    ):
        values = frame[name].dropna()
        bad = sorted(set(values) - set(allowed))
        if bad:
            problems.append(f"'{name}' has unknown value(s) {bad}")

    expected_malignant = frame["diagnosis"].isin(MALIGNANT)
    known = frame["diagnosis"].notna()
    if not (frame.loc[known, "malignant"].astype(bool) == expected_malignant[known]).all():
        problems.append("'malignant' does not agree with 'diagnosis'")

    if check_files:
        root = paths.data_dir()
        absent = [f for f in frame["file"].dropna() if not (root / f).is_file()]
        if absent:
            problems.append(f"{len(absent)} image file(s) not found, e.g. {absent[0]}")

    if problems:
        raise RegistryError("; ".join(problems))


def registry_path(source: str) -> Path:
    return paths.subdir("registry") / f"{source}.csv"


def save(frame: pd.DataFrame, source: str) -> Path:
    """Validate and write the registry of one dataset. Returns the file path."""
    validate(frame)
    path = registry_path(source)
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False)
    return path


def load(source: str | None = None) -> pd.DataFrame:
    """Load the registry of one dataset, or of all datasets when ``source`` is None."""
    if source is not None:
        files = [registry_path(source)]
    else:
        files = sorted(paths.subdir("registry").glob("*.csv"))
    if not files or not all(f.is_file() for f in files):
        raise FileNotFoundError(
            f"No registry found in {paths.subdir('registry')}. "
            "Build it with: neo-data registry <dataset>"
        )
    frames = [pd.read_csv(f, dtype={"fitzpatrick": "Int64"}) for f in files]
    return pd.concat(frames, ignore_index=True)
