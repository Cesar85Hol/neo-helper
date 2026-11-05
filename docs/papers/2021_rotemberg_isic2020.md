# Rotemberg et al., 2021 — ISIC 2020: un dataset centrato sul paziente

- **Rivista:** *Scientific Data* 8:34 (2021) · [DOI 10.1038/s41597-021-00815-z](https://doi.org/10.1038/s41597-021-00815-z) · PMID 33510154 · PMC7843971
- **Gruppo:** Memorial Sloan Kettering (Rotemberg, Halpern), con centri in Australia, Austria e Spagna
- **Testo letto:** abstract e parti dei metodi e dei dati (PMC); non tutto il testo.

## In una frase
Il primo dataset ISIC che raggruppa le lesioni **per paziente**, perché il dermatologo non giudica un neo da solo: lo confronta con gli altri nei della stessa persona (segno del **brutto anatroccolo**).

## Cosa contiene
- **33.126 immagini dermoscopiche** di **2.056 pazienti**, in media **16 lesioni per paziente**.
- Il 20,8% dei pazienti ha almeno un melanoma.
- Solo **584 melanomi** confermati dall'istologia, cioè l'**1,8%** delle immagini. È molto sbilanciato, come nella realtà.
- **Benigni:** lesioni che imitano il melanoma, confermate da istologia o da più di 1,5 anni di follow-up dermoscopico (per Barcellona).
- **Centri:**
  - Memorial Sloan Kettering (New York);
  - Melanoma Institute Australia e Sydney Melanoma Diagnostic Centre;
  - University of Queensland;
  - Medical University of Vienna;
  - Hospital Clínic de Barcelona.
- **Metadati:** età approssimativa, sesso, sede anatomica, **identificativo anonimo del paziente**.
- **Licenza: CC BY-NC 4.0** (non commerciale). Sull'archivio ISIC c'è anche un file con i **duplicati**.
- È stata la base della gara su Kaggle "SIIM-ISIC Melanoma Classification" (27 maggio – 20 agosto 2020).

## Messaggi chiave per la tesi
1. La prevalenza reale del melanoma è **molto bassa**: con l'1,8% di positivi l'AUC è instabile, e l'accuratezza non ha senso.
2. Il contesto del paziente è un'informazione clinica vera, ma va dimostrato che serva alle macchine (vedi Kurtansky 2024 sui risultati della gara).

## Cosa porto in Neo Helper
- Neo Helper per ora lavora **su una lesione alla volta**. ISIC 2020 è la base per un'estensione futura con "più lesioni dello stesso paziente".
- Possibile **test esterno binario** (melanoma sì/no) con forte squilibrio, per misurare il punteggio di malignità in condizioni realistiche.
- Attenzione ai **duplicati** con gli altri dataset ISIC prima di usarlo come test.
