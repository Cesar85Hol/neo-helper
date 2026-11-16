# 12 — Milestone 2, prima parte: cosa abbiamo fatto

> Riassunto dei pacchetti P1, P2 e P3 della Milestone 2 (11–17 novembre 2026), scritto per essere letto o ascoltato senza aprire il codice.
> I dettagli sono in [`11_eda_ham10000.md`](11_eda_ham10000.md), nel [diario](diario.md) e nei README di `ml/`.

## In una frase
Abbiamo preparato il terreno per addestrare il primo modello: l'ambiente di lavoro, i dati scaricati e controllati, e una fotografia onesta di cosa c'è dentro HAM10000, comprese due trappole che avrebbero falsato i risultati.

## Dove eravamo
La Milestone 1 si era chiusa con le scelte sulla carta:
- addestrare su **HAM10000**;
- usare un modello già addestrato, **congelato**, e insegnare solo una piccola "testa" finale;
- dividere i dati **per lesione**;
- controllare gli **artefatti** prima di addestrare.

La Milestone 2 trasforma queste scelte in codice e dati. È divisa in sei pacchetti; i primi tre sono fatti.

## Pacchetto 1 — L'ambiente
- **Cosa:** una cartella `ml/` con il codice Python, gestita con lo strumento `uv`.
- **Perché `uv`:** scrive in un file le versioni esatte di ogni libreria. Chiunque, su un altro computer, ricostruisce lo stesso ambiente con un comando. Serve alla tesi e serve ai centri con poche risorse (RQ6).
- **Tutto gira sul Mac.** Con il modello congelato non serve una scheda grafica in cloud. Il codice sceglie da solo tra la grafica del Mac, una scheda NVIDIA o il solo processore.
- **I dati stanno fuori dal progetto**, in una cartella a parte, così non finiscono su GitHub né su iCloud.

**Un imprevisto:** la cartella del progetto è sincronizzata con iCloud, e iCloud rompeva l'ambiente Python (nascondeva dei file, rinominava i collegamenti). Soluzione: l'ambiente sta fuori dalla cartella sincronizzata.

## Pacchetto 2 — I dati e il registro
- **Scaricati:**
  - HAM10000 dall'archivio di Harvard: 10.015 immagini;
  - le annotazioni di Chanda (criteri dermoscopici segnati dai dermatologi);
  - DDI e Derm7pt, scaricati a mano perché chiedono una registrazione.
- **Ogni download è verificato:** il programma confronta il file con un'"impronta digitale" (checksum) fissata in anticipo. Se non coincide, il file viene rifiutato.
- **Prima si prova, poi si scarica:** ogni comando mostra file e dimensioni e si ferma; scarica solo con un consenso esplicito.
- **Il registro dati:** una tabella con una riga per immagine e le stesse 23 colonne per qualsiasi dataset: diagnosi, come è stata stabilita, lesione, centro, paese, età, sesso, sede, e soprattutto **licenza e fonte per ogni immagine**. Tutto il resto del progetto legge solo questa tabella.

**Le licenze, verificate alla fonte:**
- HAM10000: CC BY-NC 4.0, solo uso non commerciale;
- Derm7pt: CC BY-NC-ND 4.0;
- DDI: accordo di Stanford, solo ricerca personale, niente ridistribuzione;
- annotazioni di Chanda: CC BY 4.0, la più aperta.

## Pacchetto 3 — Guardare i dati prima di usarli
Si chiama analisi esplorativa, in inglese EDA: tabelle e grafici per capire i dati **prima** di addestrare.

### Cosa abbiamo visto
1. **Le classi sono molto sbilanciate.** Due immagini su tre sono nevi. Un modello che rispondesse sempre "nevo" avrebbe ragione nel 67% dei casi e non troverebbe nessun tumore. Per questo si misura l'accuratezza **bilanciata**, che dà lo stesso peso a ogni classe.
2. **Una lesione su quattro è fotografata più volte.** Queste immagini sono quasi metà del dataset. Se finissero un po' nel training e un po' nel test, il modello verrebbe interrogato su lesioni già viste.
3. **I tumori hanno diagnosi solide, i nevi meno.** Melanomi e carcinomi sono tutti confermati dall'istologia; i nevi solo per il 37%.
4. **Classe e centro sono legati.** Il 90% delle cheratosi attiniche viene dall'Australia; una raccolta di Vienna contiene quasi solo nevi.
5. **Non ci sono fototipo né paziente.** L'equità per tono della pelle non si può misurare su HAM10000: servono i dataset esterni.

### La divisione
70% delle lesioni per addestrare, 15% per scegliere, 15% per l'esame finale: 7.005, 1.509 e 1.501 immagini. È salvata nel progetto e il programma rifiuta di rifarla. **L'esame finale si usa una volta sola.**

### I duplicati
Abbiamo cercato immagini quasi identiche. Ne esistono 17 coppie, tutte dentro la stessa lesione: nessuna fuga tra training e test.

Un primo metodo, più grossolano, segnalava migliaia di falsi duplicati, perché le dermoscopie si somigliano tutte. Lo abbiamo scartato.

## Le due trappole trovate

### 1. MONET non vede gli artefatti come pensavamo
MONET è un modello che collega immagini e parole: gli si chiede "c'è una penna viola?" e dà un punteggio. Volevamo usarlo per trovare penna, righello, adesivo, bordo nero e peli.

Guardando le immagini con i punteggi più alti:
- **peli:** funziona;
- **penna viola:** trova soprattutto le lesioni vascolari, che sono viola;
- **bordo nero:** trova i nevi scuri;
- **righello, adesivo, bolle:** quasi mai giusti.

MONET confonde il **colore della lesione** con l'artefatto. Se lo avessimo usato alla cieca, avremmo "scoperto" un legame tra artefatti e classi che in realtà era un errore dello strumento. È anche la prima risposta, parziale, a una domanda rimasta aperta dalla Milestone 1.

⚠️ È un giudizio a occhio su 24 immagini per concetto: va confermato da un dermatologo.

### 2. Il bordo nero è una possibile scorciatoia
Il bordo nero è il cerchio scuro lasciato da alcuni dermatoscopi. Lo abbiamo misurato direttamente sui pixel, contando quelli scuri negli angoli.

- È nel **9,5%** delle immagini.
- Viene per il **91%** da una sola raccolta, quella con più melanomi.
- È nel **16,7% delle immagini maligne** contro il **7,8% delle benigne**.
- La differenza resta anche dentro quella raccolta: 31,7% contro 23,6%.

Un modello potrebbe imparare "bordo nero, quindi tumore", come nello studio di Winkler con i segni di penna. Nelle prossime prove i risultati saranno riportati **separati con e senza bordo nero**, e per centro.

## I controlli automatici
Il codice ha **51 test** che girano in pochi secondi. Controllano, per esempio, che:
- un file corrotto venga rifiutato;
- nessuna lesione finisca in due parti della divisione;
- una lesione scura al centro non venga scambiata per un bordo nero.

Uno dei test era scritto male e falliva; è stato corretto l'esempio, non il codice.

## Numeri
| Voce | Valore |
|------|--------|
| Immagini di HAM10000 | 10.015, di 7.470 lesioni |
| Spazio su disco | 7,6 GB |
| Tempo per i vettori di MONET | 11,5 minuti sul Mac |
| Test automatici | 51 |
| Issue chiuse | #11 (ambiente) |
| README | in inglese, italiano e spagnolo |

## Cosa resta da decidere
- **Le cheratosi attiniche contano tra le maligne?** Per ora sì, come in Tschandl 2020. Cambia il punteggio di malignità.
- **Penna, righello, adesivo, bolle** non sono misurati: servirebbe un piccolo campione annotato a mano.

## Cosa viene dopo
- **Pacchetto 4:** le prime baseline. Quattro modelli congelati (PanDerm, DINOv2, Derm Foundation, ImageNet) sugli stessi dati, per rispondere alla RQ1: quanto vale PanDerm, e quanto si perde con un modello a licenza libera?
- **Pacchetto 5:** gli altri dataset, per i test fuori dal laboratorio e per la RQ6.
- **Pacchetto 6:** chiusura con la dashboard della Milestone 2.
