"""Genera gli MP3 degli episodi audio dai copioni in docs/audio/ con edge-tts.

Uso:
    .venv/bin/python tools/build_audio.py                 # tutti gli episodi
    .venv/bin/python tools/build_audio.py S2_ep05         # solo quelli che iniziano così
    .venv/bin/python tools/build_audio.py --voice it-IT-DiegoNeural --rate=-5%

Voci italiane: it-IT-IsabellaNeural, it-IT-ElsaNeural, it-IT-DiegoNeural,
it-IT-GiuseppeMultilingualNeural.
"""

import argparse
import asyncio
import re
from pathlib import Path

import edge_tts

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "docs" / "audio"
OUT = ROOT / "outputs" / "audio"


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


async def synth(path: Path, voice: str, rate: str) -> None:
    text = to_speech_text(path.read_text(encoding="utf-8"))
    out = OUT / f"{path.stem}.mp3"
    await edge_tts.Communicate(text, voice, rate=rate).save(str(out))
    print(f"✓ {out.relative_to(ROOT)}")


async def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("prefix", nargs="?", default="")
    p.add_argument("--voice", default="it-IT-IsabellaNeural")
    p.add_argument("--rate", default="+0%")
    args = p.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    for path in sorted(SCRIPTS.glob(f"{args.prefix}*.md")):
        await synth(path, args.voice, args.rate)


if __name__ == "__main__":
    asyncio.run(main())
