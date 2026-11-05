# Codella et al., 2019 — La challenge ISIC 2018

- **Fonte:** report della challenge ISIC 2018 (MICCAI 2018, Granada) · [arXiv 1902.03368](https://arxiv.org/abs/1902.03368)
- **Gruppo:** IBM Research, Memorial Sloan Kettering (Halpern), Medical University of Vienna (Tschandl, Kittler), Emory, Kitware
- **Testo letto:** **completo** (arXiv, v2), con le tabelle supplementari. Le sfide precedenti, ISBI 2016 (Gutman et al., arXiv 1605.01397) e ISBI 2017 (Codella et al., arXiv 1710.05006), sono solo citate qui: non le ho lette ⚠️.

## In una frase
La sfida più grande del 2018 introduce tre regole che ancora oggi contano: **accuratezza bilanciata** al posto dell'accuratezza, un **test esterno** da centri mai visti, e una misura che conta i **fallimenti** della segmentazione invece di nasconderli nella media.

## Come era fatta
Tre compiti, 900 iscritti:

| Compito | Dati di training | Test | Metrica |
|---------|------------------|------|---------|
| 1. Segmentazione della lesione | 2.594 immagini con maschera | 1.000 | **Jaccard con soglia** (sotto 0,65 vale 0) |
| 2. Attributi dermoscopici (5) | 2.594 immagini, 12.970 maschere | 1.000 | Jaccard |
| 3. Classificazione in 7 classi | **HAM10000** (10.015) | 1.512: **1.196 interne** + **316 esterne** (Turchia, Nuova Zelanda, Svezia, Argentina) | **Accuratezza bilanciata** |

- Si potevano usare altri dati dermoscopici, ma andava dichiarato.
- Il numero di invii per compito è diverso tra abstract e testo (115 contro 112 per la segmentazione, 159 contro 141 per la classificazione) ⚠️.

## Risultati
- **Segmentazione:** il migliore arriva a 0,802 di Jaccard con soglia. Ma quasi tutti i metodi **sbagliano più del 10% delle immagini**, soprattutto sulle cheratosi seborroiche. La media alta nascondeva i fallimenti.
- **Attributi dermoscopici:** risultati molto bassi, al massimo 0,473 di Jaccard. Anche gli esperti sono poco d'accordo tra loro su questi criteri.
- **Classificazione:** accuratezza bilanciata massima **0,885**.
  - La maggior parte dei metodi va **meglio sui dati interni che su quelli esterni**: è overfitting. I migliori però no.
  - Metodi con lo stesso punteggio totale possono **generalizzare in modo molto diverso**.
  - Non servono dati proprietari per generalizzare bene.
  - **La metrica cambia la classifica:** con l'accuratezza semplice vince chi si adatta alla prevalenza del dataset (troppi nevi); con l'AUC media contano anche zone della curva ROC poco utili in clinica.

## Messaggi chiave per la tesi
1. Su HAM10000 la metrica giusta è l'**accuratezza bilanciata** (media del richiamo per classe), non l'accuratezza.
2. Un test esterno, anche piccolo, rivela l'overfitting che il test interno non vede.
3. Riconoscere gli attributi dermoscopici è difficile anche per gli esperti: aspettative basse per MONET e per un concept bottleneck sui criteri.
4. È la challenge su cui Tschandl 2019 (§2) ha confrontato 511 lettori e 139 algoritmi.

## Cosa porto in Neo Helper
- Metrica principale: **accuratezza bilanciata** sulle 7 classi, più AUC per classe e la sensibilità sul melanoma.
- Riportare sempre separati i risultati **interni ed esterni**, e la loro differenza.
- Per la segmentazione (M3.2): contare i **fallimenti** (Jaccard < 0,65), non solo la media.
- Le maschere e gli attributi di ISIC 2018 (compiti 1 e 2) sono una risorsa per la segmentazione e per verificare i concetti.
