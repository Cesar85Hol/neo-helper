# 05 — Scelte di progetto e pipeline preliminare

> Versione del 2026-11-04, scritta dopo i Pacchetti di letteratura 1 e 2. Raccoglie le scelte fatte, il nodo della licenza del backbone, la pipeline, il ruolo di ISIC 2019 e lo spazio per nuovi dati e annotazioni manuali.

**Storyboard delle decisioni** (in inglese, continuano lo storyboard 1 di [S2](papers/S2_introduzione.md)):
- [Parte 2 — modelli e pipeline](figures/storyboard_02_models_pipeline.png)
- [Parte 3 — spiegabilità, incertezza, agenti e MCP](figures/storyboard_03_trust_agents.png)
- [Parte 4 — i blocchi di Neo Helper e il loro stato](figures/storyboard_04_building_blocks.png)

## 1. Registro delle scelte

### Confermate (2026-11-04)
| # | Scelta | Perché (fonte) |
|---|--------|----------------|
| C1 | **PanDerm come backbone** | Migliore su 28 compiti, buono con poche etichette (Yan 2025) |
| C2 | **L'LLM descrive e orchestra, non classifica** | SkinGPT-4 valutato solo con giudizi di gradimento; ChatGPT e Gemini con molti falsi positivi e sensibili al prompt (Zhou 2024, Bhagwat 2026) |
| C3 | **DDI come test esterno** | Biopsia per tutte le immagini, fototipi abbinati (Daneshjou 2022) |
| C4 | **Agente di controllo** (qualità e artefatti) | Segni di penna: specificità dall'84% al 46% (Winkler 2019) |
| C5 | **CLEAR Derm come griglia di valutazione** | Checklist ISIC di 25 punti (Daneshjou 2022) |

### Confermate anche queste (2026-11-04)
| # | Scelta | Perché | Alternativa scartata (per ora) |
|---|--------|--------|-------------|
| P1 | **HAM10000 come dataset iniziale** | 10.015 immagini dermoscopiche, 7 classi, oltre metà con istologia, campo `lesion_id`; è il dataset di Tschandl 2019/2020 e quindi confrontabile con la letteratura | ISIC 2019 (25k immagini, contiene HAM10000) in un secondo momento |
| P2 | **Compito: 7 classi + punteggio di malignità** derivato | Le probabilità multiclasse aiutano il medico (Tschandl 2020, PanDerm) | Solo benigno/maligno |
| P3 | **Soglia di malignità bassa** (circa 17–20%), da ricalibrare sui dati | Soglia scelta d'istinto dai medici e vicina all'ottimo (Tschandl 2020) | Soglia a specificità fissata |
| P4 | **Split per `lesion_id`** (70/15/15) | Evitare che la stessa lesione finisca sia nel training sia nel test (CLEAR Derm, item 10–12) | — |
| P5 | **PanDerm congelato + testa leggera** (*linear probe*) come **primo passo**; il fine-tuning è il **secondo esperimento**, non escluso (vedi §1.1) | Veloce, poche risorse, e i nuovi dati si aggiungono riaddestrando solo la testa (vedi §4) | — |
| P6 | **Baseline di confronto:** ResNet/ViT ImageNet, DINOv2 e Derm Foundation | Per misurare quanto aggiunge PanDerm e quanto si perde con un backbone a licenza libera (vedi §1.2) | — |
| P7 | **MONET per i concetti** (vedi §2) | Spiegare con le parole della clinica e controllare i dataset | Solo Grad-CAM |
| P8 | **Incertezza:** calibrazione + insiemi conformal + capacità di dire "non so" | Contro l'automation bias (Tschandl 2020) | — |
| P9 | **Test esterni:** DDI, PAD-UFES-20, PH2, Derm7pt; ISIC 2019 senza la parte HAM10000 ⚠️ | Generalizzazione e domain shift (Tschandl 2019, DDI) | — |
| P10 | **Uso dichiarato:** supporto al medico, non autodiagnosi | Rischio di falsa rassicurazione (CLEAR Derm, item 24–25) | — |

### 1.1 Backbone congelato o fine-tuning?
- **Congelato:** PanDerm viene usato così com'è, come "occhio" già addestrato. Ogni immagine diventa un vettore di numeri (*embedding*) e si addestra solo una piccola **testa** che da quel vettore ricava le 7 classi. I pesi di PanDerm (circa 300 milioni) **non cambiano**.
- **Fine-tuning:** si riaddestra anche PanDerm, tutto o in parte (ultimi blocchi, oppure LoRA), sulle nostre immagini.

| | Congelato (linear probe) | Fine-tuning |
|---|---|---|
| Costo | Minuti, anche su un portatile (gli embedding si calcolano una volta) | Ore su una GPU da data center; molto lento sul Mac |
| Rischio con 10.000 immagini | Basso | Overfitting, va controllato bene |
| Guadagno atteso | Già vicino allo stato dell'arte: secondo il paper di PanDerm, il linear probing è paragonabile al fine-tuning completo ⚠️ (tabella supplementare non letta) | Qualche punto in più, da misurare ⚠️ |
| Aggiungere nuovi dati | Si riaddestra solo la testa | Si ripete il fine-tuning |
| Licenza (vedi §1.2) | Si usa PanDerm senza modificarlo | Si crea un "materiale adattato": permesso solo per uso interno, non si può pubblicare |

**Piano:** prima il congelato (baseline), poi il **fine-tuning come esperimento** di confronto. Il confronto "congelato contro fine-tuning" è esso stesso un risultato della tesi.

### 1.2 La licenza di PanDerm, detta onestamente
Fonti lette il 2026-11-04: README di PanDerm ("CC-BY-NC-ND 4.0", "may only be used for non-commercial academic research purposes") e testo legale della licenza CC BY-NC-ND 4.0, sezione 2(a)(1). Non sono un avvocato: per un uso fuori dalla tesi serve un parere legale o il permesso degli autori.

**Cosa dice la licenza:**
- **NC (non commerciale):** niente uso "principalmente rivolto a un vantaggio commerciale".
- **ND (no derivati):** si possono **creare e usare** materiali adattati per scopi non commerciali, ma **non condividerli** con il pubblico (testo: *produce and reproduce, but not Share, Adapted Material*).
- Il README aggiunge un limite più stretto: **ricerca accademica**.

**Quindi:**

| Uso | Con PanDerm |
|-----|-------------|
| Esperimenti della tesi, congelato **o** con fine-tuning | ✅ Permesso |
| Pubblicare risultati, codice (MIT) e istruzioni per scaricare i pesi ufficiali | ✅ Permesso |
| Pubblicare i pesi di PanDerm **modificati** dal fine-tuning | ❌ Non permesso (ND) |
| Pubblicare la sola testa addestrata sugli embedding | ⚠️ Zona grigia: non è chiaro se conti come "derivato" |
| App o demo aperta al pubblico, uso clinico, prodotto | ❌ Non permesso (non è ricerca accademica; se commerciale anche NC) |

**Un vincolo che vale comunque:** anche HAM10000 e i dataset ISIC sono **CC-BY-NC**. Un Neo Helper commerciale sarebbe bloccato **dai dati**, non solo da PanDerm. Per un prodotto bisognerebbe cambiare dati **e** backbone. Un'eccezione utile (Pacchetto 4): **BCN20000** è pubblicato con licenza **CC BY 4.0** ⚠️ da verificare sul repository. E anche con dati e modelli liberi servirebbe la certificazione come dispositivo medico (MDR, almeno classe IIa) e il rispetto dell'AI Act: vedi [04_etica_regolatorio.md](04_etica_regolatorio.md).

**Tracce per non dover cambiare backbone:**
1. **Chiedere agli autori** (Monash University, gruppo di Siyuan Yan e Zongyuan Ge ⚠️) un permesso scritto per l'uso previsto. È una mail; per un progetto accademico capita spesso che dicano di sì.
2. **DermFM-Zero** (2026, stesso gruppo): costruito sopra PanDerm, immagine + testo, con scoperta automatica di concetti (simile a MONET). Il **repository GitHub** dice **CC BY-NC 4.0** con derivati permessi se non commerciali; la **model card su Hugging Face** dice invece **CC BY-NC-ND 4.0** e vieta di ridistribuire i checkpoint derivati. Le due fonti **si contraddicono**: va chiarito con gli autori. Attenzione anche al pre-training: include ISIC, BCN20000 e Fitzpatrick17k, quindi questi non vanno usati come test.
3. **Architettura con backbone intercambiabile:** il tool `embed_image` nasconde quale backbone c'è sotto. Si può cambiare senza toccare il resto.

**Backbone alternativi con licenze più aperte (verificate il 2026-11-04):**

| Backbone | Licenza | Pro | Contro |
|----------|---------|-----|--------|
| **DINOv2** (Meta) | Apache 2.0: uso commerciale, fine-tuning e ridistribuzione permessi | Libero; ottimo con il linear probe | Non specifico per la pelle: PanDerm lo supera nei benchmark del suo paper |
| **Derm Foundation** (Google) | Termini HAI-DEF: modifiche e ridistribuzione permesse con condizioni; uso clinico richiede autorizzazione regolatoria; uso commerciale non trattato esplicitamente ⚠️ | Specifico per la dermatologia | Pensato per foto **cliniche**; accesso con registrazione |
| **PanDerm** | CC-BY-NC-ND 4.0 | Il migliore nei benchmark | Solo ricerca accademica |

**Decisione (confermata il 2026-11-04):**
- **Per la tesi** si tiene **PanDerm** (uso permesso) e si confronta con **DINOv2** e **Derm Foundation** sugli stessi split.
- Il confronto risponde a una domanda utile: **quanto si perde** passando a un backbone con licenza libera?
- In parallelo, mail agli autori di PanDerm/DermFM-Zero per chiarire la licenza.
- Solo se il progetto diventa un'app pubblica o un prodotto si passa al backbone libero migliore.

## 2. Dove entra MONET: tradurre le immagini in parole

MONET era nelle schede ma non nel riassunto finale. Il suo posto è questo:

1. **Tool MCP `describe_concepts`**: per ogni immagine dà un punteggio a una lista di concetti clinici (per esempio i 48 di SKINCON: papula, placca, crosta, eritema, pigmentato, ulcera…). Il **Reporter** li usa per scrivere frasi come "presenza di crosta: alta; pigmentazione: alta". L'LLM racconta i numeri di MONET, non li inventa.
2. **Audit dei dati** prima del training: cercare in HAM10000 i concetti "inchiostro", "righello", "peli" e contare per classe dove si concentrano. Se i segni di penna sono soprattutto tra i melanomi, c'è rischio di scorciatoia (Winkler).
3. **Supporto all'agente di controllo**: gli stessi punteggi degli artefatti diventano avvisi ("immagine con segni chirurgici").
4. **Più avanti (opzionale):** un modello *concept bottleneck*, che prima prevede i concetti e poi la diagnosi, e quindi si spiega da solo.

**Due cautele:**
- MONET è validato su **immagini cliniche** con etichette vere (SkinCon su Fitzpatrick17k e DDI); sulle dermoscopiche ci sono solo esempi qualitativi e l'audit di ISIC. I criteri dermoscopici (reticolo, velo, strie) non sono stati valutati: va controllato su Derm7pt o su un campione annotato a mano (vedi §5). Licenza: repository CC BY-NC-SA 4.0, solo ricerca, come PanDerm.
- I concetti di SKINCON sono **clinici**, non i criteri **dermoscopici** (reticolo atipico, velo blu-biancastro…). Per questi servono il dataset Derm7pt e l'agente "Criteri".

**Divisione dei compiti tra i modelli:**

| Modello | Domanda a cui risponde |
|---------|------------------------|
| PanDerm + testa | "Che lesione è?" (probabilità sulle 7 classi) |
| MONET | "Che cosa si vede, a parole?" (concetti clinici e artefatti) |
| Grad-CAM / attention | "Dove guarda il modello?" |
| Indice di casi simili | "Quali casi già diagnosticati gli assomigliano?" (funzione secondaria) |
| LLM Reporter | "Come lo spiego al medico?" (solo testo, dai numeri sopra) |

## 3. Pipeline preliminare

### 3.1 Addestramento e valutazione (offline)

```
 Dataset (HAM10000, poi altri)
        │  registro dati: un file di metadati comune per ogni immagine (vedi §4.1)
        ▼
 [1] Audit dei dati ── MONET: artefatti per classe; duplicati; squilibrio
        ▼
 [2] Split per lesion_id (train / val / test interno)
        ▼
 [3] Pre-processing ── segmentazione e ritaglio sulla lesione
        ▼
 [4] Embedding PanDerm (congelato) ── calcolati UNA volta e salvati su disco
        ▼
 [5] Testa di classificazione (7 classi) ── addestramento in minuti
        ▼
 [6] Calibrazione (temperature scaling) + soglie conformal + soglia "non so"
        ▼
 [7] Valutazione
       ├─ test interno (HAM10000)
       ├─ test esterni (DDI, PAD-UFES-20, PH2, Derm7pt)
       ├─ per sottogruppo: fototipo, sede, età, sesso, artefatti
       └─ confronto con baseline (ImageNet, DINOv2)
        ▼
 [8] Model card + tabella CLEAR Derm
```

### 3.2 Uso su un nuovo caso (online, con agenti)

```
 Immagine del medico (+ metadati dichiarati)
        ▼
 Agente di controllo (Quality Gate)
   - tipo di immagine: dermoscopica o clinica? → se non adatta: rifiuto motivato
   - qualità: sfocata, luce, non è pelle
   - artefatti (MONET): penna, righello, peli → avviso
        ▼
 Segmentazione + ritaglio
        ▼
 Embedding PanDerm (una volta) ──┬── Testa → probabilità 7 classi + incertezza + insieme conformal
                                 ├── Indice casi simili (CBIR)
 MONET ──────────────────────────┴── concetti clinici a parole
 Grad-CAM ── mappa di dove guarda il modello
        ▼
 Critic / Safety ── incoerenze, incertezza alta, classe fuori distribuzione → "consigliata valutazione specialistica"
        ▼
 Reporter (LLM) ── report per il medico: probabilità, concetti, avvisi, limiti
                   I metadati dichiarati dall'utente sono segnalati come "non verificati".
```

Questa pipeline corrisponde alle versioni v0 → v3 di [03_architettura.md](03_architettura.md): prima i passi [1]–[8] in Python puro, poi gli stessi passi come tool MCP, poi gli agenti.

### 3.3 ISIC 2019: prima o dopo?
**Che cos'è:** il dataset della sfida ISIC 2019, con **25.331 immagini dermoscopiche** di training in **8 classi**: le 7 di HAM10000 più il **carcinoma squamocellulare** (SCC). Il test della sfida aveva una nona classe, "nessuna delle altre", per le diagnosi mai viste. Fonte: sito della challenge ISIC 2019. Unisce tre raccolte ⚠️ (composizione esatta da verificare nei paper di Codella e Combalia):
- **HAM10000** (Vienna e Queensland), cioè tutte le nostre immagini;
- **BCN20000** (Barcellona): immagini "difficili", con lesioni su unghie e mucose e molti **bordi neri** del dermatoscopio;
- **MSK** (New York).

**Aggiungerlo PRIMA (training subito su ISIC 2019)**
- ➕ 2,5 volte più immagini e **tre centri**: la rete vede più varietà fin dall'inizio.
- ➕ Una classe in più (SCC), utile clinicamente.
- ➖ **Si perde il test esterno "gratuito":** BCN20000 e MSK sono l'unico test esterno **dermoscopico grande** che abbiamo. Se entrano nel training, restano solo PH2 (200 immagini) e Derm7pt.
- ➖ **Risultati non confrontabili** con Tschandl 2019/2020 e con i benchmark di PanDerm, che usano HAM10000.
- ➖ **Più pulizia dei dati:** 7 contro 8 classi, duplicati con HAM10000, immagini di dimensioni diverse, e i **bordi neri di BCN** sono un artefatto che può diventare una scorciatoia (come la penna di Winkler).
- ➖ Più passaggi da spiegare insieme nella tesi, e più difficile capire **da dove** viene un miglioramento.

**Aggiungerlo DOPO (prima baseline su HAM10000)**
- ➕ Baseline **pulita e confrontabile** con la letteratura.
- ➕ BCN20000 + MSK diventano un **test esterno multicentrico**: misuriamo il domain shift tra centri, come Tschandl 2019.
- ➕ Poi l'aggiunta di ISIC 2019 al training diventa un **esperimento a sé** ("quanto aiutano i dati di altri centri?"), con la stessa procedura del §4.2.
- ➖ La prima versione del modello non conosce l'SCC: va dichiarato, e l'agente deve trattarlo come classe sconosciuta ("non so").
- ➖ Un passaggio in più nel calendario.

**Raccomandazione: DOPO.** Ordine proposto:
1. Training su HAM10000.
2. Test interno + test esterno su BCN20000/MSK + DDI, PH2, Derm7pt.
3. Training su ISIC 2019 completo (senza le immagini usate come test).
4. Confronto prima/dopo.

Dal punto di vista dei costi la differenza è piccola: con il backbone congelato anche 25.000 embedding si calcolano una volta sola. La vera differenza è **metodologica**.

## 4. Spazio aperto per nuovi dati (possibilità futura)

> **Stato:** solo un'idea, da discutere con l'ospedale di contatto. **Non è nel piano di lavoro.** La pipeline viene progettata in modo da renderla possibile (registro dati comune, metriche per sottogruppo), ma non si fa niente di più finché non c'è un dataset reale. Le istruzioni per chi annota sono in [annotazione/](annotazione/).

Esempio: arriva un dataset di **pazienti ispanici o latinoamericani**, con pelle intermedia (spesso fototipi III–V).

### 4.1 Perché la pipeline è pronta ad accoglierlo
1. **Registro dati comune.** Ogni immagine, da qualunque dataset, viene descritta con gli stessi campi:
   - `source`, `modality` (dermoscopica / clinica / smartphone), `diagnosis`, `label_source` (istologia / follow-up / consenso / singolo esperto);
   - `fitzpatrick` e **come** è stato stabilito (visita / foto), `ethnicity_self_reported` (campo separato), `country`;
   - `age`, `sex`, `site`, `artifacts` (penna, righello, peli…), `lesion_id`, `patient_id`.
   Un nuovo dataset è un nuovo "pezzo" da agganciare: basta un convertitore verso questo formato.
2. **Backbone congelato ed embedding salvati.** Aggiungere dati vuol dire calcolare gli embedding delle sole immagini nuove e riaddestrare la **testa**: minuti, non giorni.
3. **Metriche già divise per sottogruppo.** Il miglioramento si vede subito nei numeri per fototipo.

### 4.2 Procedura quando arriva il dataset
1. **Misurare prima di toccare.** Valutare il modello attuale sul nuovo dataset, per fototipo e per classe. Questo è il "prima".
2. **Dividere i nuovi dati** per paziente: una parte per l'addestramento, una parte **tenuta da parte** solo per il test.
3. **Riaddestrare la testa su vecchi + nuovi dati insieme**, con campionamento bilanciato per gruppo (fototipo × classe). Usare tutti i dati, non solo i nuovi, evita che il modello "dimentichi" quello che sapeva (*catastrophic forgetting*).
4. **Se non basta:** fine-tuning leggero del backbone (ultimi blocchi o LoRA). ⚠️ Attenzione alla licenza ND.
5. **Ricalibrare** probabilità e soglie conformal: possono essere diverse tra gruppi.
6. **Confrontare con il "prima":**
   - il divario sul nuovo gruppo si è ridotto?
   - **nessun peggioramento** sui test vecchi (test di non regressione)?
7. **Nuova versione del modello** con model card aggiornata (dati, risultati per gruppo, limiti).

### 4.3 Cosa dice la letteratura che ci aspetta
- **DDI:** il divario tra pelli chiare e scure si chiude solo aggiungendo **immagini diverse**; i trucchi di addestramento "per l'equità" non sono bastati.
- **Fitzpatrick17k:** la rete va meglio sui fototipi **vicini** a quelli visti. I fototipi intermedi (III–IV) sono un ponte utile verso entrambi gli estremi.
- **Attenzione:** etnia e fototipo **non** sono la stessa cosa. Le popolazioni ispaniche/latinoamericane coprono quasi tutta la scala. Vanno registrati entrambi, separatamente.
- **Nota:** DDI contiene già pazienti che si dichiarano ispanici o latinoamericani (selezionati a Stanford insieme a pazienti neri) e PAD-UFES-20 viene dal Brasile. Sono già un primo banco di prova per questo scenario.
- **Nuovo (verifica del 2026-11-09):** sull'archivio ISIC c'è il dataset **HIBA** dell'Hospital Italiano de Buenos Aires (2019–2022):
  - 1.616 immagini, di cui 1.270 dermoscopiche e 346 cliniche;
  - 623 pazienti argentini;
  - licenza **CC BY**.
  
  È un test esterno **latinoamericano e dermoscopico**, già pubblico e utilizzabile senza aspettare l'ospedale. Nel campione esaminato i fototipi sono però soprattutto II–III: misura il cambio di popolazione e di centro, non le pelli scure.
- **Altro rischio:** se il nuovo dataset è fatto di **foto cliniche** e non dermoscopiche, il problema principale diventa la modalità, non il colore della pelle. Il campo `modality` serve proprio a separare i due effetti.

## 5. L'annotazione manuale che aiuta di più

### 5.1 Dove la macchina fa fatica (dalla letteratura)
| Punto debole | Fonte |
|--------------|-------|
| Pelli scure e intermedie | Fitzpatrick17k, DDI, Bhagwat 2026 |
| Malattie rare o atipiche | DDI, Anriot 2026 |
| Artefatti (penna, righelli, peli) | Winkler 2019 |
| Cambio di modalità (dermoscopica ↔ clinica/smartphone) | Tschandl 2020 (telemedicina), DDI |
| Lesioni dubbie: cheratosi attiniche, carcinomi intraepiteliali, nevi atipici | Tschandl 2020 |
| Etichette rumorose date "a vista" | DDI, Fitzpatrick17k |
| Classi mai viste in addestramento | CLEAR Derm, item 13–15 |

### 5.2 Le annotazioni, in ordine di utilità

1. **Fonte della diagnosi** (`label_source`), *priorità massima, costo basso*.
   - Istologia per i tumori; follow-up dermoscopico (lesione stabile nel tempo) o consenso per le lesioni benigne non asportate.
   - Non serve "rifare" la diagnosi: serve **sapere quanto è affidabile** ogni etichetta. Così si possono pesare gli esempi e scegliere il test set solo tra le etichette istologiche.
2. **Fototipo stabilito alla visita**, *priorità massima*.
   - Scala di Fitzpatrick decisa **di persona o dalla cartella**, non dalla foto: DDI ha fatto così, con due dermatologi. Facoltativo: anche la scala Monk (10 toni), più fine. Etnia dichiarata in un campo separato.
   - Senza questo dato non si può misurare l'equità.
3. **Checklist degli artefatti**, *costo molto basso*.
   - Sì/no per: penna, righello, peli, bolle, bordo nero (vignettatura), sfocatura, riflessi.
   - Qualche secondo per immagine. Serve all'audit, ad addestrare l'agente di controllo e a verificare i concetti di MONET.
4. **Diagnosi differenziale + sicurezza dell'annotatore**, *costo basso*.
   - Prime 3 diagnosi e sicurezza da 1 a 5.
   - Dice **quanto è difficile** ogni caso. Si può confrontare con l'incertezza del modello.
5. **Doppia lettura su un sottoinsieme** (per esempio 10–20%).
   - Due annotatori indipendenti, poi accordo (kappa) e discussione dei disaccordi.
   - Misura il "rumore umano": serve a capire fino a dove ha senso spingere il modello.
6. **Criteri dermoscopici strutturati** (7-point checklist o ABCD, formato Derm7pt), *costo medio-alto*.
   - Alimenta l'agente "Criteri", dà spiegazioni dermoscopiche vere e permette di controllare MONET sulle dermoscopiche.
7. **Maschere di segmentazione** su un sottoinsieme, *costo alto*.
   - Servono a verificare il ritaglio e a controllare se la heatmap guarda la lesione o lo sfondo.

### 5.3 Quali immagini annotare per prime (*apprendimento attivo*)
Il tempo dell'esperto è la risorsa più cara. Conviene annotare prima le immagini dove il modello è **più in difficoltà**:
- **incertezza alta** (insieme conformal con 2 o più classi, probabilità vicine tra loro);
- **fototipi poco rappresentati** (IV–VI e intermedi del nuovo dataset);
- casi segnalati dal **Critic** (incoerenze tra classificatore, concetti e criteri);
- **errori del modello** sul set di validazione;
- immagini con **artefatti**.

Ciclo: modello → lista delle immagini più difficili → annotazione → riaddestramento della testa → nuova lista. Bastano poche centinaia di annotazioni mirate per vedere l'effetto ⚠️ (stima da verificare con un esperimento).

### 5.4 Come si raccoglie
- Strumento di annotazione open source (per esempio Label Studio o CVAT ⚠️ da scegliere) con un modulo fisso per i campi del §4.1 e del §5.2.
- Esportazione in un file di metadati (CSV o JSON) che entra direttamente nel registro dati.

## 6. Decisioni ancora aperte
1. ~~Confermare P1–P10~~ → confermate il 2026-11-04.
2. ~~Backbone~~ → confermato il 2026-11-04: **PanDerm per la tesi** + confronto con DINOv2 e Derm Foundation sugli stessi split; mail agli autori per chiarire la licenza (da scrivere).
3. ISIC 2019: **dopo** la baseline su HAM10000 (raccomandato)?
4. Nuovi dati e annotazione: in attesa dell'ospedale di contatto; istruzioni pronte in [annotazione/](annotazione/).
