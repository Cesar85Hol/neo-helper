"""Genera gli MP3 degli episodi audio dai copioni in docs/audio/ con edge-tts.

Gli MP3 vanno in ~/Music/Neo Helper (cartella aggiunta ai "File locali" di Spotify),
con tag ID3 (titolo, album, numero traccia) così la playlist è ordinata e leggibile.

Uso:
    .venv/bin/python tools/build_audio.py                 # tutti gli episodi
    .venv/bin/python tools/build_audio.py S2_ep05         # solo quelli che iniziano così
    .venv/bin/python tools/build_audio.py --voice it-IT-DiegoNeural --rate=-5%
    .venv/bin/python tools/build_audio.py --out outputs/audio

Voci italiane: it-IT-IsabellaNeural, it-IT-ElsaNeural, it-IT-DiegoNeural,
it-IT-GiuseppeMultilingualNeural.
"""

import argparse
import asyncio
import re
from pathlib import Path

import edge_tts
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "docs" / "audio"
DEFAULT_OUT = Path.home() / "Music" / "Neo Helper"
ALBUM = "Neo Helper – Letteratura"


def to_speech_text(md: str) -> str:
    """Il titolo (# …) diventa la frase d'apertura; il resto è testo parlato."""
    lines = []
    for line in md.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("#"):
            line = line.lstrip("#").strip().replace("—", ".") + "."
        lines.append(re.sub(r"[*_`]", "", line))
    return "\n\n".join(lines)


def episode_title(md: str) -> str:
    first = next(l for l in md.splitlines() if l.startswith("#"))
    return first.lstrip("#").strip()


def tag(mp3: Path, title: str, track: int, total: int) -> None:
    try:
        tags = EasyID3(mp3)
    except ID3NoHeaderError:
        tags = EasyID3()
    tags.update(
        title=title,
        album=ALBUM,
        artist="Neo Helper",
        tracknumber=f"{track}/{total}",
        genre="Podcast",
    )
    tags.save(mp3)


async def synth(path: Path, out_dir: Path, voice: str, rate: str, track: int, total: int) -> None:
    md = path.read_text(encoding="utf-8")
    out = out_dir / f"{path.stem}.mp3"
    await edge_tts.Communicate(to_speech_text(md), voice, rate=rate).save(str(out))
    tag(out, episode_title(md), track, total)
    print(f"✓ {out}")


async def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("prefix", nargs="?", default="")
    p.add_argument("--voice", default="it-IT-IsabellaNeural")
    p.add_argument("--rate", default="+0%")
    p.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = p.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    # Numero traccia sempre calcolato su tutti i copioni, anche se ne rigeneri solo uno.
    all_scripts = sorted(SCRIPTS.glob("*.md"))
    for track, path in enumerate(all_scripts, start=1):
        if path.name.startswith(args.prefix):
            await synth(path, args.out, args.voice, args.rate, track, len(all_scripts))


if __name__ == "__main__":
    asyncio.run(main())
