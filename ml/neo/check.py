"""Environment check: print the setup and run a tiny embedding smoke test.

Usage:
    uv run neo-check                 # best available device
    uv run neo-check --device cpu    # force the CPU-only path

The smoke test builds a very small Vision Transformer with random weights
(nothing is downloaded), turns a few random images into embeddings and reports
the time. It only proves that the environment works; it says nothing about
accuracy.
"""

from __future__ import annotations

import argparse
import platform
import time

import timm
import torch

from neo import __version__, paths
from neo.device import CHOICES, available_devices, select_device

SMOKE_MODEL = "vit_tiny_patch16_224"


def run_smoke_test(device: torch.device, n_images: int = 10, batch_size: int = 5) -> dict:
    """Embed ``n_images`` random images on ``device`` and return shape and timing."""
    torch.manual_seed(0)
    # num_classes=0 removes the classification head: the model returns embeddings.
    model = timm.create_model(SMOKE_MODEL, pretrained=False, num_classes=0).eval().to(device)
    images = torch.rand(n_images, 3, 224, 224)

    start = time.perf_counter()
    chunks = []
    with torch.inference_mode():
        for batch in images.split(batch_size):
            chunks.append(model(batch.to(device)).cpu())
    embeddings = torch.cat(chunks)
    seconds = time.perf_counter() - start

    return {
        "device": device.type,
        "shape": tuple(embeddings.shape),
        "seconds": seconds,
        "finite": bool(torch.isfinite(embeddings).all()),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check the Neo Helper environment.")
    parser.add_argument(
        "--device", choices=CHOICES, default="auto", help="Device to test (default: auto)."
    )
    parser.add_argument(
        "--images", type=int, default=10, help="Number of random images to embed (default: 10)."
    )
    args = parser.parse_args(argv)

    print(f"neo-helper {__version__}")
    print(f"Python     {platform.python_version()} on {platform.platform()}")
    print(f"PyTorch    {torch.__version__}, timm {timm.__version__}")
    print(f"Devices    {', '.join(available_devices())}")
    data_dir = paths.data_dir()
    state = "exists" if data_dir.exists() else "not created yet"
    print(f"Data dir   {data_dir} ({state}; set {paths.ENV_VAR} to change it)")

    device = select_device(args.device)
    result = run_smoke_test(device, n_images=args.images)
    print(
        f"Smoke test {SMOKE_MODEL} on {result['device']}: "
        f"embeddings {result['shape']} in {result['seconds']:.2f} s"
    )
    if not result["finite"]:
        print("FAILED: the embeddings contain NaN or infinite values.")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
