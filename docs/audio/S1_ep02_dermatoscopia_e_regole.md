# Episodio 2 — Come il medico guarda un neo: ABCDE, dermatoscopio e 7-point checklist

Bentornato. Nel primo episodio abbiamo visto cosa riconoscere. Oggi vediamo come lo fa il medico. Perché se vogliamo costruire un sistema che aiuti il medico, dobbiamo prima capire il suo modo di ragionare.

Cominciamo dall'esame a occhio nudo, con una regola che forse conosci già: la regola A B C D E.

A come Asimmetria: le due metà del neo non coincidono.
B come Bordi: irregolari, frastagliati.
C come Colore: non uniforme, con più tonalità di marrone, nero, rosso, blu o bianco.
D come Diametro: superiore a sei millimetri.
E come Evoluzione: il neo cambia nel tempo.

E questa è la lettera più importante. Un neo che cambia, in forma, colore o dimensione, merita sempre attenzione.

C'è poi un'idea molto elegante, chiamata il segno del brutto anatroccolo. In una persona con tanti nei, quelli che si somigliano tra loro sono probabilmente benigni. Quello diverso da tutti gli altri, il brutto anatroccolo, è sospetto. Tieni a mente questa idea: quasi tutti i sistemi di intelligenza artificiale guardano un neo alla volta, e quindi non possono usarla. È un limite che ritroveremo spesso.

Passiamo allo strumento chiave: il dermatoscopio. È una lente con una luce speciale che permette di vedere strutture sotto la superficie della pelle, invisibili a occhio nudo. Migliora la diagnosi, ma richiede formazione ed esperienza. Le immagini dermatoscopiche sono molto più uniformi delle foto normali, con la stessa distanza e la stessa luce. Per questo quasi tutti i dataset per l'intelligenza artificiale usano immagini dermatoscopiche.

Ora, come si passa dall'osservare al decidere? Con degli algoritmi diagnostici, cioè delle ricette. Te ne racconto tre.

La prima è la pattern analysis, il metodo degli esperti: si riconosce il disegno generale della lesione e le sue strutture. È il metodo più accurato, ma anche il più difficile da imparare.

La seconda è la regola A B C D della dermatoscopia, proposta da Stolz. Si dà un punteggio ad asimmetria, bordi, colori e strutture, e lo si combina in un punteggio totale. Sotto quattro virgola settantacinque, probabilmente benigno. Sopra cinque virgola quarantacinque, molto sospetto per melanoma. Per noi è interessante perché una parte di questo punteggio si può calcolare automaticamente dal contorno della lesione.

La terza è la sette punti di Argenziano, un lavoro italiano, pubblicato nel millenovecentonovantotto da un gruppo di Napoli. Ci sono tre criteri maggiori, che valgono due punti ciascuno, come il velo blu biancastro o il reticolo atipico. E quattro criteri minori, che valgono un punto, come le strie irregolari. Se il totale arriva a tre, si sospetta il melanoma.

E come funzionava? Nello studio originale, su trecentoquarantadue lesioni confermate al microscopio, la sette punti trovava il novantacinque per cento dei melanomi. La regola A B C D l'ottantacinque. La pattern analysis degli esperti il novantuno per cento, ma con molti meno falsi allarmi. E, dato importante, con la sette punti anche i medici meno esperti diventavano più accurati.

Ultimo punto, ed è una lezione di umiltà. Nel duemilatre, quaranta esperti di tutto il mondo hanno valutato le stesse centootto lesioni via Internet. Sulla diagnosi finale erano abbastanza d'accordo. Ma sui singoli criteri, cioè su cosa vedevano nell'immagine, l'accordo era scarso. Esperti diversi vedono strutture diverse nella stessa foto.

Che cosa significa per Neo Helper? Che quando il nostro sistema calcolerà i criteri dermatoscopici, dovrà presentarli come un aiuto, non come la verità. Perché neanche gli esperti umani sono d'accordo su di essi.

Chiudiamo con la domanda: come si sa qual è la diagnosi vera? Nel dataset HAM diecimila, più della metà delle lesioni è stata asportata e analizzata al microscopio. Le altre sono confermate dal controllo nel tempo, dal consenso di due esperti o da altri esami. Ricordalo: la qualità della diagnosi di riferimento è la base di tutto.

Con questo si chiude la sezione uno. Dalla prossima sezione entriamo nei paper che hanno portato l'intelligenza artificiale in dermatologia.
