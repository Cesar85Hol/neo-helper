# §7 — Introduzione: le challenge ISIC dal 2016 al 2024

> Issue #3 (M1.3) · Fonti: PubMed, alphaXiv. Ogni scheda riporta DOI o link e dice cosa è stato letto.

Le challenge dell'**International Skin Imaging Collaboration (ISIC)** sono il banco di prova pubblico dell'AI dermatologica. Dal 2016 ogni edizione ha cambiato le regole per avvicinare la gara alla clinica. Leggerle in fila spiega molte scelte di Neo Helper.

**Le tappe:**
- **2016–2017** (ISBI): melanoma contro nevo e cheratosi seborroica, metrica AUC. Le prime gare con dati pubblici (non lette in dettaglio ⚠️).
- **2018** (Codella 2019):
  - 7 classi su **HAM10000**;
  - metrica **accuratezza bilanciata**;
  - **test esterno** da quattro paesi non presenti nel training.
  
  La maggior parte degli algoritmi va peggio sui dati esterni. La segmentazione sbaglia più del 10% delle immagini.
- **2019** (Combalia 2022):
  - 8 classi con **BCN20000**;
  - una classe **"mai vista"** nel test.
  
  L'accuratezza bilanciata crolla **dall'82% al 59%**. Gli algoritmi riconoscono il 6% delle lesioni sconosciute (i dermatologi il 26%) e ne chiamano maligne quasi la metà.
- **2020** (Rotemberg 2021, Ha 2020, Kurtansky 2024):
  - **33.126 immagini** raggruppate **per paziente**, con solo l'1,8% di melanomi;
  - vince un **ensemble di 18 reti** con una validazione stabile (AUC 0,949).
  
  Il contesto delle altre lesioni del paziente **non aiuta** né le reti né i medici.
- **2024** (Kurtansky 2025):
  - **900.000 ritagli** da fotografie 3D di tutto il corpo;
  - circa 1 tumore su 1.100 lesioni;
  - metrica **pAUC sopra l'80% di sensibilità**.
  
  Il vincitore usa il **contesto del paziente** (il "brutto anatroccolo") e riduce a circa 52 le lesioni da controllare per ogni tumore trovato.

**Tre lezioni che attraversano tutte le edizioni:**
1. **La metrica decide chi vince.** L'accuratezza premia chi si adatta alla prevalenza; l'accuratezza bilanciata e la pAUC ad alta sensibilità sono più vicine alla clinica.
2. **Fuori dal laboratorio le prestazioni calano:** centri nuovi, lesioni difficili, malattie mai viste, artefatti.
3. **Le classifiche pubbliche ingannano:** chi ottimizza sul test pubblico va in overfitting (2020: correlazione quasi nulla; 2024: il 95,5% degli invii peggiora sul test privato).

**Il filo conduttore per Neo Helper:**
- metriche: **accuratezza bilanciata** sulle 7 classi; per il punteggio di malignità **specificità a sensibilità fissa** (90–95%) e **pAUC**; il numero di lesioni da controllare per trovare un tumore;
- **BCN20000** come test esterno severo (coerente con "ISIC 2019 dopo"), con le sue lesioni sconosciute per misurare il **"non so"**;
- risultati separati **per centro** e **per artefatto**;
- il test si usa **una volta sola**;
- **licenze:** HAM10000 e ISIC 2020 sono **CC BY-NC**; **BCN20000 è CC BY 4.0** e permette anche l'uso commerciale.

| Anno | Challenge | Dati | Metrica | Lezione |
|------|-----------|------|---------|---------|
| 2016–17 | ISBI | ~2.000 dermoscopie, melanoma vs benigno | AUC | Prime gare pubbliche |
| 2018 | MICCAI (Codella) | HAM10000, 7 classi | Accuratezza bilanciata | Test esterno: overfitting visibile |
| 2019 | Combalia (*Lancet Digit Health*) | 25.331 img, 8 classi + "mai vista" | Accuratezza bilanciata | 82% → 59%; le lesioni sconosciute diventano "maligne" |
| 2020 | SIIM-ISIC su Kaggle | 33.126 img, 2.056 pazienti | AUC | Ensemble + validazione stabile; il contesto non aiuta |
| 2024 | SLICE-3D su Kaggle | 900.000 ritagli 3D | pAUC > 80% sens. | Il contesto del corpo intero aiuta il triage |

**Da leggere in seguito:** i report del 2016 e del 2017; il paper del dataset SLICE-3D (*Scientific Data* 2024); la challenge MILK10k del 2025 ⚠️.
