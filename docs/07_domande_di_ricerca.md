# 07 — Domande di ricerca e contributo originale (issue #10, M1.10)

> **Stato: proposta del 2026-11-09, da confermare.** Scritta alla fine della revisione della letteratura (pacchetti 1–4). Sostituisce la bozza RQ1–RQ4 di [00_roadmap.md](00_roadmap.md).
> Ogni domanda indica: perché è aperta (fonti), ipotesi, dati, metriche e milestone in cui si risponde.

## Titolo di lavoro (proposta)
**"Neo Helper: un assistente agentico, spiegabile e capace di dire 'non so' per la diagnosi dermoscopica — foundation model, incertezza garantita e orchestrazione tramite Model Context Protocol"**

## Il problema in tre righe
I modelli di AI per le lesioni pigmentate sono accurati in laboratorio, ma:
- **crollano fuori dal laboratorio**: altri centri, lesioni mai viste, pelli scure (Combalia 2022, DDI 2022, Anriot 2026);
- **non sanno dire "non so"**: chiamano "maligna" quasi metà delle lesioni sconosciute;
- **spiegano poco** nel linguaggio del dermatologo (Chanda 2024).

Gli agenti con LLM promettono di unire più strumenti, ma di solito non hanno:
- controllo umano;
- gestione degli errori;
- garanzie di sicurezza (Vatsal 2026).

Il sistema più vicino, DermAgent (2026), lavora senza un classificatore addestrato e senza un "non so" garantito.

---

## RQ1 — Vedere: quanto vale un foundation model dermatologico, e quanto costa farne a meno?
**Domanda.** Su HAM10000 e su test esterni:
- quanto rende **PanDerm congelato con una testa lineare** rispetto a un backbone generico (**DINOv2**, ImageNet) e a **Derm Foundation**?
- **quanto si perde** passando a un backbone con licenza libera?

- **Perché è aperta:**
  - PanDerm è il migliore nei benchmark (Yan 2025), ma in condizioni realistiche scende al livello di un dermatologo di media esperienza (Anriot 2026);
  - la sua licenza (CC BY-NC-ND) blocca ogni uso fuori dalla ricerca.
- **Ipotesi:**
  - H1a: PanDerm batte DINOv2 e ImageNet sul test interno;
  - H1b: il vantaggio **si riduce** sui test esterni;
  - H1c: tutti i modelli perdono di più su BCN20000 e DDI che su PH2 e Derm7pt.
- **Dati:**
  - training su HAM10000, divisione per `lesion_id`;
  - test esterni: BCN20000 (da Figshare), DDI, PAD-UFES-20, **HIBA** (Argentina), PH2, Derm7pt.
- **Metriche:**
  - accuratezza bilanciata a 7 classi;
  - AUC e **specificità a sensibilità 90% e 95%** per il punteggio di malignità;
  - **pAUC sopra l'80% di sensibilità**;
  - calo tra test interno ed esterno;
  - tutto con intervalli di confidenza (bootstrap).
- **Milestone:** M2 (dati), M3 (modelli).

## RQ2 — Dubitare: il sistema sa dire "non so" quando serve, per tutti?
**Domanda.** Calibrazione, **insiemi conformal** e un controllo fuori distribuzione permettono a Neo Helper di astenersi in modo affidabile?
- su **lesioni di classi mai viste**;
- su **centri nuovi**;
- su **fototipi diversi**.

E quanti casi in più manda allo specialista per farlo?

- **Perché è aperta:**
  - sulle lesioni mai viste i migliori algoritmi del 2019 ne riconoscono il 6%, contro il 26% dei dermatologi (Combalia 2022);
  - un'AI sbagliata trascina i medici (Tschandl 2020, Krakowski 2024);
  - la garanzia conformal vale solo se i dati nuovi assomigliano a quelli di calibrazione (Angelopoulos e Bates 2021);
  - DermAgent usa soglie di confidenza senza garanzia.
- **Ipotesi:**
  - H2a: con gli insiemi conformal, la quota di lesioni sconosciute classificate con sicurezza come "maligne" scende molto rispetto alla sola softmax;
  - H2b: la copertura garantita **si rompe** sui test esterni e sui fototipi V–VI, e la calibrazione per gruppo la recupera solo in parte.
- **Dati:**
  - lesioni "OOD/sconosciute" del test di BCN20000 (se le etichette sono disponibili ⚠️) e classi assenti da HAM10000 in DDI e PAD-UFES-20;
  - fototipi da DDI.
- **Metriche:**
  - errore di calibrazione (ECE);
  - **copertura** e dimensione degli insiemi, per classe, per centro e per fototipo;
  - quota di lesioni sconosciute riconosciute come "non so";
  - **tumori mancati** ("lethal miss");
  - casi inviati allo specialista.
- **Milestone:** M3 (M3.3, M3.5).

## RQ3 — Spiegare: le spiegazioni sono fedeli al modello e parlano la lingua del dermatologo?
**Domanda.** Le spiegazioni di Neo Helper sono **fedeli** al modello e **concordano** con ciò che indicano i dermatologi? Le spiegazioni sono:
- i **criteri dermoscopici** (MONET o un piccolo concept bottleneck);
- le **heatmap**;
- i **casi simili** (CBIR).

- **Perché è aperta:**
  - molte heatmap non superano i test di sanità (Adebayo 2018);
  - MONET non è mai stato valutato sui criteri dermoscopici (Kim 2024);
  - le spiegazioni "come un dermatologo" aumentano la fiducia ma non l'accuratezza, e spingono a seguire l'AI anche quando sbaglia (Chanda 2024).
- **Ipotesi:**
  - H3a: MONET da solo riconosce male i criteri dermoscopici; un concept bottleneck allenato sugli embedding di PanDerm fa meglio;
  - H3b: Grad-CAM supera i test di sanità, ma si sovrappone solo in parte alle zone indicate dagli esperti;
  - H3c: 16 casi simili danno un'accuratezza vicina a quella del classificatore (come in Tschandl 2019).
- **Dati:**
  - **annotazioni localizzate di Chanda 2024** su HAM10000 (Figshare, CC BY 4.0);
  - criteri della 7-point checklist di Derm7pt.
- **Metriche:**
  - AUC per criterio;
  - correlazione delle mappe dopo la randomizzazione dei pesi;
  - sovrapposizione (Dice) tra mappe e zone degli esperti;
  - accuratezza dei casi simili con k = 16.
- **Milestone:** M3 (M3.4).

## RQ4 — Coordinare: un agente con tool MCP rende il report migliore senza inventare, e il multi-agente vale il suo costo?
**Domanda.** Un LLM che orchestra i tool via **MCP**, con un **critico a regole**, produce report più completi e **tracciabili** di una pipeline fissa, senza numeri inventati? E l'architettura multi-agente (v3) migliora abbastanza rispetto all'agente singolo (v2) da giustificare token e tempo in più?

- **Perché è aperta:**
  - i sistemi multi-agente costano circa 15 volte i token di una chat e servono solo per compiti parallelizzabili (Anthropic 2025);
  - in medicina mancano quasi ovunque controllo umano, gestione degli errori e risoluzione dei conflitti (Vatsal 2026);
  - DermAgent usa un modello chiuso (GPT-4o) e non misura i costi.
- **Ipotesi:**
  - H4a: con la regola "i numeri solo dai tool" e la catena di prove, i numeri inventati sono zero;
  - H4b: il critico a regole intercetta la maggior parte dei conflitti e degli artefatti inseriti apposta nei casi di prova;
  - H4c: v3 migliora poco rispetto a v2 a un costo molto più alto.
- **Dati:**
  - casi di prova dai test esterni;
  - **casi "trappola"**: immagini con penna o bordo nero, lesioni sconosciute, conflitti tra modelli, metadati sbagliati (come in Bhagwat 2026).
- **Metriche:**
  - quota di affermazioni del report riconducibili a un tool;
  - numeri inventati;
  - conflitti intercettati;
  - qualità del report con una griglia (LLM giudice verificato su un campione di medici);
  - token, tempo, costo per caso: v0 contro v2 contro v3.
  
  Se possibile, anche un **LLM locale o open** contro un LLM via API, per la privacy.
- **Milestone:** M4.

## RQ5 (facoltativa) — Aiutare: Neo Helper migliora le decisioni dei medici non specialisti?
Solo se l'ospedale di contatto lo rende possibile, con approvazione del comitato etico.

- **Domanda:** in un piccolo studio con medici non specialisti, prima senza e poi con Neo Helper, cambiano sensibilità e specificità? E quanto si seguono i suoi consigli **quando sbaglia**?
- **Perché:** i non dermatologi sono quelli che guadagnano di più dall'AI (Krakowski 2024), e l'effetto delle spiegazioni sui medici è poco studiato.
- **Milestone:** dopo M5, se fattibile.

---

## Il contributo originale (rispetto alla letteratura e a DermAgent)
1. **Un "non so" con una garanzia**, misurata anche dove si rompe: classi sconosciute, centri nuovi, fototipi. Entra nel percorso dell'agente: i casi incerti passano dal critico e finiscono con la raccomandazione di valutazione specialistica. DermAgent usa soglie senza garanzia (RQ2).
2. **Spiegazioni nella lingua del dermatologo, verificate** su annotazioni di esperti localizzate e con i test di sanità (RQ3).
3. **Una valutazione onesta e ampia:**
   - test esterni multipli (BCN20000, DDI, HIBA, PAD-UFES-20, PH2, Derm7pt);
   - metriche cliniche (specificità ad alta sensibilità, pAUC, tumori mancati);
   - risultati per fototipo e per centro;
   - rendiconto con CLEAR Derm (RQ1, RQ2).
4. **Un confronto misurato tra architetture agentiche** (pipeline, agente singolo, multi-agente) con costi e sicurezza, e uno strato di tool **MCP aperto** e riutilizzabile (RQ4).
5. **Trasparenza su licenze e regole:**
   - quanto costa, in prestazioni, un backbone libero (RQ1);
   - cosa servirebbe per un prodotto (MDR, AI Act).
   
   Codice aperto (MIT), con le licenze di dati e modelli documentate.

## Cosa NON fa la tesi
- Non è un dispositivo medico e non dà diagnosi ai pazienti.
- Niente raccolta di dati di pazienti, salvo lo studio facoltativo RQ5 con l'ospedale.
- Le foto cliniche da smartphone (SLICE-3D, PAD-UFES-20 clinico) sono un'**estensione** (M6), non il cuore della tesi.
- Niente ensemble "da gara": la priorità è l'affidabilità, non l'ultimo decimale.

## Cosa cambia rispetto alla bozza iniziale
| Bozza (ottobre 2026) | Proposta (novembre 2026) | Perché |
|---|---|---|
| RQ1 modelli open contro stato dell'arte | **RQ1** PanDerm contro backbone liberi, con test esterni e metriche cliniche | Licenze (§1.2 delle scelte); calo fuori dal laboratorio (Combalia, Anriot) |
| RQ2 il multi-agente migliora affidabilità e utilità | Divisa in **RQ2** (il "non so"), **RQ3** (le spiegazioni), **RQ4** (gli agenti e i costi) | Sono tre problemi diversi con metriche diverse |
| RQ3 pelli diverse e smartphone | Pelli diverse **dentro** RQ1 e RQ2; lo smartphone diventa un'estensione | DDI e HIBA disponibili subito; lo smartphone è un altro problema (modalità) |
| RQ4 rischi dell'LLM | Dentro **RQ4** con metriche precise (numeri inventati, conflitti intercettati) | Bhagwat 2026, Vatsal 2026 |
| — | **RQ5** facoltativa, studio con medici | Krakowski 2024, Chanda 2024 |
