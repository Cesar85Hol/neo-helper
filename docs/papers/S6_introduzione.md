# §6 — Introduzione: agenti, sistemi multi-agente e MCP

> Issue #7 (M1.7) · Fonti: blog di ingegneria di Anthropic, specifica MCP, PubMed, alphaXiv. Ogni scheda dice cosa è stato letto.

Fin qui abbiamo parlato di **modelli**. Questa sezione parla di **sistemi**: come si mettono insieme i modelli, gli strumenti e un LLM che coordina, in modo che il risultato sia utile, verificabile e sicuro.

**1. Come si costruisce un agente (Anthropic 2024 e 2025).**
- **Partire semplice.** Prima un *workflow* con un percorso fisso, poi un agente che decide, poi più agenti. Ogni passo va giustificato con una misura.
- Gli schemi principali:
  - catena con cancelli di controllo;
  - routing;
  - parallelizzazione;
  - **orchestratore–lavoratori**;
  - **valutatore–ottimizzatore**.
- Il sistema multi-agente di ricerca di Anthropic supera un agente singolo del 90%, ma usa circa **15 volte** i token di una chat. Conviene solo quando il compito si divide bene in parti indipendenti.

**2. Lo standard per collegare gli strumenti (MCP).**
- Il **Model Context Protocol** definisce come un'applicazione con un LLM parla con server che offrono **tool**, **resource** e **prompt**.
- Principi di sicurezza: consenso dell'utente, privacy dei dati, tool trattati come codice non fidato.

**3. Agenti in medicina.**
- **AMIE** (Google, *Nature* 2025 e 2026): un LLM che fa l'anamnesi in chat. In visite simulate batte i medici di base su quasi tutti gli assi, e nel 2026 si àncora alle linee guida. Gli autori: "non pronto per la clinica".
- **MDAgents** (NeurIPS 2024): una squadra di LLM che si adatta alla **complessità** del caso, come un triage. Più accurata e più economica delle squadre fisse.
- **DermAgent** (Monash, preprint 2026): il lavoro **più vicino a Neo Helper**. GPT-4o orchestra PanDerm, un annotatore di concetti dermoscopici, modelli descrittivi, ricerca di casi simili e di linee guida, più un **critico a regole** che rileva i conflitti e fa ripetere.
- **Vatsal 2026** (rassegna di 49 studi): gli agenti medici usano quasi tutti RAG e più agenti, ma quasi nessuno ha **controllo umano, recupero dagli errori, sicurezza o conformità alle regole**.

**Il filo conduttore per Neo Helper:**
- **v0** (pipeline fissa) → **v1** (server MCP `neo-vision`) → **v2** (un agente con tool) → **v3** (multi-agente con Critic). Il passo v2 → v3 va **misurato** in accuratezza, qualità del report, token e tempo;
- l'LLM **orchestra e scrive**, i numeri vengono solo dai tool, e ogni frase del report cita il tool che l'ha prodotta (catena di prove);
- **critico deterministico** (regole, non un LLM): qualità, copertura dei tool, conflitti tra classificatore, casi simili e concetti, incertezza conformal;
- routing per **incertezza**: percorso breve per i casi chiari, lungo per quelli incerti;
- la tassonomia di Vatsal come **checklist** degli agenti, CLEAR Derm per il modello.

**Il contributo originale, rispetto a DermAgent.** Sono ipotesi da fissare nella M1.10:
- classificatore **addestrato e calibrato** con "non so" garantito, invece dello zero-shot;
- risultati **per fototipo** e su test esterni con biopsia;
- criteri dermoscopici collegati alle annotazioni di Chanda 2024;
- controller **locale o open source** con MCP standard, per la privacy;
- confronto misurato **v2 contro v3**;
- interfaccia pensata per **medici non specialisti**.

| Anno | Fonte | Tipo | Messaggio |
|------|-------|------|-----------|
| 2024 | Anthropic, *Building effective agents* | guida | Workflow vs agenti; partire semplice; tool a prova di errore |
| 2024– | Specifica **MCP** (ultima 2026-07-28) | standard | Tool, resource, prompt; consenso e sicurezza |
| 2024 | Kim, **MDAgents** (NeurIPS) | multi-agente medico | Squadra adattata alla complessità: più accurata e più economica |
| 2025 | Anthropic, sistema di ricerca multi-agente | caso di studio | +90% ma circa 15 volte i token; serve parallelismo vero |
| 2025 | Tu, **AMIE** (*Nature*) | LLM conversazionale | Meglio dei medici di base in OSCE simulati; non pronto per la clinica |
| 2026 | Liu, **DermAgent** (preprint) | agente dermatologico | Tool + RAG + critico a regole; il più vicino a Neo Helper |
| 2026 | Vatsal (*IEEE Access*) | rassegna | Mancano controllo umano, errori, sicurezza, regole |

**Da leggere in seguito:** MedAgents (Tang 2024) ⚠️; la rassegna "LLM-based agents in medicine" (Wang 2025, arXiv 2502.11211) ⚠️; MedAgent-Pro ⚠️.
