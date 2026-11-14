# ml/ — código de aprendizaje automático de Neo Helper

[English](README.md) · [Italiano](README_it.md) · **Español**

Aquí vive el código a partir del Hito 2: datos, líneas base con modelos congelados, evaluación.

## Requisitos
- macOS, Linux o Windows; Python 3.12 (`uv` lo descarga por sí solo).
- [`uv`](https://docs.astral.sh/uv/): en Mac, `brew install uv`.
- No hace falta GPU: todo funciona también **solo con CPU**, más despacio.

## Primer arranque
Desde la carpeta `ml/`:

```bash
uv sync
```

Crea el entorno `ml/.venv` con las versiones exactas escritas en `uv.lock`.

```bash
uv run neo-check
```

Muestra versiones, dispositivos disponibles y la carpeta de datos, y luego hace una prueba con 10 imágenes falsas.
Para probar el camino solo con CPU: `uv run neo-check --device cpu`.

```bash
uv run pytest
```

Ejecuta las pruebas. Cada prueba aparece con su nombre y su resultado (`PASSED`, `FAILED` o `SKIPPED`), seguida de una línea de resumen.

## Qué comprueban las pruebas
| Archivo | Qué comprueba |
|---------|---------------|
| `tests/test_environment.py` | carpeta de datos a partir de `NEO_DATA_DIR`; elección del dispositivo (MPS, CUDA, CPU) y errores para dispositivos desconocidos o ausentes; vectores de imágenes falsas en cada dispositivo; mismos vectores en CPU y GPU |
| `tests/test_data.py` | entradas del catálogo completas; descarga con suma de verificación, omisión si el archivo ya existe, rechazo de archivos corruptos; extracción segura de los zip; el ensayo de descarga no descarga nada; conversión de HAM10000; controles del registro |

Las pruebas nunca usan la red ni los conjuntos de datos reales: trabajan con pequeños archivos falsos en una carpeta temporal.

## Si el proyecto está en una carpeta sincronizada con iCloud
En macOS, iCloud marca como "ocultos" algunos archivos dentro de `ml/.venv`, y Python 3.12 los ignora: el resultado es el error `ModuleNotFoundError: No module named 'neo'`. Un enlace simbólico no basta: iCloud lo renombra.

La solución real es mantener el proyecto **fuera** de las carpetas sincronizadas. Como alternativa, se indica a `uv` que ponga el entorno en otro lugar, en cada terminal antes de los demás comandos:

```bash
export UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml"
```

Después, `uv sync` y los demás comandos funcionan como arriba. Desde cualquier carpeta del repositorio, en una sola línea:

```bash
UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml" uv run --project ml pytest ml/tests
```

## En VS Code
1. Abrir la carpeta del proyecto.
2. `Cmd+Shift+P` → **Python: Select Interpreter** → elegir `ml/.venv/bin/python` (o `~/.venvs/neo-helper-ml/bin/python` en el caso de iCloud).
3. En los cuadernos, elegir el mismo intérprete como kernel.

## Dónde están los datos
Los datos, los pesos de los modelos y los vectores guardados **no** están en el repositorio. Están en la carpeta indicada por la variable de entorno `NEO_DATA_DIR`; si no está definida, en `~/neo-helper-data`.

| Subcarpeta | Contenido |
|------------|-----------|
| `raw/` | conjuntos de datos tal como se descargaron |
| `registry/` | registro de datos común (una fila por imagen) y particiones |
| `weights/` | pesos de los modelos base |
| `embeddings/` | vectores guardados, un archivo por modelo y conjunto de datos |
| `mlruns/` | experimentos registrados con MLflow |

Los conjuntos de datos, las licencias y el formato del registro se describen en [data/README_es.md](data/README_es.md).

## Estructura
| Ruta | Contenido |
|------|-----------|
| `pyproject.toml` | dependencias y configuración de las herramientas |
| `uv.lock` | versiones exactas, generado por `uv` (no se edita a mano) |
| `neo/paths.py` | carpetas de datos |
| `neo/device.py` | elección del dispositivo: MPS, CUDA o CPU |
| `neo/check.py` | comprobación del entorno (`neo-check`) |
| `neo/data/` | catálogo de conjuntos de datos, descargas, registro de datos (`neo-data`) |
| `tests/` | pruebas automáticas |

## Comandos útiles
| Propósito | Comando |
|-----------|---------|
| Ver los conjuntos de datos y lo que hay en disco | `uv run neo-data list` |
| Añadir una biblioteca | `uv add nombre` |
| Añadir una herramienta de desarrollo | `uv add --dev nombre` |
| Comprobar el estilo del código | `uv run ruff check .` |
| Realinear el entorno con el archivo de bloqueo | `uv sync` |
