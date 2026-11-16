"""Find duplicate images inside a registry.

Two checks:

1. exact duplicates: files with the same MD5 checksum;
2. near duplicates: the same picture saved again (re-encoded, slightly
   resized). Each image is reduced to a 32x32 colour thumbnail and two images
   are a pair when their thumbnails differ, on average, by less than
   ``threshold`` grey levels (on the 0-255 scale).

A coarse perceptual hash (8x8 dHash) was tried first and rejected: dermoscopic
images all look like a centred blob, and it matched thousands of unrelated
images. The thumbnail difference keeps the colour and the position.

What matters for the split is a pair that links two *different* lesions:
those would leak between training and test.
"""

from __future__ import annotations

import hashlib
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

from neo import paths

THUMBNAIL = 32
DEFAULT_THRESHOLD = 3.0
PAIR_COLUMNS = ["uid_a", "uid_b", "difference", "exact", "same_lesion", "same_diagnosis"]


def _md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def _thumbnail(path: Path) -> np.ndarray:
    with Image.open(path) as image:
        small = image.convert("RGB").resize((THUMBNAIL, THUMBNAIL), Image.BILINEAR)
    return np.asarray(small, dtype=np.float32).ravel()


def find_pairs(
    frame: pd.DataFrame,
    threshold: float = DEFAULT_THRESHOLD,
    root: Path | None = None,
    workers: int = 8,
    chunk: int = 500,
) -> pd.DataFrame:
    """Return one row per pair of duplicate images found in ``frame``.

    ``frame`` is a registry; ``root`` is the data folder (default: NEO_DATA_DIR).
    """
    root = root or paths.data_dir()
    files = [root / f for f in frame["file"]]
    with ThreadPoolExecutor(workers) as pool:
        checksums = list(pool.map(_md5, files))
        thumbs = torch.from_numpy(np.stack(list(pool.map(_thumbnail, files))))

    uid = frame["uid"].to_numpy()
    lesion = frame["lesion_id"].to_numpy()
    diagnosis = frame["diagnosis"].to_numpy()

    rows = []
    for start in range(0, len(thumbs), chunk):
        # Mean absolute difference between every thumbnail of the chunk and all thumbnails.
        distance = torch.cdist(thumbs[start : start + chunk], thumbs, p=1) / thumbs.shape[1]
        first, second = torch.nonzero(distance < threshold, as_tuple=True)
        for a, b in zip((first + start).tolist(), second.tolist(), strict=True):
            if a < b:
                rows.append(
                    {
                        "uid_a": uid[a],
                        "uid_b": uid[b],
                        "difference": round(float(distance[a - start, b]), 3),
                        "exact": checksums[a] == checksums[b],
                        "same_lesion": lesion[a] == lesion[b],
                        "same_diagnosis": diagnosis[a] == diagnosis[b],
                    }
                )
    pairs = pd.DataFrame(rows, columns=PAIR_COLUMNS)
    return pairs.sort_values(["difference", "uid_a"]).reset_index(drop=True)


def summarise(pairs: pd.DataFrame) -> dict[str, int]:
    """Count the pairs by kind."""
    return {
        "pairs": len(pairs),
        "exact": int(pairs["exact"].sum()),
        "same_lesion": int(pairs["same_lesion"].sum()),
        "across_lesions": int((~pairs["same_lesion"].astype(bool)).sum()),
        "across_diagnoses": int((~pairs["same_diagnosis"].astype(bool)).sum()),
    }
