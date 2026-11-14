# 02 — Risorse libere: dataset, modelli, librerie, tool

> ⚠️ Prima di usare un dataset, **leggere e annotare la licenza** (molti sono CC-BY-NC: ok per progetto open non commerciale, ma vincola i pesi addestrati).

## 1. Dataset
| Dataset | Tipo immagini | Dimensione (circa) | Classi / annotazioni | Licenza (da verificare) | Uso previsto |
|---------|---------------|--------------------|----------------------|-------------------------|--------------|
| **ISIC Archive** (isic-archive.com, API) | Dermatoscopiche + cliniche | 581.002 (2026-11-09) | Diagnosi, metadati, alcune maschere | CC-0 / CC-BY / CC-BY-NC per immagine | Sorgente principale |
| **HAM10000** | Dermatoscopiche | 10.015 img, 7.470 lesioni; 2,8 GB | 7 classi, istologia per 5.340 immagini (53%) | **CC BY-NC 4.0** (Harvard Dataverse V4.0, DOI 10.7910/DVN/DBW86T, verificato 2026-11-11) | Training/benchmark |
| **ISIC 2019** (BCN20000 + HAM + MSK) | Dermatoscopiche | ~25k train | 8 classi + "unknown" al test | CC-BY-NC | Training multiclasse |
| **BCN20000** (Hospital Clínic Barcelona) | Dermatoscopiche | 18.946 img, 5.583 lesioni (12.413 train / 6.533 test) | 8 classi + OOD nel test; sedi difficili (unghie, mucose) | **CC BY 4.0 su Figshare** (10.6084/m9.figshare.24140028); **CC BY-NC sull'archivio ISIC** | Test esterno severo; dati con licenza aperta |
| **HIBA** (Hospital Italiano de Buenos Aires, 2019–2022) | 1.270 dermoscopiche polarizzate + 346 cliniche | 1.616 img, 1.246 lesioni, 623 pazienti | Diagnosi, conferma, sede, storia di melanoma | **CC BY** (archivio ISIC, DOI 10.34970/587329) | Test esterno latinoamericano (fototipi soprattutto II–III) |
| **ISIC 2020** | Dermatoscopiche | ~33k | Benigno/maligno, molto sbilanciato, ID paziente | CC BY-NC 4.0 nel paper; sull'archivio ISIC miste: 19.557 CC BY, 13.569 CC BY-NC | Binario, contesto paziente |
| **ISIC 2024 / SLICE-3D** | Crop da total body 3D (simili a smartphone) | ~400k | Binario, pochissimi maligni, metadati ricchi | Miste sull'archivio: CC-0, CC BY, CC BY-NC (401.059 img); Sci Data 11:884 | Domain shift verso foto non dermatoscopiche; metrica pAUC > 80% sens. (Kurtansky 2025) |
| **ISIC 2018 Task 1/2** | Dermatoscopiche | ~2.6k | **Maschere di segmentazione** + attributi dermoscopici | CC-BY-NC | Segmentazione |
| **PH2** | Dermatoscopiche | 200 | Maschere, criteri ABCD, colori | Uso accademico ⚠️ da verificare | Test esterno, ABCD |
| **Derm7pt** | Dermatoscopiche + cliniche (coppie) | ~1k casi, 2.045 img; 152 MB | **7-point checklist** | **CC BY-NC-ND 4.0** (pagina di download, verificato 2026-11-11) | Agente criteri 7-point |
| **Annotazioni di Chanda 2024** (su HAM10000) | Dermatoscopiche | 3.611 img (MEL+NV con istologia) | Criteri dermoscopici **localizzati**, 14 dermatologi | **CC BY 4.0**, Figshare 10.6084/m9.figshare.23766477 | Validare MONET, concept bottleneck, controllo delle heatmap |
| **PAD-UFES-20** (Brasile) | Cliniche da smartphone | 2.298 (archivio ISIC) | 6 classi + metadati clinici | CC BY (verificato sull'archivio ISIC) | Test smartphone; **RQ6** |
| **Fitzpatrick17k** | Cliniche (web) | ~17k | 114 condizioni + fototipo | Uso ricerca | Fairness |
| **DDI** (Stanford) | Cliniche | 656 img, 570 pazienti; 226 MB | Fototipi I–VI, biopsia | **Stanford Research Use Agreement**: solo ricerca personale non commerciale, niente ridistribuzione né lavori derivati (verificato 2026-11-11; ⚠️ letti i primi sei punti) | Fairness |
| **BALD** (lesioni acrali, BRAAFF) | Dermatoscopiche | 666 | Melanomi e nevi **acrali**, anche da centri giapponesi | CC BY-NC (archivio ISIC, DOI 10.34970/669187) | **RQ6**: sede acrale, proxy asiatico |
| **MSKCC Skin Tone Labeling** | Varie (esame di tutto il corpo) | 4.879 img, 64 pazienti | Annotazioni dettagliate del **tono della pelle** | CC BY (DOI 10.34970/962049) | **RQ6**: misurare il tono della pelle |
| **Cheratosi seborroiche, Pontificia Universidad Católica de Chile** | Dermatoscopiche | 150 | Una sola diagnosi | CC BY (DOI 10.34970/478917) | **RQ6**: piccolo test cileno |
| **MILK10k** (ISIC 2025) | Coppie clinica+dermatoscopica | 10.480 | Multiclasse | CC BY-NC (archivio ISIC, DOI 10.34970/648456) | Multimodale |

Provenienza, file e checksum dei dataset già scaricati: [`ml/data/README_it.md`](../ml/data/README_it.md).

Dove scaricare: sito ISIC (challenge.isic-archive.com), Kaggle (mirror ISIC 2019/2020/2024, HAM10000), Harvard Dataverse (HAM10000), Mendeley Data (PAD-UFES-20).

**Trappole note**
- HAM10000 è incluso in ISIC 2018/2019 → non usare uno come test dell'altro.
- Più immagini della stessa lesione (`lesion_id`) → split per lesione/paziente.
- Duplicati tra mirror Kaggle e archivio ISIC.

## 2. Modelli pre-addestrati
| Risorsa | Cosa offre | Note |
|---------|-----------|------|
| **timm** (Hugging Face) | ResNet, EfficientNet, ConvNeXt, ViT, EVA, DINOv2… | Baseline e backbone |
| **DINOv2 / DINOv3** (Meta) | Feature self-supervised fortissime | Linear probe molto efficace; DINOv2 **Apache 2.0** (anche uso commerciale) |
| **MONET** (GitHub suinleelab) | CLIP dermatologico, concetti | Explainability concept-based; pesi su HF `chanwkim/monet`. Repository **CC BY-NC-SA 4.0**; la model card esclude qualsiasi uso in produzione (verificato 2026-11-04) |
| **PanDerm** (GitHub SiyuanYan1) | Foundation model dermatologico multimodale (ViT-L) | Pesi pubblici, licenza **CC-BY-NC-ND 4.0** (solo ricerca non commerciale) |
| **DermFM-Zero** (GitHub SiyuanYan1, HF `redlessone/DermFM-Zero`) | Successore immagine-testo di PanDerm, zero-shot e concetti (arXiv 2602.10624) | ⚠️ Licenza ancora contraddittoria (2026-11-09): metadati HF `cc-by-nc-4.0`, ma il testo per l'accesso ai pesi dice CC BY-NC-ND e vieta la ridistribuzione; pre-training include ISIC, BCN20000, Fitzpatrick17k |
| **Derm Foundation** (Google, HF) | Embedding dermatologici (BiT ResNet101x3, vettore da 6.144) | Gated: termini d'uso Health AI Developer Foundations |
| **BiomedCLIP** (Microsoft) | CLIP biomedico | Zero-shot, retrieval |
| **MedSAM / SAM 2** | Segmentazione promptable | Segmentazione lesione |
| Soluzioni vincenti ISIC su Kaggle (2019, 2020, 2024) | Codice + trucchi (ensemble, TTA, metadati) | Ottimo materiale di studio |

## 3. Librerie (ML / imaging)
- **PyTorch** + **Lightning** (training pulito), **timm**, **torchvision**
- **MONAI** (imaging medico: transform, metriche, segmentazione)
- **Albumentations** (augmentation)
- **segmentation_models_pytorch** (U-Net, DeepLabV3+…)
- **pytorch-grad-cam** (Grad-CAM, Grad-CAM++, EigenCAM…), **Captum**
- **scikit-learn** (metriche), **torchmetrics**, **netcal** / codice proprio per calibrazione, **MAPIE** / **TorchCP** per conformal prediction
- **Weights & Biases** o **MLflow** per tracciare esperimenti
- **FAISS** per retrieval di casi simili (CBIR)
- Export: **ONNX**, **coremltools** (iOS), **LiteRT/TFLite** o **ExecuTorch** (Android/iOS)

## 4. Agenti, LLM, MCP
- **MCP Python SDK** (`mcp`, include **FastMCP**) → scrivere server MCP con i tool di analisi
- **Claude Agent SDK** (Python/TS) → orchestratore + subagent, supporto MCP nativo
- Alternative per confronto: **LangGraph**, **OpenAI Agents SDK**, **Google ADK**, **CrewAI**, **AutoGen/AG2**, **smolagents**
- LLM locali per privacy/costi: **Ollama** + modelli open (es. Qwen-VL, MedGemma)
- **MedGemma** (Google, 2025; HF `google/medgemma-4b-it`, termini HAI-DEF ⚠️ non letti): modello open medico multimodale, interessante come agente "descrittivo"
- Valutazione agenti: **Inspect AI**, **promptfoo**, **DeepEval** (test sul report generato)

## 5. Backend / Web
- **FastAPI** (API inferenza), **Celery/RQ** o task asincroni, **Redis**
- **Gradio** (demo rapida, deploy gratis su **Hugging Face Spaces**), **Streamlit**
- Frontend: **Next.js + React + Tailwind + shadcn/ui**; visualizzazione immagini/heatmap con **OpenSeadragon** o canvas; **Konva** per annotazione
- Report PDF: **WeasyPrint** / **react-pdf**
- Standard sanitari (per il futuro): **DICOM** (supplemento per dermatologia/VL photographic), **FHIR** (DiagnosticReport)

## 6. Mobile
| Opzione | Pro | Contro |
|---------|-----|--------|
| **React Native + Expo** | Condivide TS/logica con il web Next.js, rapido | Inferenza on-device richiede moduli nativi (react-native-fast-tflite, ONNX Runtime RN) |
| **Flutter** | UI eccellente, camera ottima, tflite_flutter | Linguaggio Dart separato dal web |
| **Nativo Swift (iOS)** | CoreML + Vision ottimi, camera controllabile | Solo iOS |

Raccomandazione iniziale: **Expo (React Native)** + inferenza **ibrida**: modello leggero on-device per qualità immagine/triage, agenti e modelli grandi sul server.

## 7. Infrastruttura / compute
- Locale: Mac Apple Silicon (PyTorch MPS) per prototipi e modelli piccoli
- **Kaggle Notebooks** (GPU gratis circa 30 h/settimana, quota non pubblicata ufficialmente e variabile; sessioni al massimo di 12 h), **Google Colab**, **Lightning Studio**
- Deploy: Hugging Face Spaces (demo), Fly.io / Render / Railway (API), Vercel (frontend)

## 8. Progetti open source di riferimento da studiare
- [ ] Soluzioni top ISIC 2019/2020/2024 su Kaggle (writeup + codice)
- [ ] Repository MONET (suinleelab)
- [ ] Esempi MCP server ufficiali (github.com/modelcontextprotocol/servers)
- [ ] Esempi Claude Agent SDK / cookbook multi-agent
- [ ] Cercare su GitHub: `skin lesion classification gradio`, `dermatology mcp`
