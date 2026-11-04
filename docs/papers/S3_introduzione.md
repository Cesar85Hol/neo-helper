# §3 — Introduzione: foundation model e LLM multimodali

> Issue #4 (M1.4) · Fonti: PubMed, alphaXiv, repository e model card ufficiali. Ogni scheda riporta DOI e se è stato letto il testo completo o solo l'abstract.

Dopo il 2020 cambia il modo di costruire le reti. Non si addestra più una rete da zero per ogni compito: si parte da un **foundation model**, una rete grande pre-addestrata su milioni di immagini (spesso senza etichette), e la si adatta con pochi esempi. In parallelo arrivano gli **LLM multimodali**, che guardano un'immagine e rispondono a parole.

Questa sezione racconta tre filoni.

**Filone 1 — Immagini e parole (MONET, 2024).**
- **MONET** impara dalla letteratura medica a collegare immagini e **concetti clinici** ("eritema", "crosta"). Serve a spiegare i modelli e a controllare i dataset.

**Filone 2 — Il foundation model della dermatologia (PanDerm, 2025; Derm Foundation).**
- **PanDerm** è pre-addestrato su 2,1 milioni di immagini di 4 tipi (cliniche, dermoscopiche, total body, istologiche) e vince su 28 compiti, spesso con il 10% delle etichette. Aiuta i medici, soprattutto i meno esperti.
- **Anriot 2026** lo mette alla prova in condizioni realistiche: batte i medici giovani, pareggia quelli di media esperienza, **perde contro gli esperti**.
- **Derm Foundation** (Google) è un modello di embedding per foto cliniche, senza un paper dedicato (vedi tabella).

**Filone 3 — Gli LLM che guardano le immagini (SkinGPT-4, 2024; LLM generalisti).**
- **SkinGPT-4** descrive la lesione e dialoga con l'utente, ma la sua valutazione è un giudizio di gradimento, non una misura di accuratezza.
- **Bhagwat 2026** mostra che ChatGPT e Gemini, su immagini con biopsia, danno **molti falsi positivi**, peggiorano sui fototipi scuri e si lasciano ingannare da un prompt sbagliato.

**Il filo conduttore per Neo Helper:**
- usare un **foundation model** come backbone (meno etichette, migliore generalizzazione);
- usare i **concetti clinici** per spiegare;
- lasciare all'**LLM** il ruolo di orchestratore e narratore, **mai** di classificatore;
- valutare sempre in condizioni **realistiche** e con lettori di diversa esperienza.

| Anno | Lavoro | Tipo | Dati | Messaggio |
|------|--------|------|------|-----------|
| 2024 | MONET (*Nat Med*) | immagine-testo (CLIP) | 105.550 immagini + testi dalla letteratura | Concetti clinici per spiegare e controllare |
| 2024 | SkinGPT-4 (*Nat Commun*) | LLM multimodale | 52.929 immagini | Dialoga e descrive; valutazione debole |
| 2025 | PanDerm (*Nat Med*) | foundation model visivo | 2,1 milioni di immagini, 4 modalità | Stato dell'arte su 28 compiti; aiuta i medici |
| 2026 | Anriot (*JAMA Dermatol*) | studio realistico | 1.117 casi, 652 medici | PanDerm < esperti oltre 10 anni |
| 2026 | Bhagwat (*Bioengineering*) | valutazione LLM generalisti | 656 immagini DDI | Molti falsi positivi; non per uso autonomo |

## Disponibilità dei pesi (verificata il 2026-11-03)

| Modello | Dove | Licenza / accesso | Uso in Neo Helper |
|---------|------|-------------------|-------------------|
| **PanDerm** (ViT-L/16), PanDerm_Base, DermLIP_PanDerm | GitHub SiyuanYan1/PanDerm (Google Drive, Hugging Face) | **CC-BY-NC-ND 4.0**, solo ricerca non commerciale | Backbone principale per la tesi |
| **MONET** | Hugging Face `chanwkim/monet` | Pubblici; repository **CC BY-NC-SA 4.0**, model card: "uso in produzione fuori ambito" (solo ricerca) | Tool "concetti", audit dei dataset |
| **Derm Foundation** (Google) | Hugging Face `google/derm-foundation` | **Gated**: accettare i termini Health AI Developer Foundations | Alternativa per foto cliniche |
| **SkinGPT-4** | Codice indicato nel paper | ⚠️ non verificato | Solo come confronto |

**Derm Foundation in breve** (dalla model card, non c'è un paper dedicato):
- rete **BiT ResNet101x3**, pre-addestrata in modo contrastivo su coppie immagine-testo e poi su dati clinici di **USA, Colombia e Australia**;
- input 448×448, output un **vettore di 6.144 numeri** (embedding): **non** fa diagnosi da sola;
- pensata per foto **cliniche**; può peggiorare su foto troppo chiare o scure e su popolazioni diverse da quelle di addestramento.
