# ml/data — provenance and licences of the data

**English** · [Italiano](README_it.md) · [Español](README_es.md)

The data is **not** in the repository: it is in the `NEO_DATA_DIR` folder (default `~/neo-helper-data`), sub-folder `raw/<dataset>/`. This page records where each dataset comes from, under which licence, and how it is downloaded.

The code is in `ml/neo/data/`:

| File | Content |
|------|---------|
| `sources.py` | catalogue: address, size and MD5 checksum of every file |
| `download.py` | download with verification and safe zip extraction |
| `registry.py` | format of the common data registry and its checks |
| `ham10000.py` | converter from HAM10000 to the registry |
| `cli.py` | the `neo-data` command |

## Commands
From the `ml/` folder:

| Purpose | Command |
|---------|---------|
| Show the catalogue and what is on disk | `uv run neo-data list` |
| **Dry run** of a download: shows files and sizes, downloads nothing | `uv run neo-data download ham10000` |
| Real download | `uv run neo-data download ham10000 --yes` |
| Other file groups | `uv run neo-data download ham10000 --groups segmentations --yes` |
| Extract the images and build the registry | `uv run neo-data registry ham10000` |

A file already present with the right size and checksum is not downloaded again. A download that does not match the catalogue is rejected and deleted.

## Datasets

### HAM10000
- **What it is:** 10,015 dermoscopic images of 7,470 lesions, 7 classes (Tschandl, Rosendahl and Kittler, Scientific Data 2018).
- **Source:** Harvard Dataverse, DOI [10.7910/DVN/DBW86T](https://doi.org/10.7910/DVN/DBW86T), version 4.0 of 2023-02-07.
- **Licence:** CC BY-NC 4.0 (read in the Dataverse terms of use on 11 November 2026).
- **How to download:** automatic, no registration.

| Group | File | Size |
|-------|------|------|
| `core` | `HAM10000_images_part_1.zip` | 1.37 GB |
| `core` | `HAM10000_images_part_2.zip` | 1.40 GB |
| `core` | `HAM10000_metadata.csv` | 0.7 MB |
| `segmentations` | `HAM10000_segmentations_lesion_tschandl.zip` | 10.8 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_Images.zip` | 421 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_GroundTruth.csv` | 0.1 MB |

The `isic2018_test` group is the official test set of the ISIC 2018 challenge (task 3), published with its labels in the same Dataverse.

### Chanda 2024 annotations
- **What it is:** dermoscopic criteria localised by dermatologists on HAM10000 images (melanomas and nevi), plus the reader-study data.
- **Source:** Figshare, DOI [10.6084/m9.figshare.23766477](https://doi.org/10.6084/m9.figshare.23766477), version 9 of 2025-07-14.
- **Licence:** CC BY 4.0.
- **How to download:** automatic.

| Group | File | Size |
|-------|------|------|
| `core` | `annotations_gt.zip`, `metadata_gt.csv`, `README.md` | 12.7 MB |
| `reader_study` | `metadata_phase1–3.csv`, `Source Data.zip`, `Datasets.zip` | 5.5 MB |

### Downloaded by hand (access with registration)
| Dataset | File in `raw/` | Licence | Constraints |
|---------|----------------|---------|-------------|
| **DDI** (Stanford) | `ddi/ddidiversedermatologyimages.zip` (226 MB) | Stanford Research Use Agreement | Personal non-commercial research only; no redistribution of images or links; no derivative works; every user registers individually. ⚠️ Only the first six points of the agreement were read |
| **Derm7pt** | `derm7pt/release_v0.zip` (152 MB) | CC BY-NC-ND 4.0 | Non-commercial use only; not redistributed in modified form |

Converters and checks for these two come with package P5.

## The data registry
One CSV file per dataset in `registry/`, one row per image, **the same columns for all**. Everything that follows (EDA, splits, embeddings, evaluation by subgroup) reads only the registry.

| Column | Meaning |
|--------|---------|
| `uid` | unique identifier: `<source>/<image_id>` |
| `source` | dataset, for example `ham10000` |
| `image_id` | identifier given by the authors |
| `file` | image path, relative to `NEO_DATA_DIR` |
| `modality` | `dermoscopic`, `clinical` or `smartphone` |
| `diagnosis` | label in the common vocabulary (below) |
| `diagnosis_original` | label as written in the source |
| `malignant` | true or false, derived from `diagnosis` |
| `label_source` | `histology`, `follow_up`, `consensus`, `confocal`, `single_expert`, `unknown` |
| `lesion_id`, `patient_id` | same lesion, same patient |
| `centre`, `country` | acquisition centre and country |
| `age`, `sex`, `site` | age, sex, anatomical site |
| `fitzpatrick`, `fitzpatrick_method` | phototype 1–6 and how it was established |
| `ethnicity_self_reported` | self-reported ethnicity, never inferred |
| `artifacts` | artifacts found by the audit (ink, ruler…) |
| `license`, `license_url`, `source_doi` | licence and source **per image** |

**Diagnosis vocabulary** (the 7 classes of HAM10000; extended in package P5): `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`.

**Malignant for the malignancy score:** `mel`, `bcc`, `akiec`. ⚠️ `akiec` (actinic keratoses and intraepithelial carcinoma) is counted as malignant, as in Tschandl 2020: to be confirmed before the baselines.

**Missing in HAM10000:** patient identifier, phototype, ethnicity. The columns stay empty.
