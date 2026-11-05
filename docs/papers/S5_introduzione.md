# §5 — Introduzione: spiegare, dire "non so", collaborare con il medico

> Issue #6 (M1.6) · Fonti: PubMed, alphaXiv. Ogni scheda riporta DOI o link e dice cosa è stato letto: testo completo, oppure sintesi strutturata di alphaXiv.

Le sezioni precedenti chiedevano: **quanto è brava** la rete, e **su chi**? Questa sezione chiede: **come deve parlare al medico**, perché il medico decida meglio e non peggio? Le risposte sono di tre tipi.

**1. Spiegare dove guarda la rete: le mappe di calore.**
- **Grad-CAM** (Selvaraju 2017) colora le zone che hanno spinto la rete verso una classe. Funziona su quasi ogni rete.
- **Adebayo 2018** mostra che molte mappe "belle" non dipendono da ciò che la rete ha imparato: restano uguali anche con pesi casuali.
  - Grad-CAM supera questi test, Guided Grad-CAM no.
  - E comunque una mappa dice **dove**, non **perché**.

**2. Spiegare con le parole della clinica: concetti e casi simili.**
- I **concept bottleneck** (Koh 2020) fanno passare la decisione da concetti leggibili e correggibili dal medico. Servono però annotazioni dei concetti; MONET (§3) le genera in automatico.
- **Chanda 2024** porta i criteri dermoscopici localizzati su HAM10000, con 116 medici:
  - le spiegazioni aumentano **sicurezza** (+12%) e **fiducia** (+18%);
  - ma **non** l'accuratezza rispetto all'AI senza spiegazioni;
  - e fanno seguire un po' di più l'AI anche quando sbaglia.
- **Tschandl 2019 (CBIR):** mostrare le 16 immagini più simili, con la loro diagnosi, è accurato quanto le probabilità della rete. Funziona anche su classi mai viste.

**3. Dire "non so" in modo affidabile.**
- La **conformal prediction** (Angelopoulos e Bates 2021) trasforma le probabilità in un **insieme di diagnosi** che contiene quella vera con una probabilità garantita, per esempio il 95%.
- Un insieme grande è un "non sono sicuro" con un criterio preciso. Si può calibrare per classe o per sottogruppo.

**Cosa dice la clinica sulla collaborazione.**
- La meta-analisi di **Krakowski 2024** (10 studi, 67.700 valutazioni): con l'AI i medici passano da 74,8% a 81,1% di sensibilità e da 81,5% a 86,1% di specificità.
- Guadagnano di più i **non dermatologi**.
- Quasi nessuno studio ha testato le spiegazioni sui medici. Quando l'AI sbaglia, i medici la seguono.

**Il filo conduttore per Neo Helper:**
- nel report per il medico: **probabilità + insieme conformal + criteri dermoscopici + casi simili**. La heatmap resta soprattutto uno strumento di controllo per gli sviluppatori;
- verificare le heatmap con i **test di sanità** prima di usarle;
- usare le annotazioni di **Chanda 2024** su HAM10000 per validare i concetti (MONET) e per un piccolo concept bottleneck;
- nella valutazione con utenti misurare anche **quanto i medici seguono l'AI quando sbaglia**;
- pubblico principale: **medici non specialisti**.

| Anno | Lavoro | Tipo | Messaggio |
|------|--------|------|-----------|
| 2017 | Selvaraju, Grad-CAM (ICCV) | metodo | Heatmap per qualsiasi CNN, senza riaddestrare |
| 2018 | Adebayo (NeurIPS) | metodo critico | Molte heatmap non superano i test di sanità; Grad-CAM sì |
| 2019 | Tschandl, CBIR (*Br J Dermatol*) | dermoscopia | 16 casi simili ≈ softmax; aiuta su classi nuove |
| 2020 | Koh, Concept Bottleneck (ICML) | metodo | Concetti leggibili e correggibili, accuratezza simile |
| 2021 | Angelopoulos & Bates (tutorial) | metodo | Insiemi di diagnosi con copertura garantita |
| 2024 | Chanda (*Nat Commun*) | dermoscopia + 116 medici | Più fiducia e sicurezza, non più accuratezza |
| 2024 | Krakowski (*npj Digit Med*) | meta-analisi | L'AI aiuta tutti, soprattutto i non dermatologi |

Collegamenti: **Tschandl 2020** (§2) ha già mostrato che la forma dell'output conta e che un'AI difettosa trascina i medici. **MONET** (§3) è il generatore di concetti.

**Da leggere in seguito:** calibrazione e incertezza in dermatologia (per esempio Mehrtash 2020 ⚠️, studi di conformal su ISIC ⚠️); TCAV (Kim 2018) ⚠️.
