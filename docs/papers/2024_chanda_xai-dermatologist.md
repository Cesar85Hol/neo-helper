# Chanda et al., 2024 — Un'AI spiegabile "come un dermatologo" aumenta fiducia e sicurezza

- **Rivista:** *Nature Communications* 15:524 (2024) · [DOI 10.1038/s41467-023-43095-4](https://doi.org/10.1038/s41467-023-43095-4) · PMID 38225244 · PMC10789736
- **Gruppo:** consorzio europeo coordinato dal DKFZ di Heidelberg (gruppo di Titus Brinker) ⚠️
- **Testo letto:** **completo** (PMC). Letti introduzione, risultati, parte dei metodi e dei limiti; non il materiale supplementare.

## In una frase
Una rete che spiega la diagnosi **con i criteri dermoscopici e indicando dove si trovano** rende i medici più sicuri e più fiduciosi. Però **non** li rende più accurati della stessa AI senza spiegazioni.

## Cosa hanno fatto
- **Dati:** tutte le immagini di **melanoma e nevo con istologia** di **HAM10000**: 3.611 immagini, 1.981 lesioni.
- **14 dermatologi** hanno annotato ogni immagine con una **ontologia di criteri dermoscopici** (per esempio reticolo atipico, strie, velo) e con le **zone** dove li vedono. L'ontologia è stata approvata da due dermatologi. Il dataset annotato è stato **pubblicato**.
- **Modello:** ResNet-50 addestrata a predire insieme la diagnosi, i criteri e le zone.
- **Studio in tre fasi con 116 medici di vari paesi:**
  - fase 1: senza AI;
  - fase 2: con l'AI (diagnosi e confidenza);
  - fase 3: con l'AI spiegabile (diagnosi, criteri e zone).

## Risultati
- **La rete spiegabile non perde accuratezza:** accuratezza bilanciata 81%, contro l'80% della ResNet-50 normale.
- **Guarda la lesione:** il rapporto di attenzione tra dentro e fuori la lesione è 35,9, contro 4,1 della rete normale.
- **Spiegazioni simili a quelle dei medici:**
  - sovrapposizione dei criteri tra AI e medici 0,27, pari a quella tra due medici (0,28);
  - sovrapposizione delle zone 0,48, contro 0,39 della rete normale.
- **Effetto sui medici:**

  | | Senza AI | AI | AI spiegabile |
  |---|---------|----|---------------|
  | Accuratezza bilanciata | 66,2% | **72,3%** | 73,2% (differenza non significativa) |

  - **Sicurezza nella propria diagnosi:** +12,3% con le spiegazioni.
  - **Fiducia nell'AI:** +17,5% con le spiegazioni.
  - I medici sono d'accordo con l'AI più spesso con le spiegazioni (79,5% contro 77,1%). Anche quando **l'AI sbaglia**, l'accordo sale dal 63% al 67,9% (non significativo) ⚠️ segnale di automation bias.
  - **Chi ne ha beneficiato:** i più esperti in dermoscopia hanno guadagnato di più dalle spiegazioni. I meno esperti hanno guadagnato di più dalla sola AI, e alcuni sono peggiorati con le spiegazioni.

## Messaggi chiave per la tesi
1. **Spiegare non vuol dire migliorare l'accuratezza.** Le spiegazioni aumentano fiducia e sicurezza, ed è un'arma a doppio taglio: possono far seguire l'AI anche quando sbaglia.
2. La spiegazione utile per il dermatologo usa la **sua lingua**: criteri dermoscopici localizzati, non una heatmap generica. Chanda la chiama "chiudere il divario di interpretazione".
3. L'effetto dipende dall'**esperienza** del medico: lo stesso output può aiutare un esperto e confondere un principiante.

## Limiti
- Condizioni sperimentali, non cliniche. Solo melanoma contro nevo.
- Il sistema è guidato a dare spiegazioni "umane". Quindi non è detto che mostri come ragiona davvero la rete: è un rischio di fedeltà.

## Cosa porto in Neo Helper
- **Dataset preziosissimo:** annotazioni dermoscopiche **localizzate** su HAM10000, proprio il nostro dataset iniziale. Servono per:
  - validare MONET sui criteri dermoscopici;
  - addestrare un concept bottleneck;
  - misurare se le heatmap guardano i criteri giusti.
  
  Dataset: Figshare [10.6084/m9.figshare.23766477](https://doi.org/10.6084/m9.figshare.23766477), **CC BY 4.0** (verificato 2026-11-09). Attenzione alle immagini duplicate tra i gruppi.
- Nel report, mostrare i **criteri con la loro posizione** quando possibile.
- Nella valutazione con utenti, misurare **anche** l'accordo con l'AI quando sbaglia, non solo l'accuratezza e la fiducia.
- Adattare la presentazione all'**esperienza** dell'utente (Fase 5–6: interfaccia per medici di base o per dermatologi).
