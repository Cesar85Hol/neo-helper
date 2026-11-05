# Ha, Liu e Liu, 2020 — La soluzione vincente di ISIC 2020 (SIIM-ISIC su Kaggle)

- **Fonte:** report tecnico · [arXiv 2010.05351](https://arxiv.org/abs/2010.05351) · codice: github.com/haqishen/SIIM-ISIC-Melanoma-Classification-1st-Place-Solution
- **Autori:** Qishen Ha (LINE), Bo Liu (NVIDIA), Fuxu Liu (ReadSense)
- **Testo letto:** **completo** (arXiv).

## In una frase
Ha vinto tra **più di 3.300 squadre** con un **ensemble di 18 reti** (quasi tutte EfficientNet). Il vero segreto però non è il modello: è una **validazione stabile** e la scelta di prevedere la **diagnosi** invece del solo "melanoma sì/no".

## Le quattro chiavi, secondo gli autori
1. **Validazione stabile.**
   - Nel 2020 i positivi erano solo l'1,76%, quindi l'AUC su un fold era molto rumorosa.
   - Hanno unito i dati 2018–2019 (17,85% di positivi) a quelli 2020 e fatto la cross-validation su tutto.
   - **Non hanno mai usato la classifica pubblica di Kaggle:** era così rumorosa che la sua correlazione con la loro validazione era praticamente zero.
2. **Il bersaglio giusto:** invece del binario, una classificazione in **9 classi** di diagnosi (quelle del 2019 più "sconosciuto"). Il punteggio finale è la probabilità della classe melanoma. Più informazione per la rete.
3. **Una pipeline curata:**
   - immagini grandi (da 384 a 896 pixel);
   - molte trasformazioni di data augmentation;
   - 15 epoche con learning rate a coseno.
4. **Ensemble molto diverso:**
   - 18 modelli: EfficientNet da B3 a B7, SE-ResNeXt-101, ResNeSt-101;
   - input di dimensioni diverse;
   - 4 modelli usano anche **14 metadati** (sesso, età, sede, dimensione del file, numero di immagini del paziente);
   - media dei **ranghi** delle probabilità.

## Risultati
- AUC **0,9600** in cross-validation sui dati 2020 e **0,9490** sulla classifica privata finale.
- I modelli con soli metadati vanno peggio di quelli con sole immagini, ma aggiungono **diversità** all'ensemble.

## Messaggi chiave per la tesi
1. Nelle gare, la differenza la fa spesso la **valutazione affidabile**, non l'architettura.
2. **Ottimizzare sulla classifica pubblica** porta all'overfitting. È la stessa lezione di ISIC 2024 (Kurtansky 2025).
3. Usare la diagnosi fine come bersaglio aiuta: è coerente con la nostra scelta di **7 classi + punteggio di malignità** (P2).

## Cosa porto in Neo Helper
- Una regola: **il test si guarda una volta sola**. Le scelte si fanno sulla validazione, possibilmente con cross-validation divisa per lesione.
- Gli ensemble di 18 reti non fanno per noi: il costo e la spiegabilità contano più dell'ultimo decimale di AUC. Ma l'idea di **unire più dati per stabilizzare la validazione** è utile.
- Il codice pubblico è una buona baseline "da gara" per il confronto (opzionale).
