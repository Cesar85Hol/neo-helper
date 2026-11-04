# Anriot et al., 2026 — I limiti dell'AI per il cancro della pelle in condizioni realistiche

- **Rivista:** *JAMA Dermatology* 162(7):701–708 (2026) · [DOI 10.1001/jamadermatol.2026.1492](https://doi.org/10.1001/jamadermatol.2026.1492) · PMID 42234423 · PMC13234745
- **Gruppo:** studio multi-istituzionale con, tra gli altri, Yan (PanDerm) e Tschandl (Vienna)
- **Testo letto:** **solo abstract e Key Points** (PMC restituisce solo questi). Ogni dettaglio oltre l'abstract è ⚠️.

## In una frase
Su casi **di tutti i giorni**, compresi quelli rari e atipici, un foundation model moderno (PanDerm) supera i medici meno esperti, ma **non** i dermatologi con più di 10 anni di esperienza. Una CNN di prima generazione perde contro tutti.

## Cosa hanno fatto
- **1.117 casi** che rappresentano la pratica clinica quotidiana: immagini cliniche e dermoscopiche **con metadati**. Raccolti dal 2023 al 2025.
- **3 modelli:** una **CNN di prima generazione**, **PanDerm unimodale** (solo immagine) e **PanDerm multimodale** (immagine + metadati).
- **652 medici** (1.092 test), con esperienza da meno di 1 anno a più di 10. Ogni lettore valuta **100 casi** stratificati.
- Esito principale: accuratezza **multiclasse**. Secondari: sensibilità, specificità e accuratezza bilanciata per benigno/maligno.

## Risultati

| Chi | Accuratezza multiclasse media |
|-----|------------------------------|
| CNN prima generazione | 56,7% |
| Medici con meno di 1 anno | 59,1% |
| Medici (tutti) | 65,9% |
| PanDerm multimodale | 66,3% |
| Medici con meno di 3 anni | 68,2% |
| **PanDerm unimodale** | **72,2%** |
| **Esperti oltre 10 anni** | **74,2%** |

- PanDerm unimodale supera i medici con meno di 3 anni (+4,0 punti) e **pareggia** quelli con 3–10 anni.
- Sorpresa: la versione **multimodale** (con i metadati) va **peggio** di quella solo-immagine ⚠️ (motivo da leggere nel testo completo).

## Messaggi chiave per la tesi
1. I risultati dei benchmark (PanDerm, Nature Medicine 2025) **si riducono** in condizioni realistiche. È la stessa lezione di Tschandl 2019 sui centri esterni.
2. L'AI moderna è al livello di un dermatologo di **media esperienza**: utile soprattutto come supporto per i **meno esperti** e per il triage.
3. Aggiungere metadati non migliora automaticamente il modello.

## Cosa porto in Neo Helper
- Scenario d'uso realistico: **supporto a medici non esperti** e triage, non sostituzione dello specialista.
- Valutazione: includere casi **rari e atipici** e confrontare con lettori stratificati per esperienza (CLEAR Derm, item 21–23).
- Prima di usare i metadati nel modello, verificare con un esperimento che aiutino davvero.
- ⚠️ Recuperare il testo completo per i dettagli su CNN, metadati e casi rari. Tentativo del 2026-11-04: PMC e la pagina di JAMA Dermatology mostrano solo abstract e Key Points. Strade possibili: il PDF dall'accesso universitario, o chiederlo agli autori insieme alla mail su PanDerm.
- ⚠️ Nell'abstract, il confronto medici–CNN riporta una differenza di 9,2 punti con IC 95% "da −9,8 a 8,5", che non contiene la differenza stessa: probabile refuso. Non citare quell'intervallo senza il testo completo.
