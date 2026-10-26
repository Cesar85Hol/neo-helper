# Episodio 4 — Haenssle 2018 e Brinker 2019: la macchina contro decine di dermatologi

Secondo episodio della sezione due. Oggi due studi tedeschi, molto simili tra loro, che hanno confermato il risultato di Stanford sulle immagini dermatoscopiche.

Il primo è di Haenssle, Università di Heidelberg, pubblicato su Annals of Oncology nel duemiladiciotto. Titolo provocatorio: uomo contro macchina.

La rete è sempre di Google, Inception, versione quattro, addestrata su immagini dermatoscopiche. Il test usa cento immagini. Gli sfidanti sono cinquantotto dermatologi di diciassette Paesi, di cui trenta esperti.

La parte interessante è che lo studio ha due livelli. Al livello uno, il medico vede solo l'immagine dermatoscopica. Al livello due, riceve anche informazioni cliniche e foto d'insieme, come in una visita vera.

I risultati. Al livello uno i dermatologi trovano l'ottantasei virgola sei per cento dei melanomi, con una specificità del settantuno per cento. Con le informazioni cliniche migliorano: la specificità sale a quasi il settantasei per cento.

E la rete? Alla stessa sensibilità dei medici, ha una specificità dell'ottantadue virgola cinque per cento. Tradotto: trova gli stessi melanomi, ma fa molti meno falsi allarmi. Significa meno nei benigni asportati per niente. L'area sotto la curva è zero virgola ottantasei per la rete, contro zero virgola settantanove per i dermatologi.

Conclusione degli autori: i medici, qualunque sia la loro esperienza, potrebbero beneficiare dell'aiuto di una rete neurale.

Il titolo, però, ha fatto discutere. La rivista ha pubblicato una lettera critica e una risposta degli autori. Perché la domanda vera non è chi vince, ma come lavorano insieme. Ricordatelo: ci torneremo nell'ultimo episodio.

Passiamo al secondo studio: Brinker e colleghi, centro tedesco di ricerca sul cancro, European Journal of Cancer, duemiladiciannove. Titolo: il deep learning supera centotrentasei dermatologi su centocinquantasette.

Due novità. Prima: la rete è addestrata solo con immagini pubbliche, circa dodicimila. Niente database segreti: chiunque potrebbe ripetere l'esperimento. Seconda: i dermatologi sono tantissimi, centocinquantasette, da dodici ospedali universitari, dagli specializzandi ai primari.

I risultati. I dermatologi in media trovano il settantaquattro per cento dei melanomi con il sessanta per cento di specificità. Alla stessa sensibilità, la rete arriva all'ottantasei e mezzo per cento di specificità. E anche contro i primari, i migliori, la rete vince.

Ma il dato che a me colpisce di più è un altro: la variabilità tra medici. La sensibilità dei dermatologi va da un minimo del quaranta a un massimo del cento per cento. La stessa immagine riceve giudizi molto diversi. Una macchina, almeno, è sempre coerente con se stessa.

Attenzione però a non confrontare i numeri tra studi diversi. In Haenssle i dermatologi sembrano molto più bravi che in Brinker. Cambiano le immagini, le istruzioni, i medici. Ogni test ha le sue regole.

Limiti comuni ai due studi: test piccoli, cento immagini. Solo melanoma contro neo, nessuna delle altre lesioni. E studi su immagini, non su pazienti veri.

Cosa portiamo in Neo Helper? Primo: si può fare con dati aperti, ed è proprio il nostro caso. Secondo: la variabilità tra medici giustifica un sistema di seconda opinione. Terzo: l'esperimento a due livelli, solo immagine e poi immagine più dati clinici, è un'idea da copiare per misurare quanto aiutano età, sesso e sede della lesione.

Nel prossimo episodio parliamo dei dati: il dataset HAM diecimila, su cui probabilmente costruiremo il nostro primo modello.
