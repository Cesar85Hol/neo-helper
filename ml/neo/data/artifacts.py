"""Image artifacts measured directly on the pixels.

Some artifacts are easier to measure than to describe in words. The dark
border left by a round dermoscope (vignetting) is one: the four corners of the
picture are black. A text-image model confuses "black border" with a dark
lesion; counting dark pixels in the corners does not.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
from PIL import Image

CORNER_FRACTION = 0.12  # side of each corner square, as a share of the image side
DARK_LEVEL = 50  # grey level (0-255) below which a pixel counts as dark
DEFAULT_THRESHOLD = 0.05  # share of dark corner pixels above which the border is "present"


def dark_corner_share(image: Image.Image) -> float:
    """Share of dark pixels in the four corner squares of ``image`` (0 to 1)."""
    grey = np.asarray(image.convert("L").resize((100, 100), Image.BILINEAR))
    side = max(1, round(grey.shape[0] * CORNER_FRACTION))
    corners = np.concatenate(
        [
            grey[:side, :side].ravel(),
            grey[:side, -side:].ravel(),
            grey[-side:, :side].ravel(),
            grey[-side:, -side:].ravel(),
        ]
    )
    return float((corners < DARK_LEVEL).mean())


def dark_corner_shares(files: list[Path], workers: int = 8) -> np.ndarray:
    """``dark_corner_share`` for many image files."""

    def one(path: Path) -> float:
        with Image.open(path) as image:
            return dark_corner_share(image)

    with ThreadPoolExecutor(workers) as pool:
        return np.array(list(pool.map(one, files)), dtype=np.float32)
