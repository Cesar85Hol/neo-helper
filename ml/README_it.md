# ml/ — codice di machine learning di Neo Helper

[English](README.md) · **Italiano** · [Español](README_es.md)

Qui vive il codice della Milestone 2 in poi: dati, baseline con backbone congelati, valutazione.

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

Esegue i test. Ogni test è elencato per nome con il suo esito (`PASSED`, `FAILED` o `SKIPPED`), seguito da una riga di riepilogo.

## Cosa controllano i test
| File | Cosa controlla |
|------|----------------|
| `tests/test_environment.py` | cartella dei dati da `NEO_DATA_DIR`; scelta del dispositivo (MPS, CUDA, CPU) ed errori per dispositivi sconosciuti o assenti; vettori di immagini finte su ogni dispositivo; stessi vettori su CPU e GPU |
| `tests/test_data.py` | voci del catalogo complete; download con checksum, salto se il file c'è già, rifiuto dei file corrotti; estrazione sicura degli zip; la prova di download non scarica nulla; conversione di HAM10000; controlli del registro |

I test non usano mai la rete né i dataset veri: lavorano su piccoli file finti in una cartella temporanea.

## Se il progetto è in una cartella sincronizzata con iCloud
Su macOS, iCloud segna come "nascosti" alcuni file dentro `ml/.venv`, e Python 3.12 li ignora: il risultato è l'errore `ModuleNotFoundError: No module named 'neo'`. Un collegamento simbolico non basta: iCloud lo rinomina.

La soluzione vera è tenere il progetto **fuori** dalle cartelle sincronizzate. In alternativa, si dice a `uv` di mettere l'ambiente altrove, in ogni terminale prima degli altri comandi:

```bash
export UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml"
```

Poi `uv sync` e gli altri comandi funzionano come sopra. Da qualunque cartella del repository, in una riga sola:

```bash
UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml" uv run --project ml pytest ml/tests
```

## In VS Code
1. Aprire la cartella del progetto.
2. `Cmd+Shift+P` → **Python: Select Interpreter** → scegliere `ml/.venv/bin/python` (oppure `~/.venvs/neo-helper-ml/bin/python` nel caso di iCloud).
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

Dataset, licenze e formato del registro sono descritti in [data/README_it.md](data/README_it.md).

## Struttura
| Percorso | Contenuto |
|----------|-----------|
| `pyproject.toml` | dipendenze e configurazione degli strumenti |
| `uv.lock` | versioni esatte, generato da `uv` (non si modifica a mano) |
| `neo/paths.py` | cartelle dei dati |
| `neo/device.py` | scelta del dispositivo: MPS, CUDA o CPU |
| `neo/check.py` | controllo dell'ambiente (`neo-check`) |
| `neo/data/` | catalogo dei dataset, download, registro dati (`neo-data`) |
| `tests/` | test automatici |

## Comandi utili
| Scopo | Comando |
|-------|---------|
| Vedere i dataset e cosa c'è su disco | `uv run neo-data list` |
| Aggiungere una libreria | `uv add nome` |
| Aggiungere uno strumento di sviluppo | `uv add --dev nome` |
| Controllare lo stile | `uv run ruff check .` |
| Riallineare l'ambiente al file di blocco | `uv sync` |
