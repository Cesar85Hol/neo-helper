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

📖 Fonte consigliata per iniziare: Argenziano G. et al., *Dermoscopy of pigmented skin lesions* (JAAD 2003, consensus net meeting) ⚠️; un manuale di dermatoscopia (es. Marghoob / Kittler).

## 2. Paper fondativi di Deep Learning in dermatologia
| Paper | Perché è importante | Stato |
|-------|---------------------|-------|
| Esteva A. et al., *Dermatologist-level classification of skin cancer with deep neural networks*, **Nature 2017** | Il paper "big bang": Inception-v3, livello dermatologo | 📖 |
| Haenssle H.A. et al., *Man against machine…*, **Annals of Oncology 2018** | CNN vs 58 dermatologi su dermatoscopia | 📖 |
| Brinker T.J. et al., *Deep learning outperformed 136 of 157 dermatologists…*, **Eur J Cancer 2019** | Confronto su larga scala | 📖 |
| Tschandl P. et al., *The HAM10000 dataset*, **Scientific Data 2018** | Dataset di riferimento | 📖 |
| Tschandl P. et al., *Comparison of the accuracy of human readers versus machine-learning algorithms…*, **Lancet Oncology 2019** | Benchmark open (ISIC 2018) uomo vs macchina | 📖 |
| Tschandl P. et al., *Human–computer collaboration for skin cancer recognition*, **Nature Medicine 2020** | **Fondamentale per il tuo progetto**: come l'AI aiuta (o danneggia) il medico a seconda di come viene presentata | 📖 |
| Codella N. et al., report ISIC Challenge 2017/2018 (arXiv) | Descrizione task: segmentazione, attributi, classificazione | 📖 |
| Combalia M. et al., *BCN20000: Dermoscopic lesions in the wild*, 2019 (arXiv) ⚠️ | Dataset "difficile", base di ISIC 2019 | 📖 |
| Rotemberg V. et al., *A patient-centric dataset of images and metadata…* (ISIC 2020), **Scientific Data 2021** | Dataset con contesto paziente | 📖 |
| Kurtansky N. et al., SLICE-3D / ISIC 2024 (Scientific Data 2024) ⚠️ | Crop da total body photography, simili a foto smartphone | 📖 |

## 3. Foundation model e vision-language in dermatologia
| Paper / modello | Note | Stato |
|-----------------|------|-------|
| Kim C. et al., **MONET** — *Transparent medical image AI via an image–text foundation model grounded in medical literature*, **Nature Medicine 2024** | CLIP-like addestrato su immagini dermatologiche + testo; **annotazione automatica di concetti** → spiegabilità | 📖 |
| **PanDerm** (Yan S. et al., 2024–2025) ⚠️ | Foundation model multimodale per dermatologia, molti task | 📖 |
| **Derm Foundation** (Google Health) ⚠️ | Embedding model per immagini dermatologiche (pesi su Hugging Face con termini d'uso) | 📖 |
| Liu Y. et al., *A deep learning system for differential diagnosis of skin diseases*, **Nature Medicine 2020** (Google) | Diagnosi differenziale su 26 condizioni, immagini cliniche | 📖 |
| SkinGPT-4 (Zhou J. et al., Nature Communications 2024) ⚠️ | LLM multimodale per dermatologia | 📖 |
| Valutazioni di GPT-4V / Gemini / Claude su immagini dermatologiche (vari, 2023–2025) | **Cautela**: LLM generalisti spesso inaffidabili come classificatori → usarli come orchestratori/narratori, non come diagnosti | 📖 |
| DINOv2 / DINOv3, MedSAM, SAM 2 | Backbone e segmentazione general-purpose / medical | 📖 |

## 4. Bias, fairness e generalizzazione
| Paper | Note | Stato |
|-------|------|-------|
| Groh M. et al., *Evaluating deep neural networks trained on clinical images in dermatology with the Fitzpatrick 17k dataset*, CVPR-W 2021 | Annotazioni del fototipo | 📖 |
| Daneshjou R. et al., *Disparities in dermatology AI performance on a diverse, curated clinical image set* (**DDI**), **Science Advances 2022** | Calo di performance su pelli scure | 📖 |
| Winkler J.K. et al., *Association between surgical skin markings… and diagnostic performance of a CNN*, **JAMA Dermatology 2019** | Artefatti (inchiostro) → **shortcut learning** | 📖 |
| Bissoto A. et al., studi su bias/artefatti in ISIC (2019–2020) ⚠️ | I modelli imparano "scorciatoie" | 📖 |
| Daneshjou R. et al., *Checklist for evaluation of image-based AI reports in dermatology* (**CLEAR Derm**), JAMA Dermatology 2022 | **Da usare come checklist per la tua valutazione** | 📖 |

## 5. Explainability, incertezza e collaborazione uomo-AI
- Grad-CAM (Selvaraju 2017); limiti delle saliency map in medicina.
- Concept-based explanations: TCAV, Concept Bottleneck Models (Koh 2020), MONET.
- Conformal prediction per insiemi di diagnosi con copertura garantita (Angelopoulos & Bates, tutorial 2021).
- Tschandl 2020 (sopra): il formato dell'output (probabilità multiclasse vs CBIR "casi simili") cambia l'efficacia per il medico.
- CBIR (content-based image retrieval): mostrare **casi simili** dal dataset è un'ottima feature di interfaccia.

## 6. LLM, sistemi multi-agente, MCP
| Fonte | Note | Stato |
|-------|------|-------|
| Anthropic, *Building effective agents* (blog, dic 2024) | Pattern: workflow vs agenti, **orchestrator-workers**, evaluator-optimizer | 📖 |
| Anthropic, *How we built our multi-agent research system* (2025) | Orchestratore + subagent in parallelo, pro/contro (costo token) | 📖 |
| Specifica **Model Context Protocol** (modelcontextprotocol.io) | Tool, resource, prompt; client/server; trasporti stdio/HTTP | 📖 |
| Tu T. et al., **AMIE** (Google), Nature 2025 ⚠️ | LLM conversazionale diagnostico | 📖 |
| MedAgents (Tang X. et al., 2023/2024) ⚠️, MDAgents (Kim Y. et al., NeurIPS 2024) ⚠️ | Collaborazione multi-agente per ragionamento medico | 📖 |
| Survey "LLM-based multi-agent systems in healthcare" (2024–2025) | Cercare una survey recente | 📖 |

## 7. Prodotti esistenti e regolatorio
- **SkinVision** (app consumer, CE marked), **Miiskin**, **Google DermAssist** (CE class I, ora ritirato/limitato ⚠️).
- **DermaSensor**: primo dispositivo AI per cancro cutaneo autorizzato FDA per medici di base (gen 2024) — basato su spettroscopia, non immagini.
- **Moleanalyzer pro** (FotoFinder), **Derm** di Skin Analytics (CE classe III nel 2025 ⚠️).
- Revisioni critiche su app smartphone: Freeman K. et al., BMJ 2020 (*Algorithm based smartphone apps to assess risk of skin cancer in adults: systematic review*).
- Vedi [04_etica_regolatorio.md](04_etica_regolatorio.md).

## 8. Gap identificabili (ipotesi per il contributo originale)
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
