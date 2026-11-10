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
📖 Fonte consigliata per approfondire: Argenziano G. et al., *Dermoscopy of pigmented skin lesions: results of a consensus meeting via the Internet*, JAAD 48(5):679–693 (2003), DOI 10.1067/mjd.2003.281; un manuale di dermatoscopia (es. Marghoob / Kittler).

## 2. Paper fondativi di Deep Learning in dermatologia
| Paper | Perché è importante | Stato |
|-------|---------------------|-------|
| Esteva A. et al., *Dermatologist-level classification of skin cancer with deep neural networks*, **Nature 2017** | Il paper "big bang": Inception-v3, livello dermatologo | ✅ [scheda](papers/2017_esteva_dermatologist-level.md) |
| Haenssle H.A. et al., *Man against machine…*, **Annals of Oncology 2018** | CNN vs 58 dermatologi su dermatoscopia | ✅ [scheda](papers/2018_haenssle_man-against-machine.md) |
| Brinker T.J. et al., *Deep learning outperformed 136 of 157 dermatologists…*, **Eur J Cancer 2019** | Confronto su larga scala | ✅ [scheda](papers/2019_brinker_136-of-157.md) |
| Tschandl P. et al., *The HAM10000 dataset*, **Scientific Data 2018** | Dataset di riferimento | ✅ [scheda](papers/2018_tschandl_ham10000.md) |
| Tschandl P. et al., *Comparison of the accuracy of human readers versus machine-learning algorithms…*, **Lancet Oncology 2019** | Benchmark open (ISIC 2018) uomo vs macchina | ✅ [scheda](papers/2019_tschandl_human-vs-machine-isic2018.md) |
| Tschandl P. et al., *Human–computer collaboration for skin cancer recognition*, **Nature Medicine 2020** | **Fondamentale per il tuo progetto**: come l'AI aiuta (o danneggia) il medico a seconda di come viene presentata | ✅ [scheda](papers/2020_tschandl_human-computer-collaboration.md) |
| Challenge ISIC 2016–2024 (report, dataset, soluzioni vincenti) | Compiti, metriche, test esterni, classi sconosciute | ✅ vedi **§7** |

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
| Bissoto A. et al., *(De)Constructing Bias on Skin Lesion Datasets* (arXiv 1904.08818, 2019) e *Debiasing Skin Lesion Datasets and Models? Not So Fast* (arXiv 2004.11457, 2020); workshop ISIC a CVPR ⚠️ sede | I modelli imparano "scorciatoie" | 📖 |
| Daneshjou R. et al., *Checklist for evaluation of image-based AI reports in dermatology* (**CLEAR Derm**), JAMA Dermatology 2022 | **Da usare come checklist per la tua valutazione** | ✅ [scheda](papers/2022_daneshjou_clear-derm.md) |

> **Pelli non chiare, popolazioni latinoamericane, asiatiche e africane (RQ6):** dataset e studi raccolti in [09_pelli_non_chiare.md](09_pelli_non_chiare.md) (Wen 2022, Gröger 2026, Pérez-Lalinde 2026, Groh 2024, Kunwor 2026, Han 2018, Wang 2020, HIBA, PASSION, SCIN).

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
| TCAV (Kim B. et al., ICML 2018, arXiv 1711.11279); calibrazione/conformal su ISIC (da cercare) | Approfondimenti | 📖 |

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
| MedAgents (Tang X. et al., arXiv 2311.10537, 2023; sede ⚠️); survey "LLM-based agents in medicine" (arXiv 2502.11211) | Approfondimenti | 📖 |

## 7. Challenge ISIC (2016–2024)
Introduzione: [S7_introduzione.md](papers/S7_introduzione.md).

| Paper | Note | Stato |
|-------|------|-------|
| Gutman D. et al. (ISBI 2016) e Codella N. et al. (ISBI 2017), arXiv 1605.01397 e 1710.05006 | Prime gare: melanoma vs benigno, AUC | 📖 (solo citati) |
| Codella N. et al., *Skin lesion analysis toward melanoma detection 2018* (ISIC 2018), arXiv 2019 | Accuratezza bilanciata, test esterno, Jaccard con soglia | ✅ [scheda](papers/2019_codella_isic2018.md) |
| Combalia M. et al., *Validation of AI prediction models… the 2019 ISIC Grand Challenge*, **Lancet Digit Health 2022** | 82% → 59% su BCN20000; le lesioni mai viste diventano "maligne" | ✅ [scheda](papers/2022_combalia_isic2019.md) |
| Hernández-Pérez C. et al., *BCN20000: Dermoscopic Lesions in the Wild*, **Sci Data 2024** | 18.946 immagini difficili, classe OOD, **CC BY 4.0** | ✅ [scheda](papers/2024_hernandez-perez_bcn20000.md) |
| Rotemberg V. et al., *A patient-centric dataset…* (ISIC 2020), **Sci Data 2021** | 33.126 immagini per paziente, 1,8% melanomi, CC BY-NC | ✅ [scheda](papers/2021_rotemberg_isic2020.md) |
| Ha Q. et al., soluzione vincente SIIM-ISIC 2020, arXiv 2020 | Ensemble di 18 reti, validazione stabile, bersaglio a 9 classi | ✅ [scheda](papers/2020_ha_isic2020-winner.md) |
| Kurtansky N. et al., risultati ISIC 2020 e contesto del paziente, **JEADV 2024** | Il contesto (7 lesioni) non aiuta né reti né medici | ✅ [scheda](papers/2024_kurtansky_isic2020-context.md) (abstract) |
| Kurtansky N. et al., *Automated triage… 3D total-body photography* (ISIC 2024), **npj Digit Med 2025** | pAUC > 80% sens.; contesto del paziente utile; 1 tumore ogni ~52 lesioni controllate | ✅ [scheda](papers/2025_kurtansky_isic2024.md) |
| Kurtansky N. et al., *The SLICE-3D dataset*, Sci Data 11:884 (2024), DOI 10.1038/s41597-024-03743-w; MILK10k (collezione ISIC, 10.480 immagini, CC BY-NC) | Dataset (verificati) | 📖 |

## 8. Prodotti esistenti e regolatorio
Introduzione: [S8_introduzione.md](papers/S8_introduzione.md) · documento: [04_etica_regolatorio.md](04_etica_regolatorio.md).

| Fonte | Note | Stato |
|-------|------|-------|
| Freeman K. et al., *Algorithm based smartphone apps…*, **BMJ 2020** | 9 studi, 6 app; SkinVision sens. 80% / spec. 78%; CE insufficiente | ✅ [scheda](papers/2020_freeman_smartphone-apps.md) |
| Wongvibulsin S. et al., *Current state of dermatology mobile apps with AI*, **JAMA Dermatol 2024** | 41 app, nessuna FDA, poca trasparenza | ✅ [scheda](papers/2024_wongvibulsin_ai-apps.md) (abstract) |
| Jaklitsch E. et al., DermaSensor e medici di base, **J Prim Care Community Health 2023** (+ FDA De Novo DEN230008, 12 gennaio 2024, verificato) | Spettroscopia; sens. dei medici di base 67% → 88% | ✅ [scheda](papers/2023_jaklitsch_dermasensor.md) |
| Marsden H. et al., DERM (Skin Analytics) nel servizio sanitario inglese, **Front Med 2024** | Meno invii inutili a pari sensibilità; CE classe III 2025 (fonte aziendale) | ✅ [scheda](papers/2024_marsden_derm.md) |
| Malvehy J. et al., *New regulation of medical devices in the EU: impact in dermatology*, **JEADV 2022** | MDR: software diagnostico almeno classe IIa | ✅ [scheda](papers/2022_malvehy_mdr-dermatology.md) |
| Van Kolfschooten H. et al., *High-risk without safeguards? The EU AI Act…*, **BMJ Digit Health AI 2026** | AI Act alto rischio; riforme 2025–2026 | ✅ [scheda](papers/2026_vankolfschooten_ai-act.md) |
| Moleanalyzer Pro (FotoFinder), Miiskin; Google DermAssist (CE classe I 2021, "non più in sviluppo" secondo Google) | Altri prodotti | 📖 |

## 9. Gap identificabili e contributo originale
Aggiornato il 2026-11-09 dopo i pacchetti 1–4, anche alla luce di **DermAgent** (2026). Domande di ricerca e contributo in [07_domande_di_ricerca.md](07_domande_di_ricerca.md).

1. **"Non so" senza garanzie.** I classificatori chiamano "maligne" quasi metà delle lesioni mai viste (Combalia 2022). Gli agenti dermatologici usano soglie di confidenza (DermAgent), e nessuno integra un'astensione con copertura garantita e misurata per fototipo e per centro → **RQ2**.
2. **Spiegazioni non verificate.** Le heatmap spesso non superano i test di sanità (Adebayo 2018); MONET non è mai stato valutato sui criteri dermoscopici; le annotazioni localizzate degli esperti (Chanda 2024) sono pubbliche ma poco usate per validare → **RQ3**.
3. **Valutazioni troppo ottimistiche.** Spesso c'è un solo test interno (HAM10000); la metrica non rispecchia la clinica; mancano i risultati per fototipo (DDI, CLEAR Derm, Kurtansky 2025) → **RQ1**.
4. **Agenti medici poco controllati.** Mancano controllo umano, gestione degli errori e risoluzione dei conflitti (Vatsal 2026); nessuno misura il costo del multi-agente rispetto all'agente singolo; DermAgent dipende da un modello chiuso → **RQ4**.
5. **Licenze e riproducibilità.** I modelli migliori sono non commerciali (PanDerm, MONET); pochi sistemi aperti end-to-end documentano licenze e regole → **RQ1** e il contributo 5.

## 10. Strategia di ricerca bibliografica
- Banche dati: PubMed, Google Scholar, Semantic Scholar, arXiv (cs.CV, eess.IV), IEEE Xplore.
- Query base:
  - `(melanoma OR "skin lesion" OR nevus) AND (dermoscopy OR dermatoscopy) AND ("deep learning" OR CNN OR transformer)`
  - `dermatology AND ("foundation model" OR "vision-language")`
  - `("multi-agent" OR "LLM agent") AND (medical imaging OR dermatology)`
- Metodo: schema PRISMA semplificato (identificati → screening → inclusi), finestra 2017–2026.
- Strumenti: Zotero, Connected Papers / ResearchRabbit, Semantic Scholar alerts.

---

## 11. Tabella comparativa dei risultati
Deliverable della Fase 1, aggiunto nella revisione finale (2026-11-10).
- **Colonna "Esterno":** il risultato principale viene da un test **esterno**, cioè da centri o dati diversi da quelli dell'addestramento.
- **Colonna "Fototipo":** lo studio riporta i risultati **per fototipo**.
- I numeri vengono dalle schede, dove è indicato cosa è stato letto.

**A. Reti contro medici (dermoscopia o foto)**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2017 | Esteva (*Nature*) | ~130.000 foto cliniche, 2.032 malattie | Tumore contro benigno | AUC > 0,91; pari a 21 dermatologi | No | No |
| 2018 | Haenssle (*Ann Oncol*) | Dermoscopie | Melanoma contro nevo | AUC 0,86 contro 0,79 di 58 dermatologi; specificità 82,5% contro 71,3–75,7% a pari sensibilità | No | No |
| 2018 | Han (*J Invest Dermatol*) | Foto cliniche di pazienti coreani (Asan) | 12 tumori e benigni | AUC per il melanoma 0,96 sui coreani, 0,88 sugli europei (Edinburgh) | Sì | Etnia sì |
| 2019 | Brinker (*Eur J Cancer*) | ~12.000 dermoscopie pubbliche | Melanoma contro nevo | Specificità 86,5% contro 60,0% di 157 dermatologi a pari sensibilità | No | No |
| 2019 | Tschandl (*Lancet Oncol*) | HAM10000 (ISIC 2018) | 7 classi | Sensibilità media per classe 84,5–88,5% (algoritmi) contro 79,2% (511 lettori); calo sulle immagini di altri centri | In parte | No |
| 2020 | Wang (*Chin Med J*) | Dermoscopie di pazienti cinesi | Tumori comuni + psoriasi | Accuratezza 81,5%; pari a 164 dermatologi | No | Etnia sì |

**B. Fuori dal laboratorio: challenge, bias e test esterni**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2019 | Codella, ISIC 2018 (arXiv) | HAM10000 + 316 immagini esterne | 7 classi | Accuratezza bilanciata massima 0,885; la maggior parte va peggio sul test esterno | Sì | No |
| 2019 | Winkler (*JAMA Dermatol*) | 130 lesioni con e senza segni di penna | Melanoma contro nevo | Specificità dall'84% al 46% con i segni di penna | — | No |
| 2021 | Groh, Fitzpatrick17k (CVPR-W) | 16.577 foto cliniche | 114 malattie | Accuratezza 20,2% (114 classi); migliore sui fototipi visti in addestramento | — | **Sì** |
| 2022 | Combalia, ISIC 2019 (*Lancet Digit Health*) | 25.331 dermoscopie, 8 classi + "mai viste" | 8 classi | Accuratezza bilanciata dall'82,0% (HAM10000) al 58,8% (BCN20000); lesioni mai viste riconosciute al 6% (dermatologi 26%); il 47% chiamate maligne | Sì | No |
| 2022 | Daneshjou, DDI (*Sci Adv*) | 656 foto con biopsia, fototipi I–VI | Tumore contro benigno | AUC da 0,88–0,94 dichiarate a 0,56–0,67; sensibilità sulle pelli scure fino a 0,12–0,23 | Sì | **Sì** |
| 2024 | Kurtansky, ISIC 2020 (*JEADV*) | 33.126 dermoscopie per paziente | Melanoma | AUROC 0,943–0,949 (primi 50); il contesto del paziente non aiuta | No | No |
| 2025 | Kurtansky, ISIC 2024 (*npj Digit Med*) | 900.000 ritagli da foto 3D | Triage dei tumori | pAUC 0,173, AUC 0,967; circa 52 lesioni controllate per ogni tumore all'80% di sensibilità | No | No |
| 2026 | Anriot (*JAMA Dermatol*) | 1.117 casi reali | Multiclasse | PanDerm 72,2% contro esperti 74,2%; CNN di prima generazione 56,7% | Sì | No |
| 2026 | Kunwor (arXiv) | DDI + SCIN | Tumori e malattie infiammatorie | Il tipo di malattia pesa più del tono (0,62 → 0,21); circa 10 esempi per categoria bastano per adattarsi | Sì | **Sì** |

**C. Foundation model e concetti**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2024 | Kim, MONET (*Nat Med*) | 105.550 immagini con testo | Concetti | AUROC media 0,766 sui concetti SkinCon (CLIP 0,692); concept bottleneck per il melanoma 0,892 | — | Solo sintesi |
| 2025 | Yan, PanDerm (*Nat Med*) | 2,15 milioni di immagini, 4 modalità | 28 compiti | Migliore su 9 dataset su 10; con il 10–30% delle etichette pari agli altri | Sì | Solo accuratezza complessiva |
| 2019 | Tschandl, CBIR (*Br J Dermatol*) | 3 dataset dermoscopici | Tumore contro benigno | 16 casi simili: AUC 0,806–0,852, pari alla softmax | In parte | No |

**D. Medici con l'AI**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2020 | Tschandl (*Nat Med*) | 302 medici, HAM10000 | 7 classi | Accuratezza dal 63,6% al 77,0% con le probabilità multiclasse; l'AI sbagliata inganna anche gli esperti | — | No |
| 2024 | Chanda (*Nat Commun*) | 116 medici, HAM10000 | Melanoma contro nevo | Accuratezza bilanciata dal 66,2% al 72,3% con l'AI e al 73,2% con le spiegazioni; fiducia +17,5% | — | No |
| 2024 | Krakowski (*npj Digit Med*) | Meta-analisi di 10 studi | Tumori della pelle | Sensibilità dal 74,8% all'81,1%, specificità dall'81,5% all'86,1% con l'AI; più beneficio ai non dermatologi | — | No |
| 2024 | Groh (*Nat Med*) | 848 medici, 39 paesi, 46 malattie | Diagnosi differenziale | Medici 4 punti peggio sulle pelli scure; l'AI +33% ma allarga il divario per i medici di base | — | **Sì** |

**E. LLM e agenti**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2024 | Zhou, SkinGPT-4 (*Nat Commun*) | Immagini cliniche | Descrizione e diagnosi | "Corretta o pertinente" nell'80,6% secondo i dermatologi: non è una misura di accuratezza | No | No |
| 2026 | Bhagwat (*Bioengineering*) | DDI, ChatGPT 5.2 e Gemini 3.1 | Prime 3 diagnosi | Top-1 23–32%; tumori mancati nel 32–50%; specificità 23–43%; peggio sui fototipi V–VI | Sì | **Sì** |
| 2026 | Liu, DermAgent (arXiv) | 5 benchmark, poche centinaia di immagini | Agente con tool | Zero-shot su HAM10000 61,8% (MedAgent-Pro 57,6%) | — | No |

**F. Prodotti**

| Anno | Lavoro | Dati | Compito | Risultato principale | Esterno | Fototipo |
|------|--------|------|---------|----------------------|---------|----------|
| 2020 | Freeman (*BMJ*), app | 9 studi, 6 app | Rischio di tumore | SkinVision: sensibilità 80%, specificità 78% su lesioni scelte da medici | — | No |
| 2024 | Venkatesh e Jaklitsch, DermaSensor | 1.579 lesioni (DERM-SUCCESS) | Indagare o monitorare | Sensibilità 95,5%, specificità 20,7%; 97,1% di pazienti bianchi | Sì | In parte |
| 2024 | Marsden (*Front Med*), DERM | 789 lesioni, NHS | Triage | A pari sensibilità (~91%) evita più invii inutili dei teledermatologi | Sì | 4% fototipi IV–VI |

**Cosa dice la tabella, in breve:**
1. I risultati migliori sono quasi sempre **interni**. Quando il test è esterno o realistico, le prestazioni scendono: Combalia, DDI, Anriot.
2. **Pochissimi studi riportano i risultati per fototipo**: 5 righe su 28. Quando lo fanno, il divario c'è (DDI, Groh 2024, Bhagwat) ma non sempre nella stessa direzione (Kunwor).
3. L'AI **aiuta i medici**, soprattutto i meno esperti, ma può trascinarli quando sbaglia e può allargare i divari.

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
