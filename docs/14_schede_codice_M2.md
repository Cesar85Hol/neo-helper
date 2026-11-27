# 14 — Schede del codice della Milestone 2

> Una scheda per ogni file di codice scritto finora (pacchetti P1–P3), in italiano e in parole semplici, pensata per essere **ascoltata** con NotebookLM.
> Aggiornata al 28 novembre 2026. Il codice vero è in inglese, in `ml/neo/`; la mappa visiva di come i file si collegano è nella vista "Codice" della [dashboard della M2](dashboard/neo_helper_M2.html).

## Come leggere queste schede
Ogni scheda risponde alle stesse domande:
- **A cosa serve** il file;
- **cosa entra e cosa esce**;
- **le funzioni principali**, spiegate a parole;
- **con chi parla**, cioè quali altri file usa e da quali è usato;
- **quali test lo proteggono**;
- **come provarlo** da soli.

Qualche parola che torna spesso:
- **Modulo:** un file di codice Python. Per esempio `split.py` è il modulo della divisione.
- **Funzione:** un pezzo di codice con un nome, che riceve qualcosa e restituisce qualcosa. Per esempio `split_by_lesion` riceve il registro e restituisce la divisione.
- **Test:** un piccolo programma che controlla in automatico che una funzione faccia quello che deve. Se qualcuno rompe la funzione, il test fallisce e lo dice.
- **Commit:** una fotografia salvata del progetto, con una frase che dice cosa è cambiato.
- **Ramo e pull request:** un ramo è una copia del progetto su cui si lavora senza toccare la versione principale; la pull request è la richiesta di unire il ramo alla versione principale, che Cesar legge e approva.

## Il quadro d'insieme
Il codice è organizzato a strati, come una casa.

- **Le fondamenta** non dipendono da nessun altro file: dicono dove stanno i dati (`paths`), su quale processore si calcola (`device`), quali file scaricare (`sources`), come si divide il dataset (`split`), come si misura il bordo nero (`artifacts`), come si disegnano i grafici (`plots`).
- **Il piano di mezzo** usa le fondamenta: scaricare e verificare (`download`), il registro dati (`registry`), i duplicati (`duplicates`), i punteggi di MONET (`concepts`), il controllo dell'ambiente (`check`).
- **Il piano alto** mette insieme i pezzi per un dataset preciso: `ham10000`.
- **Il tetto** è il comando `neo-data` (`cli`): è la porta d'ingresso. Quando si scrive `neo-data split ham10000`, è lui che chiama il modulo della divisione.

Il percorso dei dati è sempre lo stesso: **scaricare → costruire il registro → cercare i duplicati → dividere per lesione → controllare gli artefatti → guardare i dati nel notebook**.

---

## Fondamenta

### `neo/paths.py` — dove stanno i dati
- **A cosa serve:** dice a tutto il resto del codice dove si trovano dati, pesi dei modelli e vettori. Tutto sta in una cartella **fuori dal progetto**, così non finisce né su GitHub né su iCloud.
- **Entra / esce:** legge la variabile d'ambiente `NEO_DATA_DIR`; se non c'è, usa `~/neo-helper-data`. Restituisce i percorsi delle cinque sottocartelle: `raw` (dataset scaricati), `registry` (registro e risultati), `weights` (pesi), `embeddings` (vettori), `mlruns` (esperimenti).
- **Funzioni:** `data_dir` restituisce la cartella principale; `subdir` restituisce una sottocartella e, se richiesto, la crea. Se si chiede una sottocartella che non esiste nell'elenco, dà errore: così un errore di battitura non crea cartelle a caso.
- **Con chi parla:** quasi tutti i moduli lo usano.
- **Test:** quattro test in `test_environment.py` (cartella predefinita, cartella dalla variabile, creazione solo su richiesta, nome sconosciuto rifiutato).

### `neo/device.py` — dove si fanno i calcoli
- **A cosa serve:** sceglie il "motore" per i calcoli: la grafica del Mac (si chiama MPS), una scheda NVIDIA (CUDA) o il processore normale (CPU). Lo stesso codice deve girare sul Mac, su un computer in cloud e su un portatile senza grafica, come in un centro con poche risorse (RQ6).
- **Funzioni:** `available_devices` elenca i motori presenti, dal migliore; `select_device` restituisce quello richiesto, oppure il migliore se si chiede "auto".
- **Una scelta importante:** se si chiede un motore che non c'è, il codice **dà errore invece di ripiegare in silenzio** sulla CPU. Così non si scopre dopo ore che un calcolo è andato lento per sbaglio.
- **Test:** cinque test in `test_environment.py`, più quello che controlla che CPU e grafica diano gli stessi vettori.

### `neo/data/sources.py` — il catalogo
- **A cosa serve:** è l'elenco di tutto ciò che si può scaricare. Per ogni dataset o modello: titolo, licenza, DOI, versione e, per ogni file, indirizzo, dimensione e **impronta digitale** (il checksum).
- **Perché le impronte sono scritte qui:** sono state lette dagli archivi una volta e fissate. Un file scaricato è accettato solo se la sua impronta coincide: così tutti lavorano esattamente sugli stessi file.
- **Contenuto oggi:** HAM10000 (dal Dataverse di Harvard), annotazioni di Chanda (da Figshare), pesi di MONET (da Hugging Face, versione fissata). I file sono divisi in gruppi: "core" è quello essenziale, gli altri (maschere, test ISIC 2018, studio con i lettori) si scaricano su richiesta.
- **Test:** `test_data.py` controlla che ogni voce sia completa e che senza opzioni si scarichi solo il gruppo essenziale.

### `neo/data/split.py` — la divisione per lesione
- **A cosa serve:** divide le lesioni in tre parti: 70% per addestrare, 15% per scegliere (validazione), 15% per l'esame finale (test). Tutte le immagini della stessa lesione stanno dalla stessa parte.
- **Funzioni:**
  - `split_by_lesion` fa la divisione, **stratificata** per diagnosi (ogni parte ha le stesse proporzioni di classi), con seme 2026, cioè sempre uguale;
  - `check` verifica le regole: ogni immagine una volta sola, nessuna lesione in due parti, tutte le classi in ogni parte;
  - `save` salva la divisione nel progetto e **rifiuta di sovrascriverne una già pubblicata**;
  - `load` la rilegge; `summary` fa la tabella dei conteggi.
- **Esce:** `ml/splits/ham10000_lesion_v1.csv`, l'unico file di dati salvato su GitHub.
- **Test:** nove test in `test_split_and_duplicates.py`, compreso uno che sposta a mano una lesione e verifica che il controllo se ne accorga.

### `neo/data/artifacts.py` — il bordo nero, misurato sui pixel
- **A cosa serve:** trova le immagini con il cerchio nero del dermatoscopio. Lo fa contando i pixel scuri nei quattro angoli dell'immagine: un pixel è "scuro" sotto 50 su 255, e l'immagine ha il bordo se gli angoli sono scuri per più del 5%.
- **Perché sui pixel e non con MONET:** MONET confondeva il bordo nero con le lesioni scure. Contare i pixel negli angoli invece non si confonde, perché la lesione sta al centro.
- **Funzioni:** `dark_corner_share` misura un'immagine; `dark_corner_shares` ne misura molte in parallelo.
- **Test:** cinque test in `test_artifacts.py`, su immagini disegnate apposta, tra cui una lesione nera al centro che non deve contare come bordo.

### `neo/plots.py` — i grafici
- **A cosa serve:** disegna i grafici dell'EDA tutti con lo stesso stile, con colori scelti e verificati perché si distinguano anche per chi è daltonico.
- **Funzioni:** `bar_counts` (barre di conteggi), `bar_shares` (barre di percentuali), `stacked_share` (barre impilate al 100%), `save` (salva in SVG e PNG).
- **Un dettaglio recente:** i file SVG ora si salvano senza data e con identificativi fissi. Prima, rieseguendo il notebook, i file risultavano "modificati" anche se il disegno era identico.
- **Test:** quattro test in `test_split_and_duplicates.py`, compreso quello che salva lo stesso grafico due volte e controlla che i file siano identici.

## Piano di mezzo

### `neo/data/download.py` — scaricare e verificare
- **A cosa serve:** scarica i file del catalogo e controlla che siano integri.
- **Come funziona, passo per passo:**
  1. se il file c'è già con la dimensione e l'impronta giuste, non lo riscarica;
  2. altrimenti lo scarica in un file temporaneo che finisce con `.part`;
  3. mentre scarica calcola l'impronta;
  4. solo se dimensione e impronta coincidono, rinomina il file con il nome vero; se no, lo cancella e dà errore.
  
  Così un download interrotto non sembra mai completo.
- **Tre tipi di impronta:** MD5 (Dataverse e Figshare), SHA-256 (pesi su Hugging Face) e impronta git (file piccoli su Hugging Face).
- **Estrazione sicura degli zip:** prima di estrarre controlla ogni percorso dentro lo zip; se uno provasse a scrivere fuori dalla cartella di destinazione, l'estrazione si ferma. È una protezione standard per file presi da internet.
- **Funzioni:** `download_file`, `is_complete`, `checksum_matches`, `extract_zip`, `free_space` (spazio libero sul disco), `human_size` (scrive "1,37 GB" invece di un numero lunghissimo).
- **Test:** sei test in `test_data.py`, tra cui un file corrotto che deve essere rifiutato e uno zip "malevolo" che deve essere bloccato.

### `neo/data/registry.py` — il registro dati
- **A cosa serve:** definisce il **registro**, la tabella comune a tutti i dataset: una riga per immagine e sempre le stesse 23 colonne. Tutto ciò che viene dopo legge solo il registro, quindi aggiungere un dataset vuol dire solo scrivere un convertitore.
- **Le colonne più importanti:** identificativo, file dell'immagine, modalità (dermoscopica, clinica, smartphone), diagnosi, se è maligna, da cosa viene la diagnosi (istologia, follow-up...), lesione, paziente, centro, paese, età, sesso, sede, fototipo e come è stato stabilito, etnia dichiarata, artefatti, e soprattutto **licenza e fonte per ogni immagine**.
- **Il vocabolario comune:** le 7 classi di HAM10000. Sono maligne `mel`, `bcc` e `akiec` (decisione del 17 novembre).
- **Funzioni:** `validate` controlla tutto e **elenca ogni problema trovato**, non solo il primo: colonne sbagliate, campi obbligatori vuoti, doppioni, diagnosi sconosciute, colonna "maligna" incoerente con la diagnosi, immagini mancanti su disco. `save` salva solo un registro valido; `load` rilegge uno o tutti i registri.
- **Test:** tre test in `test_data.py`.

### `neo/data/duplicates.py` — i duplicati
- **A cosa serve:** cerca immagini uguali o quasi. Se due immagini quasi identiche appartenessero a lesioni diverse, una potrebbe finire nell'addestramento e l'altra nel test: il modello verrebbe interrogato su qualcosa che ha già visto.
- **Come funziona:** ogni immagine diventa una miniatura a colori di 32 per 32 pixel; due immagini sono una coppia se le miniature differiscono, in media, di meno di 3 livelli su 255. In più confronta l'impronta dei file per trovare i doppioni esatti.
- **Una lezione:** il primo metodo, un'impronta più grossolana in bianco e nero, segnalava migliaia di coppie sbagliate, perché le dermoscopie si somigliano tutte. Lo abbiamo scartato.
- **Funzioni:** `find_pairs` trova le coppie; `summarise` le conta per tipo.
- **Test:** un test in `test_split_and_duplicates.py` con quattro immagini finte: una originale, una copia esatta, una risalvata con una minima differenza, una diversa.

### `neo/concepts.py` — i punteggi di MONET
- **A cosa serve:** usa MONET, un modello che mette immagini e frasi nello stesso spazio, per dare a ogni immagine un punteggio per un concetto descritto a parole, per esempio "peli" o "righello".
- **Come funziona il punteggio** (è la formula degli autori di MONET):
  1. confronta l'immagine con frasi che nominano il concetto, come "questa è un'immagine della pelle con un righello";
  2. la confronta anche con le stesse frasi senza il concetto, "questa è un'immagine della pelle";
  3. trasforma le due somiglianze in un numero tra 0 e 1 e fa la media su tre modi di formulare la frase.
- **Un risparmio di tempo:** i vettori delle immagini si calcolano una volta sola (11,5 minuti per HAM10000 sul Mac) e si salvano; le volte dopo si rileggono, ma solo se le immagini sono esattamente le stesse.
- **Il limite trovato:** sulle dermoscopie MONET funziona per i peli, non per penna, righello, adesivo, bordo nero e bolle, perché confonde il colore della lesione con l'artefatto.
- **Test:** sei test in `test_concepts.py`, su vettori costruiti a mano, senza caricare il modello vero.

### `neo/check.py` — il controllo dell'ambiente
- **A cosa serve:** è il comando `neo-check`. Stampa le versioni dei programmi, i motori disponibili e la cartella dei dati, poi fa una prova: costruisce un piccolo modello e trasforma 10 immagini finte in vettori.
- **Perché serve:** in un minuto dice se l'ambiente funziona, su un computer nuovo o dopo un aggiornamento.
- **Test:** due test in `test_environment.py`.

## Piano alto e tetto

### `neo/data/ham10000.py` — il convertitore di HAM10000
- **A cosa serve:** prende HAM10000 come lo pubblicano gli autori e lo traduce nel formato del registro.
- **Cosa fa:** estrae le 10.015 immagini dai due zip, poi riempie le 23 colonne: per esempio "histo" diventa "istologia", e la raccolta "rosendahl" diventa paese Australia, le altre Austria. Le colonne che HAM10000 non ha (paziente, fototipo, etnia) restano vuote.
- **Funzioni:** `convert` fa la traduzione; `build_registry` fa tutto il percorso, dall'estrazione al salvataggio, passando per il controllo.
- **Test:** due test in `test_data.py`, tra cui uno che costruisce un piccolo HAM10000 finto e lo porta fino al file del registro.

### `neo/data/cli.py` — il comando `neo-data`
- **A cosa serve:** è la porta d'ingresso. Ogni sottocomando chiama i moduli giusti:
  - `list`: cosa c'è nel catalogo e cosa è già su disco;
  - `download`: prova di download, o download vero con `--yes`;
  - `registry`: estrae le immagini e costruisce il registro;
  - `duplicates`: cerca i duplicati;
  - `split`: crea la divisione, o la ricontrolla se esiste già;
  - `artifacts`: bordo nero e punteggi di MONET.
- **Una regola di sicurezza:** senza `--yes`, il download fa solo la prova: elenca file, dimensioni vere e spazio libero, e si ferma.
- **Test:** `test_data.py` controlla che la prova di download non scarichi nulla e che i pesi dei modelli vadano nella cartella giusta.

## Il notebook

### `ml/notebooks/01_eda_ham10000.ipynb` — guardare i dati
- **A cosa serve:** è l'analisi esplorativa: tabelle e grafici su classi, lesioni ripetute, fonte delle diagnosi, centri, pazienti, duplicati, artefatti e divisione.
- **Cosa produce:** i sette grafici in `docs/figures/` e i numeri del documento `11_eda_ham10000.md`.
- **Perché è salvato vuoto:** le immagini di esempio sono sotto licenza CC BY-NC e non vanno copiate nel progetto pubblico. Si apre in VS Code e si esegue dall'alto in basso.

---

## Come seguiamo il codice da qui in poi
Deciso da Cesar il 28 novembre 2026: tre strumenti insieme.

1. **La dashboard** (controllo visivo). A fine di ogni pacchetto viene rigenerata dal codice: mappa dei moduli, esiti dei test, dati su disco, commit. Se compare un modulo nuovo senza spiegazione, la dashboard lo segnala.
2. **Una pull request per pacchetto** (controllo riga per riga). Il lavoro si fa su un ramo separato; la pull request su GitHub contiene un giro guidato (quali file guardare e perché) e commenti sulle righe importanti. La versione principale cambia **solo quando Cesar approva e unisce**.
3. **Queste schede** (ascolto). Si aggiornano a ogni pacchetto e diventano un file Word da caricare su NotebookLM.

### Come si guarda una pull request su GitHub
1. Aprire il link della pull request.
2. Nella scheda **Conversation** c'è la descrizione con il giro guidato.
3. Nella scheda **Files changed** ci sono le modifiche: in verde le righe aggiunte, in rosso quelle tolte. I commenti sulle righe importanti compaiono lì accanto.
4. Se qualcosa non è chiaro, si può scrivere un commento su una riga: lo leggo e rispondo.
5. Se va bene: pulsante **Merge pull request**. Da quel momento le modifiche sono nella versione principale.

## Numeri a oggi
| Voce | Valore |
|------|--------|
| File di codice | 13 |
| Righe di codice | circa 1.300 |
| Test | 52, tutti superati |
| Comandi | `neo-check`, `neo-data` con 6 sottocomandi |
