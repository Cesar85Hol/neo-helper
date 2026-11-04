# Bhagwat et al., 2026 — LLM multimodali generalisti, fototipo e diagnosi

- **Rivista:** *Bioengineering (Basel)* 13(8):932 (2026) · [DOI 10.3390/bioengineering13080932](https://doi.org/10.3390/bioengineering13080932) · PMID 42649821 · PMC13509600
- **Gruppo:** Indiana University School of Medicine
- **Testo letto:** **completo** (PMC, 2026-11-04), senza il materiale supplementare (modelli di prompt, ontologia di punteggio, matrici di confusione complete). Scelto come esempio recente e ben costruito di valutazione di LLM generalisti su immagini dermatologiche, perché usa un dataset con **biopsia** (DDI, vedi §4).

## In una frase
Due LLM multimodali commerciali, messi alla prova su 656 foto con diagnosi confermata da biopsia, **non** sono adatti a un uso diagnostico autonomo. Sovrastimano spesso il tumore, e dire al modello il fototipo del paziente **non aiuta**.

## Cosa hanno fatto
- **Dati:** le **656 immagini cliniche del dataset DDI** (570 pazienti, Stanford, tutte con biopsia). Il fototipo è dato in tre gruppi:

  | Gruppo | Immagini | Benigne | Maligne |
  |--------|----------|---------|---------|
  | I–II | 208 | 159 | 49 |
  | III–IV | 241 | 167 | 74 |
  | V–VI | 207 | 159 | 48 |

- **Modelli:** ChatGPT 5.2 (licenza Edu) e Gemini 3.1 Pro, usati **dal browser** in chat temporanea, febbraio–marzo 2026. Non si controllano temperatura, compressione dell'immagine né istruzioni nascoste.
- **Prompt fisso:** "sei un assistente diagnostico di dermatologia, dai le **3 diagnosi più probabili** in ordine, senza spiegazioni".
- **Quattro condizioni** per ogni immagine:
  - nessun fototipo;
  - il fototipo **corretto**;
  - due fototipi **sbagliati**, uno **vicino** al vero e uno **estremo** (per esempio I–II indicato come V–VI).
- **5.248 valutazioni** in tutto.
- **Punteggio da 0 a 3:**
  - 3 se la diagnosi giusta è la prima;
  - 2 se è la seconda, 1 se è la terza;
  - 0 se manca.
  
  Lo assegna un solo revisore, che non sa quale prompt è stato usato. Analisi con un modello misto ordinale.
- **"Lethal miss"** (esito esplorativo): un tumore confermato che **non compare** tra le prime 3 diagnosi.

## Risultati

**Accuratezza** (senza fototipo):

| | Top-1 | Top-3 |
|---|------|-------|
| ChatGPT 5.2 | 23,0% | 45,4% |
| Gemini 3.1 Pro | 31,6% | 53,5% |

- Gemini è più accurato di ChatGPT (odds ratio **2,32**; IC 95% 2,01–2,67).
- **Il fototipo nel prompt non cambia nulla in modo significativo:**

  | Fototipo nel prompt | Odds ratio | IC 95% |
  |---------------------|------------|--------|
  | Corretto | 1,16 | 0,95–1,40 |
  | Vicino | 0,99 | 0,82–1,18 |
  | Estremo | 0,88 | 0,70–1,12 |

**Lethal miss** sui 171 tumori:

| Prompt | ChatGPT | Gemini |
|--------|---------|--------|
| Senza fototipo | **50,3%** (86/171) | 32,2% (55/171) |
| Fototipo corretto | 47,4% | 33,3% |
| Fototipo estremo (97 tumori I–II e V–VI) | 64,9% | 44,3% |

- Con il fototipo estremo, ChatGPT passa da "trovato" a "mancato" in 10 immagini e torna indietro solo in 2 (odds ratio appaiato **5,0**; p = 0,043, esplorativo). Gemini non cambia (6 contro 5).

**Divario per fototipo** (senza fototipo nel prompt, solo tumori, punteggio medio 0–3):

| Gruppo | ChatGPT | Gemini |
|--------|---------|--------|
| I–II | 1,37 | **2,10** |
| III–IV | 1,45 | **2,09** |
| V–VI | **0,69** | **0,65** |

Anche ChatGPT va significativamente peggio sui fototipi V–VI.

**Benigno contro maligno** (analisi post hoc: "maligno" se una delle 3 diagnosi è un tumore):

| | Sensibilità | Specificità | VPP |
|---|-------------|-------------|-----|
| ChatGPT | 67,3% | **42,5%** | 29,2% |
| Gemini | 81,3% | **22,9%** | 27,1% |

I modelli chiamano "tumore" troppe lesioni benigne. Gli errori tipici:
- nevi benigni e cheratosi seborroiche presi per **melanoma**;
- verruche prese per **carcinoma squamocellulare**;
- basocellulare e squamocellulare scambiati tra loro.

## Messaggi chiave per la tesi
1. Gli LLM generalisti **non sono classificatori affidabili**: anche il migliore manca un terzo dei tumori confermati, e intanto dà molti falsi positivi.
2. Anche gli LLM mostrano il **divario per fototipo** già visto nelle CNN (DDI 2022). Sui tumori dei fototipi V–VI il punteggio è circa un terzo di quello sui fototipi chiari.
3. Il prompt può **peggiorare** la diagnosi se contiene un'informazione sbagliata: è un rischio concreto in un sistema ad agenti.
4. Gli autori dicono che il confronto giusto è con un **sistema addestrato per il compito** e validato, non con una chat generalista.

## Limiti
- Un solo dataset e un solo centro. DDI non ha sesso, etnia né sede anatomica.
- Una sola risposta per immagine: la variabilità delle risposte non è misurata.
- Un solo revisore per il punteggio, quindi niente misura di accordo tra revisori.
- Configurazioni del browser non controllabili. I risultati valgono per quelle versioni, in quel periodo.
- Il "lethal miss" non è un falso negativo binario: il modello può mancare la diagnosi giusta ma citare un altro tumore.

## Cosa porto in Neo Helper
- Conferma la regola di progetto: **l'LLM non classifica**. Le probabilità vengono dai modelli di visione.
- L'agente non deve passare **metadati non verificati** come se fossero certi. Meglio segnalarli come "dichiarati dall'utente", e non metterli nel prompt dell'LLM se non servono.
- Usare DDI anche per testare **l'agente completo**, non solo il classificatore:
  - con la metrica "lethal miss" nelle prime 3 diagnosi;
  - con punteggi separati per gruppo di fototipo;
  - con l'ontologia "a famiglie" del paper (melanoma, squamocellulare, basocellulare, melanocitico benigno, cheratosi seborroica, verruca).
- Confronto per la tesi: il classificatore di Neo Helper contro questi numeri di ChatGPT e Gemini, sullo stesso DDI.
