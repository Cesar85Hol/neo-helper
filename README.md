# Neo Helper

> Sistema di supporto alla decisione clinica (CDSS) per l'analisi di immagini di nevi/lesioni cutanee.
> Web + mobile, architettura multi-agente orchestrata, con tool esposti via MCP.
> Progetto di studio/ricerca, open source. **Non è un dispositivo medico** e non sostituisce il medico.

## Obiettivi personali del progetto
1. Approfondire l'**analisi di immagini mediche** (classificazione, segmentazione, explainability, calibrazione).
2. Imparare a progettare **pool di agenti** con un **orchestratore** che coordina agenti specializzati.
3. Usare **MCP (Model Context Protocol)** per esporre modelli e strumenti come tool riutilizzabili.
4. Costruire un prodotto end-to-end: modello → API → interfaccia web → app mobile.
5. Verificare se lo stato dell'arte funziona anche su pelli **latinoamericane e asiatiche**, e rendere Neo Helper **usabile da centri di ricerca con poche risorse**, in particolare in America Latina (RQ6).

## Struttura della documentazione
| File | Contenuto |
|------|-----------|
| [docs/00_roadmap.md](docs/00_roadmap.md) | Piano di lavoro "stile tesi magistrale": fasi, deliverable, milestone |
| [docs/01_stato_dell_arte.md](docs/01_stato_dell_arte.md) | Letteratura: paper chiave, domande di ricerca, gap |
| [docs/02_risorse.md](docs/02_risorse.md) | Dataset, modelli pre-addestrati, librerie, tool UI/mobile |
| [docs/03_architettura.md](docs/03_architettura.md) | Architettura del sistema e del pool di agenti / MCP |
| [docs/04_etica_regolatorio.md](docs/04_etica_regolatorio.md) | Disclaimer, privacy, bias, MDR / AI Act |
| [docs/05_scelte_e_pipeline.md](docs/05_scelte_e_pipeline.md) | Scelte confermate, licenze, pipeline, ISIC 2019, nuovi dati, annotazione |
| [docs/06_verifiche_M1.md](docs/06_verifiche_M1.md) | Verifica dei riferimenti e delle licenze (M1.9) |
| [docs/07_domande_di_ricerca.md](docs/07_domande_di_ricerca.md) | Domande di ricerca RQ1–RQ6 e contributo originale |
| [docs/08_revisione_M1.md](docs/08_revisione_M1.md) | Revisione finale della Milestone 1 |
| [docs/annotazione/](docs/annotazione/) | Istruzioni per chi annota (italiano, inglese, spagnolo) |
| [docs/figures/](docs/figures/) | Storyboard delle decisioni |
| [docs/audio/](docs/audio/) | Copioni degli episodi audio |
| [docs/diario.md](docs/diario.md) | Diario di bordo: decisioni prese, cose da verificare, note |
| [docs/papers/](docs/papers/) | Schede di lettura dei paper |
| [docs/refs.bib](docs/refs.bib) | Bibliografia BibTeX |

## Licenze
- Codice: [MIT](LICENSE)
- Documentazione (`docs/`): [CC BY 4.0](docs/LICENSE)
- Dataset e modelli di terze parti restano soggetti alle loro licenze (spesso CC-BY-NC).

## Stato
- [x] Fase 0 — Impostazione documentazione
- [x] Fase 1 — Revisione della letteratura (revisione finale in corso, M1.11)
- [ ] Fase 2 — Dati e baseline
- [ ] Fase 3 — Modello e valutazione
- [ ] Fase 4 — Agenti e MCP
- [ ] Fase 5 — Web app
- [ ] Fase 6 — Mobile app
- [ ] Fase 7 — Valutazione finale e scrittura
