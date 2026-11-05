# Kurtansky et al., 2025 — ISIC 2024: triage automatico dalla fotografia 3D di tutto il corpo

- **Rivista:** *npj Digital Medicine* 8:708 (2025) · [DOI 10.1038/s41746-025-02070-7](https://doi.org/10.1038/s41746-025-02070-7) · PMID 41272121 · PMC12639164
- **Gruppo:** Memorial Sloan Kettering (Kurtansky, Rotemberg, Kose), con Codella e un consorzio internazionale
- **Testo letto:** abstract, risultati e discussione (PMC); i metodi solo in parte.
- Il dataset si chiama **SLICE-3D** (Kurtansky et al., *Scientific Data* 2024 ⚠️ non letto).

## In una frase
Da una **fotografia 3D di tutto il corpo** si ritagliano centinaia di lesioni per paziente. Il modello vincente le mette in ordine di rischio, e con il **contesto del paziente** (il "brutto anatroccolo") riduce le lesioni da far vedere al dermatologo.

## Come era fatta
- **Più di 900.000 ritagli di lesioni** da fotografie 3D di tutto il corpo (sistema Vectra WB360). Sono immagini **non dermoscopiche**, di qualità simile a una foto da smartphone.
- **Test privato:**
  - 370.704 lesioni di 935 pazienti, con una mediana di **243 lesioni per paziente**;
  - solo **342 maligne**: 99 melanomi (55 in situ), 190 basocellulari, 53 squamocellulari;
  - circa **1 lesione maligna su 1.100**, e 1 melanoma su 3.744.
- **Metrica:** **AUC parziale sopra l'80% di sensibilità** (pAUC, massimo 0,2). Conta solo la parte della curva ROC utile in clinica, dove si mancano pochi tumori.
- **2.739 squadre**, 4.998 invii ufficiali, su Kaggle.

## Risultati
- **Modello vincente:** pAUC **0,1726**, AUC completa **0,967**.
- **Quante lesioni da far controllare** per trovare un tumore:

  | Tumori trovati | Lesioni controllate per ogni tumore |
  |----------------|-------------------------------------|
  | 80% | circa **52** |
  | 90% | circa **98** |

  Il punto di partenza era 1 su 1.100.
- **Per paziente:** controllando le 15 lesioni più sospette di ciascuno, i modelli trovano il tumore in fino al **79%** dei pazienti malati.
- **Il contesto del paziente conta:**
  - senza le informazioni "rispetto alle altre lesioni dello stesso paziente", l'AUC scende da 0,967 a 0,956;
  - all'80% di sensibilità bisogna controllare **22 lesioni benigne in più** per ogni tumore.
  - Il vincitore normalizzava ogni lesione rispetto alle altre del paziente, come il segno del **brutto anatroccolo**.
- **Metadati più utili delle immagini:** le misure automatiche del sistema 3D (colore, forma, dimensioni) da sole battono le sole immagini (AUC 0,939 contro 0,922). Età, sesso, sede e centro aiutano ancora.
- **Cosa guarda il modello:**
  - il rischio sale con il colore **più rosso**, con la **variabilità del colore** e con le **dimensioni**;
  - bordo irregolare e asimmetria contano poco (correlazione 0,18 e 0,07).
- **Ribaltamento della classifica:** il 95,5% degli invii ha avuto un punteggio più alto sulla classifica pubblica che su quella privata. I vincitori sono saliti di 30–1.137 posizioni. È overfitting sulla classifica pubblica, aggravato dai pochi casi positivi.

## Limiti dichiarati
- I modelli migliori usano **misure proprietarie** del sistema Vectra WB360: non si applicano ad altri dati.
- Il modello vincente **non funziona su una lesione singola**: ha bisogno di tutte le lesioni del paziente.

## Messaggi chiave per la tesi
1. La metrica giusta dipende dall'uso clinico. Per il triage conta la **zona ad alta sensibilità** della curva ROC, non l'AUC intera.
2. Con prevalenze bassissime, l'utilità si misura in "**quante lesioni controllare per trovare un tumore**" (numero necessario).
3. Il contesto del paziente funziona con l'**intero corpo** (2024) e non con 7 lesioni (2020).

## Cosa porto in Neo Helper
- Nella valutazione, oltre all'accuratezza bilanciata:
  - **specificità a sensibilità fissa** (90% e 95%) per il punteggio di malignità;
  - **pAUC sopra l'80% di sensibilità**.
- Tradurre la soglia di malignità in "**lesioni da biopsiare per trovare un melanoma**", un numero comprensibile per il medico.
- SLICE-3D è un possibile **test di domain shift** verso foto non dermoscopiche, per la parte mobile (M6). Neo Helper resta però centrato sulla dermoscopia.
- Regola già vista: niente scelte basate sul test.
