#!/usr/bin/env bash
# Build the literature Word documents (one per section) from the Markdown notes in docs/papers/.
# Usage: tools/build_word.sh   → output in outputs/letteratura/
# Document titles stay in Italian: they are content, not code.
set -euo pipefail
cd "$(dirname "$0")/.."

OUT=outputs/letteratura
mkdir -p "$OUT"
P=docs/papers

# build <output-file> <document-title> <markdown-files...>
build() {
  local out="$1" title="$2"; shift 2
  pandoc "$@" \
    --from gfm --to docx \
    --metadata title="$title" \
    --metadata subtitle="Neo Helper — riassunti di letteratura" \
    --metadata date="$(date +%d/%m/%Y)" \
    --metadata lang=it-IT --metadata toc-title="Indice" \
    --toc --toc-depth=2 \
    -o "$OUT/$out"
  echo "✓ $OUT/$out"
}

build "S1_background_clinico.docx" "§1 — Background clinico" \
  "$P/00_background_clinico.md"

build "S2_paper_fondativi.docx" "§2 — Paper fondativi del deep learning in dermatologia" \
  "$P/S2_introduzione.md" \
  "$P/2017_esteva_dermatologist-level.md" \
  "$P/2018_haenssle_man-against-machine.md" \
  "$P/2018_tschandl_ham10000.md" \
  "$P/2019_brinker_136-of-157.md" \
  "$P/2019_tschandl_human-vs-machine-isic2018.md" \
  "$P/2020_tschandl_human-computer-collaboration.md"
