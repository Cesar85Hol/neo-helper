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
          │  - assess_quality        │
          │  - segment_lesion        │
          │  - classify_lesion       │
          │  - compute_abcd          │
          │  - explain_gradcam       │
          │  - find_similar_cases    │
          └──────────────────────────┘
          ┌──────────────────────────┐
          │  MCP server "neo-knowledge" │ (opzionale)
          │  - search_guidelines     │  RAG su linee guida / letteratura
          │  - search_pubmed         │
          └──────────────────────────┘
```

## Agenti (bozza)
| Agente | Input | Tool MCP usati | Output |
|--------|-------|----------------|--------|
| **Quality Gate** | immagine | `assess_quality` | ok / rifiuto + motivo (sfocata, luce, non è pelle, non dermatoscopica) |
| **Segmentation** | immagine | `segment_lesion` | maschera, bounding box, area |
| **Classifier** | immagine (+ crop) | `classify_lesion` (ensemble) | probabilità calibrate per classe, incertezza, conformal set |
| **Dermoscopic Criteria** | immagine + maschera | `compute_abcd`, (modello 7-point) | punteggi ABCD/TDS, criteri 7-point |
| **Explainer** | immagine + output | `explain_gradcam`, `find_similar_cases` | heatmap, casi simili, concetti (MONET) |
| **Critic / Safety** | tutti gli output | — | segnala incoerenze (es. classificatore "benigno" ma criteri 7-point alti), forza "consigliata valutazione specialistica" |
| **Reporter** | tutto | `search_guidelines` | report strutturato (JSON + testo) per il medico |

L'orchestratore può eseguire Segmentation/Classifier/Criteria **in parallelo** dopo il Quality Gate.

## Prima workflow, poi agenti
Strategia di apprendimento incrementale:
1. **v0 — Pipeline fissa** (Python puro): quality → classify → gradcam. Nessun LLM.
2. **v1 — Server MCP**: stessi passi esposti come tool; li provi da Claude Desktop/Code come client.
3. **v2 — Orchestratore singolo** con tool MCP (un solo agente che chiama i tool).
4. **v3 — Multi-agente**: subagent specializzati + Critic. Confronto v2 vs v3 (costi, latenza, qualità report) = esperimento per RQ2/RQ4.

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
  "criteria": {"abcd_tds": 4.1, "seven_point": 2},
  "explanations": {"heatmap_url": "…", "similar_cases": ["ISIC_…"]},
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
- [ ] LLM: API (Claude) vs locale (Ollama) — privacy delle immagini: all'LLM passano **solo output strutturati**, non le immagini? (scelta di design interessante da discutere nella tesi)
- [ ] Inferenza mobile on-device: quale modello è abbastanza piccolo?
- [ ] Storage immagini: locale/S3-compatibile, cifratura, retention
