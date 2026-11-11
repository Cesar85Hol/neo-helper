"""Tests for the environment helpers: data paths, device choice, smoke test."""

from pathlib import Path

import pytest
import torch

from neo import paths
from neo.check import main, run_smoke_test
from neo.device import available_devices, select_device


def test_data_dir_default(monkeypatch):
    monkeypatch.delenv(paths.ENV_VAR, raising=False)
    assert paths.data_dir() == Path.home() / "neo-helper-data"


def test_data_dir_from_environment(monkeypatch, tmp_path):
    monkeypatch.setenv(paths.ENV_VAR, str(tmp_path))
    assert paths.data_dir() == tmp_path


def test_subdir_is_created_only_on_request(monkeypatch, tmp_path):
    monkeypatch.setenv(paths.ENV_VAR, str(tmp_path))
    assert not paths.subdir("embeddings").exists()
    assert paths.subdir("embeddings", create=True).is_dir()


def test_subdir_rejects_unknown_name():
    with pytest.raises(ValueError):
        paths.subdir("not-a-folder")


def test_cpu_is_always_available():
    assert available_devices()[-1] == "cpu"
    assert select_device("cpu") == torch.device("cpu")


def test_auto_picks_the_best_available_device():
    assert select_device("auto").type == available_devices()[0]


def test_unknown_device_is_rejected():
    with pytest.raises(ValueError):
        select_device("gpu")


def test_unavailable_device_raises_instead_of_falling_back():
    missing = [name for name in ("cuda", "mps") if name not in available_devices()]
    if not missing:
        pytest.skip("Both CUDA and MPS are available on this machine.")
    with pytest.raises(RuntimeError):
        select_device(missing[0])


@pytest.mark.parametrize("device_name", available_devices())
def test_smoke_test_on_each_device(device_name):
    result = run_smoke_test(torch.device(device_name), n_images=4, batch_size=2)
    assert result["shape"] == (4, 192)
    assert result["finite"]


def test_embeddings_agree_between_cpu_and_accelerator():
    """The same weights and images must give the same embeddings on every device."""
    devices = available_devices()
    if len(devices) < 2:
        pytest.skip("Only the CPU is available.")
    import timm

    torch.manual_seed(0)
    model = timm.create_model("vit_tiny_patch16_224", pretrained=False, num_classes=0).eval()
    images = torch.rand(2, 3, 224, 224)
    with torch.inference_mode():
        reference = model(images)
        accelerator = torch.device(devices[0])
        other = model.to(accelerator)(images.to(accelerator)).cpu()
    assert torch.allclose(reference, other, atol=1e-3)


def test_command_line_check_on_cpu(capsys):
    assert main(["--device", "cpu", "--images", "2"]) == 0
    assert "OK" in capsys.readouterr().out
