"""Locations of data, model weights and cached embeddings.

Everything large lives outside the git repository, in one folder chosen with
the ``NEO_DATA_DIR`` environment variable (default: ``~/neo-helper-data``).
"""

from __future__ import annotations

import os
from pathlib import Path

ENV_VAR = "NEO_DATA_DIR"
DEFAULT_DATA_DIR = Path.home() / "neo-helper-data"

# Sub-folders of the data folder and what they contain.
SUBDIRS = {
    "raw": "datasets exactly as downloaded",
    "registry": "common data registry (one row per image) and splits",
    "weights": "pre-trained backbone weights",
    "embeddings": "cached embeddings, one file per backbone and dataset",
    "mlruns": "MLflow experiment tracking",
}


def data_dir() -> Path:
    """Return the root data folder, without creating it."""
    value = os.environ.get(ENV_VAR, "").strip()
    return Path(value).expanduser() if value else DEFAULT_DATA_DIR


def subdir(name: str, create: bool = False) -> Path:
    """Return one of the known sub-folders, optionally creating it."""
    if name not in SUBDIRS:
        raise ValueError(f"Unknown data sub-folder '{name}'. Choose one of: {sorted(SUBDIRS)}")
    path = data_dir() / name
    if create:
        path.mkdir(parents=True, exist_ok=True)
    return path
