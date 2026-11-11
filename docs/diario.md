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

## 2026-11-06 — Storyboard delle decisioni, regola sui commit
- **Nuova regola per i commit** (in `CLAUDE.md`): l'oggetto inizia con milestone, pacchetto e issue chiuse, per esempio `M1-P3 #6 #7: …`. I due commit non ancora pushati sono stati rinominati così.
- **Tre storyboard in inglese** in `docs/figures/`, che continuano lo storyboard 1:
  - `storyboard_02_models_pipeline`: pannelli 7–12 (dati, controllo qualità, PanDerm, baseline, output, parole e test) e le due pipeline, di costruzione e d'uso;
  - `storyboard_03_trust_agents`: pannelli 13–18 (heatmap, concetti, casi simili, "non so", MCP, agenti) e il flusso di un caso secondo l'incertezza;
  - `storyboard_04_building_blocks`: **41 blocchi in 7 livelli**, con lo stato di ognuno (21 decisi, 12 proposti, 6 domande aperte, 2 opzioni future) e le 8 domande aperte.
  
  Collegati in `05_scelte_e_pipeline.md`.
- Audio: la generazione si era bloccata ed è stata rifatta. Ora le 15 tracce sono complete (1/15 – 15/15).
- **Push:** per un po' GitHub ha rifiutato ogni push con "fatal error in commit_refs_rules", anche un commit vuoto di prova: era un problema lato GitHub. Al secondo tentativo il push è riuscito.
- Chiuse **M1.6** (#6) e **M1.7** (#7): Pacchetto 3 completato.

## 2026-11-06 — Pacchetto letteratura 4 (§7 challenge ISIC + §8 prodotti e regole)
- **§7 (issue #3, M1.3):** schede su:
  - ISIC 2018 (Codella 2019);
  - ISIC 2019 (Combalia 2022, *Lancet Digit Health*);
  - BCN20000 (Hernández-Pérez 2024);
  - ISIC 2020 (Rotemberg 2021; soluzione vincente di Ha 2020; risultati e contesto del paziente di Kurtansky 2024);
  - ISIC 2024 / SLICE-3D (Kurtansky 2025, *npj Digit Med*).
  
  Introduzione `S7_introduzione.md`.
- **§8 (issue #8, M1.8):** schede su Freeman 2020 (app, *BMJ*), Wongvibulsin 2024 (app con AI), DermaSensor (Jaklitsch 2023), DERM di Skin Analytics (Marsden 2024), MDR in dermatologia (Malvehy 2022), AI Act e riforme 2025–2026 (Van Kolfschooten 2026). Introduzione `S8_introduzione.md`. Aggiornato `04_etica_regolatorio.md` con una sezione "Cosa significa per Neo Helper".
- **Cosa è stato letto:**
  - testo completo: Codella 2019, Ha 2020, Malvehy 2022, BCN20000 (salvo i risultati delle baseline);
  - parti sostanziali del testo: Combalia 2022, Kurtansky 2025, Rotemberg 2021, Freeman 2020, Marsden 2024, Jaklitsch 2023, Van Kolfschooten 2026;
  - solo abstract: Kurtansky 2024, Wongvibulsin 2024.
  
  Le notizie regolatorie su DermaSensor (FDA 2024) e DERM (CE classe III 2025) vengono da fonti web secondarie o aziendali: sono segnate con ⚠️.
- **Scoperte importanti:**
  - ISIC 2019: l'accuratezza bilanciata crolla dall'82% al 59% su BCN20000, e gli algoritmi chiamano "maligna" quasi metà delle lesioni mai viste. È una conferma forte del "non so" (P8) e di BCN20000 come test esterno.
  - **BCN20000 ha licenza CC BY 4.0**, a differenza di HAM10000 (non commerciale).
  - Metriche da aggiungere alla valutazione: specificità a sensibilità fissa, pAUC sopra l'80% di sensibilità, lesioni da controllare per trovare un tumore.
  - AI Act: il quadro per i dispositivi medici è in movimento (Health Innovation Package, Digital Omnibus). Va ricontrollato prima della tesi.
- **Stato dell'arte** riorganizzato:
  - nuova §7 "Challenge ISIC", §8 "Prodotti e regolatorio", §9 "Gap";
  - le righe ISIC della §2 rimandano alla §7.
- Output: `S7_challenge_isic.docx`, `S8_prodotti_e_regolatorio.docx`; episodi audio 16–19 (tutte le tracce ritaggate x/19).

## 2026-11-09 — Chiusura della M1: verifiche (#9) e domande di ricerca (#10)
- **Verifica dei ⚠️ (issue #9):** registro completo in [`06_verifiche_M1.md`](06_verifiche_M1.md).
  - Fonti: Crossref, API di arXiv, API dell'archivio ISIC (licenza per immagine), Hugging Face, GitHub, Figshare, banca dati FDA, EUR-Lex, sintesi legali.
  - Esito: ✅ 19 confermati, ✏️ 13 corretti, ❓ 2 non risolti (licenza di DermFM-Zero, CE di DERM). Restano da confermare alcune sedi di pubblicazione e alcuni termini di licenza (§6 del registro).
- **Correzioni importanti:**
  - **BCN20000** è CC BY 4.0 solo su **Figshare**; sull'archivio ISIC è CC BY-NC;
  - **ISIC 2020** e **SLICE-3D** hanno licenze **miste** immagine per immagine;
  - l'archivio ISIC ha **581.002** immagini;
  - **AI Act:** obblighi per i dispositivi medici rinviati al **2 agosto 2028** (Digital Omnibus, reg. UE 2026/1744);
  - DermaSensor confermato (De Novo DEN230008, 12 gennaio 2024, classe II, sensibilità 95,5%, specificità 20,7%);
  - il seguito di AMIE ha primo autore Liévin;
  - Vatsal 2026 risulta solo come preprint;
  - MONET su Hugging Face è ora `suinleelab/monet`.
- **Scoperte:**
  - le **annotazioni di Chanda 2024** sono su Figshare con licenza CC BY 4.0;
  - **HIBA**, un dataset argentino sull'archivio ISIC (1.616 immagini, CC BY), aggiunto alle risorse e al §4.3 delle scelte.
- **Domande di ricerca (issue #10):** proposta in [`07_domande_di_ricerca.md`](07_domande_di_ricerca.md), **da confermare**.
  - RQ1 vedere, RQ2 dubitare, RQ3 spiegare, RQ4 coordinare, RQ5 facoltativa aiutare;
  - nuovo titolo di lavoro;
  - contributo originale rispetto a DermAgent.
  
  Aggiornati `00_roadmap.md` e la §9 (gap) dello stato dell'arte.
- Output: `S9_domande_e_verifiche.docx`; episodio audio 20 (tutte le tracce ritaggate x/20).

## 2026-11-10 — RQ6 e conferma delle domande di ricerca
- **Domande di ricerca confermate** da Cesar, con l'aggiunta della **RQ6 — Includere**: lo stato dell'arte funziona anche sulle pelli latinoamericane e asiatiche? Lo scopo è rendere Neo Helper usabile da centri di ricerca latinoamericani e di paesi con poco accesso.
- **Dati per la RQ6**, trovati sull'archivio ISIC:
  - HIBA (Argentina, CC BY);
  - PAD-UFES-20 (Brasile, CC BY);
  - cheratosi seborroiche della Pontificia Universidad Católica (Cile, CC BY);
  - BALD, lesioni acrali con centri giapponesi (CC BY-NC);
  - MSKCC Skin Tone Labeling (CC BY).
  
  Non ho trovato dataset asiatici pubblici di lesioni generali: da cercare nella M2.
- Corretto il §4.3 delle scelte: i metadati pubblici di DDI non riportano l'etnia.
- Nuovo titolo di lavoro (proposta) e contributo 6 (accessibilità). Episodio 20 aggiornato.

## 2026-11-10 — Revisione finale della M1 (issue #31, M1.11)
- Pushati i commit della M1.9 e della M1.10; chiuse **#9** e **#10** con un commento. Creata la issue **#31** "M1.11_Final review of milestone 1". La Milestone 1 resta **aperta**.
- **Revisione completa** in [`08_revisione_M1.md`](08_revisione_M1.md):
  - controllo dei principi: tutti rispettati;
  - 10 cose dimenticate o non allineate;
  - giudizio sulla logica del percorso;
  - tabella "obiettivi, scelte, criticità, perché" per 16 aree.
- **Già corretti:**
  - README con i nuovi documenti, la Fase 1 e l'obiettivo RQ6;
  - roadmap con la spunta del repository pubblico;
  - etichetta "Testo letto" nella scheda MCP.
- **Da decidere con Cesar:**
  - tabella comparativa dei risultati (deliverable della Fase 1 mancante);
  - roadmap delle Fasi 2–5 e `03_architettura.md` da allineare;
  - storyboard 2 e 4 da aggiornare;
  - testo delle issue #12, #14, #19, #21, #24 da aggiornare;
  - nuove issue per la RQ6.

## 2026-11-10 — Roadmap e issue allineate alla M1
- **Roadmap aggiornata** alle decisioni finali:
  - titolo proposto;
  - Fasi 2–7 con dataset, baseline congelate, metriche, RQ6, demo compatibile con le licenze;
  - struttura della tesi per RQ;
  - criteri delle milestone;
  - nuova sezione **"Azioni in sospeso"**: mail agli autori di PanDerm, ospedale, Zotero, tenute in conto per decidere più avanti.
- **Issue M2–M7 controllate** (20 aperte): 4 non allineate (#12, #14, #21, #24), 4 in parte, le altre quasi. Testi in inglese pronti; più 3 nuove issue per la RQ6 (M3.6, M4.5, M5.3). Da applicare su GitHub con il permesso di Cesar. Tabella al §7 di `08_revisione_M1.md`.

## 2026-11-10 — Correzioni completate e ricerca sulle pelli non chiare (M1.11, M1.12)
- **Nuova issue #32 (M1.12):** ricerca di dataset e studi su pelli non chiare per la RQ6 → [`09_pelli_non_chiare.md`](09_pelli_non_chiare.md).
  - Fototipi V–VI solo nel 5,8% di 1,1 milioni di immagini pubbliche; Sud America e Africa quasi assenti (Gröger 2026).
  - Fototipo riportato nel 2,1% delle immagini (Wen 2022).
  - Nessuno studio identifica pazienti ispanici o latinoamericani (Pérez-Lalinde 2026).
  - L'AI allarga il divario per tono nei medici di base (Groh 2024).
  - Il tipo di malattia pesa più del tono, e circa 10 esempi per categoria bastano per adattare un foundation model (Kunwor 2026): conferma l'ipotesi H6d.
  - I dataset "diversi" pubblici (SCIN, PASSION, DermaCon-IN) sono soprattutto di malattie infiammatorie; manca un dataset pubblico di **dermoscopie di tumori su pelli IV–VI**.
  
  Word S9 aggiornato; episodio 21 "Oltre le pelli chiare"; 11 voci BibTeX.
- **Correzioni della revisione completate:**
  - tabella comparativa dei risultati (§11 dello stato dell'arte, 28 studi);
  - `03_architettura.md` allineato (tabella dei tool di riferimento, report con catena di prove e lingua);
  - storyboard 2 e 4 aggiornati (8 livelli, 47 blocchi, nuovo livello "Inclusion");
  - **20 issue M2–M7 aggiornate su GitHub**;
  - nuove issue **#33 M3.6**, **#34 M4.5**, **#35 M5.3** per la RQ6.

### Prossimi passi
1. **Chiudere la Milestone 1** su GitHub (tutte le issue chiuse), quando Cesar conferma.
2. **Inviare** la mail agli autori di PanDerm/DermFM-Zero (Cesar), poi annotare la risposta nel file.
3. **Milestone 2 (dati):**
   - ambiente Python (M2.1);
   - download riproducibile di HAM10000, BCN20000 da Figshare, DDI, PAD-UFES-20, HIBA, PH2, Derm7pt e annotazioni di Chanda, con la **licenza registrata per immagine** (M2.2);
   - EDA e divisione per `lesion_id` (M2.3).
4. Testo completo di Anriot 2026; leggere i testi di MDR (regola 11) e AI Act consolidato prima della consegna della tesi.
5. (Opzionale) Caricare su NotebookLM i Word nuovi (S5–S9) e quelli aggiornati (S3).

## 2026-11-10 — Chiusura della Milestone 1
- **Dashboard di uscita dalla M1**, da usare come riferimento nelle milestone successive:
  - [`10_dashboard_M1.md`](10_dashboard_M1.md): si legge in due minuti; scelte chiave con il perché, RQ, pipeline, passi definiti con le issue, cose aperte, mappa dei documenti;
  - [`dashboard/neo_helper_M1.html`](dashboard/neo_helper_M1.html): versione interattiva in un solo file, senza dipendenze, in **italiano, inglese e spagnolo** (selettore in alto a destra). Sette viste:
    - panoramica con contatori animati e percorso della M1;
    - 14 scelte filtrabili per area, ognuna con perché, fonte e grafico;
    - 13 grafici di evidenze dalla letteratura;
    - le due pipeline animate;
    - le domande RQ1–RQ6;
    - la mappa dei 47 blocchi con ciambella e filtro per stato;
    - il Gantt M1–M7 con le issue.
  
  Tema chiaro e scuro, adatta al telefono, rispetta "riduci movimento".
- **Bilancio della M1:**
  - 42 schede di paper;
  - 9 file Word, 21 episodi audio;
  - 4 storyboard;
  - 6 domande di ricerca (cuore: RQ1, RQ2, RQ6);
  - 47 blocchi in 8 livelli;
  - 12 issue chiuse: #1–#10, #31, #32.
- **Milestone 1 chiusa** anche su GitHub.

### Prossimi passi
1. **Milestone 2 (dati e baseline):**
   - ambiente Python con percorso solo CPU (#11);
   - download con licenza e fonte per immagine (#12);
   - EDA e divisione per `lesion_id` (#13);
   - baseline congelate PanDerm, DINOv2, Derm Foundation, ImageNet (#14).
2. **Azioni di Cesar, da decidere:**
   - mail agli autori di PanDerm (bozza pronta);
   - ospedale di contatto;
   - Zotero sì o no.
3. Restano da leggere prima della tesi: il testo completo di Anriot 2026, MDR (regola 11) e il testo consolidato dell'AI Act.

## 2026-11-11 — Avvio della Milestone 2: piano e ambiente (M2.1)
- **Piano della M2 in sei pacchetti**, concordato con Cesar:
  - P1 ambiente (#11);
  - P2 registro dati e HAM10000 (#12, prima parte);
  - P3 EDA e divisione per lesione (#13);
  - P4 baseline congelate (#14);
  - P5 test esterni e dataset per la RQ6 (#12, #13);
  - P6 chiusura con dashboard (#36).
- **Decisioni:**
  - tutta la M2 gira sul Mac (M4, 24 GB): con i backbone congelati non serve una GPU in cloud. Kaggle è la riserva; la scelta per il fine-tuning si fa in M3.1;
  - dati, pesi e vettori **fuori dal repository**, nella cartella della variabile `NEO_DATA_DIR` (predefinita `~/neo-helper-data`);
  - ambiente con **`uv`** e Python 3.12 in `ml/.venv`, con versioni bloccate in `uv.lock`;
  - tracciamento con MLflow in locale;
  - baseline ImageNet: ResNet-50 e ViT-B/16;
  - Derm Foundation in un ambiente TensorFlow separato.
- **GitHub:** descrizione della milestone M2 aggiornata; issue #11, #12 e #14 allineate al piano; nuova issue **#36 M2.5** per la chiusura.
- **Pacchetto P1 fatto** (`ml/`):
  - `pyproject.toml`, `uv.lock`, [`ml/README.md`](../ml/README.md);
  - `neo/paths.py` (cartelle dei dati), `neo/device.py` (MPS, CUDA o CPU), `neo/check.py` (comando `neo-check`);
  - 12 test superati; prova con 10 immagini finte riuscita su MPS e su sola CPU;
  - PyTorch 2.15.0, timm 1.0.31; l'ambiente occupa 930 MB.
- `.gitignore`: le regole `data/` e `datasets/` valgono ora solo alla radice, così `ml/data/` può contenere gli script di download.
- **Stime da verificare:** dimensioni dei dataset (30–40 GB in tutto) e tempi di calcolo dei vettori; gli script mostreranno le dimensioni reali prima di scaricare.

### Prossimi passi
1. **P2:** schema del registro dati, script di download con modalità di prova, HAM10000 e annotazioni di Chanda.
2. **Azioni di Cesar:** richiesta di accesso a DDI e a Derm7pt; accettare i termini di Derm Foundation su Hugging Face.
