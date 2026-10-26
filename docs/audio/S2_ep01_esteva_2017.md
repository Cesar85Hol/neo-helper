# Episodio 3 — Esteva 2017: l'intelligenza artificiale arriva al livello del dermatologo

Sezione due, paper fondativi. Primo episodio. Oggi raccontiamo il paper che ha acceso tutto: Esteva e colleghi, Università di Stanford, pubblicato su Nature nel duemiladiciassette.

La domanda era audace: una rete neurale può riconoscere un tumore della pelle bene quanto un dermatologo?

Prima di questo lavoro, i sistemi automatici avevano un grosso problema: pochi dati. Spesso meno di mille immagini. E richiedevano passaggi fatti a mano, come ritagliare la lesione o misurare bordi e colori. Funzionavano in laboratorio, ma non generalizzavano.

Esteva cambia approccio con tre idee.

Prima idea: tanti dati. Il gruppo raccoglie quasi centotrentamila immagini cliniche, cioè normali fotografie, di oltre duemila malattie della pelle. Cento volte di più di qualsiasi dataset precedente.

Seconda idea: riciclare una rete già esperta. Usano Inception, una rete di Google già addestrata a riconoscere oggetti comuni, come gatti, auto e tazze, su più di un milione di foto. Poi la riaddestrano sulle immagini mediche. Si chiama transfer learning: la rete sa già vedere forme e colori, e impara a usarli per la pelle.

Terza idea, la più furba: un albero delle malattie. I dermatologi organizzano le duemila malattie in un albero, con tre rami principali: benigne, maligne e non tumorali. La rete impara su settecentocinquantasette classi molto specifiche. Poi, per sapere la probabilità di melanoma, si sommano le probabilità di tutte le sue varianti. Addestrare sul dettaglio e poi sommare funziona meglio che addestrare direttamente sulle categorie grandi.

E il test? Qui sta la serietà del lavoro. Il confronto finale usa solo lesioni confermate con biopsia, in tre compiti: carcinomi contro cheratosi benigne, melanoma contro neo nelle foto, e melanoma contro neo al dermatoscopio. Ai dermatologi, almeno ventuno per ogni compito, non viene chiesto solo "che cos'è?". Viene chiesto: faresti la biopsia, o rassicureresti il paziente? Cioè la vera decisione clinica.

Risultato. In tutti e tre i compiti l'area sotto la curva supera zero virgola novantuno. E quasi tutti i dermatologi si collocano sotto la curva della rete. La macchina eguaglia gli esperti.

Un dettaglio che ci servirà: le mappe di salienza, cioè dove guarda la rete, mostrano che si concentra sulla lesione e ignora la pelle sana intorno. E sbaglia in modo simile ai medici: confonde nei e melanomi, proprio come loro.

Ora i limiti, perché ci sono. Il confronto è solo sull'immagine: il dermatologo vero usa anche la storia del paziente e confronta i nei tra loro. I dati di addestramento non sono pubblici, quindi nessuno può rifare l'esperimento. E le immagini sfuocate sono state tolte dal test, mentre nella vita reale, con lo smartphone, ci saranno eccome.

Che cosa portiamo in Neo Helper? Tre cose. L'albero delle classi, da cui ricavare benigno o maligno. La domanda clinica giusta nei test: asportare o rassicurare. E la regola d'oro di separare bene le immagini della stessa lesione tra addestramento e test, altrimenti i risultati sono gonfiati.

Il sogno della diagnosi dallo smartphone nasce qui. Nei prossimi episodi vedremo quanto è difficile renderlo reale.
