# Neo Helper — project conventions

## Language rule
- **Code is always in English**: scripts, source files, identifiers, comments, docstrings, CLI help and log/output messages, config files. Anyone should be able to read the code and understand what to do.
- **Git and GitHub are in English too**: commit messages, branch names, and the title and text of every issue and pull request.
- **Issue titles start with a milestone prefix** `M<milestone>.<n>_`, e.g. `M1.2_Write notes on ...` = 2nd issue of milestone M1. Number new issues after the last one in the same milestone.
- **Commit subjects start with the milestone**, then the package if there is one, then the issues the commit closes, then a colon and the description:
  - `M1-P3 #6 #7: Add notes on explainability and agents/MCP` = milestone M1, literature package 3, closes issues #6 and #7;
  - `M1-P3: Update MONET note from full text` = same package, no issue closed;
  - `M2: Add HAM10000 download script` = milestones without packages.
  
  In the body, write `Closes #6, closes #7` so GitHub closes the issues on push. Never reword commits that are already pushed.
- **Documentation and audio stay in Italian**: `README.md`, everything in `docs/` (roadmap, literature notes in `docs/papers/`, audio scripts in `docs/audio/`, diary), generated Word files and MP3 episodes.
- Text that is *content* produced by a script (e.g. Word document titles, ID3 tags of Italian episodes) may stay in Italian; the code around it is English.

## Repository layout
- `docs/` — research documentation (Italian). `docs/diario.md` is the project log: update it at the end of each work session.
- `docs/papers/` — one literature note per paper; `docs/refs.bib` — BibTeX.
- `docs/audio/` — spoken-style scripts for the audio episodes.
- `docs/figures/` — figures: the SVG is the source, the PNG is rendered from it with headless Chrome (2x scale). The decision storyboards (`storyboard_0N_*.svg`) are in English.
- `tools/` — helper scripts (`build_word.sh`, `build_audio.py`).
- `outputs/` — generated files, not tracked by git. MP3s go to `~/Music/Neo Helper` (Spotify local files).

## Literature workflow
1. Find papers with the PubMed / alphaXiv MCP connectors; always record the DOI.
2. Write the note in `docs/papers/`; mark unverified facts with ⚠️ and say whether the full text or only the abstract was read.
3. `tools/build_word.sh` → Word files; write the spoken script in `docs/audio/`; `.venv/bin/python tools/build_audio.py` → MP3s.
