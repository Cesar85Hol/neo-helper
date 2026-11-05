# Episodio 12 — Mappe di calore e concetti: come spiega una rete

Pacchetto tre, primo episodio. Una rete dice "melanoma, ottanta per cento". Il medico chiede: perché? Oggi vediamo i modi per rispondere, e quali funzionano davvero.

Il modo più famoso è la mappa di calore. Il metodo si chiama Grad-CAM, ed è del duemiladiciassette, da Georgia Tech. L'idea è semplice. Si guarda l'ultimo strato della rete, quello che vede ancora la forma dell'immagine, e si misura quanto ogni zona ha spinto verso la risposta "melanoma". Il risultato è una macchia colorata sopra l'immagine: rosso dove la rete ha guardato di più. Funziona su quasi ogni rete, senza modificarla. E serve davvero: gli autori l'hanno usata per scoprire che un modello che distingueva medici e infermieri guardava i capelli e il viso, cioè il genere, invece del camice.

Ma c'è un problema, e lo ha mostrato un gruppo di Google nel duemiladiciotto: Adebayo e colleghi. Hanno fatto un esperimento crudele. Hanno distrutto i pesi della rete, cioè tutto quello che aveva imparato, e hanno ricalcolato le mappe. Molte mappe restavano quasi uguali. Erano belle, convincenti, e non dicevano nulla sul modello. Assomigliavano a un semplice rilevatore di bordi. Grad-CAM supera questo test di sanità. La sua versione più nitida, Guided Grad-CAM, no.

E anche quando funziona, la mappa dice dove guarda la rete, non perché. Se la macchia rossa cade sul bordo della lesione, il medico deve indovinare: è per le strie irregolari? Per il colore? O per la penna del chirurgo?

Per questo esiste un secondo modo di spiegare: con i concetti. Nel duemilaventi Koh e colleghi, a Stanford, hanno proposto i concept bottleneck models. La rete non va direttamente dall'immagine alla diagnosi. Prima deve dire quali concetti vede, per esempio "reticolo atipico: sì, velo blu-biancastro: no", e solo da questi concetti ricava la diagnosi. Il bello è che il medico può correggere un concetto sbagliato e vedere la diagnosi cambiare. E l'accuratezza resta simile a quella di una rete normale. Il difetto: servono immagini annotate concetto per concetto. Qui torna utile MONET, di cui abbiamo parlato nell'episodio otto, che i concetti li genera da solo.

Poi c'è uno studio che per Neo Helper è un regalo. Chanda e colleghi, Nature Communications, duemilaventiquattro, un consorzio europeo guidato da Heidelberg. Hanno preso tutte le immagini di melanoma e di nevo con istologia di HAM10000, il nostro dataset, più di tremilaseicento. Quattordici dermatologi le hanno annotate con i criteri dermoscopici, indicando anche dove si trovano. E hanno pubblicato queste annotazioni.

Poi hanno addestrato una rete che dà la diagnosi insieme ai criteri e alla loro posizione, e l'hanno provata con centosedici medici, in tre fasi. Da soli, i medici avevano un'accuratezza del sessantasei per cento. Con l'AI, del settantadue. Con l'AI che spiega, del settantatré: praticamente uguale. Le spiegazioni però hanno aumentato la sicurezza dei medici nella propria diagnosi, del dodici per cento, e la fiducia nella macchina, del diciassette per cento. E qui c'è il rovescio della medaglia: con le spiegazioni, i medici erano un po' più d'accordo con l'AI anche quando l'AI sbagliava.

Che cosa portiamo in Neo Helper? La mappa di calore resta, ma soprattutto come strumento di controllo per noi sviluppatori, per vedere se la rete guarda la lesione o il righello, e solo dopo averla verificata con i test di sanità. Al medico parliamo con i criteri dermoscopici, possibilmente localizzati. E le annotazioni di Chanda ci servono per verificare se MONET riconosce davvero i criteri della dermoscopia.

Nel prossimo episodio: i casi simili, il "non so" e cosa succede quando un medico lavora con l'AI.
