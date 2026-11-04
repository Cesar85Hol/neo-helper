# Neo Helper — Istruzioni per l'annotazione delle immagini

> Versione 0.1 (bozza, 2026-11-04) · Altre lingue: [English](guidelines_en.md) · [Español](guia_es.md)
> Documento per i medici che annotano immagini di lesioni cutanee per il progetto di ricerca Neo Helper.

## 1. A cosa serve
Neo Helper è un progetto di ricerca su un sistema di supporto alla diagnosi delle lesioni cutanee. I modelli di intelligenza artificiale fanno più fatica:
- sulle pelli **intermedie e scure**;
- sulle lesioni **rare o atipiche**;
- sulle immagini con **artefatti** (segni di penna, righelli);
- quando le etichette di addestramento sono **incerte**.

Le vostre annotazioni servono a **misurare** questi problemi e a **correggerli**. Non serve rifare la diagnosi di ogni caso: serve sapere, per ogni immagine, **quanto è affidabile** la diagnosi e **che caratteristiche** ha l'immagine.

## 2. Prima di iniziare: regole di base
1. **Privacy.** Nessun dato identificativo (nome, data di nascita, numero di cartella) nei campi o nel nome dei file. Usare solo i codici pseudonimi forniti. Niente volti, tatuaggi riconoscibili o gioielli nell'immagine: in quel caso segnalare l'immagine.
2. **Etica.** Annotare solo immagini coperte dall'approvazione del comitato etico e dal consenso dei pazienti, secondo le regole dell'ospedale.
3. **Indipendenza.** **Non** guardare l'output di un'intelligenza artificiale prima di annotare. Se un caso è assegnato a due annotatori, non confrontarsi prima di aver finito.
4. **Onestà sull'incertezza.** "Non so" è una risposta valida e utile. Non indovinare.
5. **Un record per lesione e per immagine.** Se la stessa lesione ha più immagini, usare lo stesso `lesion_id`.

## 3. I campi da compilare

### 3.1 Identificativi e immagine (obbligatori)
| Campo | Valori | Note |
|-------|--------|------|
| `image_id` | codice fornito | — |
| `lesion_id` | codice pseudonimo | Lo stesso per tutte le immagini della stessa lesione |
| `patient_id` | codice pseudonimo | Lo stesso per tutte le lesioni dello stesso paziente |
| `modality` | `dermoscopic_polarized` / `dermoscopic_nonpolarized` / `clinical` / `smartphone` | Tipo di immagine |
| `image_quality` | `good` / `acceptable` / `poor` | `poor` = non utilizzabile per la diagnosi |

### 3.2 Diagnosi e fonte della diagnosi (obbligatori) — *il campo più importante*
| Campo | Valori |
|-------|--------|
| `diagnosis` | uno dei codici della tabella sotto |
| `diagnosis_detail` | testo libero facoltativo (es. "melanoma in situ", "nevo di Spitz") |
| `label_source` | `histopathology` / `followup` / `consensus` / `single_expert` |

**Codici di diagnosi**
| Codice | Diagnosi |
|--------|----------|
| `MEL` | Melanoma (incluso in situ) |
| `NV` | Nevo melanocitico |
| `BCC` | Carcinoma basocellulare |
| `AKIEC` | Cheratosi attinica / carcinoma intraepiteliale (Bowen) |
| `SCC` | Carcinoma squamocellulare invasivo |
| `BKL` | Lesione cheratosica benigna (cheratosi seborroica, lentigo solare, cheratosi lichenoide) |
| `DF` | Dermatofibroma |
| `VASC` | Lesione vascolare |
| `OTHER` | Altra diagnosi (specificare in `diagnosis_detail`) |

**Come scegliere `label_source`**
- `histopathology`: diagnosi confermata dall'esame istologico. **Obbligatoria per i tumori**, se disponibile.
- `followup`: lesione benigna non asportata, **stabile** al controllo dermoscopico digitale (indicare i mesi in `followup_months`).
- `consensus`: accordo di almeno due dermatologi, senza istologia.
- `single_expert`: diagnosi di un solo dermatologo, senza istologia né follow-up.

### 3.3 Fototipo e dati del paziente (obbligatori se disponibili)
| Campo | Valori | Note |
|-------|--------|------|
| `fitzpatrick` | `I`–`VI` / `unknown` | **Stabilito alla visita o dalla cartella clinica**, non dalla foto |
| `fitzpatrick_method` | `in_person` / `chart` / `photo` | Come è stato stabilito |
| `ethnicity_self_reported` | testo, facoltativo | Come dichiarata dal paziente. **Non** è la stessa cosa del fototipo |
| `age` | anni (anche per fascia: 30–39) | — |
| `sex` | `F` / `M` / `other` / `unknown` | — |
| `site` | `head_neck` / `trunk` / `upper_limb` / `lower_limb` / `palm_sole` / `nail` / `mucosa` / `genital` / `other` | Sede anatomica |

**Scala di Fitzpatrick (riassunto)**
| Fototipo | Reazione al sole | Pelle tipica |
|----------|------------------|--------------|
| I | Si scotta sempre, non si abbronza mai | Molto chiara |
| II | Si scotta spesso, si abbronza poco | Chiara |
| III | Si scotta a volte, si abbronza gradualmente | Intermedia chiara |
| IV | Si scotta raramente, si abbronza bene | Intermedia scura / olivastra |
| V | Si scotta molto raramente, si abbronza molto | Scura |
| VI | Non si scotta mai | Molto scura |

### 3.4 Artefatti (obbligatori, pochi secondi)
Segnare **sì/no** per ciascuno:
`ink_marking` (segni di penna) · `ruler` (righello o scala) · `hair` (peli sopra la lesione) · `bubbles` (bolle del liquido d'immersione) · `dark_corners` (bordo nero o vignettatura del dermatoscopio) · `blur` (sfocatura) · `glare` (riflessi) · `other_artifact` (specificare).

### 3.5 Diagnosi differenziale e sicurezza (obbligatori)
| Campo | Valori |
|-------|--------|
| `ddx_1`, `ddx_2`, `ddx_3` | le vostre prime 3 ipotesi **guardando solo l'immagine** (codici sopra) |
| `confidence` | da 1 a 5 (vedi sotto) |

| Valore | Significato |
|--------|-------------|
| 1 | Pura ipotesi |
| 2 | Poco sicuro |
| 3 | Abbastanza sicuro |
| 4 | Sicuro |
| 5 | Certo, caso da manuale |

Questi campi misurano **quanto è difficile** il caso per un medico. Vanno compilati anche quando la diagnosi istologica è nota: rispondete come se non la conosceste.

### 3.6 Facoltativi (solo se richiesto per il vostro lotto)
- **7-point checklist** (solo immagini dermoscopiche di lesioni melanocitiche). Segnare presente/assente:
  - criteri maggiori (2 punti ciascuno): reticolo pigmentato atipico · velo blu-biancastro · pattern vascolare atipico;
  - criteri minori (1 punto ciascuno): strie irregolari · punti/globuli irregolari · macchie (*blotches*) irregolari · strutture di regressione.
- **Maschera di segmentazione:** contorno della lesione nello strumento di annotazione. Il bordo segue la pigmentazione visibile; i peli e i segni di penna restano fuori.

## 4. Doppia lettura
Circa il 10–20% delle immagini viene assegnato a **due annotatori**, senza dirlo. Serve a misurare l'accordo tra medici. Non è una valutazione di chi annota.

## 5. Casi particolari
- **Immagine non utilizzabile:** `image_quality = poor`, compilare solo gli artefatti e passare oltre.
- **Più lesioni nella stessa immagine:** annotare solo la lesione centrale; segnalare in `notes`.
- **Diagnosi non nella lista:** `OTHER` + `diagnosis_detail`.
- **Dubbio sul fototipo:** `unknown` è meglio di un'ipotesi.

## 6. Formato di consegna
Un file CSV (o l'esportazione dello strumento di annotazione) con un'intestazione come questa:

```
image_id,lesion_id,patient_id,modality,image_quality,diagnosis,diagnosis_detail,label_source,followup_months,fitzpatrick,fitzpatrick_method,ethnicity_self_reported,age,sex,site,ink_marking,ruler,hair,bubbles,dark_corners,blur,glare,other_artifact,ddx_1,ddx_2,ddx_3,confidence,annotator_id,notes
```

## 7. Contatti
Per domande sull'annotazione: ⚠️ da definire con l'ospedale.
