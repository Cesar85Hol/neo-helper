# Model Context Protocol (MCP) — la specifica

- **Fonte:** [modelcontextprotocol.io/specification](https://modelcontextprotocol.io/specification/latest). Protocollo aperto presentato da Anthropic nel novembre 2024 ⚠️ data di lancio da verificare.
- **Testo letto (2026-11-04):** la pagina introduttiva della versione **2025-06-18** e quella della versione più recente, **2026-07-28**. Non ho letto le pagine di dettaglio (architettura, protocollo di base, trasporti).

## In una frase
MCP è uno **standard per collegare un LLM a strumenti e dati esterni**, come una presa universale. Lo stesso server di strumenti funziona con qualsiasi applicazione compatibile.

## Come è fatto
- **Messaggi JSON-RPC 2.0.** Si ispira al Language Server Protocol degli editor di codice.
- **Ruoli:**
  - **host:** l'applicazione con l'LLM, per esempio Claude Desktop o l'app di Neo Helper;
  - **client:** il connettore dentro l'host;
  - **server:** il servizio che offre le capacità.
- **Cosa offre un server:**
  - **Tool:** funzioni che il modello può chiamare (per esempio `classify`);
  - **Resource:** dati e contesto (per esempio la scheda di un dataset);
  - **Prompt:** modelli di messaggio e workflow per l'utente.
- **Cosa può offrire un client:**
  - **Elicitation:** il server chiede informazioni all'utente;
  - nella versione 2025-06-18 anche **sampling** (il server chiede all'LLM di generare) e **roots** (confini del filesystem).
- **Novità della versione 2026-07-28:**
  - richieste **senza stato** e autosufficienti;
  - capacità negoziate a ogni richiesta;
  - **estensioni** opzionali: **Tasks** (operazioni lunghe asincrone), Skills, MCP Apps (interfacce dentro la conversazione).
  - ⚠️ Da verificare nei dettagli prima di scrivere il server.

## Principi di sicurezza della specifica
1. **Consenso e controllo dell'utente** su tutti gli accessi ai dati e le azioni.
2. **Privacy:** l'host non espone i dati dell'utente ai server senza consenso esplicito.
3. **Sicurezza dei tool:**
   - i tool sono esecuzione di codice;
   - le loro descrizioni sono **non affidabili** se il server non è fidato;
   - serve il consenso prima di invocarli.
4. MCP **non può imporre** questi principi da solo: tocca a chi implementa.

## Cosa porto in Neo Helper
- **Server `neo-vision`** (issue M4.2) con i tool:
  - `check_quality`
  - `segment_lesion`
  - `embed_image`
  - `classify`
  - `predict_set` (conformal)
  - `explain_heatmap`
  - `describe_concepts` (MONET)
  - `similar_cases` (CBIR)
- **Resource:** model card, data card, soglie in uso, versioni dei modelli. L'agente può citarle nel report.
- **Prompt:** "report per il medico" e "report per lo studente".
- **Privacy:** le immagini dei pazienti restano sul server locale. Al modello linguistico vanno solo i risultati numerici, non l'immagine, se non serve.
- Vantaggio per la tesi: gli stessi tool si possono usare **da Claude Desktop** per le prove e poi dall'app web o mobile, senza riscriverli.
- Partire dalla versione stabile supportata dall'SDK Python ufficiale ⚠️ da controllare al momento dello sviluppo.
