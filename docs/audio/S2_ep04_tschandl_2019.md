# Episodio 6 — Tschandl 2019: 511 medici contro 139 algoritmi

Quarto episodio della sezione due. Oggi la sfida più grande mai organizzata tra medici e algoritmi in dermatologia. Lo studio è di Tschandl e colleghi, pubblicato su Lancet Oncology nel duemiladiciannove.

La domanda è più ambiziosa di quelle viste finora. Non più solo melanoma contro neo, ma tutte e sette le classi di lesioni pigmentate. Perché nei pazienti con la pelle molto danneggiata dal sole, fino alla metà delle lesioni asportate non sono melanocitiche. Un sistema che conosce solo nei e melanomi, nella realtà, serve a poco.

Come hanno fatto. Il dataset HAM diecimila viene dato come materiale di addestramento ai partecipanti della sfida internazionale ISIC duemiladiciotto. Rispondono settantasette laboratori, con centotrentanove algoritmi.

Dall'altra parte, i medici: cinquecentoundici lettori da sessantatré Paesi. Più della metà dermatologi, poi specializzandi e medici di base. Si collegano a una piattaforma web e diagnosticano gruppi di trenta immagini scelte a caso. Gli esperti sono quelli con più di dieci anni di esperienza.

Il test contiene millecinquecentoundici immagini. E qui c'è un'idea furba: trecentosedici di queste vengono da centri che non hanno contribuito all'addestramento. Turchia, Nuova Zelanda, Svezia, Argentina. Immagini nuove per tutti, anche per gli algoritmi.

La metrica è il numero di diagnosi corrette su trenta, in gruppi bilanciati con lo stesso numero di lesioni per classe. Così non conviene rispondere sempre "neo".

I risultati. Tieniti forte.

Su trenta immagini, i lettori umani ne indovinano in media quasi diciotto. I tre migliori algoritmi quasi ventisei. Otto diagnosi corrette in più.

E gli esperti? Diciotto virgola otto contro venticinque virgola quattro. Anche gli esperti sono nettamente battuti.

Il caso più clamoroso riguarda le cheratosi attiniche e la malattia di Bowen. Gli esperti ne riconoscono circa la metà. Gli algoritmi il novanta per cento.

Ma ora arrivano le sfumature, e sono queste a contare davvero.

Prima sfumatura: se si guarda solo benigno contro maligno, il voto di maggioranza di tutti i medici raggiunge lo stesso livello dei migliori algoritmi. La saggezza della folla funziona.

Seconda sfumatura, la più importante: sulle immagini dei centri nuovi, il vantaggio delle macchine crolla. Il distacco scende da circa l'undici per cento a meno del quattro per cento. Gli algoritmi sono molto bravi sulle immagini simili a quelle che hanno visto, e meno bravi sul resto. Si chiama problema della generalizzazione, o fuori distribuzione, e sarà uno dei temi centrali della nostra tesi.

Terza sfumatura: i medici non avevano età, sede della lesione, né la possibilità di confrontare il neo con gli altri del paziente. Lo studio simula la telemedicina, non una visita vera.

Quarta sfumatura, sulla metrica. Questa misura tratta tutti gli errori allo stesso modo. Ma scambiare un melanoma per un basocellulare non è grave, perché si asportano tutti e due. Scambiarlo per un neo, invece, sì. Gli autori stessi suggeriscono una metrica più clinica: asportare o rassicurare.

E la conclusione degli autori è profetica. In futuro i classificatori saranno usati sotto la guida dei medici. Quindi bisogna testarli nelle mani dei medici, non da soli.

Che cosa portiamo in Neo Helper. Primo: misurare sempre sia l'accuratezza bilanciata sulle sette classi, sia la capacità di distinguere benigno da maligno. Secondo: prevedere fin dall'inizio un test su dati esterni. Terzo: usare età e sede della lesione, che qui mancavano. Quarto: l'idea della folla. Più modelli insieme, o più agenti insieme, possono essere più robusti di uno solo.

Nell'ultimo episodio della sezione, la svolta: che cosa succede quando medico e macchina lavorano insieme.
