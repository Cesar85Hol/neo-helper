# 03 — Architettura del sistema e pool di agenti

## Risposta breve alla domanda "posso usare un agente che orchestra altri agenti + MCP?"
**Sì.** È il pattern **orchestrator–workers**: un agente orchestratore (LLM) riceve il caso, decide quali agenti specializzati chiamare, raccoglie i risultati e compone il report. Ogni capacità "dura" (modelli di visione) viene esposta come **tool MCP**, così è riutilizzabile da qualsiasi client (Claude Desktop/Code, il tuo backend, altri framework).

**Principio di sicurezza chiave**: l'LLM **non fa diagnosi dall'immagine**. I numeri (probabilità, maschere, punteggi) arrivano **solo** dai modelli di visione validati via tool; l'LLM orchestra, verifica coerenza e scrive il report.

## Vista d'insieme

```
┌────────────┐   ┌────────────┐
│  Web app   │   │ Mobile app │  (camera, on-device quality check)
└─────┬──────┘   └─────┬──────┘
      └───────┬────────┘
              ▼
     ┌─────────────────┐
     │  API (FastAPI)  │  auth, upload, storico casi, job asincroni
     └────────┬────────┘
              ▼
     ┌──────────────────────────┐
     │  ORCHESTRATORE (agente)  │  Claude Agent SDK / LangGraph
     │  piano → chiamate → sintesi │
     └──┬─────┬─────┬─────┬─────┬┘
        ▼     ▼     ▼     ▼     ▼
     [Qualità][Segm.][Classif.][Criteri][Spiegaz./Report]   ← subagent / workflow
        │     │     │     │     │
        └─────┴─────┴──┬──┴─────┘
                       ▼
          ┌──────────────────────────┐
          │  MCP server "neo-vision" │  tool deterministici (PyTorch)
          │  - check_quality         │
          │  - segment_lesion        │
          │  - embed_image           │
          │  - classify              │
          │  - predict_set           │
          │  - explain_heatmap       │
          │  - describe_concepts     │
          │  - similar_cases         │
          └──────────────────────────┘
          ┌──────────────────────────┐
          │  MCP server "neo-knowledge" │ (opzionale)
          │  - search_guidelines     │  RAG su linee guida / letteratura
          │  - search_pubmed         │
          └──────────────────────────┘
```

> **Aggiornato il 2026-11-10** alle decisioni della Milestone 1 ([05_scelte_e_pipeline.md](05_scelte_e_pipeline.md), [07_domande_di_ricerca.md](07_domande_di_ricerca.md), storyboard 3). I nomi dei tool qui sotto sono quelli di riferimento per le issue M4.

## Tool MCP del server `neo-vision` (nomi di riferimento)
| Tool | Cosa fa | Modello o metodo | Decisione |
|------|---------|------------------|-----------|
| `check_quality` | Tipo di immagine, sfocatura, luce, artefatti (penna, righello, adesivo, bordo nero) | Regole + punteggi MONET | C4, P7 |
| `segment_lesion` | Maschera e ritaglio della lesione | U-Net o MedSAM (da scegliere) | M3.2 |
| `embed_image` | Vettore dell'immagine; nasconde quale backbone c'è sotto | PanDerm congelato (DINOv2 o Derm Foundation in alternativa) | P5, P6 |
| `classify` | 7 probabilità + punteggio di malignità con soglia bassa | Testa lineare calibrata | P2, P3 |
| `predict_set` | Insieme conformal ("non so" se contiene più classi, tra cui un tumore) + controllo fuori distribuzione | Conformal prediction | P8, RQ2 |
| `explain_heatmap` | Dove guarda il modello, per controllo | Grad-CAM (variante per ViT) con test di sanità | RQ3 |
| `describe_concepts` | Criteri dermoscopici e clinici in parole | MONET validato su Derm7pt e sulle annotazioni di Chanda; concept bottleneck facoltativo | P7, RQ3 |
| `similar_cases` | 16 casi più simili con diagnosi e origine dell'etichetta | Ricerca del coseno sui vettori salvati (FAISS) | RQ3 |

**Resource:** model card, data card (licenza e fonte per immagine), soglie in uso, versioni dei modelli.
**Prompt:** "report per il medico" (in italiano, inglese, spagnolo e portoghese, RQ6).

## Agenti (bozza)
| Agente | Input | Tool MCP usati | Output |
|--------|-------|----------------|--------|
| **Quality Gate** | immagine | `check_quality` | ok / rifiuto + motivo (sfocata, luce, non è pelle, non dermatoscopica) e avvisi sugli artefatti |
| **Segmentation** | immagine | `segment_lesion` | maschera, bounding box, area |
| **Classifier** | immagine (+ crop) | `embed_image`, `classify`, `predict_set` | probabilità calibrate per classe, punteggio di malignità, insieme conformal, "non so" |
| **Dermoscopic Criteria** | immagine + maschera | `describe_concepts` | criteri della 7-point checklist e concetti clinici con punteggio (ABCD/TDS calcolato dalla maschera solo come opzione) |
| **Explainer** | immagine + output | `explain_heatmap`, `similar_cases`, `describe_concepts` | heatmap (soprattutto per controllo), casi simili, concetti |
| **Critic / Safety** | tutti gli output | — (regole, non un LLM) | controlla qualità, copertura dei tool, conflitti (classificatore contro casi simili contro criteri) e incertezza; forza "consigliata valutazione specialistica" |
| **Reporter** | tutto | `search_guidelines` (facoltativo) | report strutturato (JSON + testo) con **catena di prove**: ogni frase cita il tool da cui viene; più lingue |

L'orchestratore può eseguire Segmentation/Classifier/Criteria **in parallelo** dopo il Quality Gate.

## Prima workflow, poi agenti
Strategia di apprendimento incrementale:
1. **v0 — Pipeline fissa** (Python puro): qualità → segmentazione → vettore → classificazione + insieme conformal → spiegazioni → report a modello fisso. Nessun LLM.
2. **v1 — Server MCP**: stessi passi esposti come tool; li provi da Claude Desktop/Code come client.
3. **v2 — Orchestratore singolo** con tool MCP (un solo agente che chiama i tool).
4. **v3 — Multi-agente**: subagent specializzati + Critic a regole + percorso guidato dall'incertezza. Confronto v0, v2 e v3 (accuratezza, numeri inventati, conflitti intercettati, token, latenza) su casi trappola = esperimento della **RQ4**.

## Output strutturato (bozza schema)
```json
{
  "case_id": "…",
  "quality": {"ok": true, "issues": []},
  "classification": {
    "model_version": "…",
    "probabilities": {"MEL": 0.12, "NV": 0.80, "BKL": 0.05, "...": 0.03},
    "malignancy_score": 0.15,
    "uncertainty": 0.21,
    "conformal_set_90": ["NV", "MEL"]
  },
  "criteria": {"seven_point": {"atypical_network": 0.71, "blue_white_veil": 0.12}, "source_tool": "describe_concepts"},
  "explanations": {"heatmap_url": "…", "similar_cases": [{"id": "ISIC_…", "diagnosis": "NV", "label_source": "histopathology", "similarity": 0.83}]},
  "evidence": [{"sentence": "…", "tool": "classify"}],
  "language": "it",
  "flags": ["MEL in conformal set: considerare dermatoscopia digitale di follow-up / valutazione specialistica"],
  "disclaimer": "Strumento di supporto, non sostituisce il giudizio clinico."
}
```

## Struttura repo (proposta)
```
neo-helper/
├── docs/                 # questi MD
├── ml/                   # training, valutazione, notebook
│   ├── data/             # script di download (dati NON in git)
│   ├── src/
│   └── notebooks/
├── mcp_servers/
│   ├── neo_vision/       # FastMCP server con i tool di visione
│   └── neo_knowledge/
├── agents/               # orchestratore + subagent
├── backend/              # FastAPI
├── web/                  # Next.js
└── mobile/               # Expo
```

## Decisioni aperte
- [ ] Framework orchestratore: Claude Agent SDK vs LangGraph (si può fare v2 con uno e v3 con l'altro per confronto)
- [ ] LLM: API (Claude) vs locale (Ollama) — decisione presa sul principio: all'LLM passano **solo output strutturati**, non le immagini. Resta da scegliere il modello (RQ4, RQ6: LLM locale per i centri con poche risorse)
- [ ] Inferenza mobile on-device: PanDerm (ViT-Large) è troppo pesante; serve un backbone leggero o l'inferenza sul server (M6.2)
- [ ] Storage immagini: locale/S3-compatibile, cifratura, retention
