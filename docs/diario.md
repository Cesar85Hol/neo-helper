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

### Prossimi passi
1. Creare repo GitHub pubblico, milestone M1–M7 e issues dalla roadmap.
2. Iniziare la lettura: Esteva 2017 → Tschandl 2019 → Tschandl 2020 → Daneshjou 2022 → MONET 2024.
3. Scaricare HAM10000 ed eseguire la prima EDA.
