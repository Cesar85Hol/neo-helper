# 10 — Dashboard: come siamo usciti dalla Milestone 1

> **Milestone 1 (letteratura) chiusa il 2026-11-10.** Questa pagina si legge in due minuti: dice cosa abbiamo deciso, perché e cosa viene dopo. Per i dettagli si segue il link di ogni riga.
> Versione interattiva in italiano, inglese e spagnolo: [dashboard/neo_helper_M1.html](dashboard/neo_helper_M1.html).

## In una frase
Neo Helper sarà un assistente **per il medico**, non per il paziente:
- **vede** la lesione con un foundation model dermatologico congelato;
- **dice "non so"** con una garanzia;
- **spiega** con i criteri del dermatologo;
- **coordina** i suoi strumenti con un agente via MCP, senza mai inventare numeri;
- è valutato **fuori dal laboratorio**, anche su **pelli latinoamericane e acrali**.

## I numeri della M1
| 42 | 9 | 21 | 12 | 6 | 47 |
|---|---|---|---|---|---|
| schede di paper | file Word | episodi audio | issue chiuse | domande di ricerca | blocchi del sistema in 8 livelli |

## Le scelte chiave
| Area | Scelta | Perché, in breve | Dettagli |
|------|--------|------------------|----------|
| Dati | **HAM10000** per partire, divisione per `lesion_id` 70/15/15; ISIC 2019 **dopo** | Oltre metà istologica, confrontabile; nessuna lesione in training e test insieme | [05 §1, §3.3](05_scelte_e_pipeline.md) |
| Test esterni | **BCN20000** (da Figshare), DDI, PAD-UFES-20, **HIBA**, PH2, Derm7pt; **licenza e fonte per immagine** | Fuori dal laboratorio l'accuratezza scende dall'82% al 59% (ISIC 2019) | [S7](papers/S7_introduzione.md), [06](06_verifiche_M1.md) |
| Modello | **PanDerm congelato + testa lineare**; fine-tuning come secondo esperimento | Migliore su 28 compiti, servono poche etichette; costo basso | [05 §1.1–1.2](05_scelte_e_pipeline.md) |
| Licenza libera | Confronto con **DINOv2**, Derm Foundation, ImageNet sugli stessi split | PanDerm è CC BY-NC-ND: va bene per la tesi, non per un prodotto | [05 §1.2](05_scelte_e_pipeline.md) |
| Uscita | **7 classi + punteggio di malignità**, soglia bassa (17–20%) | Le probabilità aiutano i medici; la falsa rassicurazione è l'errore peggiore | [Tschandl 2020](papers/2020_tschandl_human-computer-collaboration.md) |
| Qualità | **Controllo qualità e artefatti** prima di tutto | Segni di penna: specificità dall'84% al 46% | [Winkler 2019](papers/2019_winkler_surgical-markings.md) |
| "Non so" | Calibrazione + **insiemi conformal** + controllo fuori distribuzione | Gli algoritmi riconoscono il 6% delle lesioni mai viste (i dermatologi il 26%) | [S5](papers/S5_introduzione.md), [Combalia 2022](papers/2022_combalia_isic2019.md) |
| Spiegazioni | **Criteri dermoscopici** (MONET, validato sulle annotazioni di Chanda), **casi simili** (16), Grad-CAM solo per controllo | Le heatmap spesso ingannano; i medici si fidano dei criteri | [S5](papers/S5_introduzione.md) |
| LLM | **Scrive e coordina, non classifica**; i numeri vengono solo dai tool | ChatGPT e Gemini mancano dal 32 al 50% dei tumori | [Bhagwat 2026](papers/2026_bhagwat_mllm-fitzpatrick.md) |
| Agenti | **v0 → v1 (MCP) → v2 → v3**, critico a regole; multi-agente solo se migliora davvero | Il multi-agente costa circa 15 volte i token di una chat | [S6](papers/S6_introduzione.md), [03](03_architettura.md) |
| Valutazione | Accuratezza bilanciata, specificità ad alta sensibilità, pAUC, tumori mancati, **per fototipo**, CLEAR Derm | Le metriche cambiano le conclusioni | [S7](papers/S7_introduzione.md), [S4](papers/S4_introduzione.md) |
| Inclusione | **RQ6:** HIBA, PAD-UFES-20, lesioni acrali (BALD); adattamento con pochi dati locali; spagnolo e portoghese; uso con poche risorse | Pelli V–VI = 5,8% delle immagini pubbliche; nessuno studio su pazienti latinoamericani | [09](09_pelli_non_chiare.md) |
| Regole | **Prototipo di ricerca**, non un dispositivo; AI Act come lista volontaria | MDR: almeno classe IIa; AI Act: alto rischio, obblighi dal 2028 | [04](04_etica_regolatorio.md) |

## Le domande di ricerca
| RQ | Verbo | Domanda in breve | Milestone |
|----|-------|------------------|-----------|
| RQ1 | Vedere | Quanto vale PanDerm rispetto ai backbone liberi, dentro e fuori dal laboratorio? | M2–M3 |
| RQ2 | Dubitare | Il "non so" conformal regge su lesioni mai viste, centri nuovi e fototipi diversi? | M3 |
| RQ3 | Spiegare | Le spiegazioni sono fedeli al modello e concordano con gli esperti? | M3 |
| RQ4 | Coordinare | L'agente MCP scrive report tracciabili, senza numeri inventati? Il multi-agente vale il suo costo? | M4 |
| RQ5 | Aiutare (facoltativa) | Neo Helper migliora le decisioni dei medici non specialisti? | dopo M5 |
| RQ6 | Includere | Lo stato dell'arte funziona su pelli latinoamericane e asiatiche, e può essere adattato da centri con poche risorse? | M2–M5 |

Il cuore della tesi sono **RQ1, RQ2 e RQ6**. Dettagli in [07](07_domande_di_ricerca.md).

## La pipeline
- **Costruzione (una volta):**
  1. controllo dei dati (MONET);
  2. divisione per lesione;
  3. segmentazione;
  4. vettori di PanDerm;
  5. testa a 7 classi;
  6. calibrazione e conformal;
  7. valutazione esterna e per fototipo;
  8. model card e CLEAR Derm.
- **Uso (ogni caso):**
  1. foto;
  2. controllo qualità;
  3. segmentazione;
  4. vettore;
  5. classificazione + insieme conformal;
  6. criteri, casi simili, heatmap;
  7. critico;
  8. report con catena di prove, in più lingue.

## I passi definiti
| Milestone | Cosa | Issue |
|-----------|------|-------|
| ✅ **M1** Letteratura | 42 schede, scelte, RQ, verifiche, revisione | #1–#10, #31, #32 (chiuse) |
| **M2** Baseline | Ambiente (anche solo CPU), download con licenza per immagine, EDA, baseline congelate | #11–#14 |
| **M3** Modello finale | Fine-tuning, segmentazione, "non so", spiegazioni, test esterni, **RQ6** | #15–#19, #33 |
| **M4** MCP e agenti | v0, server MCP, v2, v3 con critico, report multilingue | #20–#23, #34 |
| **M5** Demo web | Demo compatibile con le licenze, web app, pacchetto per centri con poche risorse | #24, #25, #35 |
| **M6** App mobile | Expo con guida all'acquisizione; dispositivo o server | #26, #27 |
| **M7** Release | Model card e data card, tesi, DOI | #28–#30 |

## Cosa resta aperto
- **Domande:**
  - licenza di PanDerm (risposta degli autori);
  - MONET legge i criteri dermoscopici?;
  - segmentazione U-Net o MedSAM;
  - LLM locale o via API;
  - demo pubblica e licenze;
  - dispositivo o server;
  - regole in movimento (AI Act al 2028);
  - dataset asiatici pubblici.
- **Azioni di Cesar:**
  - mail agli autori di PanDerm (bozza pronta);
  - ospedale di contatto;
  - Zotero sì o no.
- **Rischi principali:**
  - ambizione contro tempo, per cui RQ1, RQ2 e RQ6 vengono prima;
  - dipendenza da PanDerm, coperta da DINOv2;
  - pochi dati dermoscopici su pelli scure.

## Dove trovare cosa
| Documento | Contenuto |
|-----------|-----------|
| [00 roadmap](00_roadmap.md) | Fasi, milestone, azioni in sospeso |
| [01 stato dell'arte](01_stato_dell_arte.md) | Tutte le fonti, gap, tabella comparativa |
| [02 risorse](02_risorse.md) | Dataset, modelli, licenze |
| [03 architettura](03_architettura.md) | Tool MCP, agenti, schema del report |
| [04 etica e regole](04_etica_regolatorio.md) | MDR, AI Act, privacy |
| [05 scelte e pipeline](05_scelte_e_pipeline.md) | Scelte confermate, licenze, pipeline |
| [06 verifiche](06_verifiche_M1.md) | Riferimenti e licenze verificati |
| [07 domande di ricerca](07_domande_di_ricerca.md) | RQ1–RQ6 e contributo |
| [08 revisione](08_revisione_M1.md) | Controllo finale della M1 |
| [09 pelli non chiare](09_pelli_non_chiare.md) | Dataset e studi per la RQ6 |
| [figures/](figures/) | Storyboard 1–4 |
