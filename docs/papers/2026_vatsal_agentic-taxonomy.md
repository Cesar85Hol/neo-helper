# Vatsal et al., 2026 — Agenti LLM in sanità: una tassonomia in sette dimensioni

- **Fonte:** preprint TechRxiv (v1 ottobre 2025, v2 febbraio 2026) e [arXiv 2602.04813](https://arxiv.org/abs/2602.04813). La pubblicazione su *IEEE Access* indicata dalla sintesi alphaXiv **non risulta** su Crossref ⚠️
- **Gruppo:** New York University e Cleveland State University
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF. Percentuali da ricontrollare ⚠️.

## In una frase
Una rassegna di **49 studi** (ottobre 2023 – giugno 2025) sugli agenti LLM in medicina. Gli agenti sono bravi a cercare informazioni e consigliare, ma quasi nessuno ha **controllo umano, recupero dagli errori, sicurezza e conformità alle regole**.

## Cosa hanno fatto
- Ricerca in Google Scholar, PubMed, DBLP, Scopus e arXiv: 137 articoli, 49 inclusi. Selezione fatta da tre revisori.
- **7 dimensioni e 29 sotto-dimensioni:**
  - capacità cognitive;
  - gestione della conoscenza;
  - modalità di interazione;
  - adattamento;
  - sicurezza ed etica;
  - tipo di architettura;
  - compiti clinici.
- Ogni studio è valutato per ogni voce come implementato, parziale o assente.

## Risultati (percentuale di studi con la voce implementata per intero)
| Voce | Implementata | Assente |
|------|--------------|---------|
| Conoscenza esterna (RAG) | ~76% | — |
| Design multi-agente | ~82% | — |
| **Human-in-the-loop** | ~12% | ~86% |
| **Recupero dagli errori** | ~4% | ~80% |
| Attivazione da eventi | ~6% | ~92% |
| Protezioni di sicurezza | ~6% | ~65% |
| Bias ed equità | ~10% | ~65% |
| **Conformità alle regole** | ~10% | ~86% |
| Rilevamento della deriva dei dati | — | ~98% |
| Risoluzione dei conflitti tra fonti | — | ~61% |

- I compiti più maturi sono quelli **informativi**: documentazione, risposte a domande, benchmark.
- Diagnosi e triage sono maturi solo in parte; terapia e monitoraggio sono indietro.

## Messaggi chiave per la tesi
1. Le **lacune comuni** degli agenti medici sono proprio le cose che un sistema clinico serio deve avere: controllo umano, gestione degli errori, sicurezza, equità, regole.
2. Il multi-agente è ormai **la norma**: non è un contributo originale in sé. Lo diventa se misurato e giustificato (Anthropic 2025).

## Cosa porto in Neo Helper
Usare la tassonomia come **checklist di progetto** per gli agenti, insieme a CLEAR Derm per il modello:
- **human-in-the-loop:** il medico conferma o corregge i concetti, come negli interventi dei concept bottleneck;
- **recupero dagli errori:** tool che falliscono → messaggio chiaro, nessuna diagnosi inventata;
- **risoluzione dei conflitti:** è il compito del critico (DermAgent);
- **bias:** risultati per fototipo (DDI);
- **regole:** uso dichiarato, avvisi, registro delle decisioni (AI Act, MDR → Pacchetto 4);
- **deriva:** monitorare la distribuzione degli embedding delle immagini in arrivo rispetto a HAM10000 (fuori distribuzione).
