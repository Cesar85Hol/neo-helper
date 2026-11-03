# Groh et al., 2021 — Il dataset Fitzpatrick 17k e l'accuratezza per colore della pelle

- **Pubblicazione:** CVPR Workshops 2021 (ISIC Skin Image Analysis Workshop) · arXiv [2104.09957](https://arxiv.org/abs/2104.09957) · [DOI 10.48550/arXiv.2104.09957](https://doi.org/10.48550/arXiv.2104.09957) ⚠️ DOI della versione CVPR-W non verificato
- **Gruppo:** MIT Media Lab (Matthew Groh) con Scale AI e dermatologi USA
- **Testo letto:** **completo** (versione arXiv, tramite alphaXiv).
- **Dataset:** [github.com/mattgroh/fitzpatrick17k](https://github.com/mattgroh/fitzpatrick17k)

## In una frase
Il primo grande dataset pubblico di foto cliniche con l'etichetta del **fototipo di Fitzpatrick**. Mostra che le pelli scure sono **poco rappresentate** e che una rete funziona meglio sui fototipi **simili a quelli visti in addestramento**.

## Il fototipo di Fitzpatrick (in breve)
Una scala da **I a VI** nata per descrivere come la pelle reagisce al sole: I = pelle molto chiara che si scotta sempre, VI = pelle molto scura che non si scotta mai. In AI si usa per misurare l'equità tra colori di pelle, anche se **non** rappresenta bene tutta la diversità della pelle umana.

## Cosa hanno fatto
- **16.577 immagini cliniche** da due atlanti online (DermaAmin 12.672, Atlas Dermatologico 3.905), **114 malattie**.
- Le diagnosi vengono dagli atlanti, **senza biopsia**. Controllo di qualità su 504 immagini: diagnostiche il 69,0%, sbagliate il 3,4%.
- Fototipo assegnato da annotatori di Scale AI (da 2 a 5 per immagine, 72.277 annotazioni in totale).
- **Rete:** VGG-16 pre-addestrata su ImageNet.
- **Esperimento chiave:** addestrare la rete **solo su due fototipi** (per esempio I–II) e testarla sugli altri.
- Confronto con un metodo automatico per stimare il colore della pelle dall'immagine (**ITA**, *individual typology angle*).

## Risultati
- **Squilibrio:** 7.755 immagini di fototipi I–II, 6.089 di III–IV, solo **2.168 di V–VI**: 3,6 volte meno delle pelli chiare. **25 malattie su 114** non hanno nessuna immagine di fototipo VI.
- Accuratezza su 114 classi: 20,2% (test casuale); top-3 35,4%. Su 3 classi (benigno, maligno, non tumorale) 62,4%.
- **La rete funziona meglio sui fototipi vicini a quelli di addestramento:**
  - addestrata su I–II → meglio su III–IV che su V–VI;
  - addestrata su V–VI → meglio su III–IV che su I–II.
- L'ITA automatico sbaglia di più di un punto nella scala Fitzpatrick in **circa un terzo** delle immagini: non sostituisce l'annotazione umana.

## Messaggi chiave per la tesi
1. I dataset dermatologici sono **sbilanciati** verso le pelli chiare. Quasi tutti i dataset ISIC **non hanno** proprio l'informazione sul fototipo.
2. Una rete generalizza male verso fototipi **lontani** da quelli che ha visto: il bias viene dai **dati**.
3. Etichette da atlante senza biopsia = **rumore** nelle etichette.

## Limiti
- Immagini da atlanti online: qualità e diagnosi non controllate.
- Fototipo stimato da una foto e non visitando il paziente.
- Rete semplice; accuratezze basse in assoluto.

## Cosa porto in Neo Helper
- **Valutazione per sottogruppi:** riportare le metriche separate per fototipo quando il dato esiste (Fitzpatrick17k, DDI, PAD-UFES-20).
- Dichiarare nei limiti che **HAM10000 non ha il fototipo** ed è fatto quasi solo di pelli chiare.
- Non usare l'ITA automatico come etichetta affidabile.
- Fitzpatrick17k è utile per test su foto **cliniche**, non per le dermoscopiche.
