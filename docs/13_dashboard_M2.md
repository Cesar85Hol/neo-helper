# 13 — Dashboard della Milestone 2 (in corso)

> Versione interattiva in italiano, inglese e spagnolo: [dashboard/neo_helper_M2.html](dashboard/neo_helper_M2.html). Si apre con un doppio clic, senza connessione.
> Il riassunto a parole della prima parte della M2 è in [12_riassunto_M2_parte1.md](12_riassunto_M2_parte1.md).

## A cosa serve
Collega in un solo posto i **dati** scaricati, il **codice** che li trasforma e i **test** che lo controllano, così si può seguire il lavoro senza leggere ogni file.

## Le sette viste
| Vista | Cosa mostra |
|-------|-------------|
| Dove siamo | Numeri chiave, stato dei pacchetti P1–P6, cosa è successo dal download dei dati |
| Flusso | I sei passi della pipeline: cosa entra, comando e moduli, cosa esce, test che lo controllano |
| Codice | Mappa dei moduli (chi usa chi); per ogni modulo cosa fa, funzioni, chi lo usa, test |
| Test | Ogni test con il suo esito e, a parole, cosa controlla |
| Dati | Cosa c'è in `~/neo-helper-data` con le dimensioni; dataset e licenze; divisione per lesione |
| Risultati e decisioni | Le scoperte dell'EDA, il controllo di MONET, decisioni con data, punti aperti |
| Come seguire | Comandi da provare e storia dei commit su GitHub |

## Come resta aggiornata
- I **fatti** (moduli, funzioni, collegamenti, esiti dei test, dati su disco, commit) non sono scritti a mano: li raccoglie `tools/build_dashboard_m2.py`, che esegue anche tutti i test. Si lancia a fine pacchetto:

  ```bash
  UV_PROJECT_ENVIRONMENT="$HOME/.venvs/neo-helper-ml" uv run --project ml python tools/build_dashboard_m2.py
  ```
- I **testi** (cosa fa un modulo, cosa controlla un test, scoperte, decisioni) sono scritti a mano nelle tre lingue. Se nasce un modulo nuovo senza descrizione, la dashboard lo segnala.
- Nessun percorso personale viene salvato: la cartella dei dati compare come `~/neo-helper-data`.
- A fine milestone (pacchetto P6, issue #36) diventa la dashboard di uscita dalla M2.
