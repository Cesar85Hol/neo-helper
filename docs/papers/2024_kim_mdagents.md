# Kim et al., 2024 — MDAgents: una squadra di LLM che si adatta alla complessità del caso

- **Conferenza:** NeurIPS 2024 · [arXiv 2404.15155](https://arxiv.org/abs/2404.15155) · codice: github.com/mitmedialab/MDAgents
- **Gruppo:** MIT (Media Lab; Marzyeh Ghassemi, Cynthia Breazeal, Hae Won Park), Google Research, Seoul National University Hospital
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF. I numeri sono da ricontrollare ⚠️.

## In una frase
Come in ospedale, i casi semplici li risolve un medico solo e quelli complessi un'équipe. MDAgents fa decidere a un LLM "moderatore" quanti agenti servono, e così è più accurato **e** più economico delle squadre fisse.

## Come funziona
1. **Triage della complessità:** un LLM moderatore classifica la domanda come bassa, moderata o alta complessità.
2. **Reclutamento:**
   - bassa → un solo agente "medico di base";
   - moderata → un'**équipe multidisciplinare** di agenti specialisti;
   - alta → più équipe in sequenza (valutazione iniziale, diagnosi, revisione finale).
3. **Discussione:** l'équipe discute a turni. Se non c'è accordo, il moderatore dà un feedback a ciascuno.
4. **Decisione finale:** un agente sintetizza.

Modelli usati: GPT-4(V) e Gemini Pro (Vision), più tecniche di prompting (catena di ragionamento, self-consistency) e **MedRAG** per la conoscenza esterna.

## Risultati
- Migliore in **7 benchmark su 10**: domande d'esame (MedQA, PubMedQA), immagini (Path-VQA, PMC-VQA, MIMIC-CXR), video, ragionamento clinico (DDXPlus).
- **Adattivo meglio che fisso:** sulle domande testuali 81,2% contro 64–72% delle configurazioni fisse ⚠️.
- **RAG + revisione del moderatore:** da 71,8% a 80,3% ⚠️.
- **Più agenti non vuol dire meglio:** il massimo è con circa 3 agenti. Le chiamate alle API scendono da 20,3 a 9,3 rispetto a un gruppo fisso di 5 ⚠️.

## Limiti
- Benchmark di **domande a scelta multipla** e VQA, non casi clinici reali.
- Le immagini sono interpretate dall'LLM multimodale stesso. In dermatologia sappiamo che è debole (Bhagwat 2026).
- Allucinazioni e bias restano un rischio dichiarato dagli autori.

## Altri sistemi della stessa famiglia
- **MedAgents** (Tang et al., 2024): squadra fissa di specialisti LLM che discutono fino al consenso ⚠️ non letto.
- La rassegna di Vatsal 2026 trova che il **design multi-agente** è ormai la norma (82% degli studi).

## Messaggi chiave per la tesi
1. L'idea più utile non è "tanti agenti", ma **adattare la profondità al caso**. È l'equivalente agentico del triage.
2. Le squadre di LLM migliorano sui benchmark testuali. Non dimostrano però di saper **vedere** meglio un'immagine.

## Cosa porto in Neo Helper
- **Routing per incertezza**, invece che per "complessità":
  - caso chiaro (insieme conformal di una sola classe, buona qualità, casi simili concordi) → percorso breve;
  - caso incerto o discordante → percorso lungo con Critic, più spiegazioni e raccomandazione esplicita di invio.
- Misurare **costo e accuratezza** di entrambi i percorsi: è il confronto v2 contro v3 della issue M4.4.
