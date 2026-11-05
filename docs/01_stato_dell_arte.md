# 01 — Stato dell'arte (letteratura)

> Legenda: ✅ letto e schedato · 📖 da leggere · ⚠️ riferimento da verificare (anno/venue/dettagli)
> Per ogni paper letto: compilare la scheda in fondo al file.

## 1. Background clinico (da studiare prima di tutto)
- Melanoma: epidemiologia, perché la diagnosi precoce conta (sopravvivenza alta se diagnosticato in fase iniziale).
- **Regola ABCDE** (clinica): Asimmetria, Bordi, Colore, Diametro, Evoluzione.
- **Dermatoscopia** e algoritmi diagnostici:
  - ABCD rule of dermoscopy (Stolz) → punteggio TDS
  - **7-point checklist** (Argenziano) → criteri maggiori/minori
  - Pattern analysis, Menzies method, CASH
- Segno del "brutto anatroccolo" (ugly duckling): confronto tra nevi dello stesso paziente → rilevante per **total body photography** (ISIC 2024).
- Classi tipiche nei dataset: nevo melanocitico (NV), melanoma (MEL), cheratosi seborroica (BKL), carcinoma basocellulare (BCC), cheratosi attinica (AK), carcinoma squamocellulare (SCC), dermatofibroma (DF), lesioni vascolari (VASC).

✅ Sintesi: [papers/00_background_clinico.md](papers/00_background_clinico.md) (include Argenziano 1998 e 2003).
📖 Fonte consigliata per approfondire: Argenziano G. et al., *Dermoscopy of pigmented skin lesions* (JAAD 2003, consensus net meeting) ⚠️; un manuale di dermatoscopia (es. Marghoob / Kittler).

## 2. Paper fondativi di Deep Learning in dermatologia
| Paper | Perché è importante | Stato |
|-------|---------------------|-------|
| Esteva A. et al., *Dermatologist-level classification of skin cancer with deep neural networks*, **Nature 2017** | Il paper "big bang": Inception-v3, livello dermatologo | ✅ [scheda](papers/2017_esteva_dermatologist-level.md) |
| Haenssle H.A. et al., *Man against machine…*, **Annals of Oncology 2018** | CNN vs 58 dermatologi su dermatoscopia | ✅ [scheda](papers/2018_haenssle_man-against-machine.md) |
| Brinker T.J. et al., *Deep learning outperformed 136 of 157 dermatologists…*, **Eur J Cancer 2019** | Confronto su larga scala | ✅ [scheda](papers/2019_brinker_136-of-157.md) |
| Tschandl P. et al., *The HAM10000 dataset*, **Scientific Data 2018** | Dataset di riferimento | ✅ [scheda](papers/2018_tschandl_ham10000.md) |
| Tschandl P. et al., *Comparison of the accuracy of human readers versus machine-learning algorithms…*, **Lancet Oncology 2019** | Benchmark open (ISIC 2018) uomo vs macchina | ✅ [scheda](papers/2019_tschandl_human-vs-machine-isic2018.md) |
| Tschandl P. et al., *Human–computer collaboration for skin cancer recognition*, **Nature Medicine 2020** | **Fondamentale per il tuo progetto**: come l'AI aiuta (o danneggia) il medico a seconda di come viene presentata | ✅ [scheda](papers/2020_tschandl_human-computer-collaboration.md) |
| Codella N. et al., report ISIC Challenge 2017/2018 (arXiv) | Descrizione task: segmentazione, attributi, classificazione | 📖 |
| Combalia M. et al., *BCN20000: Dermoscopic lesions in the wild*, 2019 (arXiv) ⚠️ | Dataset "difficile", base di ISIC 2019 | 📖 |
| Rotemberg V. et al., *A patient-centric dataset of images and metadata…* (ISIC 2020), **Scientific Data 2021** | Dataset con contesto paziente | 📖 |
| Kurtansky N. et al., SLICE-3D / ISIC 2024 (Scientific Data 2024) ⚠️ | Crop da total body photography, simili a foto smartphone | 📖 |

## 3. Foundation model e vision-language in dermatologia
| Paper / modello | Note | Stato |
|-----------------|------|-------|
| Kim C. et al., **MONET** — *Transparent medical image AI via an image–text foundation model grounded in medical literature*, **Nature Medicine 2024** | CLIP-like addestrato su immagini dermatologiche + testo; **annotazione automatica di concetti** → spiegabilità | ✅ [scheda](papers/2024_kim_monet.md) (preprint completo) |
| **PanDerm** (Yan S. et al., *Nature Medicine* 2025) | Foundation model multimodale per dermatologia, 28 task; pesi CC-BY-NC-ND | ✅ [scheda](papers/2025_yan_panderm.md) |
| **Derm Foundation** (Google Health) | Embedding model per immagini dermatologiche (pesi gated su Hugging Face); nessun paper dedicato | ✅ [in §3](papers/S3_introduzione.md) |
| Liu Y. et al., *A deep learning system for differential diagnosis of skin diseases*, **Nature Medicine 2020** (Google) | Diagnosi differenziale su 26 condizioni, immagini cliniche | 📖 |
| SkinGPT-4 (Zhou J. et al., *Nature Communications* 2024) | LLM multimodale per dermatologia; valutazione debole | ✅ [scheda](papers/2024_zhou_skingpt4.md) |
| Valutazioni di GPT-4V / Gemini / Claude su immagini dermatologiche (vari, 2023–2025) | **Cautela**: LLM generalisti spesso inaffidabili come classificatori → usarli come orchestratori/narratori, non come diagnosti | ✅ [scheda](papers/2026_bhagwat_mllm-fitzpatrick.md) Bhagwat 2026 (testo completo) |
| Anriot et al., *Limits of AI models for skin cancer diagnosis in realistic settings*, **JAMA Dermatology 2026** | PanDerm in condizioni reali: < esperti oltre 10 anni | ✅ [scheda](papers/2026_anriot_limits-realistic-settings.md) (solo abstract) |
| DINOv2 / DINOv3, MedSAM, SAM 2 | Backbone e segmentazione general-purpose / medical | 📖 |

## 4. Bias, fairness e generalizzazione
| Paper | Note | Stato |
|-------|------|-------|
| Groh M. et al., *Evaluating deep neural networks trained on clinical images in dermatology with the Fitzpatrick 17k dataset*, CVPR-W 2021 | Annotazioni del fototipo | ✅ [scheda](papers/2021_groh_fitzpatrick17k.md) |
| Daneshjou R. et al., *Disparities in dermatology AI performance on a diverse, curated clinical image set* (**DDI**), **Science Advances 2022** | Calo di performance su pelli scure | ✅ [scheda](papers/2022_daneshjou_ddi.md) |
| Winkler J.K. et al., *Association between surgical skin markings… and diagnostic performance of a CNN*, **JAMA Dermatology 2019** | Artefatti (inchiostro) → **shortcut learning** | ✅ [scheda](papers/2019_winkler_surgical-markings.md) (abstract) |
| Bissoto A. et al., studi su bias/artefatti in ISIC (2019–2020) ⚠️ | I modelli imparano "scorciatoie" | 📖 |
| Daneshjou R. et al., *Checklist for evaluation of image-based AI reports in dermatology* (**CLEAR Derm**), JAMA Dermatology 2022 | **Da usare come checklist per la tua valutazione** | ✅ [scheda](papers/2022_daneshjou_clear-derm.md) |

## 5. Explainability, incertezza e collaborazione uomo-AI
Introduzione: [S5_introduzione.md](papers/S5_introduzione.md).

| Paper | Note | Stato |
|-------|------|-------|
| Selvaraju R.R. et al., **Grad-CAM**, ICCV 2017 | Heatmap per qualsiasi CNN; dice dove, non perché | ✅ [scheda](papers/2017_selvaraju_gradcam.md) (sintesi alphaXiv) |
| Adebayo J. et al., *Sanity checks for saliency maps*, NeurIPS 2018 | Molte heatmap non dipendono dal modello; Grad-CAM supera i test | ✅ [scheda](papers/2018_adebayo_sanity-checks.md) (sintesi alphaXiv) |
| Tschandl P. et al., *Content-based dermatoscopic image retrieval*, **Br J Dermatol 2019** | 16 casi simili ≈ softmax; aiuta su classi nuove | ✅ [scheda](papers/2019_tschandl_cbir.md) |
| Koh P.W. et al., **Concept Bottleneck Models**, ICML 2020 | Concetti leggibili e correggibili dal medico | ✅ [scheda](papers/2020_koh_concept-bottleneck.md) (sintesi alphaXiv) |
| Angelopoulos A.N. & Bates S., *Gentle introduction to conformal prediction*, 2021 | Insiemi di diagnosi con copertura garantita | ✅ [scheda](papers/2021_angelopoulos_conformal.md) (sintesi alphaXiv) |
| Chanda T. et al., *Dermatologist-like explainable AI…*, **Nat Commun 2024** | Criteri dermoscopici localizzati su HAM10000; +fiducia, non +accuratezza; annotazioni pubblicate | ✅ [scheda](papers/2024_chanda_xai-dermatologist.md) |
| Krakowski I. et al., *Human-AI interaction in skin cancer diagnosis* (meta-analisi), **npj Digit Med 2024** | Con AI sens. 74,8→81,1%, spec. 81,5→86,1%; più beneficio ai non dermatologi | ✅ [scheda](papers/2024_krakowski_human-ai-meta.md) |
| Tschandl 2020 (§2) | La forma dell'output conta; l'AI difettosa trascina i medici | ✅ (§2) |
| TCAV (Kim 2018); calibrazione/conformal su ISIC ⚠️ | Approfondimenti | 📖 |

## 6. LLM, sistemi multi-agente, MCP
Introduzione: [S6_introduzione.md](papers/S6_introduzione.md).

| Fonte | Note | Stato |
|-------|------|-------|
| Anthropic, *Building effective agents* (blog, dic 2024) | Workflow vs agenti, **orchestrator-workers**, evaluator-optimizer; partire semplice | ✅ [scheda](papers/2024_anthropic_building-agents.md) |
| Anthropic, *How we built our multi-agent research system* (giu 2025) | +90,2% vs agente singolo, circa 15 volte i token; quando non conviene | ✅ [scheda](papers/2025_anthropic_multi-agent-research.md) |
| Specifica **Model Context Protocol** (2025-06-18; ultima 2026-07-28) | Tool, resource, prompt; host/client/server; principi di sicurezza | ✅ [scheda](papers/2024_mcp_specification.md) (pagine introduttive) |
| Tu T. et al., **AMIE**, Nature 2025 (+ seguito Nature 2026) | LLM conversazionale diagnostico; OSCE simulati; non pronto per la clinica | ✅ [scheda](papers/2025_tu_amie.md) (abstract + discussione) |
| Kim Y. et al., **MDAgents**, NeurIPS 2024 | Squadra di LLM adattata alla complessità | ✅ [scheda](papers/2024_kim_mdagents.md) (sintesi alphaXiv) |
| Liu Y. et al., **DermAgent**, arXiv 2026 | Agente dermatologico con tool, RAG e critico a regole: **il più vicino a Neo Helper** | ✅ [scheda](papers/2026_liu_dermagent.md) (sintesi alphaXiv) |
| Vatsal S. et al., *Agentic AI in Healthcare & Medicine: seven-dimensional taxonomy*, IEEE Access 2026 | Rassegna di 49 studi: mancano HITL, recupero errori, sicurezza, regole | ✅ [scheda](papers/2026_vatsal_agentic-taxonomy.md) (sintesi alphaXiv) |
| MedAgents (Tang X. et al., 2024) ⚠️; survey "LLM-based agents in medicine" (arXiv 2502.11211) | Approfondimenti | 📖 |

## 7. Prodotti esistenti e regolatorio
- **SkinVision** (app consumer, CE marked), **Miiskin**, **Google DermAssist** (CE class I, ora ritirato/limitato ⚠️).
- **DermaSensor**: primo dispositivo AI per cancro cutaneo autorizzato FDA per medici di base (gen 2024) — basato su spettroscopia, non immagini.
- **Moleanalyzer pro** (FotoFinder), **Derm** di Skin Analytics (CE classe III nel 2025 ⚠️).
- Revisioni critiche su app smartphone: Freeman K. et al., BMJ 2020 (*Algorithm based smartphone apps to assess risk of skin cancer in adults: systematic review*).
- Vedi [04_etica_regolatorio.md](04_etica_regolatorio.md).

## 8. Gap identificabili (ipotesi per il contributo originale)
> ⚠️ Da rivedere nella M1.10 alla luce di **DermAgent** (2026), che già orchestra modelli dermatologici con tool e un critico: vedi le differenze proposte in [S6_introduzione.md](papers/S6_introduzione.md).

1. Pochi sistemi open **end-to-end** (modello + spiegazione + interfaccia + mobile) riproducibili.
2. Integrazione di **criteri dermoscopici espliciti** (ABCD/7-point) con classificatori DL, presentata al medico in modo strutturato.
3. Uso di **architetture multi-agente/MCP** in dermatologia: quasi inesplorato in letteratura peer-reviewed (da verificare con ricerca sistematica).
4. **Quantificazione dell'incertezza** e "abstention" (il sistema dice "non so / immagine inadatta").

## 9. Strategia di ricerca bibliografica
- Banche dati: PubMed, Google Scholar, Semantic Scholar, arXiv (cs.CV, eess.IV), IEEE Xplore.
- Query base:
  - `(melanoma OR "skin lesion" OR nevus) AND (dermoscopy OR dermatoscopy) AND ("deep learning" OR CNN OR transformer)`
  - `dermatology AND ("foundation model" OR "vision-language")`
  - `("multi-agent" OR "LLM agent") AND (medical imaging OR dermatology)`
- Metodo: schema PRISMA semplificato (identificati → screening → inclusi), finestra 2017–2026.
- Strumenti: Zotero, Connected Papers / ResearchRabbit, Semantic Scholar alerts.

---

## Scheda di lettura (template)
```
### [Autore Anno] Titolo
- Venue / DOI:
- Task: (classificazione / segmentazione / ...)
- Dati: (dataset, n immagini, tipo: dermatoscopiche/cliniche)
- Metodo:
- Risultati principali (metriche):
- Limiti dichiarati / che noto:
- Cosa mi serve per Neo Helper:
```
