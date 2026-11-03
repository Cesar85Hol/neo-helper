# Kim et al., 2024 — MONET: un foundation model immagine-testo per un'AI medica trasparente

- **Rivista:** *Nature Medicine* 30(4):1154–1165 (2024) · [DOI 10.1038/s41591-024-02887-x](https://doi.org/10.1038/s41591-024-02887-x) · PMID 38627560
- **Gruppo:** University of Washington (Su-In Lee) e Stanford (Daneshjou)
- **Testo letto:** **solo abstract** (non disponibile in PMC) più il README del repository ufficiale ([github.com/suinleelab/MONET](https://github.com/suinleelab/MONET)). I dettagli non presenti in queste due fonti sono segnati con ⚠️.

## In una frase
MONET impara a collegare immagini dermatologiche e **concetti clinici in parole** (per esempio "eritema", "ulcera", "pigmentato") leggendo la letteratura medica. Così può dare un **punteggio di presenza per ogni concetto** e rendere controllabili dati e modelli.

## Il problema
- Per fidarsi di un modello di immagini bisogna poterlo **interrogare** in ogni fase: dati di addestramento, modello, uso dopo il rilascio.
- Il modo naturale per un medico è usare i **suoi termini** ("questa lesione è squamosa?"). Ma servirebbero dataset annotati a mano, concetto per concetto, e sono rarissimi.

## Cosa hanno fatto
- **Dati:** **105.550 immagini dermatologiche** abbinate a descrizioni in linguaggio naturale, estratte da una grande raccolta di **letteratura medica** (articoli PubMed; secondo il repository anche fonti PDF ⚠️ composizione esatta).
- **Modello:** architettura di tipo **CLIP** (immagine + testo, addestramento contrastivo). Nel repository i pesi si caricano sopra un **CLIP ViT-L/14**.
- **Uso:** dato un concetto scritto a parole, MONET assegna a ogni immagine un punteggio di presenza (*concept retrieval*), senza bisogno di etichette manuali.

## Risultati (dall'abstract)
- Le annotazioni di concetti di MONET sono **verificate da dermatologi** e sono competitive con modelli **supervisionati** addestrati su dataset già annotati a concetti (immagini cliniche).
- Dimostrano tre usi lungo tutta la pipeline:
  1. **audit dei dati:** scoprire cosa contiene davvero un dataset (artefatti, differenze tra fonti);
  2. **audit del modello:** capire su quali concetti un classificatore sbaglia;
  3. **modelli interpretabili per costruzione** (*concept bottleneck*).
- Caso di studio: l'analisi dei risultati di un **trial clinico di AI** ⚠️ (dettagli non letti).

## Messaggi chiave per la tesi
1. Un foundation model immagine-testo può fare da **"traduttore"** tra quello che vede la rete e il linguaggio del dermatologo.
2. La spiegabilità non è solo la heatmap: può essere **a concetti**, cioè nelle parole della clinica.
3. MONET serve anche **prima** del modello: per controllare i dataset e trovare scorciatoie (vedi Winkler 2019, §4).

## Limiti
- Letto solo l'abstract: metriche precise, lista dei concetti e dettagli del caso di studio sono da verificare ⚠️.
- La letteratura medica ha le sue distorsioni: più immagini di casi "da manuale" e di pelli chiare ⚠️.
- I concetti sono quelli che si trovano scritti nei testi; non è detto che coprano i criteri dermoscopici (ABCD, 7-point) che servono a Neo Helper.

## Cosa porto in Neo Helper
- **Pesi pubblici** su Hugging Face (`chanwkim/monet`): utilizzabile subito per esperimenti. ⚠️ Licenza da controllare nel file LICENSE del repository.
- **Tool MCP "concetti":** dato un'immagine, restituire i punteggi di una lista di concetti clinici. L'agente che scrive il report può citarli ("presenza di pigmentazione irregolare: alta").
- **Audit di HAM10000/ISIC** prima di addestrare: cercare con MONET concetti come "inchiostro", "righello", "peli" per trovare possibili scorciatoie.
- Base per **concept bottleneck** nella fase di explainability (roadmap Fase 4).
