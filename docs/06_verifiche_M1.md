# 06 — Verifica dei riferimenti segnati ⚠️ (issue #9, M1.9)

> Verifica fatta il 2026-11-09. Ambito dell'issue: i ⚠️ di `01_stato_dell_arte.md` e `02_risorse.md` (anni, sedi di pubblicazione, disponibilità dei pesi, licenze dei dataset). In più ho verificato i punti regolatori di `04_etica_regolatorio.md`, perché servono per le decisioni.
>
> **Fonti usate:**
> - **Crossref** (metadati ufficiali dei DOI);
> - **API di arXiv**;
> - **API dell'archivio ISIC** (licenza di ogni immagine);
> - **Hugging Face** e **GitHub** (licenze dei modelli);
> - **Figshare**;
> - **banca dati De Novo della FDA**;
> - **EUR-Lex**;
> - per alcune date, sintesi di studi legali (indicate).
>
> **Legenda:** ✅ confermato · ✏️ corretto · ❓ non risolto (resta ⚠️)

## 1. Riferimenti bibliografici

| Voce | Cosa c'era scritto | Cosa ho trovato | Esito |
|------|--------------------|-----------------|-------|
| Argenziano 2003 | JAAD 2003, consensus net meeting ⚠️ | *Dermoscopy of pigmented skin lesions: results of a consensus meeting via the Internet*, **JAAD 48(5):679–693**, [DOI 10.1067/mjd.2003.281](https://doi.org/10.1067/mjd.2003.281) | ✅ |
| Bissoto et al., bias negli ISIC | "studi 2019–2020" ⚠️ | *(De)Constructing Bias on Skin Lesion Datasets*, arXiv 1904.08818 (2019); *Debiasing Skin Lesion Datasets and Models? Not So Fast*, arXiv 2004.11457 (2020). Workshop ISIC a CVPR: sede non confermata dall'API | ✏️ (sede ❓) |
| TCAV (Kim 2018) | — | arXiv 1711.11279, **ICML 2018** (dal riferimento della rivista su arXiv) | ✅ |
| MedAgents (Tang) | 2024 ⚠️ | arXiv 2311.10537, novembre **2023**. Pubblicazione in rivista o conferenza non confermata | ✏️ (sede ❓) |
| SLICE-3D | Sci Data 2024 ⚠️ | *The SLICE-3D dataset: 400,000 skin lesion image crops extracted from 3D TBP*, **Sci Data 11:884** (agosto 2024), [DOI 10.1038/s41597-024-03743-w](https://doi.org/10.1038/s41597-024-03743-w), 34 autori, primo Kurtansky | ✅ |
| MILK10k (ISIC 2025) | esistenza da verificare ⚠️ | **Esiste**: collezione dell'archivio ISIC con 10.480 immagini, DOI 10.34970/648456, tutte **CC BY-NC**. Più "MILK10k Benchmark" (DOI 10.34970/262082) | ✅ |
| Grad-CAM | ICCV 2017 | ICCV 2017, pp. 618–626 | ✅ |
| Tschandl 2019 (CBIR) | 181(1):155–165 ⚠️ | *Br J Dermatol* **181**:155–165; online ottobre 2018 | ✅ |
| Chanda 2024 | 15:524 ⚠️ | *Nat Commun* **15**, articolo **524** (gennaio 2024), 125 autori | ✅ |
| Krakowski 2024 | 7:78 ⚠️ | *npj Digit Med* **7**, articolo **78** (aprile 2024) | ✅ |
| Vatsal 2026 | *IEEE Access* gennaio 2026 ⚠️ | Crossref **non trova** l'articolo su *IEEE Access*. Trovo un **preprint TechRxiv** (v1 ottobre 2025, v2 febbraio 2026) e arXiv 2602.04813 | ✏️ (rivista ❓) |
| AMIE 2026 (seguito) | autore non indicato | *Towards conversational AI for disease management*, *Nature* 2026, primo autore **Liévin** (non Tu) | ✏️ |
| Kurtansky 2025 (ISIC 2024) | lista autori da verificare | 22 autori: Kurtansky, Gillis, Codella, D'Alessandro, Ge, Guitera… | ✅ |
| Marsden 2024 (DERM) | lista autori da verificare | 10 autori: Marsden, Kemos, Venzi, Noy, Maheswaran, Francis… | ✅ |

## 2. Dataset e licenze

Le licenze vengono dall'API dell'archivio ISIC, che indica la licenza **immagine per immagine**. Per alcuni dataset sono diverse da quelle dichiarate nei paper.

| Dataset | Cosa c'era scritto | Cosa ho trovato | Esito |
|---------|--------------------|-----------------|-------|
| Archivio ISIC | > 400k immagini ⚠️ | **581.002 immagini**, 63 collezioni | ✏️ |
| HAM10000 | CC-BY-NC | Sull'archivio 11.720 immagini (training + test), tutte **CC BY-NC** | ✅ |
| **BCN20000** | CC BY 4.0 (Sci Data 2024) ⚠️ | **Dipende da dove lo si scarica:** <br>• su **Figshare** ([10.6084/m9.figshare.24140028](https://doi.org/10.6084/m9.figshare.24140028)) è **CC BY 4.0**, con immagini e CSV di training e test; <br>• sull'**archivio ISIC** le 18.946 immagini sono tutte **CC BY-NC**. | ✏️ importante |
| ISIC 2020 | CC BY-NC 4.0 (paper) | Sull'archivio (collezione "Challenge 2020: Training"): **licenze miste**, 19.557 CC BY e 13.569 CC BY-NC | ✏️ |
| ISIC 2024 / SLICE-3D | CC-BY-NC ⚠️ | Sull'archivio (collezione "Challenge 2024: Training", 401.059 immagini): **licenze miste**, 28.665 CC-0, 188.812 CC BY e 183.582 CC BY-NC | ✏️ |
| Annotazioni di Chanda 2024 | link e licenza da verificare ⚠️ | Figshare *HAM10000 expert-annotated explanations and pseudonymized reader study data*, [10.6084/m9.figshare.23766477](https://doi.org/10.6084/m9.figshare.23766477) (v9, luglio 2025), **CC BY 4.0**. Contiene `annotations_gt.zip` (12 MB), `metadata_gt.csv` e i dati delle tre fasi dello studio. Attenzione: immagini duplicate tra i gruppi | ✅ |
| **Nuovo:** HIBA (Hospital Italiano de Buenos Aires, 2019–2022) | — | Collezione ISIC con **1.616 immagini** (1.270 dermoscopiche polarizzate e 346 cliniche) di 1.246 lesioni e 623 pazienti argentini; **CC BY**; DOI 10.34970/587329. Nel campione di 100 immagini i fototipi sono soprattutto II–III | ✏️ aggiunto |

## 3. Modelli e pesi

| Modello | Cosa c'era scritto | Cosa ho trovato | Esito |
|---------|--------------------|-----------------|-------|
| PanDerm | CC BY-NC-ND 4.0 (README) | Su GitHub non c'è un file di licenza riconosciuto ("none"); la licenza è dichiarata solo nel README | ✅ (README) |
| **DermFM-Zero** | Licenza contraddittoria ⚠️ | **Ancora contraddittoria:** <br>• i metadati di Hugging Face dicono `cc-by-nc-4.0`; <br>• il testo da accettare per scaricare i pesi dice "CC BY-NC-ND 4.0" e "non ridistribuirò i pesi"; <br>• su GitHub la licenza non è dichiarata in modo riconoscibile. | ❓ (domanda nella mail agli autori) |
| MONET | repository CC BY-NC-SA 4.0 | Il modello su Hugging Face si è spostato da `chanwkim/monet` a **`suinleelab/monet`**; nessuna licenza nei metadati | ✏️ (nuovo indirizzo) |
| Derm Foundation | termini HAI-DEF | Hugging Face: licenza "other", accesso con registrazione | ✅ |
| MedGemma ⚠️ | "Google, 2025" | **Esiste** (per esempio `google/medgemma-4b-it`, aggiornato a ottobre 2025), licenza "other" (termini HAI-DEF), accesso con registrazione. Termini non letti | ✅ (termini ❓) |
| DINOv2 | Apache 2.0 | Confermato su GitHub e Hugging Face | ✅ |

## 4. Prodotti e regole

| Voce | Cosa c'era scritto | Cosa ho trovato | Esito |
|------|--------------------|-----------------|-------|
| DermaSensor, FDA | De Novo gennaio 2024 ⚠️ | **Confermato** dalla banca dati FDA: **DEN230008**, decisione **12 gennaio 2024** (annuncio 17 gennaio), **classe II**, 21 CFR 878.1830, codice prodotto QZS. Indicato per **medici non dermatologi**, pazienti di **40 anni o più** | ✅ |
| DermaSensor, numeri | sens. ~96%, spec. ~21% ⚠️ | Da Venkatesh et al., *npj Digit Med* 7:156 (2024): <br>• studio DERM-SUCCESS su 1.579 lesioni di 1.005 pazienti in 22 centri; <br>• **sensibilità 95,5%**, **specificità 20,7%**, valore predittivo negativo 96,6%; <br>• il 97,1% dei pazienti era bianco: la FDA chiede studi dopo l'autorizzazione nelle popolazioni poco rappresentate. | ✅ (fonte peer-reviewed) |
| DERM, CE classe III 2025 | fonte aziendale ⚠️ | Solo notizie aziendali e stampa di settore (febbraio 2025). Non verificabile su una banca dati pubblica | ❓ (resta "fonte aziendale") |
| Google DermAssist | "ritirato/limitato" ⚠️ | CE classe I nel 2021; la pagina di Google Health lo indica come **"non più in sviluppo"** | ✏️ |
| MDR, transizione | prorogata al 2027–2028 ⚠️ | Regolamento (UE) **2023/607**, in vigore dal 20 marzo 2023: <br>• **31 dicembre 2027** per classe III e IIb impiantabili; <br>• **31 dicembre 2028** per le altre IIb, le IIa e alcune classe I; <br>• vale solo per i dispositivi già esistenti con contratto con un organismo notificato entro il 26 settembre 2024. <br>Fonti: autorità irlandese HPRA e sintesi legali | ✅ |
| **AI Act, date** | obblighi per l'Allegato I dal 2 agosto 2027 ⚠️ | **Cambiato.** Il **Digital Omnibus sull'AI**, regolamento (UE) **2026/1744** (adottato l'8 luglio 2026, Gazzetta ufficiale del 24 luglio, in vigore dal 27 luglio 2026), ha **rinviato**: <br>• Allegato I (dispositivi medici) al **2 agosto 2028**; <br>• Allegato III al 2 dicembre 2027. <br>I dispositivi medici **restano** nella sezione A dell'Allegato I (è la macchina che passa alla B). Le date vengono da sintesi di studi legali; il testo in Gazzetta l'ho solo individuato, non letto | ✏️ importante |
| Kaggle | ~30 h di GPU a settimana ⚠️ | Circa 30 ore, **non pubblicate ufficialmente** da Kaggle e variabili; sessioni al massimo di 12 ore | ✏️ |

## 5. Cosa cambia per Neo Helper
1. **BCN20000 va scaricato da Figshare** se si vuole la licenza CC BY. La copia dell'archivio ISIC è non commerciale. Annotare sempre **da dove** viene ogni dataset.
2. **Licenze per immagine:** nei dataset ISIC 2020 e 2024 convivono CC-0, CC BY e CC BY-NC. Il registro dati (§4.1 del documento delle scelte) deve avere un campo `license` per ogni immagine.
3. **Annotazioni di Chanda: disponibili in CC BY 4.0.** Si possono usare per validare MONET e per un concept bottleneck su HAM10000.
4. **Dataset argentino HIBA (CC BY):** utile come **test esterno latinoamericano** con immagini dermoscopiche e cliniche. Non risponde però alla domanda sulle pelli più scure, perché i fototipi sono soprattutto II–III. Va aggiunto al §4.3 del documento delle scelte.
5. **AI Act:** la scadenza per i dispositivi medici con AI passa al **2 agosto 2028**. Il quadro resta in movimento (Health Innovation Package).
6. **DermaSensor:** confermato da fonte ufficiale; la FDA ha chiesto **studi dopo l'autorizzazione** nelle pelli poco rappresentate. Conferma ancora l'importanza dei risultati per fototipo.

## 6. Cosa resta aperto
- **Sedi di pubblicazione non confermate:** Bissoto (workshop CVPR), MedAgents, Vatsal (*IEEE Access*).
- **Licenze:** DermFM-Zero (nella mail agli autori), termini di MedGemma, licenza dei pesi di MONET.
- **Fonti aziendali:** CE di classe III di DERM.
- **Testi di legge da leggere direttamente** prima della consegna della tesi: MDR (regola 11), AI Act consolidato dopo il 2026/1744.
- **Fuori dall'ambito dell'issue:** gli **89 ⚠️ dentro le schede** (`docs/papers/`). Sono soprattutto numeri presi da sintesi alphaXiv o da abstract. Si sciolgono leggendo i PDF quando una scheda serve davvero nella tesi.
