# Neo Helper — Image annotation guidelines

> Version 0.1 (draft, 2026-11-04) · Other languages: [Italiano](linee_guida_it.md) · [Español](guia_es.md)
> For physicians annotating images of skin lesions for the Neo Helper research project.

## 1. Purpose
Neo Helper is a research project on a decision-support system for skin lesions. AI models struggle most:
- on **intermediate and dark skin**;
- on **rare or atypical** lesions;
- on images with **artifacts** (ink markings, rulers);
- when training labels are **uncertain**.

Your annotations help us **measure** these problems and **fix** them. You do not need to re-diagnose every case. What we need to know for each image is **how reliable** the diagnosis is and **what characteristics** the image has.

## 2. Before you start: ground rules
1. **Privacy.** No identifying data (name, date of birth, record number) in any field or file name. Use only the pseudonymous codes provided. No faces, recognizable tattoos or jewelry in the image; if present, flag the image.
2. **Ethics.** Annotate only images covered by ethics committee approval and patient consent, according to hospital rules.
3. **Independence.** Do **not** look at any AI output before annotating. If a case is assigned to two annotators, do not discuss it until both have finished.
4. **Be honest about uncertainty.** "I don't know" is a valid and useful answer. Do not guess.
5. **One record per lesion and per image.** If the same lesion has several images, use the same `lesion_id`.

## 3. Fields to fill in

### 3.1 Identifiers and image (required)
| Field | Values | Notes |
|-------|--------|-------|
| `image_id` | code provided | — |
| `lesion_id` | pseudonymous code | Same for all images of the same lesion |
| `patient_id` | pseudonymous code | Same for all lesions of the same patient |
| `modality` | `dermoscopic_polarized` / `dermoscopic_nonpolarized` / `clinical` / `smartphone` | Type of image |
| `image_quality` | `good` / `acceptable` / `poor` | `poor` = not usable for diagnosis |

### 3.2 Diagnosis and label source (required) — *the most important field*
| Field | Values |
|-------|--------|
| `diagnosis` | one of the codes below |
| `diagnosis_detail` | optional free text (e.g. "melanoma in situ", "Spitz nevus") |
| `label_source` | `histopathology` / `followup` / `consensus` / `single_expert` |

**Diagnosis codes**
| Code | Diagnosis |
|------|-----------|
| `MEL` | Melanoma (including in situ) |
| `NV` | Melanocytic nevus |
| `BCC` | Basal cell carcinoma |
| `AKIEC` | Actinic keratosis / intraepithelial carcinoma (Bowen's disease) |
| `SCC` | Invasive squamous cell carcinoma |
| `BKL` | Benign keratosis-like lesion (seborrheic keratosis, solar lentigo, lichen planus-like keratosis) |
| `DF` | Dermatofibroma |
| `VASC` | Vascular lesion |
| `OTHER` | Other diagnosis (specify in `diagnosis_detail`) |

**How to choose `label_source`**
- `histopathology`: diagnosis confirmed by histology. **Required for malignant lesions** when available.
- `followup`: benign lesion not excised, **stable** at digital dermoscopy follow-up (give the months in `followup_months`).
- `consensus`: agreement of at least two dermatologists, without histology.
- `single_expert`: diagnosis by one dermatologist, without histology or follow-up.

### 3.3 Skin type and patient data (required when available)
| Field | Values | Notes |
|-------|--------|-------|
| `fitzpatrick` | `I`–`VI` / `unknown` | **Assessed at the visit or from the medical record**, not from the photo |
| `fitzpatrick_method` | `in_person` / `chart` / `photo` | How it was assessed |
| `ethnicity_self_reported` | text, optional | As reported by the patient. It is **not** the same as skin type |
| `age` | years (a range such as 30–39 is fine) | — |
| `sex` | `F` / `M` / `other` / `unknown` | — |
| `site` | `head_neck` / `trunk` / `upper_limb` / `lower_limb` / `palm_sole` / `nail` / `mucosa` / `genital` / `other` | Anatomical site |

**Fitzpatrick scale (summary)**
| Type | Reaction to sun | Typical skin |
|------|-----------------|--------------|
| I | Always burns, never tans | Very fair |
| II | Usually burns, tans minimally | Fair |
| III | Sometimes burns, tans gradually | Light intermediate |
| IV | Rarely burns, tans well | Dark intermediate / olive |
| V | Very rarely burns, tans deeply | Dark |
| VI | Never burns | Very dark |

### 3.4 Artifacts (required, a few seconds)
Mark **yes/no** for each:
`ink_marking` (pen/ink marks) · `ruler` (ruler or scale) · `hair` (hair over the lesion) · `bubbles` (immersion fluid bubbles) · `dark_corners` (black border or dermatoscope vignetting) · `blur` · `glare` (reflections) · `other_artifact` (specify).

### 3.5 Differential diagnosis and confidence (required)
| Field | Values |
|-------|--------|
| `ddx_1`, `ddx_2`, `ddx_3` | your top 3 hypotheses **from the image alone** (codes above) |
| `confidence` | 1 to 5 (see below) |

| Value | Meaning |
|-------|---------|
| 1 | Pure guess |
| 2 | Not very confident |
| 3 | Fairly confident |
| 4 | Confident |
| 5 | Certain, textbook case |

These fields measure **how hard** the case is for a physician. Fill them in even when the histological diagnosis is known: answer as if you did not know it.

### 3.6 Optional (only if requested for your batch)
- **7-point checklist** (dermoscopic images of melanocytic lesions only). Mark present/absent:
  - major criteria (2 points each): atypical pigment network · blue-whitish veil · atypical vascular pattern;
  - minor criteria (1 point each): irregular streaks · irregular dots/globules · irregular blotches · regression structures.
- **Segmentation mask:** outline of the lesion in the annotation tool. The border follows visible pigmentation; hair and ink marks stay outside.

## 4. Double reading
About 10–20% of images are assigned to **two annotators**, without notice. This measures agreement between physicians. It is not an assessment of the annotator.

## 5. Special cases
- **Unusable image:** `image_quality = poor`, fill in only the artifacts and move on.
- **Several lesions in one image:** annotate only the central lesion; note it in `notes`.
- **Diagnosis not in the list:** `OTHER` + `diagnosis_detail`.
- **Unsure about skin type:** `unknown` is better than a guess.

## 6. Delivery format
A CSV file (or the annotation tool export) with a header like this:

```
image_id,lesion_id,patient_id,modality,image_quality,diagnosis,diagnosis_detail,label_source,followup_months,fitzpatrick,fitzpatrick_method,ethnicity_self_reported,age,sex,site,ink_marking,ruler,hair,bubbles,dark_corners,blur,glare,other_artifact,ddx_1,ddx_2,ddx_3,confidence,annotator_id,notes
```

## 7. Contact
Questions about annotation: ⚠️ to be agreed with the hospital.
