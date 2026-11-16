"""Tests for the MONET concept scores. No model is loaded: the score is checked
on small hand-made vectors, where the right answer is known."""

import numpy as np
import pandas as pd
import pytest
import torch

from neo import concepts


def unit(*values: float) -> torch.Tensor:
    vector = torch.tensor(values, dtype=torch.float32)
    return vector / vector.norm()


def test_score_is_high_when_the_image_matches_the_concept():
    # Three templates, one term, two dimensions: axis 0 = "concept", axis 1 = "plain skin".
    target = torch.stack([unit(1, 0)[None, :]] * 3)
    reference = torch.stack([unit(0, 1)] * 3)
    images = torch.stack([unit(1, 0.1), unit(0.1, 1), unit(1, 1)]).numpy()
    scores = concepts.presence_score(images, target, reference)
    assert scores[0] > 0.99  # looks like the concept
    assert scores[1] < 0.01  # looks like plain skin
    assert scores[2] == pytest.approx(0.5, abs=1e-6)  # exactly in between


def test_score_averages_terms_and_templates():
    # An image only slightly closer to the concept: the softmax is sharp, so a
    # clear-cut image would give 1.0 in both cases.
    images = unit(1, 0.98)[None, :].numpy()
    reference = torch.stack([unit(0, 1)] * 3)
    one_term = torch.stack([unit(1, 0)[None, :]] * 3)
    two_terms = torch.stack([torch.stack([unit(1, 0), unit(0, 1)])] * 3)
    strong = concepts.presence_score(images, one_term, reference)[0]
    diluted = concepts.presence_score(images, two_terms, reference)[0]
    assert 0.5 < diluted < strong


def test_scores_stay_between_zero_and_one():
    generator = torch.Generator().manual_seed(0)
    images = torch.nn.functional.normalize(torch.randn(50, 16, generator=generator), dim=1)
    target = torch.nn.functional.normalize(torch.randn(3, 2, 16, generator=generator), dim=2)
    reference = torch.nn.functional.normalize(torch.randn(3, 16, generator=generator), dim=1)
    scores = concepts.presence_score(images.numpy(), target, reference)
    assert scores.shape == (50,)
    assert ((scores >= 0) & (scores <= 1)).all()


def test_artifact_list_matches_the_templates():
    assert len(concepts.TEMPLATES) == len(concepts.REFERENCES) == 3
    for name, terms in concepts.ARTIFACTS.items():
        assert name.isidentifier() and terms
        for template in concepts.TEMPLATES:
            assert "{}" in template and template.format(terms[0])


def test_missing_weights_give_a_clear_message(monkeypatch, tmp_path):
    monkeypatch.setenv("NEO_DATA_DIR", str(tmp_path))
    with pytest.raises(FileNotFoundError, match="neo-data download monet"):
        concepts.load_monet("cpu")


def test_cached_vectors_are_reused_only_for_the_same_images(monkeypatch, tmp_path):
    monkeypatch.setenv("NEO_DATA_DIR", str(tmp_path))
    calls = []

    def fake_embed(files, model, processor, device, batch_size=32):
        calls.append(len(files))
        return np.ones((len(files), 4), dtype=np.float32)

    monkeypatch.setattr(concepts, "embed_images", fake_embed)
    frame = pd.DataFrame({"uid": ["a", "b"], "file": ["a.jpg", "b.jpg"]})
    concepts.cached_image_vectors(frame, "demo", None, None, None)
    concepts.cached_image_vectors(frame, "demo", None, None, None)
    assert calls == [2]  # the second call read the cache
    longer = pd.DataFrame({"uid": ["a", "b", "c"], "file": ["a.jpg", "b.jpg", "c.jpg"]})
    assert concepts.cached_image_vectors(longer, "demo", None, None, None).shape == (3, 4)
    assert calls == [2, 3]  # different images: computed again
