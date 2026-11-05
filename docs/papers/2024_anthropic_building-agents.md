# Anthropic, 2024 — Costruire agenti efficaci

- **Fonte:** blog di ingegneria di Anthropic, 19 dicembre 2024 · Erik Schluntz e Barry Zhang · [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)
- **Testo letto:** pagina completa, tramite estrazione automatica (2026-11-04). La pagina avverte che gli strumenti sono cambiati da allora e rimanda ai nuovi *Managed Agents*.

## In una frase
Prima di costruire un agente, prova la soluzione più semplice. Aggiungi complessità solo quando migliora i risultati in modo misurabile.

## Due famiglie di "sistemi agentici"
- **Workflow:** LLM e strumenti seguono un **percorso scritto nel codice**. Sono prevedibili e adatti a compiti ben definiti.
- **Agenti:** l'LLM **decide da solo** i passi e gli strumenti da usare. Sono flessibili, ma costano di più e gli errori si accumulano.

## I mattoni e gli schemi
| Schema | Cosa fa | Quando usarlo |
|--------|---------|---------------|
| **LLM aumentato** | LLM + ricerca + strumenti + memoria (MCP è un modo per collegarli) | Sempre: è il mattone di base |
| **Catena di prompt** | Passi in sequenza, con "cancelli" di controllo nel codice | Compiti che si dividono in passi fissi |
| **Routing** | Classifica l'input e lo manda al percorso giusto | Categorie distinte, classificazione affidabile |
| **Parallelizzazione** | Sottocompiti in parallelo (*sectioning*) o stesso compito più volte (*voting*) | Velocità o più punti di vista |
| **Orchestratore–lavoratori** | Un LLM centrale divide il compito al momento e delega | Quando i sottocompiti non si possono prevedere |
| **Valutatore–ottimizzatore** | Un LLM produce, un altro critica, in ciclo | Criteri di valutazione chiari |
| **Agente autonomo** | Pianifica e agisce in ciclo, controllando il risultato di ogni passo | Problemi aperti, in ambiente protetto, con limiti di iterazioni |

## Tre principi
1. **Semplicità** del disegno.
2. **Trasparenza:** mostrare esplicitamente i passi di pianificazione.
3. **Interfaccia agente-strumento (ACI)** curata quanto un'interfaccia per persone.

## Consigli sugli strumenti
- Descrivere ogni strumento come una buona documentazione per un collega giovane: esempi, casi limite, confini con gli altri strumenti.
- Formati di uscita facili da scrivere per il modello.
- Testare con molti input e correggere.
- **"Poka-yoke":** cambiare gli argomenti in modo che sbagliare sia difficile. Esempio: percorsi di file assoluti invece che relativi.
- Framework: utili, ma nascondono prompt e risposte. Meglio partire dalle API dirette e capire cosa c'è sotto.

## Cosa porto in Neo Helper
- La roadmap è già incrementale (**pipeline fissa → MCP → agente singolo → multi-agente**). Questo testo le dà una base: ogni passo va giustificato con una misura.
- **v0 = workflow** a catena con cancelli: qualità → segmentazione → classificazione → spiegazione → report. Il cancello sulla qualità blocca le immagini inutilizzabili.
- **v2 = orchestratore** con tool MCP. **v3** aggiunge un **valutatore** (agente Critic/Safety) che controlla il report prima di consegnarlo.
- Tool "a prova di errore":
  - `classify` accetta solo un `image_id` già passato dal controllo qualità;
  - le probabilità tornano come JSON con schema fisso;
  - l'LLM **non può** scrivere numeri che non vengano da un tool.
- Trasparenza: il report mostra **quali tool** sono stati chiamati e con quali risultati (traccia).
