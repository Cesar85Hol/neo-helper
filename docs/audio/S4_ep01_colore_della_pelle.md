# Episodio 10 — Il colore della pelle: Fitzpatrick 17k e DDI

Sezione quattro: bias ed equità. Fino a qui abbiamo visto reti che battono i dermatologi. Oggi ci chiediamo: su quali pazienti? Perché se un modello funziona solo su una parte della popolazione, non è un buon modello. È un modello ingiusto.

Prima un piccolo strumento. La scala di Fitzpatrick divide la pelle in sei fototipi, dall'uno al sei. Il fototipo uno è una pelle chiarissima che si scotta sempre al sole. Il sei è una pelle molto scura che non si scotta mai. È nata per altri scopi, ma oggi si usa per misurare se un'intelligenza artificiale funziona allo stesso modo su tutti i colori di pelle.

Primo lavoro: Fitzpatrick 17k, di Matthew Groh e colleghi del MIT, duemilaventuno. L'ho letto per intero. Hanno preso circa sedicimilacinquecento foto cliniche da due atlanti online, centoquattordici malattie diverse, e hanno fatto etichettare il fototipo di ogni immagine. Il primo risultato è una fotografia del problema: le immagini di pelli chiare sono tre volte e mezzo quelle di pelli scure. E per venticinque malattie su centoquattordici non c'è nemmeno un'immagine di fototipo sei.

Poi l'esperimento. Addestrano la rete solo su due fototipi, per esempio uno e due, e la testano sugli altri. Risultato: la rete va meglio sui fototipi vicini a quelli che ha visto, e peggio su quelli lontani. Vale in tutte le direzioni: anche una rete addestrata solo su pelli scure va peggio sulle pelli chiarissime. Il messaggio è semplice: la rete conosce bene solo quello che ha visto.

Secondo lavoro, il più importante di questa sezione: DDI, Diverse Dermatology Images, di Roxana Daneshjou e colleghi a Stanford, pubblicato su Science Advances nel duemilaventidue. Letto per intero.

DDI è piccolo, seicentocinquantasei foto, ma è speciale per due motivi. Primo: ogni lesione è stata biopsiata, quindi la diagnosi è certa. Secondo: le pelli scure e quelle chiare sono abbinate. Per ogni lesione su pelle scura c'è la stessa diagnosi su pelle chiara, in un paziente dello stesso sesso e di età simile. Così il confronto è onesto.

Su questo dataset hanno messo alla prova tre modelli famosi. Sulla carta avevano un'area sotto la curva tra zero virgola ottantotto e zero virgola novantaquattro. Su DDI crollano: tra zero virgola cinquantasei e zero virgola sessantasette. Zero virgola cinque vuol dire tirare una moneta. E sulle pelli scure va ancora peggio. Un esempio: uno dei modelli riconosceva sette tumori su dieci sulle pelli chiare, e solo due su dieci sulle pelli scure.

Gli autori hanno provato a correggere il problema con tre tecniche di addestramento pensate apposta per l'equità. Non hanno funzionato. Cosa ha funzionato, invece? I dati. Riaddestrando i modelli con una parte delle immagini di DDI, il divario tra pelli chiare e scure si chiude completamente. Ma solo se tra le immagini aggiunte ci sono pelli scure. Con sole pelli chiare, il divario resta.

E c'è un'ultima scoperta, scomoda. Anche i dermatologi, guardando solo la foto, sbagliano di più sulle pelli scure e sulle malattie rare. Ed è un problema doppio, perché molti dataset vengono etichettati proprio così: un dermatologo guarda la foto e mette l'etichetta. Gli errori del medico diventano errori della macchina.

Cosa ci portiamo a casa per Neo Helper? Tre cose.

Primo: il nostro dataset di partenza, HAM diecimila, non dice il fototipo ed è fatto quasi solo di pelli chiare. Dobbiamo dichiararlo, chiaramente, nei limiti della tesi.

Secondo: useremo DDI come banco di prova esterno, e riporteremo i risultati separati per fototipo. Non un solo numero medio.

Terzo: DDI contiene foto cliniche, mentre HAM diecimila contiene immagini dermoscopiche. Un modello addestrato su un tipo di immagine va male sull'altro. Per questo l'agente di Neo Helper deve prima capire che tipo di immagine ha ricevuto, e saper dire: questa immagine non è adatta al mio modello.
