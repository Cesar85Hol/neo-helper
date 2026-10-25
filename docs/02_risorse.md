# 02 — Risorse libere: dataset, modelli, librerie, tool

> ⚠️ Prima di usare un dataset, **leggere e annotare la licenza** (molti sono CC-BY-NC: ok per progetto open non commerciale, ma vincola i pesi addestrati).

## 1. Dataset
| Dataset | Tipo immagini | Dimensione (circa) | Classi / annotazioni | Licenza (da verificare) | Uso previsto |
|---------|---------------|--------------------|----------------------|-------------------------|--------------|
| **ISIC Archive** (isic-archive.com, API) | Dermatoscopiche + cliniche | > 400k ⚠️ | Diagnosi, metadati, alcune maschere | CC-0 / CC-BY / CC-BY-NC per immagine | Sorgente principale |
| **HAM10000** | Dermatoscopiche | ~10k | 7 classi, istologia per > 50% | CC-BY-NC | Training/benchmark |
| **ISIC 2019** (BCN20000 + HAM + MSK) | Dermatoscopiche | ~25k train | 8 classi + "unknown" al test | CC-BY-NC | Training multiclasse |
| **ISIC 2020** | Dermatoscopiche | ~33k | Benigno/maligno, molto sbilanciato, ID paziente | CC-BY-NC | Binario, contesto paziente |
| **ISIC 2024 / SLICE-3D** | Crop da total body 3D (simili a smartphone) | ~400k | Binario, pochissimi maligni, metadati ricchi | CC-BY-NC ⚠️ | Domain shift verso foto non dermatoscopiche |
| **ISIC 2018 Task 1/2** | Dermatoscopiche | ~2.6k | **Maschere di segmentazione** + attributi dermoscopici | CC-BY-NC | Segmentazione |
| **PH2** | Dermatoscopiche | 200 | Maschere, criteri ABCD, colori | Uso accademico | Test esterno, ABCD |
| **Derm7pt** | Dermatoscopiche + cliniche (coppie) | ~1k casi | **7-point checklist** | Uso accademico | Agente criteri 7-point |
| **PAD-UFES-20** | Cliniche da smartphone | ~2.3k | 6 classi + metadati clinici | CC-BY | Test smartphone |
| **Fitzpatrick17k** | Cliniche (web) | ~17k | 114 condizioni + fototipo | Uso ricerca | Fairness |
| **DDI** (Stanford) | Cliniche | ~650 | Fototipi I–VI, biopsia | Accesso su richiesta | Fairness |
| **MILK10k** (ISIC 2025) ⚠️ | Coppie clinica+dermatoscopica | ~10k | Multiclasse | ⚠️ | Multimodale (da verificare esistenza/stato) |

Dove scaricare: sito ISIC (challenge.isic-archive.com), Kaggle (mirror ISIC 2019/2020/2024, HAM10000), Harvard Dataverse (HAM10000), Mendeley Data (PAD-UFES-20).

**Trappole note**
- HAM10000 è incluso in ISIC 2018/2019 → non usare uno come test dell'altro.
- Più immagini della stessa lesione (`lesion_id`) → split per lesione/paziente.
- Duplicati tra mirror Kaggle e archivio ISIC.

## 2. Modelli pre-addestrati
| Risorsa | Cosa offre | Note |
|---------|-----------|------|
| **timm** (Hugging Face) | ResNet, EfficientNet, ConvNeXt, ViT, EVA, DINOv2… | Baseline e backbone |
| **DINOv2 / DINOv3** (Meta) | Feature self-supervised fortissime | Linear probe molto efficace |
| **MONET** (GitHub suinleelab) | CLIP dermatologico, concetti | Explainability concept-based |
| **PanDerm** ⚠️ | Foundation model dermatologico | Verificare disponibilità pesi |
| **Derm Foundation** (Google, HF) | Embedding dermatologici | Termini d'uso Health AI Developer Foundations |
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
- LLM locali per privacy/costi: **Ollama** + modelli open (es. Qwen-VL, MedGemma ⚠️)
- **MedGemma** (Google, 2025) ⚠️: modello open medico multimodale, interessante come agente "descrittivo"
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
- **Kaggle Notebooks** (GPU gratis ~30 h/settimana ⚠️), **Google Colab**, **Lightning Studio**
- Deploy: Hugging Face Spaces (demo), Fly.io / Render / Railway (API), Vercel (frontend)

## 8. Progetti open source di riferimento da studiare
- [ ] Soluzioni top ISIC 2019/2020/2024 su Kaggle (writeup + codice)
- [ ] Repository MONET (suinleelab)
- [ ] Esempi MCP server ufficiali (github.com/modelcontextprotocol/servers)
- [ ] Esempi Claude Agent SDK / cookbook multi-agent
- [ ] Cercare su GitHub: `skin lesion classification gradio`, `dermatology mcp`
