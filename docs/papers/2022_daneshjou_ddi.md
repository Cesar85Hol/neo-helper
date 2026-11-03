# Daneshjou et al., 2022 — DDI: le disparità dell'AI dermatologica su un dataset diverso e curato

- **Rivista:** *Science Advances* 8(32):eabq6147 (2022) · [DOI 10.1126/sciadv.abq6147](https://doi.org/10.1126/sciadv.abq6147) · PMID 35960806 · PMC9374341
- **Gruppo:** Stanford (Roxana Daneshjou, James Zou, Albert Chiou, Roberto Novoa)
- **Testo letto:** **completo** (PMC), senza tabelle supplementari.

## In una frase
Tre modelli di AI che sulla carta avevano AUC 0,88–0,94, su un dataset con **biopsia** e **tutti i colori di pelle** scendono a **0,56–0,67**, e vanno peggio sulle **pelli scure**. Il divario si chiude solo aggiungendo **dati diversi**.

## Il dataset DDI (Diverse Dermatology Images)
- **656 immagini** cliniche (foto con smartphone dell'ambulatorio), Stanford 2010–2020.
- **Tutte con biopsia**: è il primo dataset pubblico con tumori **confermati istologicamente** su pelli scure.
- Fototipo stabilito da due dermatologi usando la cartella della visita.
- **Pazienti abbinati:** per ogni lesione di fototipo V–VI, una lesione con la stessa diagnosi in un paziente di fototipo I–II, stesso sesso, età simile, stesso periodo.

| Fototipo | Immagini | Benigne | Maligne |
|----------|----------|---------|---------|
| I–II | 208 | 159 | 49 |
| III–IV | 241 | 167 | 74 |
| V–VI | 207 | 159 | 48 |

- Contiene anche **malattie rare** (sarcoma di Kaposi, micosi fungoide…).

## Cosa hanno fatto
Hanno testato **tre modelli** sul compito benigno/maligno:
- **ModelDerm** (API commerciale, foto cliniche di pazienti bianchi e asiatici);
- **DeepDerm** (Inception-v3, ricostruito con i dati e il metodo di Esteva 2017);
- **HAM10000** (stessa rete addestrata solo su HAM10000, dermoscopiche).
E hanno confrontato con **tre dermatologi** che guardano solo la foto.

## Risultati
**1. Calo generale.**

| Modello | AUC dichiarata | AUC su DDI |
|---------|----------------|------------|
| ModelDerm | 0,93–0,94 | 0,65 |
| DeepDerm | 0,88 | 0,56 |
| HAM10000 | 0,92 | 0,67 |

**2. Peggio sulle pelli scure** (AUC I–II contro V–VI): ModelDerm 0,64 → 0,55; DeepDerm 0,61 → 0,50; HAM10000 0,72 → 0,57.
- **Sensibilità** per i tumori: DeepDerm 0,69 su pelli chiare contro **0,23** su pelli scure; ModelDerm 0,41 contro 0,12.
- Il modello HAM10000 ha sensibilità bassa ovunque, anche se sul suo test set era 0,68.

**3. Le malattie rare peggiorano ancora.** Tolte le malattie rare, le AUC salgono (0,64–0,74), ma restano lontane da quelle dichiarate.

**4. I metodi "per l'equità" non bastano.** Tre tecniche di addestramento robusto (GroupDRO, CORAL, CDANN) **non** riducono il divario.

**5. I dati sì.** Riaddestrando (fine-tuning) DeepDerm e HAM10000 su una parte di DDI il divario **si chiude**: HAM10000 arriva a 0,77 su I–II e 0,78 su V–VI. Riaddestrando solo su pelli chiare il divario **resta**.

**6. Anche i dermatologi sbagliano di più sulle pelli scure.** Sensibilità delle etichette dei dermatologi: 0,72 su I–II contro 0,59 su V–VI. Problema serio, perché molti dataset sono etichettati proprio così, guardando la foto.

**Bonus:** gli artefatti (righelli, segni) **non** spiegano il calo sulle pelli scure.

## Messaggi chiave per la tesi
1. Le AUC pubblicate **non valgono** fuori dalla distribuzione di addestramento.
2. Il bias per colore della pelle è **reale e misurabile**, e si corregge con **dati diversi**, non con trucchi di addestramento.
3. Le etichette "a vista" dei dermatologi hanno più errori su pelli scure e malattie rare: la **biopsia** resta lo standard.
4. Il modello addestrato su HAM10000 (etichette con biopsia) è il migliore dei tre su DDI, ma ha sensibilità molto bassa: HAM10000 da solo **non basta**.

## Limiti
- Dataset piccolo (656 immagini): per test e fine-tuning, non per addestrare da zero.
- Arricchito di lesioni **dubbie** (quelle che il medico ha deciso di biopsiare).
- Solo foto cliniche, non dermoscopiche.
- Accesso su richiesta.

## Cosa porto in Neo Helper
- **DDI come test set esterno** (RQ3 della roadmap): benigno/maligno per fototipo, con sensibilità a specificità fissata.
- Attenzione al **domain shift**: un modello dermoscopico (HAM10000) su foto cliniche va male. L'agente deve sapere **che tipo di immagine** ha ricevuto e rifiutare quelle non adatte.
- Riportare sempre i risultati **separati per fototipo** e dichiarare il limite.
- Esperimento possibile: fine-tuning di PanDerm su una parte di DDI per vedere se il divario si chiude anche con un foundation model.
