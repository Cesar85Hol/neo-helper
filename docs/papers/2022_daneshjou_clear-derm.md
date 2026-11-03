# Daneshjou et al., 2022 — CLEAR Derm: la checklist per valutare l'AI dermatologica

- **Rivista:** *JAMA Dermatology* 158(1):90–96 (2022; online dicembre 2021) · [DOI 10.1001/jamadermatol.2021.4915](https://doi.org/10.1001/jamadermatol.2021.4915) · PMID 34851366 · PMC9845064
- **Autori:** i 19 membri del gruppo di lavoro AI dell'**International Skin Imaging Collaboration (ISIC)**
- **Testo letto:** **completo** (manoscritto in PMC). La tabella con la checklist numerata non è nel testo estratto: i numeri degli item sono ricostruiti dai titoli delle sezioni.

## In una frase
**25 punti** da controllare quando si sviluppa o si legge un lavoro di AI su immagini dermatologiche, divisi in quattro aree: **dati, tecnica, valutazione tecnica, applicazione**.

## Perché esiste
- Le linee guida generali (SPIRIT-AI, CONSORT-AI) riguardano i trial clinici, che arrivano **dopo**. Molte scelte importanti si fanno prima, durante lo sviluppo.
- La dermatologia ha problemi suoi: immagini **non standardizzate**, **colore della pelle**, etichette rumorose, dati non rappresentativi.
- Metodo: ricerca su PubMed (2008–2021), due giri di consenso tra 19 esperti, approvazione all'ISIC Annual Meeting del 2021.

## La checklist

### A. Dati (item 1–15)
- **1–6 — Immagini:** modalità (clinica, dermoscopica polarizzata o no), dispositivo, chi ha scattato, luce, distanza, calibrazione del colore. **Artefatti:** segni di penna, righelli, peli, tatuaggi. Pre-processing (normalizzazione del colore) e post-processing (ritagli, selezione manuale). Se si usano immagini pubbliche, dire **quali**.
- **7–9 — Metadati del paziente:** sede, età, sesso, etnia, **fototipo** e **come** è stato stabilito (scala usata, di persona o da foto). Se mancano, discutere il possibile bias.
- **10–12 — Divisione dei dati:** criteri di inclusione/esclusione; dimensione di training, validation e test; set **indipendenti** (niente stesso paziente in due set = **data leakage**). Preferire test set da **distribuzioni diverse** da quella di addestramento.
- **13–15 — Test e realtà clinica:** classi **fuori distribuzione** (diagnosi non viste in addestramento): sono nel test? Se no, spiegare cosa succede quando arrivano. Distribuzione delle classi per sottogruppi; come si è gestito lo squilibrio.

### B. Tecnica (item 16–20)
- **16–18 — Etichette:** per i tumori lo standard è l'**istologia** (che però ha anche lei disaccordi tra patologi). Altrimenti spiegare il metodo (follow-up, consenso). Usare ontologie standard (ICD-11, SNOMED-CT).
- **19 — Sviluppo dell'algoritmo:** descritto in modo **replicabile**, iperparametri compresi. Strumenti di interpretabilità (saliency map, CBIR) raccomandati, ricordando che il loro valore clinico non è ancora dimostrato.
- **20 — Valutabilità pubblica:** codice aperto o modello in container, o almeno un'interfaccia di test; valutare su **benchmark pubblici**.

### C. Valutazione tecnica (item 21–23)
- Metrica adatta al compito e allo scenario d'uso; attenzione alle malattie **rare** nello screening di popolazione.
- Risultati **stratificati** per dati demografici e artefatti.
- Confronto con **esperti** nel contesto d'uso **e** con lo standard di cura reale (di solito un singolo medico, non un panel di esperti). Confronto con algoritmi precedenti sui benchmark pubblici (per esempio ISIC).

### D. Applicazione (item 24–25)
- **24 — Caso d'uso:** chi usa il sistema (paziente, infermiere, medico di base, dermatologo), dove (casa, cure primarie, centro specialistico) e come (supporto alla decisione o autonomo).
- **25 — Impatto:** valutare il medico **con e senza** l'algoritmo; considerare i danni. Esempio degli autori: un 5% di falsi negativi per il melanoma pesa molto di più se lo strumento è **in mano al paziente** (falsa rassicurazione) che se c'è un medico che può correggerlo. Considerare le popolazioni vulnerabili.

## Messaggi chiave per la tesi
1. È la **griglia** con cui valutare la parte sperimentale della tesi e con cui leggere ogni paper.
2. Riassume tutta la §4: artefatti (Winkler), fototipo (Fitzpatrick17k, DDI), etichette con biopsia, test esterni.
3. Riprende Tschandl 2020: valutare l'AI **nelle mani dell'utente**.

## Cosa porto in Neo Helper
- **Usarla come checklist del capitolo "Valutazione"** della tesi: una tabella con i 25 item e dove ciascuno è trattato.
- Item che richiedono lavoro concreto:
  - split di HAM10000 **per lesione/paziente** (`lesion_id`) per evitare il leakage;
  - test esterni (DDI, PAD-UFES-20, ISIC 2019+);
  - risultati per fototipo e per presenza di artefatti;
  - comportamento sulle classi **fuori distribuzione** → l'agente deve poter dire "non so";
  - studio con utenti con e senza Neo Helper (Fase 7).
- Caso d'uso dichiarato: **supporto al medico**, non autodiagnosi del paziente.
