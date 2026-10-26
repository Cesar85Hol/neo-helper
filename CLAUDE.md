# Neo Helper — project conventions

## Language rule
- **Code is always in English**: scripts, source files, identifiers, comments, docstrings, CLI help and log/output messages, config files. Anyone should be able to read the code and understand what to do.
- **Documentation and audio stay in Italian**: `README.md`, everything in `docs/` (roadmap, literature notes in `docs/papers/`, audio scripts in `docs/audio/`, diary), generated Word files and MP3 episodes.
- Text that is *content* produced by a script (e.g. Word document titles, ID3 tags of Italian episodes) may stay in Italian; the code around it is English.

## Repository layout
- `docs/` — research documentation (Italian). `docs/diario.md` is the project log: update it at the end of each work session.
- `docs/papers/` — one literature note per paper; `docs/refs.bib` — BibTeX.
- `docs/audio/` — spoken-style scripts for the audio episodes.
- `tools/` — helper scripts (`build_word.sh`, `build_audio.py`).
- `outputs/` — generated files, not tracked by git. MP3s go to `~/Music/Neo Helper` (Spotify local files).

## Literature workflow
1. Find papers with the PubMed / alphaXiv MCP connectors; always record the DOI.
2. Write the note in `docs/papers/`; mark unverified facts with ⚠️ and say whether the full text or only the abstract was read.
3. `tools/build_word.sh` → Word files; write the spoken script in `docs/audio/`; `.venv/bin/python tools/build_audio.py` → MP3s.
