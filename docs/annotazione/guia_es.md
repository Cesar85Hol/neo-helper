# Neo Helper — Guía para la anotación de imágenes

> Versión 0.1 (borrador, 2026-11-04) · Otros idiomas: [Italiano](linee_guida_it.md) · [English](guidelines_en.md)
> Documento para los médicos que anotan imágenes de lesiones cutáneas para el proyecto de investigación Neo Helper.

## 1. Para qué sirve
Neo Helper es un proyecto de investigación sobre un sistema de apoyo al diagnóstico de lesiones cutáneas. Los modelos de inteligencia artificial tienen más dificultades:
- con las pieles **intermedias y oscuras**;
- con las lesiones **raras o atípicas**;
- con las imágenes que tienen **artefactos** (marcas de rotulador, reglas);
- cuando las etiquetas de entrenamiento son **inciertas**.

Sus anotaciones sirven para **medir** estos problemas y **corregirlos**. No hace falta volver a diagnosticar cada caso. Lo que necesitamos saber de cada imagen es **qué tan fiable** es el diagnóstico y **qué características** tiene la imagen.

## 2. Antes de empezar: reglas básicas
1. **Privacidad.** Ningún dato identificativo (nombre, fecha de nacimiento, número de historia clínica) en los campos ni en el nombre de los archivos. Usar solo los códigos seudónimos proporcionados. Nada de rostros, tatuajes reconocibles ni joyas en la imagen; si aparecen, señalar la imagen.
2. **Ética.** Anotar solo imágenes cubiertas por la aprobación del comité de ética y el consentimiento de los pacientes, según las normas del hospital.
3. **Independencia.** **No** mirar el resultado de ninguna inteligencia artificial antes de anotar. Si un caso está asignado a dos anotadores, no comentarlo hasta que ambos hayan terminado.
4. **Honestidad sobre la incertidumbre.** "No lo sé" es una respuesta válida y útil. No adivinar.
5. **Un registro por lesión y por imagen.** Si la misma lesión tiene varias imágenes, usar el mismo `lesion_id`.

## 3. Campos que hay que completar

### 3.1 Identificadores e imagen (obligatorios)
| Campo | Valores | Notas |
|-------|---------|-------|
| `image_id` | código proporcionado | — |
| `lesion_id` | código seudónimo | El mismo para todas las imágenes de la misma lesión |
| `patient_id` | código seudónimo | El mismo para todas las lesiones del mismo paciente |
| `modality` | `dermoscopic_polarized` / `dermoscopic_nonpolarized` / `clinical` / `smartphone` | Tipo de imagen |
| `image_quality` | `good` / `acceptable` / `poor` | `poor` = no utilizable para el diagnóstico |

### 3.2 Diagnóstico y origen del diagnóstico (obligatorios) — *el campo más importante*
| Campo | Valores |
|-------|---------|
| `diagnosis` | uno de los códigos de la tabla siguiente |
| `diagnosis_detail` | texto libre opcional (p. ej. "melanoma in situ", "nevo de Spitz") |
| `label_source` | `histopathology` / `followup` / `consensus` / `single_expert` |

**Códigos de diagnóstico**
| Código | Diagnóstico |
|--------|-------------|
| `MEL` | Melanoma (incluido in situ) |
| `NV` | Nevo melanocítico |
| `BCC` | Carcinoma basocelular |
| `AKIEC` | Queratosis actínica / carcinoma intraepitelial (enfermedad de Bowen) |
| `SCC` | Carcinoma espinocelular (escamoso) invasivo |
| `BKL` | Lesión queratósica benigna (queratosis seborreica, léntigo solar, queratosis liquenoide) |
| `DF` | Dermatofibroma |
| `VASC` | Lesión vascular |
| `OTHER` | Otro diagnóstico (especificar en `diagnosis_detail`) |

**Cómo elegir `label_source`**
- `histopathology`: diagnóstico confirmado por histología. **Obligatorio para las lesiones malignas** cuando esté disponible.
- `followup`: lesión benigna no extirpada, **estable** en el seguimiento con dermatoscopia digital (indicar los meses en `followup_months`).
- `consensus`: acuerdo de al menos dos dermatólogos, sin histología.
- `single_expert`: diagnóstico de un solo dermatólogo, sin histología ni seguimiento.

### 3.3 Fototipo y datos del paciente (obligatorios si están disponibles)
| Campo | Valores | Notas |
|-------|---------|-------|
| `fitzpatrick` | `I`–`VI` / `unknown` | **Determinado en la consulta o a partir de la historia clínica**, no a partir de la foto |
| `fitzpatrick_method` | `in_person` / `chart` / `photo` | Cómo se determinó |
| `ethnicity_self_reported` | texto, opcional | Tal como la declara el paciente. **No** es lo mismo que el fototipo |
| `age` | años (también por rango: 30–39) | — |
| `sex` | `F` / `M` / `other` / `unknown` | — |
| `site` | `head_neck` / `trunk` / `upper_limb` / `lower_limb` / `palm_sole` / `nail` / `mucosa` / `genital` / `other` | Localización anatómica |

**Escala de Fitzpatrick (resumen)**
| Fototipo | Reacción al sol | Piel típica |
|----------|-----------------|-------------|
| I | Siempre se quema, nunca se broncea | Muy clara |
| II | Se quema con frecuencia, se broncea poco | Clara |
| III | A veces se quema, se broncea gradualmente | Intermedia clara |
| IV | Rara vez se quema, se broncea bien | Intermedia oscura / trigueña |
| V | Muy rara vez se quema, se broncea mucho | Oscura |
| VI | Nunca se quema | Muy oscura |

### 3.4 Artefactos (obligatorios, pocos segundos)
Marcar **sí/no** para cada uno:
`ink_marking` (marcas de rotulador) · `ruler` (regla o escala) · `hair` (vello sobre la lesión) · `bubbles` (burbujas del líquido de inmersión) · `dark_corners` (borde negro o viñeteado del dermatoscopio) · `blur` (desenfoque) · `glare` (reflejos) · `other_artifact` (especificar).

### 3.5 Diagnóstico diferencial y seguridad (obligatorios)
| Campo | Valores |
|-------|---------|
| `ddx_1`, `ddx_2`, `ddx_3` | sus 3 primeras hipótesis **mirando solo la imagen** (códigos de arriba) |
| `confidence` | de 1 a 5 (ver abajo) |

| Valor | Significado |
|-------|-------------|
| 1 | Pura suposición |
| 2 | Poco seguro |
| 3 | Bastante seguro |
| 4 | Seguro |
| 5 | Totalmente seguro, caso de libro |

Estos campos miden **qué tan difícil** es el caso para un médico. Hay que completarlos también cuando se conoce el diagnóstico histológico: responder como si no se conociera.

### 3.6 Opcionales (solo si se solicitan para su lote)
- **Lista de 7 puntos** (solo imágenes dermatoscópicas de lesiones melanocíticas). Marcar presente/ausente:
  - criterios mayores (2 puntos cada uno): retículo pigmentado atípico · velo azul-blanquecino · patrón vascular atípico;
  - criterios menores (1 punto cada uno): proyecciones (estrías) irregulares · puntos/glóbulos irregulares · manchas (*blotches*) irregulares · estructuras de regresión.
- **Máscara de segmentación:** contorno de la lesión en la herramienta de anotación. El borde sigue la pigmentación visible; el vello y las marcas de rotulador quedan fuera.

## 4. Doble lectura
Alrededor del 10–20% de las imágenes se asigna a **dos anotadores**, sin avisar. Sirve para medir el acuerdo entre médicos. No es una evaluación de quien anota.

## 5. Casos particulares
- **Imagen no utilizable:** `image_quality = poor`, completar solo los artefactos y pasar a la siguiente.
- **Varias lesiones en la misma imagen:** anotar solo la lesión central; indicarlo en `notes`.
- **Diagnóstico que no está en la lista:** `OTHER` + `diagnosis_detail`.
- **Duda sobre el fototipo:** `unknown` es mejor que una suposición.

## 6. Formato de entrega
Un archivo CSV (o la exportación de la herramienta de anotación) con un encabezado como este:

```
image_id,lesion_id,patient_id,modality,image_quality,diagnosis,diagnosis_detail,label_source,followup_months,fitzpatrick,fitzpatrick_method,ethnicity_self_reported,age,sex,site,ink_marking,ruler,hair,bubbles,dark_corners,blur,glare,other_artifact,ddx_1,ddx_2,ddx_3,confidence,annotator_id,notes
```

## 7. Contacto
Preguntas sobre la anotación: ⚠️ por definir con el hospital.
