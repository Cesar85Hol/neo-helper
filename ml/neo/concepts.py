"""Concept scores with MONET: how strongly does an image show a concept
described in words (for example "ruler" or "purple pen")?

MONET (Kim et al., Nature Medicine 2024) is a CLIP model trained on dermatology
images and text: it places images and sentences in the same vector space. The
score follows the authors' tutorial (``calculate_concept_presence_score``):

1. the image is compared with sentences that name the concept
   ("This is skin image of ruler") and with the same sentences without it
   ("This is skin image");
2. a softmax between the two similarities gives a value between 0 and 1;
3. the value is averaged over the sentence templates.

A score is a ranking signal, not a probability. MONET was validated on clinical
photographs, so on dermoscopic images every concept must be checked by eye
before its scores are used.
"""

from __future__ import annotations

import math
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import pandas as pd
import torch
from PIL import Image

from neo import paths
from neo.device import select_device

TEMPLATES = (
    "This is skin image of {}",
    "This is dermatology image of {}",
    "This is image of {}",
)
REFERENCES = ("This is skin image", "This is dermatology image", "This is image")
# Softmax temperature used by the MONET authors (the CLIP logit scale).
TEMPERATURE = 1 / math.exp(4.5944)

# Artifacts that can become shortcuts for a classifier, with the words used to
# describe each one (Winkler 2019; Kim 2024).
ARTIFACTS: dict[str, tuple[str, ...]] = {
    "ink": ("purple pen", "pen marking"),
    "ruler": ("ruler", "measurement scale bar"),
    "sticker": ("orange sticker", "sticker"),
    "dark_border": ("black border", "dark corners"),
    "hair": ("hair",),
    "bubbles": ("air bubbles", "gel bubbles"),
}


def weights_folder() -> Path:
    return paths.subdir("weights") / "monet"


def load_monet(device: torch.device | str = "auto"):
    """Load MONET from the local weights folder. Returns (model, processor, device)."""
    from transformers import AutoProcessor, CLIPModel

    folder = weights_folder()
    if not (folder / "model.safetensors").is_file():
        raise FileNotFoundError(
            f"MONET weights not found in {folder}. Get them with: neo-data download monet --yes"
        )
    if not isinstance(device, torch.device):
        device = select_device(device)
    model = CLIPModel.from_pretrained(folder).eval().to(device)
    processor = AutoProcessor.from_pretrained(folder)
    return model, processor, device


# The two encoders are called through their sub-modules (encoder, then
# projection) because the return type of CLIPModel.get_image_features changed
# between versions of the transformers library.
def _normalise(vectors: torch.Tensor) -> torch.Tensor:
    return vectors / vectors.norm(dim=-1, keepdim=True)


def embed_images(
    files: list[Path], model, processor, device: torch.device, batch_size: int = 32
) -> np.ndarray:
    """Return one normalised MONET image vector per file (float32, n x 768)."""

    def load(path: Path) -> Image.Image:
        with Image.open(path) as image:
            return image.convert("RGB")

    chunks = []
    with ThreadPoolExecutor(8) as pool, torch.inference_mode():
        for start in range(0, len(files), batch_size):
            images = list(pool.map(load, files[start : start + batch_size]))
            pixels = processor(images=images, return_tensors="pt")["pixel_values"].to(device)
            pooled = model.vision_model(pixel_values=pixels).pooler_output
            chunks.append(_normalise(model.visual_projection(pooled)).float().cpu())
    return torch.cat(chunks).numpy()


def embed_texts(sentences: list[str], model, processor, device: torch.device) -> torch.Tensor:
    """Return one normalised MONET text vector per sentence."""
    tokens = processor(text=sentences, return_tensors="pt", padding=True, truncation=True)
    with torch.inference_mode():
        pooled = model.text_model(**{k: v.to(device) for k, v in tokens.items()}).pooler_output
        features = model.text_projection(pooled)
    return _normalise(features).float().cpu()


def presence_score(
    image_vectors: np.ndarray, target: torch.Tensor, reference: torch.Tensor
) -> np.ndarray:
    """Concept presence score of every image.

    ``target`` has shape (templates, terms, dim); ``reference`` has shape
    (templates, dim). Both are normalised, like ``image_vectors``.
    """
    images = torch.from_numpy(image_vectors).float()
    target_similarity = (target @ images.T).mean(dim=1)  # templates x images
    reference_similarity = reference @ images.T  # templates x images
    stacked = torch.stack([target_similarity, reference_similarity]) / TEMPERATURE
    return torch.softmax(stacked, dim=0)[0].mean(dim=0).numpy()


def score_concepts(
    image_vectors: np.ndarray,
    concepts: dict[str, tuple[str, ...]],
    model,
    processor,
    device: torch.device,
) -> pd.DataFrame:
    """Return a table with one column of scores per concept."""
    reference = embed_texts(list(REFERENCES), model, processor, device)
    scores = {}
    for name, terms in concepts.items():
        target = torch.stack(
            [
                embed_texts([template.format(term) for term in terms], model, processor, device)
                for template in TEMPLATES
            ]
        )
        scores[name] = presence_score(image_vectors, target, reference)
    return pd.DataFrame(scores)


def cached_image_vectors(frame: pd.DataFrame, source: str, model, processor, device) -> np.ndarray:
    """MONET image vectors of a registry, computed once and saved in ``embeddings/``."""
    folder = paths.subdir("embeddings", create=True)
    vectors_path = folder / f"monet_{source}.npy"
    uids_path = folder / f"monet_{source}_uids.csv"
    if vectors_path.is_file() and uids_path.is_file():
        saved = pd.read_csv(uids_path)["uid"]
        if saved.tolist() == frame["uid"].tolist():
            return np.load(vectors_path)
    root = paths.data_dir()
    vectors = embed_images([root / f for f in frame["file"]], model, processor, device)
    np.save(vectors_path, vectors)
    frame[["uid"]].to_csv(uids_path, index=False)
    return vectors
