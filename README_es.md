# Neo Helper

[English](README.md) · [Italiano](README_it.md) · **Español**

> Sistema de apoyo a la decisión clínica (CDSS) para el análisis de imágenes de nevos y lesiones cutáneas.
> Web + móvil, arquitectura multiagente orquestada, con herramientas expuestas mediante MCP.
> Proyecto de estudio e investigación, de código abierto. **No es un dispositivo médico** y no sustituye al médico.

## Objetivos personales del proyecto
1. Profundizar en el **análisis de imágenes médicas** (clasificación, segmentación, explicabilidad, calibración).
2. Aprender a diseñar **grupos de agentes** con un **orquestador** que coordina agentes especializados.
3. Usar **MCP (Model Context Protocol)** para exponer modelos e instrumentos como herramientas reutilizables.
4. Construir un producto de extremo a extremo: modelo → API → interfaz web → aplicación móvil.
5. Comprobar si el estado del arte funciona también en pieles **latinoamericanas y asiáticas**, y hacer que Neo Helper sea **utilizable por centros de investigación con pocos recursos**, en particular en América Latina (RQ6).

## Código
| Carpeta | Contenido |
|---------|-----------|
| [ml/](ml/README_es.md) | Código de aprendizaje automático: entorno, conjuntos de datos, registro de datos, líneas base (desde el Hito 2) |
| [ml/data/](ml/data/README_es.md) | Procedencia y licencias de los conjuntos de datos; el registro de datos común |
| [tools/](tools/) | Scripts de apoyo para la documentación (archivos Word, episodios de audio) |

## Documentación
La documentación de investigación en `docs/` está escrita en italiano.

| Archivo | Contenido |
|---------|-----------|
| [docs/00_roadmap.md](docs/00_roadmap.md) | Plan de trabajo al estilo de una tesis de máster: fases, entregables, hitos |
| [docs/01_stato_dell_arte.md](docs/01_stato_dell_arte.md) | Literatura: artículos clave, preguntas de investigación, vacíos |
| [docs/02_risorse.md](docs/02_risorse.md) | Conjuntos de datos, modelos preentrenados, bibliotecas, herramientas de interfaz y móvil |
| [docs/03_architettura.md](docs/03_architettura.md) | Arquitectura del sistema y del grupo de agentes / MCP |
| [docs/04_etica_regolatorio.md](docs/04_etica_regolatorio.md) | Aviso legal, privacidad, sesgos, MDR / AI Act |
| [docs/05_scelte_e_pipeline.md](docs/05_scelte_e_pipeline.md) | Decisiones confirmadas, licencias, flujo de trabajo, ISIC 2019, datos nuevos, anotación |
| [docs/06_verifiche_M1.md](docs/06_verifiche_M1.md) | Verificación de referencias y licencias (M1.9) |
| [docs/07_domande_di_ricerca.md](docs/07_domande_di_ricerca.md) | Preguntas de investigación RQ1–RQ6 y contribución original |
| [docs/08_revisione_M1.md](docs/08_revisione_M1.md) | Revisión final del Hito 1 |
| [docs/09_pelli_non_chiare.md](docs/09_pelli_non_chiare.md) | Conjuntos de datos y estudios sobre pieles no claras (RQ6) |
| [docs/10_dashboard_M1.md](docs/10_dashboard_M1.md) | **Panel: cómo salimos del Hito 1** (decisiones, RQ, pasos) |
| [docs/dashboard/](docs/dashboard/) | Panel interactivo en italiano, inglés y español (abrir `neo_helper_M1.html` en el navegador) |
| [docs/annotazione/](docs/annotazione/) | Instrucciones para quienes anotan (italiano, inglés, español) |
| [docs/figures/](docs/figures/) | Guiones gráficos de las decisiones |
| [docs/audio/](docs/audio/) | Guiones de los episodios de audio |
| [docs/diario.md](docs/diario.md) | Diario del proyecto: decisiones tomadas, cosas por verificar, notas |
| [docs/papers/](docs/papers/) | Fichas de lectura de los artículos |
| [docs/refs.bib](docs/refs.bib) | Bibliografía BibTeX |

## Licencias
- Código: [MIT](LICENSE)
- Documentación (`docs/`): [CC BY 4.0](docs/LICENSE)
- Los conjuntos de datos y modelos de terceros siguen sujetos a sus propias licencias (a menudo CC BY-NC).

## Estado
- [x] Fase 0 — Preparación de la documentación
- [x] Fase 1 — Revisión de la literatura (**Hito 1 cerrado el 2026-11-10**; resumen en [docs/10_dashboard_M1.md](docs/10_dashboard_M1.md))
- [ ] Fase 2 — Datos y líneas base (en curso: hechos el entorno, el registro de datos y HAM10000)
- [ ] Fase 3 — Modelo y evaluación
- [ ] Fase 4 — Agentes y MCP
- [ ] Fase 5 — Aplicación web
- [ ] Fase 6 — Aplicación móvil
- [ ] Fase 7 — Evaluación final y redacción
