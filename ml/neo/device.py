"""Choose where PyTorch runs: Apple GPU (MPS), NVIDIA GPU (CUDA) or CPU.

The same code must run on a Mac, on a cloud GPU and on a CPU-only machine
(RQ6: low-resource research centres), so the device is chosen in one place.
"""

from __future__ import annotations

import torch

CHOICES = ("auto", "cpu", "mps", "cuda")


def available_devices() -> list[str]:
    """List the devices usable on this machine, best first."""
    devices = []
    if torch.cuda.is_available():
        devices.append("cuda")
    if torch.backends.mps.is_available():
        devices.append("mps")
    devices.append("cpu")
    return devices


def select_device(preference: str = "auto") -> torch.device:
    """Return the requested device, or the best available one for ``auto``.

    Raises ``ValueError`` for an unknown name and ``RuntimeError`` when the
    requested device is not available, instead of silently falling back.
    """
    if preference not in CHOICES:
        raise ValueError(f"Unknown device '{preference}'. Choose one of: {', '.join(CHOICES)}")
    usable = available_devices()
    if preference == "auto":
        return torch.device(usable[0])
    if preference not in usable:
        raise RuntimeError(
            f"Device '{preference}' is not available here. Available: {', '.join(usable)}"
        )
    return torch.device(preference)
