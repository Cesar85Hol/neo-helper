# 00 — Roadmap (impostazione "tesi magistrale")

## Titolo di lavoro
**"Un sistema multi-agente per il supporto alla diagnosi dermatoscopica di lesioni melanocitiche: classificazione, spiegabilità e orchestrazione tramite Model Context Protocol"**

## Domande di ricerca (bozza — da raffinare dopo la Fase 1)
- **RQ1** — Quanto si avvicinano i modelli open (CNN/ViT/foundation model dermatologici) allo stato dell'arte su benchmark pubblici (ISIC, HAM10000, BCN20000), con metriche clinicamente rilevanti (sensibilità per melanoma a specificità fissata, AUROC, calibrazione)?
- **RQ2** — Un'architettura **multi-agente** (agenti specializzati: qualità immagine, segmentazione, classificazione, criteri ABCD/7-point, spiegazione, report) migliora **affidabilità, trasparenza e utilità percepita** rispetto a un singolo classificatore "black box"?
- **RQ3** — Come si comporta il sistema su **pelli diverse (Fitzpatrick IV–VI)** e su immagini **cliniche da smartphone** vs dermatoscopiche (domain shift)?
- **RQ4** (opzionale) — Un LLM orchestratore, con tool esposti via MCP, introduce rischi (allucinazioni, overconfidence) e come mitigarli?

## Ipotesi di scope (cosa NON facciamo)
- Non è un dispositivo medico, non dà diagnosi al paziente: è **per il medico**, come "second opinion".
- Niente raccolta di dati reali di pazienti nella prima versione: solo dataset pubblici.
- Target iniziale: classificazione **benigno / maligno** + multiclasse (ISIC 8–9 classi) su immagini **dermatoscopiche**. Le immagini cliniche smartphone sono un'estensione.

---

## Fasi

### Fase 0 — Setup (settimana 1)
- [x] Cartella documentazione MD
- [ ] Repo GitHub pubblico (licenza: MIT o Apache-2.0 per il codice; attenzione: le licenze dei **dataset** sono spesso CC-BY-NC → i pesi addestrati vanno distribuiti rispettandole)
- [ ] Ambiente: Python 3.11+, `uv` o conda, PyTorch, GPU (locale Apple Silicon MPS / Colab / Kaggle / cloud)
- [ ] Gestore di riferimenti bibliografici (Zotero + export BibTeX in `docs/refs.bib`)

### Fase 1 — Revisione della letteratura (settimane 1–4)
Deliverable: `01_stato_dell_arte.md` completo + tabella comparativa dei risultati.
- [ ] Clinica di base: melanoma, nevi, dermatoscopia, regola ABCDE, ABCD dermoscopico, 7-point checklist, pattern analysis
- [ ] Paper fondativi DL in dermatologia (Esteva 2017, Haenssle 2018, Tschandl 2019/2020…)
- [ ] Challenge ISIC 2016–2020, ISIC 2024 (SLICE-3D)
- [ ] Foundation model e vision-language in dermatologia (MONET, PanDerm, Derm Foundation…)
- [ ] Bias e fairness (Fitzpatrick17k, DDI)
- [ ] Explainability e human-AI collaboration
- [ ] Sistemi multi-agente e LLM in medicina; MCP
- [ ] Prodotti esistenti e regolatorio (SkinVision, DermaSensor, MDR/AI Act)

### Fase 2 — Dati e analisi esplorativa (settimane 4–6)
Deliverable: notebook EDA + `data/README.md` con provenienza e licenze.
- [ ] Download ISIC 2019/2020 + HAM10000 (+ metadati)
- [ ] EDA: distribuzione classi, sbilanciamento, duplicati tra dataset (**leakage!** HAM10000 ⊂ ISIC 2018/2019), stessi pazienti in train/test, artefatti (righelli, peli, inchiostro, cerchi del dermatoscopio)
- [ ] Split **per paziente/lesione**, non per immagine
- [ ] Definire test set esterni (es. PH2, Derm7pt, PAD-UFES-20, DDI) per valutare la generalizzazione

### Fase 3 — Modelli e valutazione (settimane 6–12)
Deliverable: tabella risultati, modelli salvati, report di valutazione.
- [ ] **Baseline**: ResNet50 / EfficientNet pre-addestrato ImageNet (fine-tuning)
- [ ] **Modelli moderni**: ConvNeXt, ViT/DINOv2, EVA; confronto
- [ ] **Foundation model** dermatologico come feature extractor + linear probe (se i pesi sono accessibili)
- [ ] **Segmentazione** lesione (U-Net / SAM / MedSAM) → utile per ABCD e per ritagliare
- [ ] Gestione sbilanciamento: loss pesata/focal, oversampling, augmentation (anche rimozione peli)
- [ ] **Calibrazione** (temperature scaling, ECE) e **incertezza** (MC-dropout, ensemble, conformal prediction)
- [ ] **Explainability**: Grad-CAM, attention maps, concept-based (MONET-like), criteri dermoscopici
- [ ] Metriche: AUROC, balanced accuracy, sensibilità @ specificità 80/90%, pAUC (ISIC 2024), ECE, analisi per sottogruppi
- [ ] Export: ONNX / CoreML / TFLite per il mobile

### Fase 4 — Pool di agenti + MCP (settimane 10–15)
Deliverable: server MCP funzionante + orchestratore + test. Vedi [03_architettura.md](03_architettura.md).
- [ ] Ogni capacità (qualità immagine, segmentazione, classificazione, spiegazione, ricerca letteratura) come **tool MCP**
- [ ] Agenti specializzati + **orchestratore** (pattern orchestrator–workers)
- [ ] Output strutturato (JSON schema) → report per il medico
- [ ] Guardrail: l'LLM non inventa probabilità, le prende dai tool; disclaimer sempre presenti
- [ ] Valutazione: correttezza del report, coerenza, tracciabilità

### Fase 5 — Interfaccia web (settimane 12–16)
Deliverable: demo web online.
- [ ] Prototipo rapido con **Gradio/Streamlit** (anche su Hugging Face Spaces)
- [ ] Versione "vera": **FastAPI** backend + **Next.js/React** frontend
- [ ] Funzioni: upload, crop/qualità, heatmap sovrapposta, probabilità calibrate, criteri ABCD, report PDF, storico confronti nel tempo (follow-up)

### Fase 6 — App mobile (settimane 15–19)
Deliverable: app installabile (TestFlight / APK).
- [ ] Scelta framework: **React Native (Expo)** (riuso con il web) oppure **Flutter**
- [ ] Acquisizione da fotocamera + guida alla qualità (messa a fuoco, luce, distanza)
- [ ] Inferenza **on-device** (CoreML/TFLite, privacy) vs **server** (modelli più grandi + agenti)

### Fase 7 — Valutazione finale e scrittura (settimane 19–24)
- [ ] Esperimenti finali, ablation (singolo modello vs multi-agente)
- [ ] (Opzionale) valutazione qualitativa con 1–3 medici/dermatologi su casi pubblici: usabilità (SUS), utilità percepita
- [ ] Scrittura: struttura tesi (sotto)
- [ ] Release GitHub: README, model card, data card, limiti noti

---

## Struttura della "tesi" finale
1. Introduzione e motivazione
2. Background clinico (melanoma, dermatoscopia, criteri diagnostici)
3. Stato dell'arte (DL in dermatologia, foundation model, multi-agent/LLM, MCP)
4. Dati e metodologia
5. Modelli di classificazione/segmentazione ed esperimenti
6. Architettura multi-agente e integrazione MCP
7. Applicazioni web e mobile
8. Valutazione (quantitativa, fairness, qualitativa)
9. Etica, regolatorio, limiti
10. Conclusioni e sviluppi futuri

## Milestone
| # | Milestone | Criterio di completamento |
|---|-----------|---------------------------|
| M1 | Letteratura chiusa | ≥ 30 paper schedati, RQ definitive |
| M2 | Baseline | AUROC su ISIC val con split corretto, notebook riproducibile |
| M3 | Modello finale | Calibrato, con XAI, testato su ≥ 1 dataset esterno |
| M4 | MCP + agenti | Orchestratore produce report strutturato end-to-end |
| M5 | Demo web | Online e usabile |
| M6 | App mobile | Build installabile |
| M7 | Release | Repo pubblico documentato + documento finale |
