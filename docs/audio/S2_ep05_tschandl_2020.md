# Episodio 7 — Tschandl 2020: medico e macchina, insieme

Ultimo episodio della sezione due. Ed è, secondo me, il paper più importante per il nostro progetto. Tschandl e colleghi, Nature Medicine, duemilaventi. Titolo: collaborazione uomo computer nel riconoscimento del cancro della pelle. Questa volta l'ho letto per intero, quindi tutti i numeri che senti sono verificati.

Fino a qui, tutti gli studi si chiedevano: chi vince, l'uomo o la macchina? Questo studio cambia domanda. Nella realtà, l'intelligenza artificiale sarà usata da un medico. E allora le domande diventano quattro. Quanto migliora il medico con l'aiuto della macchina? Chi ne beneficia di più? Quale forma di aiuto funziona meglio? E cosa succede se la macchina sbaglia?

L'esperimento. La rete è una ResNet trentaquattro, addestrata sul dataset HAM diecimila. Da sola, sul test della sfida ISIC, è già migliore della maggior parte dei medici. Poi arrivano i lettori: trecentodue medici da quarantuno Paesi. Più della metà dermatologi, poi specializzandi e medici di base. Ognuno guarda le immagini, dà la sua diagnosi, poi vede il suggerimento della macchina, e può cambiare idea.

E qui la parte più interessante: l'aiuto viene presentato in quattro modi diversi.

Primo modo: le probabilità per tutte e sette le diagnosi, come un piccolo grafico a barre.

Secondo modo: un solo numero, la probabilità che la lesione sia maligna.

Terzo modo: immagini simili, cioè casi già diagnosticati che assomigliano a quello in esame.

Quarto modo: il parere della folla, cioè come avevano risposto cinquecentoundici medici in uno studio precedente.

I risultati, in cinque messaggi.

Messaggio uno: la forma conta, e conta tantissimo. Con il grafico delle probabilità sulle sette diagnosi, l'accuratezza dei medici sale dal sessantatré virgola sei al settantasette per cento. Più tredici punti. Con il singolo numero di malignità, nessun miglioramento. Con le immagini simili, nessun miglioramento: anzi, richiedono quasi quattro volte più tempo, e dopo un po' i medici smettono di guardarle. La lezione: per un problema a sette classi, serve un aiuto a sette classi.

Messaggio due: chi guadagna di più sono i medici meno esperti. Cambiano idea più spesso, e quasi sempre nella direzione giusta. Gli esperti, invece, guadagnano solo quando non sono sicuri. Quando sono sicuri, l'aiuto non serve a niente. Ne nasce una regola semplice: se sei un esperto e sei sicuro, puoi ignorare la macchina.

Messaggio tre, quello da scolpire nella memoria: un'intelligenza artificiale sbagliata inganna tutti. I ricercatori hanno fatto un esperimento furbo: hanno scambiato apposta le probabilità, così che la macchina suggerisse la diagnosi sbagliata. Risultato: il guadagno di quasi dieci punti si trasforma in una perdita di sei. In tutti i gruppi, esperti compresi. Più ti fidi, più sei vulnerabile. Si chiama automation bias, la tendenza a fidarsi troppo dell'automatismo.

Messaggio quattro: insieme si fa meglio. Un singolo medico indovina in media il sessantacinque per cento. Un piccolo gruppo di medici, votando, il settantaquattro. La macchina da sola il settantasette. Ma un gruppo di medici aiutato dalla macchina arriva all'ottantuno per cento. Il migliore di tutti.

Messaggio cinque: gli scenari reali. Nella telemedicina, con foto fatte dai pazienti stessi, la rete sbaglia di più sulle singole immagini. Ma se si ragiona per paziente, riconosce il novantacinque per cento delle persone che hanno davvero un tumore. Perfetta per fare da filtro. E come seconda opinione, ha aiutato i dermatologi a evitare asportazioni inutili in una lesione benigna su sei, senza perdere nessun tumore.

E c'è un bonus bellissimo. Guardando dove guarda la rete, con le mappe di calore Grad-CAM, i ricercatori hanno notato una cosa: per le cheratosi attiniche, la rete guarda anche la pelle intorno alla lesione, la pelle rovinata dal sole. Gli umani invece guardano solo la macchia. Allora l'hanno insegnato a centottantanove studenti di medicina: guardate anche intorno. E la loro capacità di riconoscere queste lesioni è salita dal trentadue al quarantasette per cento. L'intelligenza artificiale che fa da insegnante.

E un ultimo dettaglio curioso: quando vedono la probabilità di malignità, i medici cambiano idea già intorno al diciassette per cento, non al cinquanta. E quella soglia istintiva è quasi esattamente quella matematicamente ottimale.

Perché questo paper è così importante per Neo Helper? Perché ci dice come costruire l'interfaccia.

Primo: mostrare al medico la distribuzione su tutte le diagnosi, non un verdetto unico. Le immagini simili possono esserci, ma come funzione secondaria.

Secondo: dato che una macchina sbagliata è pericolosa, il sistema deve mostrare la sua incertezza, e saper dire "non sono sicuro" o "questa immagine non è adatta". È esattamente il compito dell'agente critico che abbiamo previsto nell'architettura.

Terzo: per decidere se asportare, usare una soglia di malignità bassa, non il cinquanta per cento.

Quarto: per valutare Neo Helper non basta misurare quanto è accurato il modello. Bisogna misurare quanto migliora il medico che lo usa, distinguendo esperti e principianti.

Quinto: le mappe di calore non sono solo una spiegazione. Possono essere uno strumento per insegnare.

Con questo si chiude la sezione due. Riassumendo la storia: nel duemiladiciassette la macchina raggiunge il dermatologo. Nel duemiladiciotto e diciannove lo supera, ma solo su immagini simili a quelle già viste. Nel duemilaventi capiamo che la vera partita è la collaborazione. Ed è proprio lì che vuole giocare Neo Helper.
