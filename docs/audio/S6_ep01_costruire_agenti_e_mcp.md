# Episodio 14 — Come si costruisce un agente, e cos'è MCP

Siamo alla sezione sei. Finora abbiamo parlato di modelli. Oggi parliamo di come si mettono insieme: un modello linguistico che coordina, e tanti strumenti specializzati.

La prima fonte non è un articolo scientifico, ma una guida molto letta: "Building effective agents", di Anthropic, dicembre duemilaventiquattro. Il primo consiglio è quasi controcorrente: parti dalla soluzione più semplice, e aggiungi complessità solo se migliora i risultati in modo misurabile. Spesso un agente non serve affatto.

La guida distingue due famiglie. I workflow, dove il percorso è scritto nel codice: prima questo passo, poi quest'altro. Sono prevedibili. E gli agenti, dove è il modello a decidere quali passi fare e quali strumenti usare. Sono flessibili, ma costano di più e gli errori si possono accumulare.

Tra gli schemi descritti, due sono importanti per noi. L'orchestratore con i lavoratori: un modello centrale divide il compito e delega le parti ad altri. E il valutatore con l'ottimizzatore: uno produce, un altro controlla e chiede di correggere. Poi c'è un consiglio pratico sugli strumenti, che la guida chiama poka-yoke, una parola giapponese che vuol dire "a prova di errore": scrivi gli strumenti in modo che usarli male sia difficile.

Seconda fonte, sempre Anthropic, giugno duemilaventicinque: come hanno costruito il loro sistema di ricerca con più agenti. Un agente capo scrive un piano, lancia diversi sottoagenti in parallelo, ognuno cerca un pezzo del problema, e alla fine un agente apposito collega ogni frase alla sua fonte. Risultato: novanta per cento meglio di un agente solo. Ma il prezzo è alto: circa quindici volte i token di una normale chat. Gli autori dicono chiaramente quando non conviene: quando le parti del compito dipendono molto l'una dall'altra.

E questo è il caso di Neo Helper. Per analizzare un neo bisogna prima controllare la qualità dell'immagine, poi trovare la lesione, poi classificarla, poi spiegare. Sono passi in fila. Quindi la nostra roadmap ha senso: prima una pipeline fissa, poi un agente singolo con gli strumenti, e solo dopo, se lo dimostriamo con i numeri, più agenti. Il confronto tra agente singolo e multi-agente, con i costi, può diventare una domanda della tesi.

Infine, MCP: Model Context Protocol. È uno standard aperto, lanciato da Anthropic, per collegare un modello linguistico a strumenti e dati. Pensatelo come una presa universale. Da una parte c'è l'applicazione con il modello, dall'altra i server che offrono tre cose: tool, cioè funzioni da chiamare; resource, cioè dati da leggere; e prompt, cioè modelli di messaggio. La versione più recente della specifica è di luglio duemilaventisei.

La specifica insiste sulla sicurezza: l'utente deve dare il consenso, i dati non escono senza permesso, e gli strumenti vanno trattati come codice che può fare danni.

Per Neo Helper avremo un server chiamato neo-vision. Dentro ci saranno gli strumenti: controllo della qualità, segmentazione, classificazione, l'insieme del "non so", la mappa di calore, i concetti di MONET e i casi simili. Il vantaggio è che gli stessi strumenti funzioneranno nelle prove con Claude Desktop, e poi nell'app web e mobile, senza riscriverli. E le immagini dei pazienti possono restare sul server locale: al modello linguistico arrivano solo i numeri.
