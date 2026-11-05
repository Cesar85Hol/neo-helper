# Hernández-Pérez et al., 2024 — BCN20000: lesioni dermoscopiche "allo stato brado"

- **Rivista:** *Scientific Data* 11:641 (2024) · [DOI 10.1038/s41597-024-03387-w](https://doi.org/10.1038/s41597-024-03387-w) · PMID 38886204 · PMC11183228
- **Gruppo:** Hospital Clínic de Barcelona (Malvehy, Podlipnik), Universitat Politècnica de Catalunya (Vilaplana), con Combalia e Codella
- **Testo letto:** **completo** (PMC): metodi, dati e validazione; non ho letto nel dettaglio i risultati delle baseline.
- Il dataset esisteva già come preprint del 2019 (Combalia et al., arXiv 1908.02288) ed è entrato in ISIC 2019. Questa è la descrizione ufficiale.

## In una frase
**18.946 immagini dermoscopiche** di Barcellona, scelte apposta **difficili**: unghie, mucose, lesioni troppo grandi per il dermatoscopio, lesioni poco pigmentate. Più una classe "fuori distribuzione" nel test. E una **licenza CC BY 4.0**.

## Cosa contiene
- **18.946 immagini** di **5.583 lesioni**, raccolte tra il 2010 e il 2016 all'Hospital Clínic. Formato JPEG 1024×1024.
- **8 categorie:** nevo, melanoma, basocellulare, cheratosi seborroica, cheratosi attinica, squamocellulare, dermatofibroma, lesione vascolare.
- **Test con una nona classe**, **OOD**: lesioni che non rientrano nelle altre.
- **Divisione:** 12.413 immagini di training, con diagnosi, e 6.533 di test, senza diagnosi pubblica.
- **Metadati:** sede anatomica, età, data di acquisizione, sesso.
- **Come sono state confermate le diagnosi:**
  - tutti i **melanomi** e gli altri tumori maligni con **istologia**;
  - le lesioni benigne con istologia, microscopia confocale, consenso di due dermatologi esperti o follow-up.
- **Licenza: CC BY 4.0** (Figshare). L'uso commerciale è permesso, purché si citi la fonte. Fa eccezione rispetto a HAM10000 e agli altri dataset ISIC, che sono **non commerciali**.
- **Curiosità tecnica:** per estrarre l'identificativo del paziente dalle etichette fotografate gli autori hanno usato reti neurali (EfficientNet, YOLOv3) con controllo umano.

## Messaggi chiave per la tesi
1. È il dataset che ha fatto crollare gli algoritmi nella challenge ISIC 2019 (Combalia 2022): un buon **test di realtà**.
2. Le lesioni in **sedi difficili** (unghie, mucose) mancano quasi del tutto in HAM10000.
3. Molte immagini hanno il **bordo nero circolare** del dermatoscopio, un artefatto che può diventare una scorciatoia (§3.3 del documento delle scelte).

## Cosa porto in Neo Helper
- **Test esterno principale dermoscopico**, coerente con la scelta di aggiungere ISIC 2019 **dopo** la baseline.
- **Licenza:** con HAM10000 non commerciale, BCN20000 (CC BY) è un pezzo di un eventuale dataset "libero" per un uso futuro fuori dalla ricerca. Va affiancato a un backbone libero come DINOv2. ⚠️ Verificare la licenza effettiva su Figshare e sull'archivio ISIC prima di usarlo così.
- Controllare con MONET la presenza del **bordo nero** per classe prima di usarlo nel training.
