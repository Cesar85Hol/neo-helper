# ml/ — codice di machine learning di Neo Helper

Qui vive il codice della Milestone 2 in poi: dati, baseline con backbone congelati, valutazione.
Il codice è in inglese; questa pagina spiega in italiano come usarlo.

## Cosa serve
- macOS, Linux o Windows; Python 3.12 (lo scarica `uv` da solo).
- [`uv`](https://docs.astral.sh/uv/): sul Mac `brew install uv`.
- Nessuna GPU obbligatoria: tutto funziona anche **solo su CPU**, più lentamente.

## Primo avvio
Dalla cartella `ml/`:

```bash
uv sync
```

Crea l'ambiente `ml/.venv` con le versioni esatte scritte in `uv.lock`.

```bash
uv run neo-check
```

Stampa versioni, dispositivi disponibili e cartella dei dati, poi fa una prova con 10 immagini finte.
Per provare il percorso solo CPU: `uv run neo-check --device cpu`.

```bash
uv run pytest
```

Esegue i test.

## In VS Code
1. Aprire la cartella del progetto.
2. `Cmd+Shift+P` → **Python: Select Interpreter** → scegliere `ml/.venv/bin/python`.
3. Nei notebook, scegliere lo stesso interprete come kernel.

## Dove stanno i dati
Dati, pesi dei modelli e vettori salvati **non** stanno nel repository. Stanno nella cartella indicata dalla variabile d'ambiente `NEO_DATA_DIR`; se non è impostata, in `~/neo-helper-data`.

| Sottocartella | Contenuto |
|---------------|-----------|
| `raw/` | dataset come scaricati |
| `registry/` | registro dati comune (una riga per immagine) e divisioni |
| `weights/` | pesi dei backbone |
| `embeddings/` | vettori salvati, un file per backbone e dataset |
| `mlruns/` | esperimenti tracciati con MLflow |

## Struttura
| Percorso | Contenuto |
|----------|-----------|
| `pyproject.toml` | dipendenze e configurazione degli strumenti |
| `uv.lock` | versioni esatte, generato da `uv` (non si modifica a mano) |
| `neo/paths.py` | cartelle dei dati |
| `neo/device.py` | scelta del dispositivo: MPS, CUDA o CPU |
| `neo/check.py` | controllo dell'ambiente (`neo-check`) |
| `tests/` | test automatici |

## Comandi utili
| Scopo | Comando |
|-------|---------|
| Aggiungere una libreria | `uv add nome` |
| Aggiungere uno strumento di sviluppo | `uv add --dev nome` |
| Controllare lo stile | `uv run ruff check .` |
| Riallineare l'ambiente al file di blocco | `uv sync` |
