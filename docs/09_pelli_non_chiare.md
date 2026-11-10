# 09 — Dataset e studi su pelli non chiare (issue #32, M1.12, per la RQ6)

> Ricerca del 2026-11-10 con PubMed, alphaXiv/arXiv, Crossref e l'API dell'archivio ISIC.
>
> **Obiettivo:** capire **che cosa esiste davvero**, cioè dataset e studi, su pelli diverse da quelle chiare: latinoamericane, asiatiche, africane, fototipi IV–VI. Serve a progettare la [RQ6](07_domande_di_ricerca.md).
>
> Ogni riga dice cosa è stato letto. ⚠️ = non verificato.

## 1. Il quadro in quattro numeri
- **21 dataset pubblici** di tumori della pelle (106.950 immagini, revisione del 2022):
  - il fototipo è riportato solo per il **2,1%** delle immagini, l'etnia per l'**1,3%**;
  - 11 dei 14 dataset con paese dichiarato vengono da **Europa, Nord America e Oceania**.
  
  (Wen et al., *Lancet Digit Health* 2022)
- **Oltre 1,1 milioni di immagini** pubbliche di dermatologia messe insieme (SkinMap, 2026):
  - i fototipi **V–VI sono il 5,8%**, mentre i fototipi III–VI sono circa l'**84%** delle visite dermatologiche nel mondo;
  - **Africa e Sud America sono praticamente assenti**;
  - la copertura delle pelli scure **non cresce** nel tempo.
  
  (Gröger et al., arXiv 2026)
- **16 studi di AI dermatologica** del 2020–2025 (scoping review del 2026):
  - **nessuno** identifica pazienti ispanici o latinoamericani;
  - pochi riportano i risultati per tono della pelle;
  - quelli che lo fanno trovano **meno specificità, più falsi positivi e meno accuratezza** sulle pelli scure.
  
  (Pérez-Lalinde et al., *Skin Res Technol* 2026)
- **Medici e AI su 46 malattie, 39 paesi:**
  - sia i dermatologi sia i medici di base sono **4 punti meno accurati** sulle pelli scure;
  - un'AI ben fatta aumenta l'accuratezza di oltre il 33%, ma **allarga** il divario tra pelli chiare e scure per i medici di base.
  
  (Groh et al., *Nature Medicine* 2024)

## 2. Dataset disponibili

| Dataset | Origine | Pelle | Tipo di immagine | Malattie | Dimensione | Licenza / accesso | Letto o verificato | Per la RQ6 |
|---------|---------|-------|------------------|----------|------------|-------------------|--------------------|------------|
| **HIBA** (Ricci Lara 2023) | Argentina, Buenos Aires | Fototipo registrato alla visita; nel campione soprattutto II–III | 1.270 dermoscopie polarizzate + 346 foto da smartphone | Tumori e lesioni benigne | 1.616 img, 1.246 lesioni, 623 pazienti | **CC BY** (approvato dal comitato etico) | Paper (PMC) e archivio ISIC | **Test principale latinoamericano**; adattamento locale |
| **PAD-UFES-20** | Brasile, Espírito Santo | Fototipo nei metadati ⚠️ distribuzione | Foto da smartphone | 6 classi di tumori e lesioni | 2.298 img | **CC BY** | Archivio ISIC | Modalità diversa (foto) |
| Cheratosi seborroiche, PUC Chile | Cile | ⚠️ | Dermoscopie | Solo cheratosi seborroica | 150 | CC BY | Archivio ISIC | Piccolo test aggiuntivo |
| **BALD** (BRAAFF) | Più centri, tra cui giapponesi | ⚠️ | Dermoscopie | **Melanomi e nevi acrali** | 666 | CC BY-NC | Archivio ISIC | Sede acrale (proxy asiatico) |
| **DDI** (Daneshjou 2022) | USA, Stanford | **Fototipi I–VI bilanciati** in tre gruppi | Foto cliniche | Tumori e lesioni con biopsia | 656 | Accesso su richiesta ⚠️ | Scheda (testo completo) | Asse "tono della pelle" a parità di malattie |
| **MSKCC Skin Tone Labeling** | USA, Memorial Sloan Kettering | Annotazioni dettagliate del **tono** | Varie (esame di tutto il corpo) | Lesioni varie | 4.879 img, 64 pazienti | CC BY | Archivio ISIC | Misurare il tono della pelle |
| Fitzpatrick17k (Groh 2021) | Atlanti web | I–VI, pochi V–VI | Foto cliniche | 114 condizioni, poche lesioni pigmentate | 16.577 | Uso di ricerca ⚠️ | Scheda (testo completo) | Equità, ma poche lesioni |
| **SCIN** (Google; Ward 2024) | USA, foto inviate dal pubblico | Fototipo dichiarato + **scala Monk** stimata | Foto da smartphone | Soprattutto infiammatorie e infettive (89%) | 5.749 invii | Aperto, con licenza d'uso (vietato reidentificare) | Paper (PMC, parti) | Tono sì, lesioni pigmentate quasi no |
| **PASSION** (MICCAI 2024) | Africa subsahariana | **Pelli pigmentate** | Foto cliniche (telemedicina) | Malattie pediatriche: eczema, funghi, scabbia, impetigine | 4.901 img, 1.653 pazienti | ⚠️ (sito del progetto) | Abstract | Non sono tumori: mostra il vuoto |
| DermaCon-IN (NeurIPS 2025) | India | Pelli indiane | Foto cliniche | Malattie della pelle con concetti | ⚠️ | ⚠️ | Solo citato (in Kunwor 2026) | Da leggere: concetti su pelli scure |
| Asan / Hallym (Han 2018) | Corea | Coreani | Foto cliniche | 12 tumori e lesioni benigne | Asan circa 17.000 img ⚠️ | In parte pubblico ⚠️ | Abstract | Un dataset asiatico, da verificare l'accesso |
| Peking Union (Wang 2020) | Cina | Cinesi | Dermoscopie | Tumori comuni e psoriasi | 7.192 + 3.115 | Non pubblico ⚠️ | Abstract | Dimostra che la dermoscopia asiatica esiste, ma chiusa |

**Cosa manca:** un dataset **pubblico di dermoscopie** di **tumori pigmentati** su **fototipi IV–VI**, e un dataset **asiatico** pubblico di lesioni generali. I dataset "diversi" oggi pubblici (SCIN, PASSION, DermaCon-IN, Fitzpatrick17k) sono quasi tutti di **foto cliniche** e di **malattie infiammatorie**.

## 3. Studi principali

| Studio | Cosa hanno fatto | Risultato chiave | Letto |
|--------|------------------|------------------|-------|
| Wen et al., *Lancet Digit Health* 2022 ([DOI](https://doi.org/10.1016/S2589-7500(21)00252-1)) | Revisione sistematica dei dataset pubblici | Fototipo solo per il 2,1% delle immagini; dati quasi solo da Europa, Nord America e Oceania | Abstract |
| Gröger et al., SkinMap, arXiv 2601.00840 (2026) | Atlante di 1,1 milioni di immagini pubbliche | V–VI = 5,8% contro circa 84% di III–VI nella popolazione dei pazienti; Sud del mondo assente; pediatria 3% | Abstract e risultati principali |
| Pérez-Lalinde et al., *Skin Res Technol* 32 (2026) ([DOI](https://doi.org/10.1111/srt.70385)) | Scoping review di 16 studi | Nessuno identifica pazienti ispanici o latinoamericani; sulle pelli scure meno specificità e più falsi positivi | Abstract e parti (PMC) |
| Ricci Lara et al., *Sci Data* 10 (2023) ([DOI](https://doi.org/10.1038/s41597-023-02630-0)) | Dataset HIBA | Primo dataset pubblico di dermoscopie e foto cliniche dell'America ispanica; CC BY | Abstract e parti (PMC) |
| Groh et al., *Nat Med* 30 (2024) ([DOI](https://doi.org/10.1038/s41591-023-02728-3)) | 389 dermatologi e 459 medici di base, 364 immagini, 46 malattie | Medici 4 punti peggio sulle pelli scure; l'AI aiuta (+33%) ma allarga il divario per i medici di base | Abstract (PMC) |
| Kunwor et al., arXiv 2609.02111 (2026) | Backbone congelati (MONET, DermLIP, DINOv3, CNN da tumori) su DDI e SCIN | **Conta più il tipo di malattia che il tono:** la CNN da tumori scende da 0,62 a 0,21 di accuratezza bilanciata; il divario per tono è 0,10–0,18 e non ha una direzione costante. I foundation model dermatologici si trasferiscono meglio. Con **circa 10 esempi per categoria** si recupera gran parte delle prestazioni. Tutto su **GPU gratuita e CPU** | Testo completo (arXiv) |
| Han et al., *J Invest Dermatol* 138 (2018) ([DOI](https://doi.org/10.1016/j.jid.2018.01.028)) | Rete addestrata su pazienti coreani (Asan), testata anche su Edinburgh | AUC per il melanoma 0,96 sui coreani, 0,88 sugli europei; gli autori chiedono più età ed etnie | Abstract |
| Wang et al., *Chin Med J* 133 (2020) ([DOI](https://doi.org/10.1097/CM9.0000000000001023)) | CNN su dermoscopie di pazienti cinesi, contro 164 dermatologi | Comparabile ai dermatologi per basocellulare, nevo e cheratosi seborroica | Abstract |
| PASSION, arXiv 2411.04584 (MICCAI 2024) | Dataset di pelli pigmentate dall'Africa subsahariana | 4.901 immagini di 1.653 pazienti; malattie pediatriche comuni; baseline per sottopopolazioni | Abstract |
| Innocent et al., *Front Artif Intell* 9 (2026) ([DOI](https://doi.org/10.3389/frai.2026.1894174)) | Rassegna su ML per il sarcoma di Kaposi in persone con HIV (Africa) | Sensibilità 89%, specificità 51% nello studio principale; la dermoscopia va meglio delle foto | Abstract |
| Già nelle schede: DDI 2022, Fitzpatrick17k 2021, Bhagwat 2026, Venkatesh 2024 (DermaSensor) | — | Calo sulle pelli scure; anche gli LLM; la FDA chiede studi dopo l'autorizzazione | Schede |

**Da leggere in seguito ⚠️:**
- Rikhye et al., *eBioMedicine* 2025 (conta la distribuzione delle malattie, non i dati demografici);
- Kinyanjui et al., MICCAI 2020 (tono della pelle stimato con l'ITA);
- Kamulegeya et al. (Uganda, preprint 2019);
- stima del tono da dermoscopie con colorimetro (arXiv 2602.10265);
- DermaCon-IN;
- studi su pazienti messicani, colombiani e peruviani (non trovati in questa ricerca);
- una fonte epidemiologica sul **melanoma acrale** nelle popolazioni asiatiche e latinoamericane.

## 4. Cosa significa per la RQ6
1. **Il vuoto è confermato e misurato.** Le pelli V–VI sono il 2–6% delle immagini pubbliche; America Latina e Africa sono quasi assenti; nessuno studio riporta pazienti ispanici o latinoamericani. La RQ6 colma un buco reale.
2. **Tre cose cambiano insieme:** tono della pelle, tipo di malattia e tipo di immagine. Kunwor 2026 mostra che spesso pesa di più la **malattia**. La RQ6 va quindi progettata per **separare i fattori**:
   - **DDI:** il tono, a parità di malattie;
   - **HIBA:** popolazione e centro, con la stessa modalità (dermoscopia);
   - **PAD-UFES-20:** la modalità (foto da smartphone);
   - **BALD:** la sede acrale.
3. **L'ipotesi H6d (pochi dati locali bastano) ha un appoggio in letteratura.** Con le caratteristiche di un foundation model dermatologico, circa 10 esempi per categoria recuperano gran parte delle prestazioni, su CPU. È il nostro scenario: backbone congelato e solo la testa riaddestrata.
4. **Attenzione al rapporto con i medici.** L'AI può **allargare** il divario per tono nei medici non specialisti (Groh 2024). Nella valutazione, e nella RQ5 se si fa, vanno misurati anche i risultati dei medici per tono.
5. **Come registrare la pelle:**
   - **fototipo** stabilito alla visita (già nelle istruzioni per gli annotatori);
   - **etnia dichiarata**, in un campo separato;
   - una misura del **tono** (ITA o scala Monk).
   
   I dataset MSKCC Skin Tone e SCIN aiutano a calibrare la misura.
6. **Il ruolo dell'ospedale diventa più chiaro.** Il pezzo che manca al mondo intero sono **dermoscopie di tumori su pelli IV–VI** e **pazienti latinoamericani con etnia e fototipo registrati**. Un ospedale latinoamericano che raccoglie questi dati darebbe un contributo nuovo. Le istruzioni in spagnolo sono pronte; una versione in **portoghese** servirebbe per il Brasile.
7. **Dataset asiatici:** quelli con dermoscopie esistono (Corea, Cina), ma non sono pubblici o lo sono solo in parte. Per ora la parte asiatica della RQ6 si limita alle **lesioni acrali** (BALD) e, se possibile, a Asan/Hallym ⚠️.
