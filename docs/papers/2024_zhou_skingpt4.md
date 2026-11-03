# Zhou et al., 2024 — SkinGPT-4: un LLM multimodale per la diagnosi dermatologica

- **Rivista:** *Nature Communications* 15(1):5649 (2024) · [DOI 10.1038/s41467-024-50043-3](https://doi.org/10.1038/s41467-024-50043-3) · PMID 38969632 · PMC11226626
- **Gruppo:** KAUST (Arabia Saudita) con ospedali di Pechino
- **Testo letto:** **completo** (PMC), senza materiale supplementare.

## In una frase
Un modello che **guarda la foto e risponde a parole**: descrive la lesione, propone una diagnosi e dei trattamenti, e si può interrogare in una conversazione. Ma la valutazione è **debole** e non va presa come prova di accuratezza.

## Cosa hanno fatto
- **Architettura** (stile MiniGPT-4):
  - un encoder visivo **ViT** con **Q-Former** (da BLIP-2), congelati;
  - un piccolo **strato lineare di allineamento**, l'unica parte addestrata;
  - un LLM **Llama-2-13b-chat**, congelato.
- **Dati:** **52.929 immagini** in totale.
  - Passo 1 — imparare i **concetti clinici**: SKINCON, cioè 3.230 immagini di Fitzpatrick17k e 656 di DDI annotate con **48 concetti** (papula, placca, crosta, eritema…).
  - Passo 2 — imparare la **diagnosi**: DermNet (18.856 immagini in 15 gruppi) più 30.187 coppie immagine–nota del medico da un dataset interno.
- **Valutazione:** **150 casi reali**. Cinque dermatologi vedono le risposte del modello e indicano quanto sono d'accordo.

## Risultati
- Diagnosi giudicate "corrette o pertinenti": **80,6%** (75,0% "molto d'accordo" + 5,6% "d'accordo").
- Utile per il medico 87,5%; informativa sulle cause 82,5%; utile sui trattamenti 85,6%.
- **Coerenza:** stessa immagine data 10 volte → stessa diagnosi nel 93,7% dei casi (45 immagini).
- Esperimento di ablazione: con solo il passo 1 il modello descrive bene ma sbaglia la diagnosi; con solo il passo 2 diagnostica senza descrivere. Servono entrambi.
- Il modello può girare **in locale** (circa 30 GB di memoria GPU o RAM): pensato per la privacy.

## Lettura critica
- **Non è una misura di accuratezza:** i dermatologi danno un giudizio di accordo dopo aver visto la risposta, **sapendo** che viene da un LLM. Mancano sensibilità e specificità, un test set indipendente e un confronto con un classificatore.
- Le 15 classi sono **molto larghe** (per esempio "melanoma skin cancer" include nevi e nei).
- Molte etichette **senza biopsia**: le diagnosi semplici non sono confermate istologicamente.
- Gli autori riconoscono: **allucinazioni**, foto da smartphone molto variabili, pochissimi fototipi V–VI nei dati, nessuna domanda di approfondimento al paziente come farebbe un medico.
- È pensato anche per **l'autodiagnosi** dei pazienti: lo scenario più rischioso secondo CLEAR Derm (§4).

## Messaggi chiave per la tesi
1. Gli LLM multimodali sono bravissimi a **descrivere e spiegare**, molto meno a **classificare** in modo misurabile.
2. Una buona idea tecnica: insegnare prima i **concetti clinici** e poi la diagnosi. Ricorda MONET.
3. Esempio utile di cosa **non** fare nella valutazione: giudizi di gradimento al posto di metriche diagnostiche.

## Cosa porto in Neo Helper
- Conferma la scelta dell'architettura: **l'LLM orchestra e scrive il report**, i numeri vengono dal classificatore di visione tramite tool MCP.
- I **48 concetti di SKINCON** possono diventare il vocabolario del report e dei tool "concetti".
- Testare la **coerenza** del report (stessa immagine → stesso testo?) come metrica dell'agente.
- Il report deve sempre dichiarare da quale tool vengono le probabilità, per evitare che l'LLM "inventi" una diagnosi.
