# Marsden et al., 2024 — DERM (Skin Analytics) nel percorso oncologico del sistema sanitario inglese

- **Rivista:** *Frontiers in Medicine* 11:1302363 (2024) · [DOI 10.3389/fmed.2024.1302363](https://doi.org/10.3389/fmed.2024.1302363) · PMID 38585154 · PMC10996444
- **Gruppo:** University Hospitals Birmingham e Skin Analytics ⚠️ verificare il conflitto d'interesse con l'azienda
- **Testo letto:** abstract e parti di introduzione e metodi (PMC).
- **Dati sulla marcatura CE di classe III (2025):** dal sito dell'azienda e dalla stampa di settore, non da documenti ufficiali ⚠️.

## In una frase
In uno studio prospettico nel servizio sanitario inglese, l'AI **DERM** trova i tumori quanto i teledermatologi, ma riconosce **molte più lesioni che non hanno bisogno** di biopsia o di visita urgente. Così può ridurre gli invii inutili.

## Il prodotto
- **DERM** (*Deep Ensemble for the Recognition of Malignancy*), di Skin Analytics (Regno Unito): un **ensemble** di reti convoluzionali su immagini **dermoscopiche fatte con lo smartphone** e una lente per dermoscopia.
- **Uso nel servizio sanitario inglese (NHS):** nei percorsi per il cancro della pelle dal 2020, con più di **81.000 pazienti**.
- **Storia regolatoria:**
  - classe I come supporto alla decisione, quando è stato fatto questo studio;
  - **UKCA classe IIa** (aprile 2022), che permette decisioni **autonome**;
  - secondo l'azienda, **marcatura CE di classe III** con l'MDR (febbraio 2025): la prima AI autorizzata in Europa a decidere da sola sulle lesioni ⚠️.

## Lo studio
- **Disegno:**
  - prospettico, un solo centro, braccio unico, in cieco;
  - di non inferiorità, con disegno adattivo;
  - nel percorso di teledermatologia per sospetto tumore.
- **700 pazienti, 867 lesioni**; nell'analisi per protocollo 622 pazienti e 789 lesioni.
  - 63% donne;
  - 89% bianchi;
  - solo il **4%** con fototipo IV–VI.
- **67 lesioni maligne**, di cui solo **8 melanomi**.
- La sensibilità dell'AI è fissata al 91% e al 92,5%, vicino a quella dei medici riportata in letteratura (91,46%).

## Risultati
- Con sensibilità simile, l'AI identifica **significativamente più lesioni** che non richiedono biopsia né visita urgente rispetto ai teledermatologi (p = 0,001).
- Il valore clinico sta nel **ridurre gli invii**, non nel trovare più tumori.

## Limiti
- Un solo centro, **pochi melanomi** (8), poche pelli scure.
- Studio legato all'azienda ⚠️.

## Messaggi chiave per la tesi
1. È l'esempio più avanzato in Europa di **AI dermatologica in uso reale**: smartphone + lente dermoscopica, dentro un percorso clinico, con studi prospettici e una classe di rischio alta.
2. Il valore misurato è **organizzativo** (meno invii inutili) a sicurezza invariata.
3. Arrivare all'uso autonomo ha richiesto anni di dati reali e una certificazione di classe III.

## Cosa porto in Neo Helper
- Mostra il **divario** tra un prototipo di tesi e un prodotto: studi prospettici, sistema di qualità, sorveglianza dopo l'immissione sul mercato.
- Idea per la valutazione: oltre all'accuratezza, misurare **quante lesioni benigne** Neo Helper eviterebbe di inviare, a parità di sensibilità.
- La parte mobile (M6) con una **lente dermoscopica per smartphone** è un modello realistico.
