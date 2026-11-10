# 08 — Revisione finale della Milestone 1 (issue #31, M1.11)

> Revisione del 2026-11-10, dopo i pacchetti di letteratura 1–5. Ho riletto:
> - roadmap e README;
> - stato dell'arte, risorse, architettura, etica e regole;
> - scelte e pipeline, verifiche, domande di ricerca;
> - le 42 schede, le istruzioni per gli annotatori, gli storyboard, il diario;
> - le issue delle milestone M2–M7.
>
> Domande:
> - abbiamo dimenticato qualcosa?
> - il percorso è logico in ogni passo?
> - rispetta i principi del progetto?

## 1. Il percorso in breve
1. **Clinica** (§1): melanoma, dermoscopia, ABCD, 7-point checklist.
2. **Paper fondativi** (§2): reti a livello dermatologo; medico + AI meglio di entrambi da soli.
3. **Foundation model e LLM** (§3) e **bias** (§4) → prime scelte: PanDerm, l'LLM non classifica, DDI, controllo qualità, CLEAR Derm.
4. **Scelte e pipeline** (05), con l'analisi onesta della licenza di PanDerm e le istruzioni per gli annotatori.
5. **Spiegabilità, incertezza** (§5) e **agenti e MCP** (§6).
6. **Challenge ISIC** (§7) e **prodotti e regole** (§8).
7. **Verifica** dei riferimenti (06) e **domande di ricerca** (07), con la RQ6 sulle popolazioni latinoamericane.

Il criterio di completamento della M1 nella roadmap è "≥ 30 paper schedati, RQ definitive". **Rispettato:** 42 schede (più il background clinico), RQ confermate il 2026-11-10.

## 2. Controllo dei principi

| Principio | Rispettato? | Note |
|-----------|-------------|------|
| Codice, git e GitHub in inglese; documenti e audio in italiano | ✅ | Unica eccezione voluta: gli storyboard in inglese, scritta in `CLAUDE.md` |
| Titoli delle issue con prefisso `M<n>.<k>_` | ✅ | Tutte le 31 issue |
| Oggetto dei commit con milestone, pacchetto e issue | ✅ dal 2026-11-06 | I commit precedenti non sono stati riscritti, come da regola |
| Ogni scheda dice cosa è stato letto e segna con ⚠️ ciò che non è verificato | ✅ | 42 schede su 42 hanno la riga "Testo letto": <br>• 30 testo completo; <br>• 6 abstract più parti del testo; <br>• 2 solo abstract; <br>• 7 sintesi alphaXiv; <br>• 2 pagine web. <br>(Una scheda può contare in più categorie.) |
| Sempre il DOI | ✅ | Tranne i blog e la specifica MCP, che hanno il link |
| Diario aggiornato a ogni sessione | ✅ | |
| L'LLM non classifica; i numeri vengono solo dai tool | ✅ | Coerente in 03, 05, storyboard, RQ4 |
| Test esterni, sottogruppi, divisione per lesione, test usato una volta | ✅ | In 05, 07 e nelle schede delle challenge |
| Licenze registrate e verificate | ✅ con correzioni | Verifica 06: BCN20000 dipende dalla fonte; licenze miste per immagine |
| Supervisione umana, "non so", uso dichiarato per il medico | ✅ | P8, P10, RQ2 |
| Onestà su incertezze e limiti | ✅ | ⚠️ visibili; registro delle verifiche con gli esiti ❓ |

## 3. Cose dimenticate o non allineate

| # | Cosa | Dove | Gravità | Proposta |
|---|------|------|---------|----------|
| 1 | **Tabella comparativa dei risultati** promessa come deliverable della Fase 1 ("stato dell'arte completo + tabella comparativa") | `00_roadmap.md` | Media | Creare una tabella unica con i numeri chiave dei paper: dati, compito, metrica, risultato, test esterno sì/no |
| 2 | **Fasi 2, 3 e 5 della roadmap** non aggiornate alle scelte: <br>• Fase 2 parla di "download ISIC 2019/2020"; <br>• Fase 3 di "fine-tuning ResNet50"; <br>• Fase 5 di demo pubblica su Hugging Face; <br>• il criterio della M2 è "AUROC su ISIC val". | `00_roadmap.md` | Media | Allineare a P1–P10 e RQ1–RQ6 (HAM10000 + test esterni, backbone congelato, accuratezza bilanciata, licenze) |
| 3 | **Issue future non allineate:** <br>• **#12** M2.2: dataset; <br>• **#14** M2.4: baseline con fine-tuning; <br>• **#19** M3.5: mancano BCN20000, HIBA, BALD e le metriche nuove; <br>• **#21** M4.2: nomi dei tool; <br>• **#24** M5.1: demo pubblica in conflitto con le licenze non commerciali. | GitHub | Media | Aggiornare il testo delle issue |
| 4 | **Nessuna issue per la RQ6:** valutazione latinoamericana e acrale, report in spagnolo e portoghese, funzionamento con poche risorse | GitHub | Alta (è uno scopo dello studio) | Nuove issue, per esempio M3.6 (valutazione RQ6), M4.5 (report multilingue), M6.3 (uso su CPU e con poche risorse) |
| 5 | **`03_architettura.md` è precedente alle scelte:** <br>• nomi dei tool diversi (`assess_quality`, `classify_lesion`… contro `check_quality`, `embed_image`, `predict_set`, `describe_concepts`, `similar_cases`); <br>• il classificatore come "ensemble"; <br>• i criteri come `compute_abcd`. | `03_architettura.md` | Media | Allinearlo a 05 e allo storyboard 3, con una tabella unica dei tool |
| 6 | **Storyboard un po' indietro:** <br>• lo storyboard 2 non ha BCN20000 e HIBA tra i test; <br>• lo storyboard 4 segna "Chanda labels: to check" (ora risolto) e non ha la RQ6. | `docs/figures/` | Bassa | Aggiornare gli storyboard 2 e 4 |
| 7 | **Letteratura che servirà nella M3**, non ancora letta: <br>• segmentazione (MedSAM, U-Net); <br>• paper di DINOv2; <br>• calibrazione e conformal in dermatologia; <br>• Bissoto sui bias; <br>• i paper dei dataset di test (PAD-UFES-20, PH2, Derm7pt); <br>• epidemiologia del **melanoma acrale**; <br>• dataset **asiatici**. | `01`, `07` | Media | Leggerla "al momento giusto", all'inizio della M3, con lo stesso metodo |
| 8 | **Licenze o accesso non verificati** per DDI (accesso su richiesta), PH2 e Derm7pt | `02_risorse.md` | Media | Verificarli nella M2.2, insieme al download |
| 9 | **89 ⚠️ dentro le schede**, soprattutto numeri da sintesi alphaXiv o da abstract | `docs/papers/` | Bassa ora, media per la tesi | Scioglierli leggendo i PDF delle schede che entrano nella tesi |
| 10 | **Azioni di Cesar in sospeso:** <br>• mail agli autori di PanDerm; <br>• contatto con l'ospedale; <br>• Zotero (Fase 0, mai fatto: la bibliografia è mantenuta a mano). | — | Media (la mail) | Inviare la mail; decidere se Zotero serve |

Già corretti in questa revisione:
- **README:** documenti nuovi, stato della Fase 1, obiettivo RQ6;
- **roadmap:** spunta "repository pubblico";
- **scheda MCP:** etichetta "Testo letto".

## 4. Il percorso è logico?
**Sì, nell'insieme.** Ogni scelta viene da una fonte letta, e ogni domanda di ricerca nasce da un limite trovato in letteratura:
- crollo fuori dal laboratorio → RQ1;
- lesioni sconosciute → RQ2;
- spiegazioni non verificate → RQ3;
- agenti poco controllati → RQ4;
- pelli non rappresentate → RQ6.

Tre punti di attenzione:
1. **Ambizione contro tempo.** Sei domande, sette milestone, web e mobile sono molto per una tesi. Il cuore della tesi sono **RQ1, RQ2 e RQ6**, che si basano sugli stessi esperimenti e sugli stessi dati. RQ3 e RQ4 sono il secondo blocco. RQ5, web completo e mobile possono ridursi a prototipi.
2. **Dipendenza da PanDerm.** La tesi regge anche senza: il confronto con DINOv2 è già nella RQ1, e il percorso con licenze aperte è nella RQ6.
3. **Dati per la RQ6.** HIBA ha soprattutto fototipi II–III, e mancano dataset asiatici pubblici generali. La RQ6 misurerà davvero il cambio di **popolazione, centro e sede acrale**. Sulle pelli scure dermoscopiche servono dati nuovi: è il ruolo dell'ospedale (§4 delle scelte).

## 5. Riepilogo: obiettivi, scelte, criticità e perché

| Area | Obiettivo | Scelta fatta | Criticità | Perché |
|------|-----------|--------------|-----------|--------|
| Clinica | Parlare la lingua del dermatologo | 7-point checklist e ABCD come vocabolario di spiegazioni e annotazioni | I criteri dermoscopici sono poco concordanti anche tra esperti (Jaccard 0,47 nella ISIC 2018) | Il medico decide con i criteri, non con le probabilità |
| Dati di partenza | Una baseline pulita e confrontabile | **HAM10000**, divisione per `lesion_id` 70/15/15; ISIC 2019 dopo | Pelli quasi solo chiare, nessun fototipo; licenza non commerciale; manca l'SCC | Oltre metà delle diagnosi è istologica; stesso dataset di Tschandl e PanDerm |
| Test esterni | Misurare la realtà fuori dal laboratorio | BCN20000 (da Figshare), DDI, PAD-UFES-20, HIBA, PH2, Derm7pt, BALD | Licenze e accessi diversi; poche dermoscopie su pelli scure; nessun dataset asiatico generale | Gli algoritmi crollano dall'82% al 59% su dati nuovi (Combalia 2022) |
| Backbone | Il miglior "occhio" con poche risorse | **PanDerm congelato + testa lineare**; fine-tuning come secondo esperimento | Licenza CC BY-NC-ND: niente app pubblica; in condizioni reali scende al livello di un dermatologo medio (Anriot 2026) | Migliore su 28 compiti, servono poche etichette; i dati nuovi richiedono solo di riaddestrare la testa |
| Alternative libere | Sapere quanto costa l'indipendenza | DINOv2 (Apache 2.0), Derm Foundation, ImageNet sugli stessi split | Derm Foundation è pensato per foto cliniche | Senza confronto non sapremmo il prezzo di un backbone libero (RQ1) |
| Uscita | Aiutare la decisione | 7 probabilità + punteggio di malignità con soglia bassa (17–20%) | La soglia va ricalibrata; la prima versione non conosce l'SCC | Le probabilità multiclasse aiutano di più; la falsa rassicurazione è l'errore peggiore (Tschandl 2020) |
| Qualità e artefatti | Fermare le scorciatoie | Controllo qualità prima di tutto, con avvisi sugli artefatti (MONET) | Gli artefatti dermoscopici di MONET sono visti solo in modo qualitativo | Segni di penna: specificità dall'84% al 46% (Winkler 2019); adesivi arancioni |
| Spiegabilità | Spiegazioni vere e utili | Criteri (MONET o concept bottleneck validati sulle annotazioni di Chanda), casi simili (16), Grad-CAM per gli sviluppatori con test di sanità | MONET non è testato sui criteri dermoscopici; le spiegazioni fanno seguire l'AI anche quando sbaglia | Le heatmap spesso non superano i test di sanità (Adebayo 2018); i medici si fidano dei criteri (Chanda 2024) |
| Incertezza | Dire "non so" quando serve | Calibrazione + **insiemi conformal** + controllo fuori distribuzione | La garanzia si rompe con dati diversi: va misurata | Il 47% delle lesioni sconosciute viene chiamato "maligno" (Combalia 2022); l'AI sbagliata trascina i medici |
| Ruolo dell'LLM | Scrivere e coordinare senza inventare | L'LLM **non classifica**; numeri solo dai tool; catena di prove | La scelta del modello (locale o via API) è ancora aperta; privacy | ChatGPT e Gemini mancano da un terzo a metà dei tumori (Bhagwat 2026) |
| Agenti e MCP | Uno strumento riutilizzabile e controllato | v0 → v1 (server MCP) → v2 → v3 solo se migliora in modo misurabile; critico a regole | Nomi dei tool non allineati tra i documenti; DermAgent già vicino; costo del multi-agente | Il multi-agente costa circa 15 volte i token (Anthropic 2025); mancano controlli negli agenti medici (Vatsal 2026) |
| Valutazione | Numeri clinicamente sensati | Accuratezza bilanciata, specificità ad alta sensibilità, pAUC, tumori mancati, sottogruppi, CLEAR Derm | Criteri di M2 nella roadmap ancora vecchi | Le metriche cambiano la classifica (Codella 2019, Kurtansky 2025) |
| Inclusione (RQ6) | Funzionare per l'America Latina e oltre | Test su HIBA, PAD-UFES-20, BALD; adattamento con pochi dati locali; percorso accessibile (CPU, licenze aperte, spagnolo e portoghese) | HIBA soprattutto fototipi II–III; nessuna issue ancora; mancano dati asiatici | Scopo dichiarato dello studio; i modelli vanno peggio su chi non è nei dati (DDI, Fitzpatrick17k) |
| Nuovi dati | Lasciare la porta aperta | Solo una possibilità, con istruzioni per gli annotatori in italiano, inglese e spagnolo | Contatto con l'ospedale da definire; servono comitato etico e consenso | Il divario sulle pelli scure si chiude solo con dati diversi (DDI 2022) |
| Regole e licenze | Restare nel lecito, dirlo chiaramente | Prototipo di ricerca, non un dispositivo; requisiti dell'AI Act come lista volontaria | Demo pubblica in conflitto con le licenze non commerciali; regole in movimento (AI Act al 2028) | MDR: software diagnostico almeno di classe IIa; AI Act: alto rischio |
| Metodo | Tracciabilità e onestà | Schede con lo stato di lettura e i ⚠️, verifiche, Word e audio, diario, convenzioni git | 7 schede da sintesi alphaXiv; 89 ⚠️ nelle schede; tabella comparativa mancante | Ogni affermazione della tesi deve avere una fonte controllabile |

## 6. Correzioni proposte e stato (completate il 2026-11-10)

| # | Correzione | Stato |
|---|------------|-------|
| 1 | Tabella comparativa dei risultati (deliverable della Fase 1) | ✅ §11 di `01_stato_dell_arte.md` (28 righe) |
| 2 | Roadmap: Fasi 2–7, struttura della tesi, criteri delle milestone, titolo | ✅ |
| 3 | Testo delle issue M2–M7 allineato alle decisioni della M1 | ✅ 20 issue aggiornate su GitHub (#11–#30) |
| 4 | Nuove issue per la RQ6 | ✅ #33 M3.6, #34 M4.5, #35 M5.3; più #32 M1.12 (ricerca su pelli non chiare) |
| 5 | `03_architettura.md` allineato (nomi dei tool, classificatore, criteri) | ✅ con la tabella dei tool di riferimento |
| 6 | Storyboard 2 e 4 aggiornati | ✅ test esterni, annotazioni di Chanda, nuovo livello "Inclusion (RQ6)" (47 blocchi in 8 livelli) |
| 7 | Letteratura per la M3 | Rimandata all'inizio della M3, scritta nelle issue M3.2, M3.3 e M3.6 |
| 8 | Licenze o accesso di DDI, PH2 e Derm7pt | Rimandate alla M2.2, scritte nella issue #12 |
| 9 | 89 ⚠️ nelle schede | Rimandati alla scrittura della tesi |
| 10 | Azioni di Cesar: mail agli autori di PanDerm, ospedale, Zotero | Tenute in conto nella roadmap ("Azioni in sospeso") |

## 7. Allineamento delle issue delle milestone successive (applicato il 2026-11-10)
Ho confrontato le 20 issue aperte delle milestone M2–M7 con le decisioni finali della M1 (P1–P10, C1–C5, RQ1–RQ6, verifiche). I testi in inglese pronti da applicare sono preparati.

| Issue | È allineata? | Cosa cambia |
|-------|--------------|-------------|
| #11 M2.1 ambiente Python | Quasi | Aggiungere il funzionamento **solo su CPU** (RQ6) e i vettori salvati fuori da git |
| #12 M2.2 download | **No** | Titolo e testo: non "ISIC 2019/2020", ma HAM10000 + test esterni (BCN20000 da Figshare, DDI, PAD-UFES-20, HIBA, PH2, Derm7pt) + dati della RQ6 + annotazioni di Chanda; **licenza e fonte per immagine**; ISIC 2019 dopo |
| #13 M2.3 EDA | Quasi | Controllo degli artefatti con MONET; duplicati BCN20000 tra ISIC e Figshare; bozza della data card |
| #14 M2.4 baseline | **No** | Non "fine-tuning ResNet50": **vettori congelati + testa lineare** per PanDerm, DINOv2, Derm Foundation e ImageNet; metriche cliniche |
| #15 M3.1 backbone | In parte | Diventa "esperimento di fine-tuning e scelta finale del backbone" (il confronto passa alla M2.4) |
| #16 M3.2 segmentazione | Quasi | Contare i fallimenti; leggere MedSAM; licenza dei pesi |
| #17 M3.3 calibrazione | Quasi | Conformal per classe, controllo fuori distribuzione, copertura per centro e fototipo, lesioni sconosciute (RQ2) |
| #18 M3.4 spiegabilità | Quasi | Test di sanità; validazione di MONET su Derm7pt e Chanda (RQ3) |
| #19 M3.5 test esterni | In parte | Aggiungere BCN20000 e HIBA; per centro e per artefatto; CLEAR Derm (RQ1) |
| #20 M4.1 v0 | Quasi | Passi allineati alla pipeline del §3.2 delle scelte |
| #21 M4.2 server MCP | **No** | **Nomi dei tool** allineati; resource; principi di sicurezza MCP |
| #22 M4.3 v2 | Quasi | Catena di prove; scelta dell'LLM locale o via API (RQ4) |
| #23 M4.4 v3 | Quasi | Critico a regole, percorso guidato dall'incertezza, casi trappola, confronto dei costi (RQ4) |
| #24 M5.1 demo Gradio | **No** | Vincolo di licenza: pubblica solo con un backbone libero, altrimenti solo per ricerca |
| #25 M5.2 web app | In parte | Insieme conformal, criteri, casi simili; **più lingue** (RQ6) |
| #26 M6.1 mobile | Quasi | Lente dermoscopica per smartphone; più lingue |
| #27 M6.2 dispositivo o server | Quasi | PanDerm è troppo pesante per il telefono; misure solo su CPU |
| #28 M7.1 model card | Quasi | Licenza per fonte; lista volontaria dell'AI Act; risultati per sottogruppo |
| #29 M7.2 tesi | In parte | Struttura per RQ1–RQ6 (roadmap aggiornata); ricontrollare l'AI Act (2028) |
| #30 M7.3 Zenodo | Quasi | Niente pesi di PanDerm modificati; licenze di terzi |

**Nuove issue proposte:**
- **M3.6** "Evaluation on Latin American and acral datasets (RQ6)":
  - HIBA, PAD-UFES-20, dati cileni, BALD, MSKCC Skin Tone;
  - adattamento con pochi dati locali;
  - ricerca di dataset asiatici.
- **M4.5** "Multilingual report (Spanish and Portuguese)".
- **M5.3** "Package for low-resource research centres": CPU, licenze aperte, LLM locale, guida per aggiungere i propri dati.
