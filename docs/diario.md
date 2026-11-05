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
- Testo completo letto: Esteva 2017, HAM10000 2018, Tschandl 2019. Solo abstract: Haenssle 2018, Brinker 2019 (paywall); Tschandl 2020 letto completo il 2026-11-03. I numeri non verificati sono segnati con ⚠️.
- Output (non in git): `outputs/letteratura/*.docx` per NotebookLM, `~/Music/Neo Helper/*.mp3` (7 episodi, circa 30 min, con tag ID3; cartella aggiunta ai File locali di Spotify).

## 2026-10-27 — Regola sulla lingua
- Codice, commit, branch, issue e PR tecniche in **inglese**; documenti, audio e chat in **italiano** (vedi `CLAUDE.md`).
- Script in `tools/` tradotti; issue tecniche #11–#27 e #30 tradotte in inglese. Le issue di letteratura e scrittura (#1–#10, #28, #29) restano in italiano.
- Label rinominate in inglese: literature, data, ml, agents-mcp, web, mobile, setup, writing, to-verify.
- MP3 spostati in `~/Music/Neo Helper` con tag ID3, per la playlist Spotify (File locali).

## 2026-11-03 — Storyboard
- Creato lo storyboard `docs/figures/storyboard_evoluzione_reti.svg` (+ PNG): 6 riquadri sulla linea del tempo, da Esteva 2017 agli agenti di Neo Helper. I riquadri 5–6 sono anteprima.
- Inserito nell'introduzione della §2 e quindi nel Word `S2_paper_fondativi.docx`.
- Versione snella `docs/figures/storyboard_snello.svg` (+ PNG): solo linea del tempo, titoli e un'illustrazione per tappa.

## 2026-11-03 — Tschandl 2020 completo, issue rinominate
- Letto il testo completo di **Tschandl 2020** (post-print, archivio ArTS dell'Università di Trieste). Numeri ⚠️ confermati (63,6% → 77,0%; studenti 32,5% → 47,3%); aggiunti la quarta forma di supporto (folla), i dati su AI difettosa, folla + AI, telemedicina, second opinion e la soglia di malignità al 17%. Aggiornati la scheda, l'introduzione della §2, il copione e l'MP3 dell'episodio 7.
- Tutte le issue in inglese con prefisso di milestone (`M1.1_…`, `M2.3_…`); regola aggiunta in `CLAUDE.md`.
- Chiuse **M1.1** (#1) e **M1.2** (#2): Pacchetto 1 completato.

## 2026-11-03 — Pacchetto letteratura 2 (§3 foundation model + §4 bias e fairness)
- **§3 (issue #4, M1.4):** schede su MONET 2024, PanDerm 2025, SkinGPT-4 2024, Anriot 2026 (PanDerm in condizioni realistiche), Bhagwat 2026 (ChatGPT e Gemini su DDI); introduzione `S3_introduzione.md` con la tabella dei pesi.
- **§4 (issue #5, M1.5):** schede su Winkler 2019, Fitzpatrick17k 2021, DDI 2022, CLEAR Derm 2022; introduzione `S4_introduzione.md`.
- Testo completo letto: PanDerm, SkinGPT-4, DDI, CLEAR Derm (PMC), Fitzpatrick17k (arXiv). Solo abstract: MONET, Winkler (abstract strutturato), Anriot 2026, Bhagwat 2026. Punti non verificati segnati con ⚠️.
- **Pesi verificati:** PanDerm pubblico ma **CC-BY-NC-ND 4.0** (solo ricerca non commerciale); MONET su Hugging Face (`chanwkim/monet`, licenza da leggere); Derm Foundation gated (termini HAI-DEF), senza paper dedicato.
- Decisioni che emergono: PanDerm come backbone candidato; l'LLM **non** classifica (confermato da SkinGPT-4 e Bhagwat); DDI come test set esterno con risultati per fototipo; agente di controllo qualità per artefatti (Winkler); CLEAR Derm come griglia del capitolo di valutazione.
- Output: `S3_foundation_model.docx`, `S4_bias_e_fairness.docx`; episodi audio 8–11 (tutti gli MP3 rigenerati per aggiornare il numero di tracce a 11).
- Aggiornati `01_stato_dell_arte.md`, `02_risorse.md`, `00_roadmap.md`, `refs.bib`, `tools/build_word.sh`.

## 2026-11-04 — Scelte di progetto e pipeline preliminare
- Nuovo documento [`05_scelte_e_pipeline.md`](05_scelte_e_pipeline.md): registro delle scelte, pipeline offline e online, ruolo di MONET, ISIC 2019, spazio per nuovi dati, annotazione manuale.
- **Confermate:** C1–C5 (PanDerm, l'LLM non classifica, DDI come test esterno, agente di controllo, CLEAR Derm) e P1–P10 (HAM10000 iniziale, 7 classi + punteggio di malignità, soglia bassa, split per `lesion_id`, PanDerm congelato come primo passo e fine-tuning come secondo esperimento, baseline, MONET per i concetti, incertezza, test esterni, supporto al medico).
- **Licenza di PanDerm (CC BY-NC-ND 4.0):** la tesi è permessa, anche con fine-tuning; non si possono condividere pesi modificati né fare un'app pubblica o un prodotto. Anche HAM10000/ISIC sono NC. DermFM-Zero ha una licenza contraddittoria (GitHub vs Hugging Face).
- **Decisione backbone:** PanDerm per la tesi + confronto con DINOv2 (Apache 2.0) e Derm Foundation sugli stessi split; `embed_image` rende il backbone sostituibile.
- **ISIC 2019:** raccomandato **dopo** la baseline su HAM10000, così BCN20000 e MSK restano test esterno.
- **Nuovi dati:** solo una possibilità da discutere con l'ospedale di contatto, fuori dal piano. Istruzioni per gli annotatori in italiano, inglese e spagnolo in [`annotazione/`](annotazione/).

## 2026-11-04 — Mail agli autori, testi completi
- **Bozza della mail** agli autori di PanDerm/DermFM-Zero in [`corrispondenza/`](corrispondenza/2026-11-04_mail_autori_panderm.md), **non ancora inviata**. Contiene cinque domande sulla licenza e la richiesta del testo completo di Anriot 2026. L'indirizzo email è da prendere dall'articolo.
- **MONET:** letto il **preprint completo** (medRxiv 2023), perché la versione di Nature Medicine non è in PMC.
  - Dati: 105.550 coppie immagine-testo (PubMed Central + 55 libri); architettura CLIP ViT-L/14.
  - Concetti SkinCon: AUROC 0,766, contro 0,692 di CLIP e della ResNet-50.
  - Audit di ISIC: adesivi arancioni come scorciatoia; "rosso" benigno a Vienna e maligno a Barcellona.
  - Concept bottleneck: AUROC 0,892 per il melanoma.
  - **Licenza** del repository: **CC BY-NC-SA 4.0**; la model card esclude qualsiasi uso in produzione.
  - Limite: i criteri dermoscopici non sono stati valutati.
- **Bhagwat 2026:** letto il **testo completo** (PMC).
  - Top-1 23% (ChatGPT) e 32% (Gemini).
  - Lethal miss 50% e 32%.
  - Sui tumori dei fototipi V–VI il punteggio è circa un terzo per entrambi i modelli.
- **Anriot 2026:** resta solo l'abstract (JAMA non accessibile). Segnato un probabile refuso nell'IC dell'abstract.
- Aggiornati `01_stato_dell_arte.md`, `02_risorse.md`, `S3_introduzione.md` e `05_scelte_e_pipeline.md` (§2); rigenerati i Word e gli episodi 8–9.

## 2026-11-05 — Pacchetto letteratura 3 (§5 spiegabilità + §6 agenti e MCP)
- Riconosciuto un errore di ordine: la Milestone 1 va chiusa prima dei dati (M2). Restano #3, #8, #9 e #10.
- **§5 (issue #6, M1.6):** schede su Grad-CAM 2017, Adebayo 2018 (test di sanità), Tschandl 2019 (CBIR), Koh 2020 (concept bottleneck), Angelopoulos e Bates 2021 (conformal), Chanda 2024 (XAI dermoscopica, 116 medici), Krakowski 2024 (meta-analisi uomo-AI). Introduzione `S5_introduzione.md`.
- **§6 (issue #7, M1.7):** schede su Anthropic 2024 (*Building effective agents*), Anthropic 2025 (sistema multi-agente), specifica MCP (2025-06-18 e 2026-07-28), AMIE (Nature 2025 e 2026), MDAgents 2024, DermAgent 2026, Vatsal 2026 (rassegna). Introduzione `S6_introduzione.md`.
- **Cosa è stato letto:**
  - testo completo: Tschandl 2019, Krakowski 2024, Chanda 2024 (tranne il supplementare);
  - abstract e discussione: AMIE;
  - pagine web complete: blog di Anthropic, pagine introduttive della specifica MCP;
  - **sintesi strutturate di alphaXiv**, non il PDF: Grad-CAM, Adebayo, Koh, Angelopoulos, MDAgents, DermAgent, Vatsal. I numeri sono segnati con ⚠️.
- **Scoperte importanti:**
  - **Chanda 2024** ha pubblicato annotazioni dermoscopiche localizzate su HAM10000, il nostro dataset; aggiunte a `02_risorse.md`.
  - **DermAgent** (Monash, 2026) è il lavoro più vicino a Neo Helper: il contributo originale va precisato nella M1.10. Aggiunta una nota alla §8 dello stato dell'arte.
- Output: `S5_spiegabilita_e_incertezza.docx`, `S6_agenti_e_mcp.docx`; episodi audio 12–15 (tutti gli MP3 rigenerati: tracce x/15).
- Aggiornati `01_stato_dell_arte.md` (§5, §6, §8), `00_roadmap.md` (spuntate anche "Clinica di base" e "Paper fondativi"), `02_risorse.md`, `refs.bib` (15 voci), `tools/build_word.sh`.

### Prossimi passi
1. **Inviare** la mail agli autori di PanDerm/DermFM-Zero (Cesar), poi annotare la risposta nel file.
2. **Pacchetto 4:** challenge ISIC 2016–2020 e 2024 (#3), prodotti esistenti e regolamentazione (#8).
3. **Chiusura M1:** verifica dei ⚠️ (#9), domande di ricerca e contributo originale rispetto a DermAgent (#10).
4. Testo completo di Anriot 2026 (accesso universitario o dagli autori); link e licenza delle annotazioni di Chanda 2024.
5. Solo dopo la M1: scaricare HAM10000 ed eseguire la prima EDA (split per `lesion_id`, conteggio artefatti).
6. (Opzionale) Caricare su NotebookLM i Word nuovi (S5, S6) e quelli aggiornati (S3).
