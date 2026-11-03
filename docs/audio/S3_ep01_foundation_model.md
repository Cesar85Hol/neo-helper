# Episodio 8 — Foundation model: MONET, PanDerm e la prova della realtà

Benvenuti nella sezione tre. Fino a qui abbiamo visto reti addestrate per un solo compito: per esempio, riconoscere sette tipi di lesioni dermoscopiche. Dal duemilaventuno in poi cambia tutto. Arrivano i foundation model.

Che cos'è un foundation model? È una rete molto grande, addestrata su milioni di immagini, spesso senza nessuna etichetta. Non impara una diagnosi: impara a vedere. Poi, con pochi esempi etichettati, la si adatta al compito che ci interessa. È come uno studente che ha guardato milioni di casi in un atlante, e a cui basta poco per specializzarsi.

Partiamo da MONET, pubblicato su Nature Medicine nel duemilaventiquattro, dal gruppo di Su-In Lee a Seattle. Di questo lavoro ho letto solo il riassunto, più la pagina del codice. L'idea è bellissima. MONET legge la letteratura medica: centocinquemila immagini dermatologiche, ognuna con la sua descrizione scritta. E impara a collegare le immagini alle parole del medico: eritema, crosta, ulcera, pigmentazione. Così, per ogni immagine, può dire quanto è presente ciascun concetto.

A cosa serve? A tre cose. Primo, a controllare i dataset: per esempio, trovare tutte le immagini con segni di penna o righelli. Secondo, a capire dove sbaglia un modello. Terzo, a costruire modelli che ragionano per concetti, e che quindi si spiegano da soli. Per Neo Helper è un candidato perfetto per un tool che dice al medico, con le sue parole, cosa vede la macchina.

Passiamo a PanDerm, Nature Medicine, duemilaventicinque, gruppo della Monash University in Australia. Questo l'ho letto per intero. PanDerm è il foundation model della dermatologia. È stato addestrato su più di due milioni di immagini, di quattro tipi diversi: foto cliniche, immagini dermoscopiche, foto di tutto il corpo, e perfino vetrini di istologia. Senza etichette. La rete vede metà dell'immagine coperta, e deve indovinare cosa c'è sotto.

I risultati sono impressionanti. Su ventotto compiti diversi è il migliore. Spesso gli basta il dieci per cento delle etichette per eguagliare gli altri modelli. Nelle foto di tutto il corpo trova il tumore in settantanove pazienti su ottanta, proponendo di controllare il sessanta per cento di lesioni in meno rispetto agli esperti. E nelle immagini dermoscopiche prese nel tempo riconosce tre melanomi su quattro già al primo controllo, quando i medici ne riconoscono uno su tre.

Ma la parte che ci interessa di più sono gli studi con i medici. Quarantuno medici diagnosticano sette tipi di lesioni, prima da soli e poi con le probabilità di PanDerm. L'accuratezza sale dal sessantanove all'ottanta per cento. E indovinate chi ne guadagna di più? I meno esperti: più diciassette punti. Esattamente come aveva visto Tschandl nel duemilaventi. C'è però un dettaglio curioso: PanDerm da solo va bene quanto, o meglio, del medico aiutato da PanDerm. I medici usano i consigli in modo selettivo. A volte troppo.

Ultima cosa importante: i pesi di PanDerm sono pubblici, ma con una licenza solo per la ricerca non commerciale. Per la tesi va benissimo. Per un prodotto, no.

E ora la prova della realtà. Nel duemilaventisei, su JAMA Dermatology, Anriot e colleghi, tra cui gli stessi autori di PanDerm e Tschandl, mettono PanDerm davanti a casi di tutti i giorni, compresi quelli rari e strani. Seicentocinquantadue medici. Anche qui ho letto solo il riassunto. Il risultato: PanDerm batte i medici con meno di tre anni di esperienza, pareggia con quelli di media esperienza, ma perde contro gli esperti con più di dieci anni. E una vecchia rete convoluzionale perde contro tutti, anche contro gli specializzandi del primo anno.

La lezione è la stessa della sezione due: i numeri dei benchmark si riducono nel mondo reale. L'intelligenza artificiale di oggi vale un dermatologo di media esperienza. Uno strumento prezioso per chi è all'inizio, o per fare triage. Non un sostituto dello specialista.

Per Neo Helper, quindi: PanDerm come motore principale per vedere, MONET per spiegare con le parole della clinica, e una valutazione sempre in condizioni realistiche, con medici di esperienza diversa.
