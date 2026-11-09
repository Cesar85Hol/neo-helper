# Episodio 20 — Le domande della tesi

Siamo alla fine della revisione della letteratura. In diciannove episodi abbiamo visto reti, dati, colori della pelle, spiegazioni, agenti, gare e regole. Oggi tiriamo le fila: quali domande deve fare la tesi di Neo Helper, e che cosa porta di nuovo.

Prima una nota sulle verifiche. Ho ricontrollato online le informazioni che avevamo segnato come incerte. Tre sorprese. La prima: il dataset di Barcellona, BCN20000, ha una licenza aperta se lo si scarica da Figshare, ma la copia sull'archivio ISIC è non commerciale. Conta da dove si scarica. La seconda: sull'archivio ISIC c'è un dataset argentino, dell'Hospital Italiano de Buenos Aires, con milleseicento immagini e licenza aperta. Un test latinoamericano già pronto, anche se con pelli soprattutto chiare. La terza: l'AI Act europeo è stato modificato a luglio duemilaventisei, e gli obblighi per i dispositivi medici con intelligenza artificiale slittano all'agosto duemilaventotto.

E ora le domande. Sono quattro, più una facoltativa. Ognuna ha un verbo.

Prima domanda: vedere. Quanto vale davvero PanDerm, il foundation model dermatologico, rispetto a modelli generici come DINOv2? E quanto si perderebbe usando un modello con licenza libera? Lo misuriamo non solo su HAM10000, ma su sei test esterni, da Barcellona a Stanford, dal Brasile all'Argentina, con metriche cliniche: quanto è specifico il modello quando trova il novanta o il novantacinque per cento dei tumori. L'ipotesi è che il vantaggio di PanDerm si riduca fuori dal laboratorio, come hanno mostrato Anriot e la gara del duemiladiciannove.

Seconda domanda: dubitare. Il sistema sa dire "non so" quando serve, e lo sa fare per tutti? Nel duemiladiciannove i migliori algoritmi riconoscevano come sconosciute solo il sei per cento delle lesioni mai viste, e quasi metà le chiamavano maligne. Noi usiamo gli insiemi conformal, che danno una garanzia sulla copertura. Ma la garanzia vale solo se i pazienti nuovi assomigliano a quelli di partenza. Quindi misuriamo dove si rompe: per classe, per centro, per colore della pelle. E quanti pazienti in più andrebbero dallo specialista.

Terza domanda: spiegare. Le spiegazioni di Neo Helper sono vere? Cioè, sono fedeli a quello che fa il modello, e corrispondono a quello che indicano i dermatologi? Qui abbiamo un alleato prezioso: le annotazioni di quattordici dermatologi sulle immagini di HAM10000, pubblicate dal gruppo di Chanda con licenza aperta. Con quelle possiamo verificare i criteri dermoscopici, le mappe di calore e i casi simili.

Quarta domanda: coordinare. Un agente che usa gli strumenti attraverso MCP, con un critico fatto di regole, scrive report migliori e tracciabili, senza mai inventare un numero? E un sistema con più agenti vale il suo costo, che può essere molte volte quello di un agente solo? Prepareremo anche dei casi trappola: segni di penna, lesioni sconosciute, conflitti tra modelli, dati del paziente sbagliati.

E la quinta, facoltativa: aiutare. Se l'ospedale di contatto sarà d'accordo, un piccolo studio con medici non specialisti, prima senza e poi con Neo Helper. Per misurare se decidono meglio, e quanto lo seguono quando sbaglia.

Qual è allora il contributo originale? In una frase: un assistente aperto che vede con un modello addestrato, dice "non so" con una garanzia misurata, spiega con la lingua del dermatologo verificata dagli esperti, e coordina gli strumenti in modo tracciabile, con un confronto onesto dei costi. E con la trasparenza su licenze e regole.

Queste domande sono una proposta. Diventano definitive quando le confermi.
