# ml/data — procedencia y licencias de los datos

[English](README.md) · [Italiano](README_it.md) · **Español**

Los datos **no** están en el repositorio: están en la carpeta `NEO_DATA_DIR` (por defecto `~/neo-helper-data`), subcarpeta `raw/<dataset>/`. Aquí se anota de dónde viene cada conjunto de datos, con qué licencia y cómo se descarga.

El código está en `ml/neo/data/`:

| Archivo | Contenido |
|---------|-----------|
| `sources.py` | catálogo: dirección, tamaño y suma de verificación MD5 de cada archivo |
| `download.py` | descarga con verificación y extracción segura de los zip |
| `registry.py` | formato del registro de datos común y sus controles |
| `ham10000.py` | conversor de HAM10000 al registro |
| `cli.py` | comando `neo-data` |

## Comandos
Desde la carpeta `ml/`:

| Propósito | Comando |
|-----------|---------|
| Ver el catálogo y lo que hay en disco | `uv run neo-data list` |
| **Ensayo** de descarga: muestra archivos y tamaños, no descarga nada | `uv run neo-data download ham10000` |
| Descarga real | `uv run neo-data download ham10000 --yes` |
| Otros grupos de archivos | `uv run neo-data download ham10000 --groups segmentations --yes` |
| Extraer las imágenes y construir el registro | `uv run neo-data registry ham10000` |

Un archivo ya presente con el tamaño y la suma de verificación correctos no se vuelve a descargar. Una descarga que no coincide con el catálogo se rechaza y se borra.

## Conjuntos de datos

### HAM10000
- **Qué es:** 10.015 imágenes dermatoscópicas de 7.470 lesiones, 7 clases (Tschandl, Rosendahl y Kittler, Scientific Data 2018).
- **Fuente:** Harvard Dataverse, DOI [10.7910/DVN/DBW86T](https://doi.org/10.7910/DVN/DBW86T), versión 4.0 del 2023-02-07.
- **Licencia:** CC BY-NC 4.0 (leída en las condiciones de uso del Dataverse el 11 de noviembre de 2026).
- **Cómo se descarga:** automático, sin registro.

| Grupo | Archivo | Tamaño |
|-------|---------|--------|
| `core` | `HAM10000_images_part_1.zip` | 1,37 GB |
| `core` | `HAM10000_images_part_2.zip` | 1,40 GB |
| `core` | `HAM10000_metadata.csv` | 0,7 MB |
| `segmentations` | `HAM10000_segmentations_lesion_tschandl.zip` | 10,8 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_Images.zip` | 421 MB |
| `isic2018_test` | `ISIC2018_Task3_Test_GroundTruth.csv` | 0,1 MB |

El grupo `isic2018_test` es el conjunto de prueba oficial del desafío ISIC 2018 (tarea 3), publicado con sus etiquetas en el mismo Dataverse.

### Anotaciones de Chanda 2024
- **Qué es:** criterios dermatoscópicos localizados por dermatólogos en imágenes de HAM10000 (melanomas y nevos), más los datos del estudio con lectores.
- **Fuente:** Figshare, DOI [10.6084/m9.figshare.23766477](https://doi.org/10.6084/m9.figshare.23766477), versión 9 del 2025-07-14.
- **Licencia:** CC BY 4.0.
- **Cómo se descarga:** automático.

| Grupo | Archivo | Tamaño |
|-------|---------|--------|
| `core` | `annotations_gt.zip`, `metadata_gt.csv`, `README.md` | 12,7 MB |
| `reader_study` | `metadata_phase1–3.csv`, `Source Data.zip`, `Datasets.zip` | 5,5 MB |

### Descargados a mano (acceso con registro)
| Conjunto | Archivo en `raw/` | Licencia | Restricciones |
|----------|-------------------|----------|---------------|
| **DDI** (Stanford) | `ddi/ddidiversedermatologyimages.zip` (226 MB) | Stanford Research Use Agreement | Solo investigación personal no comercial; prohibido redistribuir imágenes y enlaces; prohibidas las obras derivadas; cada usuario se registra por su cuenta. ⚠️ Solo se leyeron los seis primeros puntos del acuerdo |
| **Derm7pt** | `derm7pt/release_v0.zip` (152 MB) | CC BY-NC-ND 4.0 | Solo uso no comercial; no se redistribuye modificado |

Los conversores y controles para estos dos llegan con el paquete P5.

## El registro de datos
Un archivo CSV por conjunto de datos en `registry/`, una fila por imagen, **las mismas columnas para todos**. Todo lo que viene después (EDA, particiones, vectores, evaluación por subgrupo) lee solo el registro.

| Columna | Significado |
|---------|-------------|
| `uid` | identificador único: `<source>/<image_id>` |
| `source` | conjunto de datos, por ejemplo `ham10000` |
| `image_id` | identificador dado por los autores |
| `file` | ruta de la imagen, relativa a `NEO_DATA_DIR` |
| `modality` | `dermoscopic`, `clinical` o `smartphone` |
| `diagnosis` | etiqueta en el vocabulario común (abajo) |
| `diagnosis_original` | etiqueta tal como aparece en la fuente |
| `malignant` | verdadero o falso, derivado de `diagnosis` |
| `label_source` | `histology`, `follow_up`, `consensus`, `confocal`, `single_expert`, `unknown` |
| `lesion_id`, `patient_id` | misma lesión, mismo paciente |
| `centre`, `country` | centro de adquisición y país |
| `age`, `sex`, `site` | edad, sexo, localización anatómica |
| `fitzpatrick`, `fitzpatrick_method` | fototipo 1–6 y cómo se estableció |
| `ethnicity_self_reported` | etnia declarada, nunca deducida |
| `artifacts` | artefactos encontrados por el control (tinta, regla…) |
| `license`, `license_url`, `source_doi` | licencia y fuente **por imagen** |

**Vocabulario de diagnósticos** (las 7 clases de HAM10000; se amplía en el paquete P5): `akiec`, `bcc`, `bkl`, `df`, `mel`, `nv`, `vasc`.

**Malignas para la puntuación de malignidad:** `mel`, `bcc`, `akiec`. ⚠️ `akiec` (queratosis actínicas y carcinoma intraepitelial) se cuenta como maligna, como en Tschandl 2020: por confirmar antes de las líneas base.

**Lo que falta en HAM10000:** identificador del paciente, fototipo, etnia. Las columnas quedan vacías.
