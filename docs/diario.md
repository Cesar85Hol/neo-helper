# Diario di bordo

## 2026-10-25 — Avvio
- Creata la struttura di documentazione (README + docs/00–04).
- Decisioni preliminari:
  - Target iniziale: immagini **dermatoscopiche**, dataset pubblici ISIC/HAM10000.
  - L'LLM orchestra e scrive report, **non** classifica: i numeri vengono dai modelli di visione via tool MCP.
  - Sviluppo incrementale: pipeline fissa → MCP → agente singolo → multi-agente.
  - Mobile: proposta Expo (React Native) con inferenza ibrida.

### Da verificare (⚠️ nei documenti)
- Stato/disponibilità pesi di PanDerm, Derm Foundation, MedGemma.
- Licenza e dimensioni esatte di ISIC 2024 (SLICE-3D) e MILK10k.
- Riferimenti bibliografici marcati ⚠️ in 01_stato_dell_arte.md.

## 2026-10-26 — Repository
- Installato e autenticato GitHub CLI (`gh`, account Cesar85Hol).
- `git init`, `.gitignore` (esclude dati, pesi, PDF, segreti), licenze MIT (codice) + CC BY 4.0 (docs), `refs.bib`, cartella `docs/papers/`.

- Creato il repo pubblico https://github.com/Cesar85Hol/neo-helper
- Label per area (letteratura, dati, ml, agenti-mcp, web, mobile, setup, scrittura, da-verificare), milestone M1–M7, 30 issues dalla roadmap.

## 2026-10-26 — Pacchetto letteratura 1 (§1 clinica + §2 paper fondativi)
- Connettori MCP attivati: **PubMed** e **alphaXiv**.
- Pipeline: PubMed (metadati + testo completo da PMC quando disponibile) → schede MD in `docs/papers/` → Word con `tools/build_word.sh` (pandoc) → copioni parlati in `docs/audio/` → MP3 con `tools/build_audio.py` (edge-tts, voce it-IT-IsabellaNeural).
- Testo completo letto: Esteva 2017, HAM10000 2018, Tschandl 2019. Solo abstract: Haenssle 2018, Brinker 2019, Tschandl 2020 (paywall). I numeri non verificati sono segnati con ⚠️.
- Output (non in git): `outputs/letteratura/*.docx` per NotebookLM, `~/Music/Neo Helper/*.mp3` (7 episodi, circa 30 min, con tag ID3; cartella aggiunta ai File locali di Spotify).

### Prossimi passi
1. Ascoltare gli episodi; caricare i Word su NotebookLM.
2. Recuperare il testo completo di Tschandl 2020 (verificare i numeri ⚠️).
3. Pacchetto 2: §3 foundation model + §4 bias e fairness (issue #4, #5).
4. (Opzionale) Board GitHub Projects sopra le issues.
2. Iniziare la lettura: Esteva 2017 → Tschandl 2019 → Tschandl 2020 → Daneshjou 2022 → MONET 2024.
3. Scaricare HAM10000 ed eseguire la prima EDA.
