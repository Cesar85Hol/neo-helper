# Kim et al., 2024 — MONET: un foundation model immagine-testo per un'AI medica trasparente

- **Rivista:** *Nature Medicine* 30(4):1154–1165 (2024) · [DOI 10.1038/s41591-024-02887-x](https://doi.org/10.1038/s41591-024-02887-x) · PMID 38627560
- **Preprint:** medRxiv, 12 giugno 2023 · [DOI 10.1101/2023.06.07.23291119](https://doi.org/10.1101/2023.06.07.23291119) · licenza CC BY-NC 4.0
- **Gruppo:** University of Washington (Su-In Lee) e Stanford (Roxana Daneshjou)
- **Testo letto:** **testo completo del preprint** medRxiv (v1, 2023: risultati, discussione e metodi), più l'abstract della versione pubblicata, il README del repository ([github.com/suinleelab/MONET](https://github.com/suinleelab/MONET)) e la model card su Hugging Face. La versione di Nature Medicine non è in PMC: ciò che c'è solo lì è segnato con ⚠️.

## In una frase
MONET impara a collegare immagini dermatologiche e **concetti clinici in parole** (per esempio "eritema", "ulcera", "pigmentato") leggendo la letteratura medica. Così può dare un **punteggio di presenza per ogni concetto** e rendere controllabili dati e modelli.

## Il problema
- Per fidarsi di un modello di immagini bisogna poterlo **interrogare** in ogni fase: dati di addestramento, modello, uso dopo il rilascio.
- Il modo naturale per un medico è usare i **suoi termini** ("questa lesione è squamosa?"). Ma servirebbero dataset annotati a mano, concetto per concetto, e sono rarissimi (SkinCon, PH2, Derm7pt).

## Cosa hanno fatto
- **Dati di addestramento:** **105.550 coppie immagine-didascalia**:
  - **50.265** figure da articoli di dermatologia del sottoinsieme open access di PubMed Central (496.510 articoli scaricati, figure non dermatologiche tolte con clustering e controllo manuale);
  - **55.285** immagini da **55 libri di testo** di medicina, con la didascalia ricostruita dal PDF.
- **Modello:** stessa architettura di **CLIP**: immagine con **ViT-L/14** (input 224×224, embedding di 768 numeri), testo con un transformer di 12 strati. Parte dai pesi di CLIP e viene addestrato in modo **contrastivo** per 10 epoche (6 GPU A40, circa 1 ora e 40 minuti).
- **Punteggio di un concetto:** si confronta l'immagine con la frase "This is skin image of {concetto}" e con una frase di riferimento neutra ("This is skin image"). Per le dermoscopie si usa "This is dermatoscopy of {concetto}". Il risultato è una probabilità di presenza del concetto, mediata su più frasi.
- **Dati di valutazione** (non usati per l'addestramento):
  - immagini cliniche di **Fitzpatrick17k** (4.324 dopo la pulizia) e **DDI** (636);
  - **71.671** immagini dermoscopiche **ISIC** (2016–2020).

## Risultati (preprint)

**1. Generazione dei concetti.** Il confronto è fatto sulle etichette **SkinCon**: 21 concetti con almeno 30 esempi positivi, su 1.645 immagini cliniche.

| Metodo | AUROC media | Concetti con AUROC > 0,7 |
|--------|-------------|--------------------------|
| **MONET** (nessuna etichetta) | **0,766** | **19/21** |
| CLIP generico | 0,692 | 9/21 |
| ResNet-50 supervisionata | 0,692 | 11/21 |

- Prestazioni **simili tra fototipi** su Fitzpatrick17k e DDI. I numeri sono nella tabella supplementare 3, che non ho letto ⚠️.
- Riconosce anche concetti **non clinici**: segni di penna viola, adesivi arancioni, peli, unghie, bordo nero del dermatoscopio.

**2. Audit dei dati (ISIC).**
- Nelle immagini **maligne** prevalgono: ulcera, erosione, aspetto verrucoso, colore rosato, colore blu.
- Nelle **benigne** prevalgono: **adesivo arancione**, ipopigmentazione, colore salmone, xerosi, iperpigmentazione.
- L'adesivo arancione è una scorciatoia: in ISIC si usava soprattutto nei **bambini**, quasi sempre con lesioni benigne.
- **Differenze tra centri.** Il "rosso" è associato al **benigno** a Vienna (9.873 immagini) e al **maligno** a Barcellona (12.302 immagini).

**3. Audit del modello.**
- **Test controllato:** si introduce una correlazione spuria nota e si chiede a MONET di ritrovarla. MONET la ritrova nel 59% dei casi al primo posto della lista, nell'80% tra i primi 2 e nell'89% tra i primi 3. CLIP si ferma al 27%, 52% e 66%.
- **Tra centri:** un modello addestrato a Vienna passa da AUROC 0,885 a **0,707** a Barcellona. Al contrario, da Barcellona a Vienna, passa da 0,844 a 0,741.
- MONET spiega gli errori con il "rosso". Per esempio, in un cluster dove si sbaglia molto, 55 maligni su 74 sono classificati benigni.

**4. Concept bottleneck (MONET+CBM).** I concetti di MONET entrano in un modello lineare. I dermatologi hanno scelto 11 concetti; il modello è valutato su 20 suddivisioni casuali dei dati.
- **Malignità:** AUROC **0,805**. Nel preprint 0,854 con tutti i 48 concetti SkinCon.
- **Melanoma:** AUROC **0,892**.
- Batte la CBM con concetti annotati a mano, la ResNet-50 supervisionata, il linear probe su ResNet-50 e la CBM con CLIP: in 15 suddivisioni su 20 per la malignità e in 18 su 20 per il melanoma.
- I pesi del modello lineare **rispettano l'ABCDE**: asimmetria, irregolarità e colori multipli spingono verso "melanoma", "regolare" spinge verso "benigno".

## Messaggi chiave per la tesi
1. Un foundation model immagine-testo può fare da **"traduttore"** tra quello che vede la rete e il linguaggio del dermatologo, **senza** annotazioni manuali di concetti.
2. La spiegabilità non è solo la heatmap: può essere **a concetti**, cioè nelle parole della clinica. Il "rosso" che confonde Vienna e Barcellona non è un'area dell'immagine, quindi una heatmap non lo mostrerebbe.
3. MONET serve anche **prima** del modello: per controllare i dataset e trovare scorciatoie. Gli adesivi arancioni sono l'equivalente dei segni di penna di Winkler 2019 (§4).

## Limiti
- **Mancano dermoscopie su pelli scure:** lo dicono gli autori stessi. Su pelli diverse è stato valutato solo con immagini **cliniche**.
- I dati di addestramento sono soprattutto immagini **cliniche** di libri e articoli. La letteratura ha le sue distorsioni: casi "da manuale" e pelli chiare ⚠️.
- I concetti valutati sono quelli di **SkinCon**: morfologia, colore, superficie. I **criteri dermoscopici** (reticolo atipico, velo blu-biancastro, strie) **non** sono stati valutati con etichette vere. Il concetto "blu" è solo un parente del velo blu-biancastro.
- Ho letto il **preprint**: la versione pubblicata può avere numeri e analisi diversi. Per esempio, il caso di studio su un **trial clinico di AI** citato nell'abstract pubblicato non è nel preprint ⚠️.

## Licenza e uso
- **Codice e repository:** **CC BY-NC-SA 4.0**. Niente uso commerciale, e i lavori derivati vanno condivisi con la stessa licenza.
- **Model card su Hugging Face** (`chanwkim/monet`): non indica una licenza propria. Dice che il modello è un risultato di ricerca e che **qualsiasi uso in produzione, commerciale o no, è fuori ambito**.
- Per Neo Helper: va bene per la **tesi** (audit dei dati, tool "concetti" negli esperimenti). **Non** va bene per un'app pubblica o un prodotto, come PanDerm.

## Cosa porto in Neo Helper
- **Tool MCP `describe_concepts`:** data un'immagine, restituisce i punteggi di una lista di concetti clinici. L'agente che scrive il report può citarli ("presenza di colori multipli: alta"). Le frasi per le dermoscopie vanno usate con "This is dermatoscopy of {}".
- **Audit di HAM10000/ISIC** prima di addestrare:
  - confronto maligni/benigni (*concept differential analysis*);
  - ricerca di "adesivo arancione", "inchiostro viola", "bordo dermoscopico", "peli".
- **Audit del modello** sui test esterni: capire con quali concetti sbaglia su PAD-UFES-20 o DDI.
- Base per **concept bottleneck** nella fase di explainability (roadmap Fase 4). Prima verificare quanto bene MONET riconosce i criteri dermoscopici su **Derm7pt**, che ha etichette dei 7 criteri.
