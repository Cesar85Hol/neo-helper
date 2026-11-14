# ml/data — provenienza e licenze dei dati

[English](README.md) · **Italiano** · [Español](README_es.md)

I dati **non** stanno nel repository: stanno nella cartella `NEO_DATA_DIR` (predefinita `~/neo-helper-data`), sottocartella `raw/<dataset>/`. Qui si annota da dove viene ogni dataset, con quale licenza, e come si scarica.

Il codice è in `ml/neo/data/`:

| File | Contenuto |
|------|-----------|
| `sources.py` | catalogo: per ogni file indirizzo, dimensione e checksum MD5 |
| `download.py` | download con verifica ed estrazione sicura degli zip |
| `registry.py` | formato del registro dati comune e controlli |
| `ham10000.py` | convertitore di HAM10000 verso il registro |
| `cli.py` | comando `neo-data` |

## Comandi
Dalla cartella `ml/`:

| Scopo | Comando |
|-------|---------|
| Vedere il catalogo e cosa c'è su disco | `uv run neo-data list` |
| **Prova** di download: mostra file e dimensioni, non scarica | `uv run neo-data download ham10000` |
| Download vero | `uv run neo-data download ham10000 --yes` |
| Altri gruppi di file | `uv run neo-data download ham10000 --groups segmentations --yes` |
| Estrarre le immagini e costruire il registro | `uv run neo-data registry ham10000` |

Un file già presente con dimensione e checksum giusti non viene riscaricato. Un download che non corrisponde al catalogo viene rifiutato e cancellato.

## Dataset

### HAM10000
- **Cos'è:** 10.015 immagini dermoscopiche di 7.470 lesioni, 7 classi (Tschandl, Rosendahl e Kittler, Scientific Data 2018).
- **Fonte:** Harvard Dataverse, DOI [10.7910/DVN/DBW86T](https://doi.org/10.7910/DVN/DBW86T), versione 4.0 del 2023-02-07.
- **Licenza:** CC BY-NC 4.0 (letta nei termini d'uso del Dataverse l'11 novembre 2026).
- **Come si scarica:** automatico, senza registrazione.

| Gruppo | File | Dimensione |
|--------|------|-----------|
| `core` | `HAM10000_images_part_1.zip` | 1,37 GB |
| `core` | `HAM10000_images_part_2.zip` | 1,40 GB |
| `core` | `HAM10000_metadata.csv` | 0,7 MB |
| `segmentations` | `HAM10000_segmentations_lesion_tschandl.zip` | 10,8 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_Images.zip` | 421 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_GroundTruth.csv` | 0,1 MB |

Il gruppo `isic2018_test` è il test ufficiale della sfida ISIC 2018 (compito 3), pubblicato con le etichette nello stesso Dataverse.

### Annotazioni di Chanda 2024
- **Cos'è:** criteri dermoscopici localizzati da dermatologi su immagini di HAM10000 (melanomi e nevi), più i dati dello studio con i lettori.
- **Fonte:** Figshare, DOI [10.6084/m9.figshare.23766477](https://doi.org/10.6084/m9.figshare.23766477), versione 9 del 2025-07-14.
- **Licenza:** CC BY 4.0.
- **Come si scarica:** automatico.

| Gruppo | File | Dimensione |
|--------|------|-----------|
| `core` | `annotations_gt.zip`, `metadata_gt.csv`, `README.md` | 12,7 MB |
| `reader_study` | `metadata_phase1–3.csv`, `Source Data.zip`, `Datasets.zip` | 5,5 MB |

### Scaricati a mano (accesso con registrazione)
| Dataset | File in `raw/` | Licenza | Vincoli |
|---------|----------------|---------|---------|
| **DDI** (Stanford) | `ddi/ddidiversedermatologyimages.zip` (226 MB) | Stanford Research Use Agreement | Solo ricerca personale non commerciale; vietato ridistribuire immagini e link; vietati i lavori derivati; ogni utente si registra da sé. ⚠️ Letti solo i primi sei punti dell'accordo |
| **Derm7pt** | `derm7pt/release_v0.zip` (152 MB) | CC BY-NC-ND 4.0 | Solo uso non commerciale; non si ridistribuisce modificato |

Convertitori e controlli per questi due arrivano con il pacchetto P5.

## Il registro dati
Un file CSV per dataset in `registry/`, una riga per immagine, **le stesse colonne per tutti**. Tutto ciò che viene dopo (EDA, divisioni, vettori, valutazione per sottogruppo) legge solo il registro.

| Colonna | Significato |
|---------|-------------|
| `uid` | identificativo unico: `<source>/<image_id>` |
| `source` | dataset, per esempio `ham10000` |
| `image_id` | identificativo dato dagli autori |
| `file` | percorso dell'immagine, relativo a `NEO_DATA_DIR` |
| `modality` | `dermoscopic`, `clinical` o `smartphone` |
| `diagnosis` | etichetta nel vocabolario comune (sotto) |
| `diagnosis_original` | etichetta come scritta nella fonte |
| `malignant` | vero o falso, derivato da `diagnosis` |
| `label_source` | `histology`, `follow_up`, `consensus`, `confocal`, `single_expert`, `unknown` |
| `lesion_id`, `patient_id` | stessa lesione, stesso paziente |
| `centre`, `country` | centro di acquisizione e paese |
| `age`, `sex`, `site` | età, sesso, sede anatomica |
| `fitzpatrick`, `fitzpatrick_method` | fototipo 1–6 e come è stato stabilito |
| `ethnicity_self_reported` | etnia dichiarata, mai dedotta |
| `artifacts` | artefatti trovati dal controllo (penna, righello…) |
| `license`, `license_url`, `source_doi` | licenza e fonte **per immagine** |

**Vocabolario delle diagnosi** (le 7 classi di HAM10000; si estende nel pacchetto P5): `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`.

**Maligne per il punteggio di malignità:** `mel`, `bcc`, `akiec`. ⚠️ `akiec` (cheratosi attiniche e carcinoma intraepiteliale) è contata come maligna, come in Tschandl 2020: scelta da confermare prima delle baseline.

**Cosa manca in HAM10000:** identificativo del paziente, fototipo, etnia. Le colonne restano vuote.
