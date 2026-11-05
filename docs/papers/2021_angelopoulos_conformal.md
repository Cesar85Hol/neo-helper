# Angelopoulos & Bates, 2021 — Introduzione alla conformal prediction

- **Tipo:** tutorial · [arXiv 2107.07511](https://arxiv.org/abs/2107.07511). Pubblicato anche su *Foundations and Trends in Machine Learning* (2023) ⚠️.
- **Autori:** Anastasios N. Angelopoulos (UC Berkeley) e Stephen Bates
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF ⚠️. La parte base (split conformal) è descritta qui come è nota in letteratura.

## In una frase
Invece di una sola diagnosi, il modello restituisce un **insieme di diagnosi** che contiene quella vera con una probabilità scelta da noi, per esempio il 95%. Non servono ipotesi sulla distribuzione dei dati né sul modello.

## Come funziona (split conformal, il caso base)
1. Si parte da un classificatore **già addestrato**, per esempio PanDerm con la testa lineare.
2. Si tiene da parte un **set di calibrazione** di casi mai visti, per esempio qualche centinaio di immagini.
3. Per ogni caso di calibrazione si calcola un **punteggio di "non conformità"**. Il più semplice è 1 meno la probabilità data alla classe vera.
4. Si prende il **quantile** di questi punteggi al livello 1−α, per esempio il 95° percentile: è la soglia q̂.
5. Per un nuovo paziente, l'insieme contiene tutte le diagnosi con punteggio sotto q̂.

**Garanzia:** in media, l'insieme contiene la diagnosi vera almeno nel 95% dei casi. Vale con un numero finito di dati, purché i casi nuovi assomiglino a quelli di calibrazione (scambiabilità).

## Punti importanti del tutorial
- **Insiemi adattivi (APS):** usano le probabilità cumulative. Danno insiemi **piccoli per i casi facili e grandi per quelli difficili**. Un insieme grande è già un "non sono sicuro".
- **Copertura per gruppo o per classe:** si calibra separatamente per ciascun sottogruppo, per esempio per fototipo o per classe rara, così la garanzia vale anche lì. È il collegamento con l'equità.
- **Controllo del rischio:** si può garantire un tasso massimo di **falsi negativi** invece della copertura generale.
- **Spostamento dei dati:** con un cambio di distribuzione la garanzia si perde. Esistono versioni pesate, ma richiedono di conoscere lo spostamento.
- **Come verificare:** controllare la copertura effettiva sul test, la dimensione media degli insiemi e la copertura per sottogruppo.

## Limiti
- La garanzia è **media** (marginale), non per singolo paziente.
- Se il test esterno (DDI, PAD-UFES-20) è diverso dal set di calibrazione, la copertura **non è garantita**: va misurata.

## Cosa porto in Neo Helper
- **Tool `predict_set`:** restituisce l'insieme delle diagnosi al 90% o al 95%, invece della sola diagnosi più probabile.
- **"Non so" con un criterio preciso:** se l'insieme contiene più classi, alcune maligne, l'agente lo dice e raccomanda la valutazione dello specialista.
- **Calibrazione condizionata per classe**, così il melanoma, classe rara, ha la sua copertura. Per fototipo serve un dataset che lo riporti.
- **Valutazione:** copertura e dimensione degli insiemi su HAM10000 (test interno) e sui test esterni, per vedere quanto si rompe la garanzia con il domain shift.
- Libreria pratica in Python: ad esempio MAPIE o TorchCP ⚠️ da scegliere.
