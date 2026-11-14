# Neo Helper

**English** · [Italiano](README_it.md) · [Español](README_es.md)

> Clinical decision support system (CDSS) for the analysis of images of nevi and skin lesions.
> Web + mobile, orchestrated multi-agent architecture, with tools exposed through MCP.
> Study and research project, open source. **It is not a medical device** and does not replace the physician.

## Personal goals of the project
1. Go deeper into **medical image analysis** (classification, segmentation, explainability, calibration).
2. Learn to design **pools of agents** with an **orchestrator** that coordinates specialised agents.
3. Use **MCP (Model Context Protocol)** to expose models and instruments as reusable tools.
4. Build an end-to-end product: model → API → web interface → mobile app.
5. Check whether the state of the art also works on **Latin American and Asian** skin, and make Neo Helper **usable by research centres with few resources**, in particular in Latin America (RQ6).

## Code
| Folder | Content |
|--------|---------|
| [ml/](ml/README.md) | Machine-learning code: environment, datasets, data registry, baselines (Milestone 2 onwards) |
| [ml/data/](ml/data/README.md) | Provenance and licences of the datasets; the common data registry |
| [tools/](tools/) | Helper scripts for the documentation (Word files, audio episodes) |

## Documentation
The research documentation in `docs/` is written in Italian.

| File | Content |
|------|---------|
| [docs/00_roadmap.md](docs/00_roadmap.md) | Work plan in the style of a master's thesis: phases, deliverables, milestones |
| [docs/01_stato_dell_arte.md](docs/01_stato_dell_arte.md) | Literature: key papers, research questions, gaps |
| [docs/02_risorse.md](docs/02_risorse.md) | Datasets, pre-trained models, libraries, UI and mobile tools |
| [docs/03_architettura.md](docs/03_architettura.md) | Architecture of the system and of the agent pool / MCP |
| [docs/04_etica_regolatorio.md](docs/04_etica_regolatorio.md) | Disclaimer, privacy, bias, MDR / AI Act |
| [docs/05_scelte_e_pipeline.md](docs/05_scelte_e_pipeline.md) | Confirmed choices, licences, pipeline, ISIC 2019, new data, annotation |
| [docs/06_verifiche_M1.md](docs/06_verifiche_M1.md) | Check of references and licences (M1.9) |
| [docs/07_domande_di_ricerca.md](docs/07_domande_di_ricerca.md) | Research questions RQ1–RQ6 and original contribution |
| [docs/08_revisione_M1.md](docs/08_revisione_M1.md) | Final review of Milestone 1 |
| [docs/09_pelli_non_chiare.md](docs/09_pelli_non_chiare.md) | Datasets and studies on non-light skin (RQ6) |
| [docs/10_dashboard_M1.md](docs/10_dashboard_M1.md) | **Dashboard: how we left Milestone 1** (choices, RQs, steps) |
| [docs/dashboard/](docs/dashboard/) | Interactive dashboard in Italian, English and Spanish (open `neo_helper_M1.html` in a browser) |
| [docs/annotazione/](docs/annotazione/) | Instructions for annotators (Italian, English, Spanish) |
| [docs/figures/](docs/figures/) | Decision storyboards |
| [docs/audio/](docs/audio/) | Scripts of the audio episodes |
| [docs/diario.md](docs/diario.md) | Project log: decisions taken, things to verify, notes |
| [docs/papers/](docs/papers/) | Reading notes on the papers |
| [docs/refs.bib](docs/refs.bib) | BibTeX bibliography |

## Licences
- Code: [MIT](LICENSE)
- Documentation (`docs/`): [CC BY 4.0](docs/LICENSE)
- Third-party datasets and models remain subject to their own licences (often CC BY-NC).

## Status
- [x] Phase 0 — Documentation set-up
- [x] Phase 1 — Literature review (**Milestone 1 closed on 2026-11-10**; summary in [docs/10_dashboard_M1.md](docs/10_dashboard_M1.md))
- [ ] Phase 2 — Data and baselines (in progress: environment, data registry and HAM10000 done)
- [ ] Phase 3 — Model and evaluation
- [ ] Phase 4 — Agents and MCP
- [ ] Phase 5 — Web app
- [ ] Phase 6 — Mobile app
- [ ] Phase 7 — Final evaluation and writing
