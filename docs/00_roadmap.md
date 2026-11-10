# 00 — Roadmap (impostazione "tesi magistrale")

## Titolo di lavoro
**"Neo Helper: un assistente agentico, spiegabile e accessibile per la diagnosi dermoscopica — incertezza garantita, orchestrazione tramite Model Context Protocol e valutazione su popolazioni latinoamericane"** (proposta del 2026-11-10, da [07_domande_di_ricerca.md](07_domande_di_ricerca.md))

Titolo iniziale (ottobre 2026): *"Un sistema multi-agente per il supporto alla diagnosi dermatoscopica di lesioni melanocitiche: classificazione, spiegabilità e orchestrazione tramite Model Context Protocol"*.

## Domande di ricerca (confermate il 2026-11-10 — dettagli in [07_domande_di_ricerca.md](07_domande_di_ricerca.md))
- **RQ1 — Vedere:** quanto rende PanDerm congelato con una testa lineare rispetto a DINOv2, ImageNet e Derm Foundation, su HAM10000 e su test esterni (BCN20000, DDI, PAD-UFES-20, HIBA, PH2, Derm7pt)? Quanto si perde con un backbone a licenza libera?
- **RQ2 — Dubitare:** calibrazione e insiemi conformal permettono di dire "non so" in modo affidabile su lesioni mai viste, centri nuovi e fototipi diversi? A quale costo in invii allo specialista?
- **RQ3 — Spiegare:** le spiegazioni (criteri dermoscopici, heatmap, casi simili) sono fedeli al modello e concordano con le annotazioni dei dermatologi?
- **RQ4 — Coordinare:** un agente con tool MCP e un critico a regole produce report tracciabili senza numeri inventati? Il multi-agente (v3) vale il suo costo rispetto all'agente singolo (v2)?
- **RQ5 (facoltativa) — Aiutare:** con l'ospedale, Neo Helper migliora le decisioni dei medici non specialisti, e quanto lo si segue quando sbaglia?
- **RQ6 — Includere:** come si comporta l'insieme degli strumenti di AI (lo stato dell'arte) su fototipi di pelli latinoamericane e, dove ci sono dati, asiatiche (HIBA, PAD-UFES-20, lesioni acrali di BALD)? Cosa serve perché centri di ricerca latinoamericani possano usarlo e adattarlo con pochi dati locali?

La bozza di ottobre (RQ1–RQ4) è confrontata con questa proposta nella tabella finale di `07_domande_di_ricerca.md`.

## Ipotesi di scope (cosa NON facciamo)
- Non è un dispositivo medico, non dà diagnosi al paziente: è **per il medico**, come "second opinion".
- Niente raccolta di dati reali di pazienti nella prima versione: solo dataset pubblici.
- Target iniziale: **7 classi di HAM10000 + punteggio di malignità** su immagini **dermatoscopiche** (P1–P2); ISIC 2019 (8 classi) dopo la baseline. Le immagini cliniche da smartphone sono un'estensione.
- Niente ensemble "da gara": la priorità è l'affidabilità ("non so", spiegazioni verificate, test esterni), non l'ultimo decimale.
- **Cuore della tesi:** RQ1, RQ2 e RQ6, che usano gli stessi esperimenti e gli stessi dati. Poi RQ3 e RQ4. RQ5, web completo e mobile possono restare prototipi (vedi [08_revisione_M1.md](08_revisione_M1.md) §4).

---

## Fasi

### Fase 0 — Setup (settimana 1)
- [x] Cartella documentazione MD
- [x] Repo GitHub pubblico (licenza: MIT o Apache-2.0 per il codice; attenzione: le licenze dei **dataset** sono spesso CC-BY-NC → i pesi addestrati vanno distribuiti rispettandole)
- [ ] Ambiente: Python 3.11+, `uv` o conda, PyTorch, GPU (locale Apple Silicon MPS / Colab / Kaggle / cloud)
- [ ] Gestore di riferimenti bibliografici (Zotero + export BibTeX in `docs/refs.bib`)

### Fase 1 — Revisione della letteratura (settimane 1–4)
Deliverable: `01_stato_dell_arte.md` completo + tabella comparativa dei risultati.
- [x] Clinica di base: melanoma, nevi, dermatoscopia, regola ABCDE, ABCD dermoscopico, 7-point checklist, pattern analysis
- [x] Paper fondativi DL in dermatologia (Esteva 2017, Haenssle 2018, Tschandl 2019/2020…)
- [x] Challenge ISIC 2016–2020, ISIC 2024 (SLICE-3D)
- [x] Foundation model e vision-language in dermatologia (MONET, PanDerm, Derm Foundation…)
- [x] Bias e fairness (Fitzpatrick17k, DDI)
- [x] Explainability e human-AI collaboration
- [x] Sistemi multi-agente e LLM in medicina; MCP
- [x] Prodotti esistenti e regolatorio (SkinVision, DermaSensor, MDR/AI Act)
- [x] Dataset e studi su pelli non chiare per la RQ6 (M1.12, [09_pelli_non_chiare.md](09_pelli_non_chiare.md))
- [x] Tabella comparativa dei risultati (§11 di `01_stato_dell_arte.md`)

### Fase 2 — Dati e baseline (settimane 4–7) · M2
Deliverable: script di download riproducibili, registro dati con **licenza e fonte per immagine**, notebook EDA, vettori salvati, prime baseline.
- [ ] Ambiente Python (M2.1), con un percorso che funziona anche **solo su CPU** (RQ6)
- [ ] Download (M2.2):
  - **HAM10000** (training);
  - test esterni: **BCN20000 da Figshare** (CC BY 4.0), **DDI** (accesso su richiesta), **PAD-UFES-20**, **HIBA**, **PH2**, **Derm7pt**;
  - per la RQ6: **BALD** (acrali), **MSKCC Skin Tone**, cheratosi cilene;
  - **annotazioni di Chanda** (Figshare).
  
  ISIC 2019 completo **dopo** la baseline. Verificare le licenze di DDI, PH2 e Derm7pt.
- [ ] Registro dati comune (campi del §4.1 di `05_scelte_e_pipeline.md`), compresi `license` e `source`
- [ ] EDA (M2.3):
  - classi e squilibrio;
  - duplicati tra dataset (HAM10000 ⊂ ISIC 2018/2019; BCN20000 su ISIC e su Figshare);
  - **controllo degli artefatti con MONET** (penna, righello, adesivo, bordo nero) per classe;
  - divisione **per `lesion_id`** 70/15/15
- [ ] Baseline (M2.4):
  - **vettori congelati + testa lineare** per PanDerm, DINOv2, Derm Foundation e ImageNet, sugli stessi split;
  - metriche: accuratezza bilanciata, AUC per classe, specificità a sensibilità 90/95% per il punteggio di malignità, pAUC > 80% di sensibilità, intervalli bootstrap

### Fase 3 — Modello finale e valutazione (settimane 7–13) · M3
Deliverable: modello calibrato con "non so", spiegazioni verificate, report di valutazione esterna e per sottogruppi (RQ1, RQ2, RQ3, RQ6).
- [ ] Esperimento di **fine-tuning** (ultimi blocchi o LoRA) contro backbone congelato; scelta finale del backbone; percorso con licenza libera (M3.1)
- [ ] **Segmentazione** (U-Net o MedSAM, da scegliere), contando i fallimenti (Jaccard < 0,65) (M3.2)
- [ ] **Calibrazione** (temperature scaling, ECE), **insiemi conformal** (anche per classe) e **controllo fuori distribuzione**; test con le lesioni sconosciute di BCN20000; tumori mancati (M3.3, RQ2)
- [ ] **Spiegabilità** (M3.4, RQ3):
  - Grad-CAM (variante per ViT) con **test di sanità**;
  - **concetti MONET** validati su Derm7pt e sulle annotazioni di Chanda;
  - concept bottleneck facoltativo;
  - **casi simili** (k = 16)
- [ ] **Valutazione esterna** su BCN20000, DDI, PAD-UFES-20, HIBA, PH2, Derm7pt, per fototipo, sede, centro e artefatto; tabella CLEAR Derm (M3.5, RQ1)
- [ ] **Popolazioni latinoamericane e lesioni acrali** (M3.6, RQ6; base: [09_pelli_non_chiare.md](09_pelli_non_chiare.md)):
  - HIBA, PAD-UFES-20, BALD;
  - **adattamento con pochi dati locali** (solo la testa);
  - ricerca di dataset asiatici
- [ ] Letteratura "al momento giusto": segmentazione (MedSAM), DINOv2, calibrazione e conformal in dermatologia, epidemiologia del melanoma acrale
- [ ] Export per il mobile (ONNX / CoreML / TFLite) solo se serve alla Fase 6

### Fase 4 — Tool MCP e agenti (settimane 11–16) · M4
Deliverable: server MCP `neo-vision`, agente singolo e multi-agente confrontati (RQ4). Vedi [03_architettura.md](03_architettura.md) e [05_scelte_e_pipeline.md](05_scelte_e_pipeline.md) §3.2.
- [ ] **v0**, pipeline fissa senza LLM: qualità → segmentazione → vettore → classificazione + insieme conformal → spiegazioni → report a modello fisso (M4.1)
- [ ] **v1**, server MCP con i tool `check_quality`, `segment_lesion`, `embed_image`, `classify`, `predict_set`, `explain_heatmap`, `describe_concepts`, `similar_cases`, più le resource: model card, data card, soglie (M4.2)
- [ ] **v2**, un orchestratore (M4.3):
  - report JSON con **catena di prove**;
  - numeri solo dai tool;
  - scelta dell'LLM (locale o open contro API) per la privacy
- [ ] **v3**, multi-agente con **critico a regole** e percorso guidato dall'incertezza; confronto v0, v2 e v3 su accuratezza, numeri inventati, conflitti intercettati, token e tempo; **casi trappola** (M4.4)
- [ ] **Report multilingue** (italiano, inglese, spagnolo, portoghese) (M4.5, RQ6)

### Fase 5 — Interfaccia web (settimane 15–18) · M5
Deliverable: demo utilizzabile, compatibile con le licenze.
- [ ] Demo rapida con Gradio (M5.1):
  - **solo per ricerca** se usa PanDerm o MONET;
  - **pubblica** solo con un backbone libero (DINOv2) e immagini dei dataset, senza conservare le immagini;
  - avviso sempre visibile
- [ ] Web app (M5.2): FastAPI + Next.js con caricamento, controllo qualità, probabilità, insieme conformal, criteri, casi simili, heatmap, report PDF, **più lingue**
- [ ] **Pacchetto per centri con poche risorse** (M5.3, RQ6): CPU, licenze aperte, LLM locale, guida per aggiungere i propri dati

### Fase 6 — App mobile (settimane 18–21) · M6
Deliverable: prototipo installabile.
- [ ] Expo (React Native) con guida all'acquisizione: messa a fuoco, luce, distanza, lente dermoscopica per smartphone come DERM (M6.1)
- [ ] Inferenza **sul dispositivo** (backbone leggero) o **sul server** (PanDerm e agenti): misura di latenza e accuratezza (M6.2)

### Fase 7 — Valutazione finale e scrittura (settimane 21–26) · M7
- [ ] Esperimenti finali e ablazioni (singolo modello contro agente, v2 contro v3)
- [ ] (Facoltativo, RQ5) studio con medici non specialisti, solo con l'ospedale e il comitato etico
- [ ] Model card, data card (licenza per fonte), lista volontaria dell'AI Act, CLEAR Derm (M7.1)
- [ ] Scrittura della tesi (M7.2); ricontrollare le regole (MDR, AI Act) prima della consegna
- [ ] Release con DOI su Zenodo, senza pesi di PanDerm modificati (M7.3)

---

## Struttura della tesi finale
1. Introduzione e motivazione, compreso lo scopo di inclusione per l'America Latina
2. Background clinico (melanoma, dermoscopia, criteri diagnostici, melanoma acrale)
3. Stato dell'arte (DL in dermatologia, foundation model, bias, spiegabilità, agenti e MCP, challenge ISIC, prodotti e regole)
4. Dati e metodologia (dataset, licenze, divisione per lesione, metriche, CLEAR Derm)
5. **RQ1** — Modelli: PanDerm contro backbone liberi, test esterni
6. **RQ2** — Incertezza e "non so"
7. **RQ6** — Popolazioni latinoamericane, lesioni acrali, adattamento locale, accessibilità
8. **RQ3** — Spiegazioni verificate
9. **RQ4** — Tool MCP e agenti: report, sicurezza, costi
10. Applicazioni web e mobile (prototipi) e, se fatta, **RQ5**
11. Etica, licenze, regole, limiti
12. Conclusioni e sviluppi futuri

## Milestone
| # | Milestone | Criterio di completamento |
|---|-----------|---------------------------|
| M1 | Letteratura chiusa | ≥ 30 paper schedati, RQ definitive, revisione finale (M1.11) chiusa |
| M2 | Baseline | Dati scaricati con licenza e fonte per immagine; divisione per `lesion_id`; baseline con vettori congelati (PanDerm, DINOv2, Derm Foundation, ImageNet) con accuratezza bilanciata e metriche di malignità su HAM10000; notebook riproducibile |
| M3 | Modello finale | Calibrato, con "non so" conformal, spiegazioni verificate; valutato su ≥ 3 test esterni, per fototipo e su HIBA, PAD-UFES-20 e BALD (RQ6) |
| M4 | MCP + agenti | v0, v1 (server MCP), v2 e v3 funzionanti; report con catena di prove; confronto di costi e sicurezza su casi trappola |
| M5 | Demo web | Demo compatibile con le licenze, in più lingue, con avvisi; pacchetto per centri con poche risorse |
| M6 | App mobile | Prototipo installabile con guida all'acquisizione |
| M7 | Release | Repo documentato (model card, data card), tesi, DOI Zenodo |

## Azioni in sospeso (di Cesar)
- [ ] **Mail agli autori di PanDerm/DermFM-Zero** sulla licenza: bozza pronta in [corrispondenza/](corrispondenza/2026-11-04_mail_autori_panderm.md). Da decidere quando inviarla.
- [ ] **Ospedale di contatto:** dati nuovi, studio facoltativo RQ5, comitato etico. Istruzioni per gli annotatori pronte in [annotazione/](annotazione/). Da decidere più avanti.
- [ ] **Zotero sì o no:** gestore della bibliografia (Fase 0, mai fatto). Oggi `docs/refs.bib` è scritto a mano.
