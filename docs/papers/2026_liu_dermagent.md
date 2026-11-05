# Liu et al., 2026 — DermAgent: un agente dermatologico che usa strumenti e si autocorregge

- **Tipo:** preprint · [arXiv 2605.14403](https://arxiv.org/abs/2605.14403) (maggio 2026)
- **Gruppo:** Monash University (AIM for Health Lab: Siyuan Yan, Zongyuan Ge, gli stessi di PanDerm) e University College London
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF. I numeri sono da ricontrollare ⚠️. Preprint non ancora revisionato.

## In una frase
È il lavoro **più vicino a Neo Helper**: un LLM orchestra modelli dermatologici specializzati e ricerche in archivi di casi e linee guida, mentre un **critico** controlla le contraddizioni e fa ripetere i passaggi deboli.

## Come funziona: ciclo Pianifica → Esegui → Rifletti
- **Controller:** GPT-4o pianifica quali strumenti chiamare.
- **7 strumenti:**
  - **PanDerm/DermLIP:** classificazione zero-shot con punteggi di confidenza;
  - **MAKE:** annotazione dei **concetti dermoscopici** (reticolo, strie…), simile a MONET;
  - **DermoGPT:** modello visione-linguaggio dermatologico per descrivere la lesione;
  - **Qwen3-VL:** modello visione-linguaggio generalista;
  - **Case RAG:** ricerca di **casi simili** in 413.210 casi diagnosticati di Derm1M (è un CBIR);
  - **Guideline RAG:** ricerca in 3.199 brani da DermNet e Mayo Clinic, con ricerca ibrida e riordinamento;
  - **ontologia** delle malattie della pelle.
- **Critico deterministico**, con regole e non un LLM. Tre controlli:
  - **confidenza** bassa (per esempio PanDerm sotto una soglia);
  - **copertura**: sono stati chiamati gli strumenti obbligatori?;
  - **conflitto**: classificatore e casi simili danno diagnosi diverse?
  
  Se trova un problema, rimanda al controller con un'indicazione, fino a un massimo di tentativi.
- **Sintesi finale** con una **catena di prove tracciabile**: ogni affermazione rimanda allo strumento che l'ha prodotta.

## Risultati (campioni piccoli)
| Compito | Dataset | DermAgent | Miglior confronto |
|---------|---------|-----------|-------------------|
| Classificazione zero-shot | HAM10000 (642 img, 7 classi) | 61,8% | MedAgent-Pro 57,6% |
| Classificazione fine | SNU (500 img, 134 classi) | 32,6% | GPT-4o 15,0% |
| Concetti dermoscopici | Derm7pt (100 img) | F1 65,1% | DermoGPT-RL 56,9% |
| Concetti clinici | SkinCon (100 img) | F1 33,0% | GPT-4o 29,6% |
| Descrizione clinica | SkinCAP (100 img) | ROUGE-L 19,5% | GPT-4o 16,3% |

- **Ablazione:** il **critico** dà il contributo maggiore. Tra gli strumenti, la ricerca di **casi simili** è il più importante, poi le linee guida.
- **Esempio qualitativo:** un granuloma anulare. All'inizio il modello descrittivo e il classificatore dicono "eczema", mentre i casi simili dicono "granuloma". Il critico rileva il conflitto, l'agente riguarda l'immagine e corregge.

## Limiti
- Preprint. Valutazione su **poche centinaia di immagini**, con campionamento e sovracampionamento delle classi rare.
- **61,8% su HAM10000 è basso** rispetto a un classificatore addestrato (oltre l'80%). Il lavoro misura l'agente **zero-shot**, non con un classificatore addestrato sui 7 tipi.
- Il controller è un **modello commerciale chiuso** (GPT-4o). I dati del paziente escono dall'ospedale.
- Non c'è valutazione con medici, né per fototipo.
- Licenze: PanDerm e i modelli Monash sono **non commerciali** (vedi §1.2 del documento delle scelte).

## Messaggi chiave per la tesi
1. Conferma l'**architettura** che abbiamo scelto: LLM che orchestra, modelli visivi che misurano, ricerca di casi simili, agente di controllo. Questo rende la proposta di Neo Helper **credibile**.
2. Ci obbliga a chiarire il **contributo originale** rispetto a DermAgent. Possibili differenze:
   - **classificatore addestrato e calibrato** con conformal e "non so", invece dello zero-shot;
   - **valutazione per fototipo** e su test esterni con biopsia (DDI);
   - **criteri della 7-point** collegati alle annotazioni di Chanda 2024;
   - **controller locale o open source** per la privacy, con MCP standard;
   - confronto **v2 contro v3** (agente singolo contro multi-agente) con i costi;
   - interfaccia e studio con **medici non specialisti**.
3. Il **critico a regole** è una buona idea, semplice e verificabile: niente LLM che giudica un altro LLM.

## Cosa porto in Neo Helper
- Adottare il **critico deterministico** per l'agente Critic/Safety (v3), con controlli di qualità, copertura, conflitto (classificatore contro casi simili contro concetti) e incertezza (insieme conformal).
- **Catena di prove** nel report: ogni frase cita il tool che l'ha prodotta.
- Usare DermAgent come **baseline di confronto** nella discussione. Non è un esperimento, se il codice non è pubblico ⚠️ da verificare.
- Aggiornare la §9 (gap) dello stato dell'arte e la issue M1.10 (domande di ricerca) alla luce di questo lavoro.
