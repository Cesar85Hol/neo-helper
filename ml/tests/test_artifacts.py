"""Tests for the artifacts measured on the pixels."""

import numpy as np
from PIL import Image

from neo.data import artifacts


def round_dermoscope_image(radius: float) -> Image.Image:
    """A light picture seen through a round opening: black outside the circle."""
    y, x = np.mgrid[-1:1:200j, -1:1:200j]
    pixels = np.where(x**2 + y**2 <= radius**2, 200, 0).astype(np.uint8)
    return Image.fromarray(np.stack([pixels] * 3, axis=-1))


def test_full_frame_image_has_no_dark_corners():
    plain = Image.new("RGB", (600, 450), (210, 170, 160))
    assert artifacts.dark_corner_share(plain) == 0.0


def test_round_field_of_view_has_dark_corners():
    assert artifacts.dark_corner_share(round_dermoscope_image(radius=1.0)) > 0.9


def test_wider_opening_gives_a_smaller_share():
    narrow = artifacts.dark_corner_share(round_dermoscope_image(radius=1.0))
    wide = artifacts.dark_corner_share(round_dermoscope_image(radius=1.3))
    assert artifacts.DEFAULT_THRESHOLD < wide < narrow


def test_dark_lesion_in_the_centre_is_not_a_dark_corner():
    pixels = np.full((450, 600, 3), 200, dtype=np.uint8)
    pixels[150:300, 200:400] = 10  # a black lesion in the middle
    assert artifacts.dark_corner_share(Image.fromarray(pixels)) == 0.0


def test_many_files_are_measured_in_order(tmp_path):
    files = []
    for name, image in (
        ("round.png", round_dermoscope_image(1.0)),
        ("plain.png", Image.new("RGB", (60, 45), (200, 200, 200))),
    ):
        image.save(tmp_path / name)
        files.append(tmp_path / name)
    shares = artifacts.dark_corner_shares(files)
    assert shares[0] > 0.9 and shares[1] == 0.0
