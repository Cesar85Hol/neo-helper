# Selvaraju et al., 2017 — Grad-CAM: le mappe di calore che spiegano una rete

- **Conferenza:** ICCV 2017 · [DOI 10.1109/ICCV.2017.74](https://doi.org/10.1109/ICCV.2017.74) · [arXiv 1610.02391](https://arxiv.org/abs/1610.02391)
- **Gruppo:** Georgia Tech e Facebook AI Research (Devi Parikh, Dhruv Batra)
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF. I numeri sono da ricontrollare sul paper ⚠️.

## In una frase
Grad-CAM colora le zone dell'immagine che hanno spinto la rete verso una certa classe. Funziona su quasi ogni rete convoluzionale, senza modificarla né riaddestrarla.

## Come funziona
1. Si sceglie la classe da spiegare, per esempio "melanoma", e si prende il suo punteggio prima della softmax.
2. Si calcola quanto ogni mappa di attivazione dell'**ultimo strato convoluzionale** influisce su quel punteggio (gradienti).
3. Si fa la media di questi gradienti: ogni mappa riceve un peso di "importanza".
4. Si sommano le mappe pesate e si tengono solo i valori positivi (ReLU).
5. Il risultato è una mappa grossolana, per esempio 14×14, ingrandita sull'immagine.

Varianti:
- **Guided Grad-CAM**, più nitida, combina la mappa con la guided backpropagation.
- La **mappa controfattuale** mostra le zone che, tolte, aumenterebbero la fiducia nella classe.

## Risultati principali
- Localizza gli oggetti meglio dei metodi precedenti, usando solo le etichette dell'immagine.
- In uno studio con persone, aiuta a distinguere una rete "più forte" da una "più debole" anche quando danno la stessa risposta.
- **Scopre un bias nei dati:** un classificatore "medico o infermiere" guardava il viso e i capelli, cioè il genere, invece del camice. Corretto il dataset, il modello generalizza meglio.

## Limiti (anche da altri lavori)
- La mappa dice **dove** guarda la rete, non **perché**. È il "divario di interpretazione" di cui parla Chanda 2024: è il medico a dover indovinare quale caratteristica conta.
- È **grossolana**: in una lesione di pochi millimetri non distingue un reticolo da una stria.
- Grad-CAM supera i "test di sanità" di Adebayo 2018, mentre **Guided Grad-CAM no**: la versione nitida assomiglia a un rilevatore di bordi.
- Nella meta-analisi di Krakowski 2024 nessuno studio clinico ha misurato l'effetto delle heatmap sui medici.

## Cosa porto in Neo Helper
- **Grad-CAM, non Guided Grad-CAM**, come spiegazione visiva di base nel tool `explain_heatmap`.
- Uso principale: **controllo qualità** degli sviluppatori. Verifica che la rete guardi la lesione e non la penna, il righello o il bordo nero (Winkler 2019).
- Nel report per il medico va affiancata da **concetti** (MONET) e **casi simili** (CBIR), non usata da sola.
- Con un backbone ViT come PanDerm serve una variante per transformer (per esempio *attention rollout*, oppure Grad-CAM sull'ultimo blocco) ⚠️ da scegliere nella fase ML.
