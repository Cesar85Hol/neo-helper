# Episodio 7 — Tschandl 2020: medico e macchina, insieme

Ultimo episodio della sezione due. Ed è, secondo me, il paper più importante per il nostro progetto. Tschandl e colleghi, Nature Medicine, duemilaventi. Titolo: collaborazione uomo computer nel riconoscimento del cancro della pelle.

Una premessa di onestà: di questo articolo ho letto solo il riassunto ufficiale, perché il testo completo è a pagamento. Quindi oggi ti racconto le conclusioni certe, e ti segnalo quando un numero va ancora verificato.

Fino a qui, tutti gli studi si chiedevano: chi vince, l'uomo o la macchina? Questo studio cambia domanda. Nella realtà, l'intelligenza artificiale sarà usata da un medico. E allora le domande diventano quattro. Quanto migliora il medico con l'aiuto della macchina? Chi ne beneficia di più? Quale forma di aiuto funziona meglio? E cosa succede se la macchina sbaglia?

L'esperimento. Medici con esperienza molto diversa, da meno di un anno a più di dieci, guardano immagini dermatoscopiche delle solite sette classi. Danno la loro diagnosi. Poi vedono il suggerimento dell'intelligenza artificiale, e possono cambiare idea.

E qui la parte più interessante: l'aiuto viene presentato in tre modi diversi.

Primo modo: le probabilità per tutte e sette le diagnosi, come un piccolo grafico a barre.

Secondo modo: un solo numero, la probabilità che la lesione sia maligna.

Terzo modo: immagini simili, cioè casi già diagnosticati che assomigliano a quello in esame.

Vengono anche simulati scenari concreti: il medico che chiede una seconda opinione, e lo smistamento dei pazienti in telemedicina.

I risultati, in quattro messaggi.

Messaggio uno: un'intelligenza artificiale di buona qualità rende il medico più accurato. Più accurato del medico da solo, e più accurato anche della macchina da sola. Insieme si fa meglio.

Messaggio due: chi guadagna di più sono i medici meno esperti. Ha senso: l'esperto ha meno da imparare.

Messaggio tre: la forma conta. Sullo smartphone, il grafico con le probabilità per tutte le diagnosi ha funzionato meglio delle immagini simili.

Messaggio quattro, ed è quello da scolpire nella memoria: un'intelligenza artificiale sbagliata inganna tutti. Anche gli esperti. Se la macchina sbaglia con sicurezza, il medico tende a seguirla. Si chiama automation bias, la tendenza a fidarsi troppo dell'automatismo.

E c'è un bonus. Analizzando dove guarda la rete, con le mappe di attivazione, i ricercatori hanno ricavato indicazioni utili a migliorare la diagnosi umana. Da verificare sul testo completo: sembra che per alcune lesioni causate dal sole la rete guardasse anche la pelle intorno alla lesione, e che insegnare questo trucco a studenti di medicina li abbia resi più bravi. L'intelligenza artificiale che fa da insegnante.

Un altro numero da verificare: con il grafico delle probabilità, l'accuratezza dei medici sarebbe salita di circa tredici punti percentuali.

Perché questo paper è così importante per Neo Helper? Perché ci dice come costruire l'interfaccia.

Primo: mostrare al medico la distribuzione su tutte le diagnosi, non un verdetto unico. I casi simili possono esserci, ma come funzione secondaria.

Secondo: dato che una macchina sbagliata è pericolosa, il sistema deve mostrare la sua incertezza, e saper dire "non sono sicuro" o "questa immagine non è adatta". È esattamente il compito dell'agente critico e della stima dell'incertezza che abbiamo previsto nell'architettura.

Terzo: per valutare Neo Helper non basta misurare quanto è accurato il modello. Bisogna misurare quanto migliora il medico che lo usa.

Quarto: le mappe di calore non sono solo una spiegazione. Possono essere uno strumento per insegnare.

Con questo si chiude la sezione due. Riassumendo la storia: nel duemiladiciassette la macchina raggiunge il dermatologo. Nel duemiladiciotto e diciannove lo supera, ma solo su immagini simili a quelle già viste. Nel duemilaventi capiamo che la vera partita è la collaborazione. Ed è proprio lì che vuole giocare Neo Helper.
