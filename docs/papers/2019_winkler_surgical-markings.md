# Winkler et al., 2019 — I segni di penna chirurgica ingannano la rete

- **Rivista:** *JAMA Dermatology* 155(10):1135–1141 (2019) · [DOI 10.1001/jamadermatol.2019.1735](https://doi.org/10.1001/jamadermatol.2019.1735) · PMID 31411641 · PMC6694463
- **Gruppo:** Heidelberg (Haenssle, Enk) con centri europei; lo stesso gruppo di Haenssle 2018
- **Testo letto:** **abstract strutturato e Key Points** (PMC non restituisce il corpo dell'articolo). I numeri riportati sono tutti nell'abstract; i dettagli dei metodi oltre l'abstract sono ⚠️.

## In una frase
Basta un **segno di penna viola** vicino a un neo perché una rete certificata come dispositivo medico lo scambi per **melanoma**: la specificità crolla dall'84% al 46%. La rete aveva imparato una **scorciatoia**.

## Il problema
Prima dell'asportazione, il chirurgo spesso disegna sulla pelle con un pennarello al **violetto di genziana**. Quindi, nelle immagini di addestramento, i segni di penna compaiono soprattutto vicino alle lesioni **asportate**, cioè più spesso ai melanomi. La rete può imparare "penna = melanoma" invece di guardare la lesione.

## Cosa hanno fatto
- **La rete:** una CNN commerciale con **marchio CE** (mercato europeo), addestrata su più di **120.000 immagini dermoscopiche** (⚠️ nome del prodotto non nell'abstract; dovrebbe essere Moleanalyzer pro di FotoFinder, come in Haenssle 2018).
- **Le lesioni:** **130 lesioni melanocitiche**: 107 nevi benigni e 23 melanomi.
- **Tre serie di immagini delle stesse lesioni:**
  1. **senza** segni;
  2. **con** segni di penna fatti apposta;
  3. con i segni **tagliati via** ritagliando l'immagine sulla lesione.
- Mappe di calore (gradienti) per vedere dove guarda la rete.

## Risultati

| Immagini | Sensibilità | Specificità | AUC |
|----------|-------------|-------------|-----|
| Senza segni | 95,7% | 84,1% | 0,969 |
| **Con segni di penna** | 100% | **45,8%** | 0,922 |
| Ritagliate | 100% | **97,2%** | 0,993 |

- Con i segni la probabilità di melanoma **sale** per tutte le lesioni: i falsi positivi tra i nevi aumentano di circa **40 punti**.
- Le mappe di calore mostrano che la rete **guarda i segni blu**.
- Ritagliare sulla lesione dà il risultato migliore di tutti.

## Messaggi chiave per la tesi
1. È l'esempio da manuale di **shortcut learning**: la rete impara un indizio presente nei dati (la penna) che non c'entra con la malattia.
2. Il problema riguarda un dispositivo **già certificato** e in commercio.
3. Gli **artefatti** (penna, righelli, peli, bolle, bordi neri del dermatoscopio) vanno descritti e controllati: è proprio quello che chiede CLEAR Derm.
4. Le **heatmap** servono anche per scoprire questi errori.

## Limiti
- Una sola rete e un solo tipo di artefatto.
- Campione piccolo: 23 melanomi.
- Segni fatti apposta per lo studio, non nella pratica reale.

## Cosa porto in Neo Helper
- **Agente di controllo qualità** (Critic/Safety): prima di classificare, cercare artefatti come segni di penna e righelli e avvisare ("immagine con segni chirurgici: risultato meno affidabile").
- **Pre-processing:** ritaglio automatico sulla lesione (segmentazione) prima della classificazione.
- **Audit dei dati:** contare in HAM10000/ISIC quanti segni di penna ci sono per classe (con MONET o a mano su un campione).
- **Test di robustezza:** valutare il modello su immagini con e senza artefatti.
