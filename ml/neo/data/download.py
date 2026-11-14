"""Download dataset files with size and checksum verification, and extract
zip archives safely.

A file already on disk with the right size and checksum is never downloaded
again. A download is written to a ``.part`` file and renamed only after the
checksum matches, so an interrupted download never looks complete.
"""

from __future__ import annotations

import hashlib
import shutil
import urllib.request
import zipfile
from pathlib import Path

from neo.data.sources import RemoteFile

CHUNK = 1024 * 1024  # 1 MiB
USER_AGENT = "neo-helper-research-script/0.1"


class DownloadError(RuntimeError):
    """A downloaded file does not match the catalogue."""


def human_size(n_bytes: int) -> str:
    """Format a size in bytes for people: 1366522108 -> '1.37 GB'."""
    size = float(n_bytes)
    for unit in ("B", "kB", "MB", "GB"):
        if size < 1000 or unit == "GB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.2f} {unit}"
        size /= 1000
    raise AssertionError("unreachable")


def md5_of(path: Path) -> str:
    digest = hashlib.md5()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK):
            digest.update(chunk)
    return digest.hexdigest()


def is_complete(remote: RemoteFile, folder: Path) -> bool:
    """True when the file is on disk with the expected size and checksum."""
    path = folder / remote.name
    return path.is_file() and path.stat().st_size == remote.size and md5_of(path) == remote.md5


def download_file(remote: RemoteFile, folder: Path, verbose: bool = True) -> Path:
    """Download one file into ``folder`` and verify it. Returns the final path."""
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / remote.name
    if is_complete(remote, folder):
        if verbose:
            print(f"  already there, checksum OK: {remote.name}")
        return target

    partial = target.with_name(target.name + ".part")
    digest = hashlib.md5()
    done = 0
    next_report = 0.1
    request = urllib.request.Request(remote.url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=60) as response, partial.open("wb") as out:
        while chunk := response.read(CHUNK):
            out.write(chunk)
            digest.update(chunk)
            done += len(chunk)
            if verbose and remote.size and done / remote.size >= next_report:
                print(f"  {remote.name}: {done / remote.size:4.0%} of {human_size(remote.size)}")
                next_report += 0.1

    if done != remote.size or digest.hexdigest() != remote.md5:
        partial.unlink(missing_ok=True)
        raise DownloadError(
            f"{remote.name}: expected {remote.size} bytes with MD5 {remote.md5}, "
            f"got {done} bytes with MD5 {digest.hexdigest()}. The partial file was removed."
        )
    partial.replace(target)
    if verbose:
        print(f"  downloaded, checksum OK: {remote.name}")
    return target


def free_space(folder: Path) -> int:
    """Free bytes on the disk that holds ``folder`` (the folder may not exist yet)."""
    probe = folder
    while not probe.exists():
        probe = probe.parent
    return shutil.disk_usage(probe).free


def extract_zip(archive: Path, destination: Path) -> int:
    """Extract ``archive`` into ``destination`` and return the number of files.

    Archives come from the internet, so every member path is checked: an entry
    that would be written outside ``destination`` stops the extraction.
    """
    destination.mkdir(parents=True, exist_ok=True)
    root = destination.resolve()
    count = 0
    with zipfile.ZipFile(archive) as bundle:
        for member in bundle.infolist():
            resolved = (root / member.filename).resolve()
            if not resolved.is_relative_to(root):
                raise DownloadError(f"{archive.name}: unsafe path in archive: {member.filename!r}")
        for member in bundle.infolist():
            if member.is_dir():
                continue
            # Skip files that are already extracted with the right size.
            out = root / member.filename
            if not (out.is_file() and out.stat().st_size == member.file_size):
                bundle.extract(member, root)
            count += 1
    return count
