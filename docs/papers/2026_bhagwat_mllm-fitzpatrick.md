# Bhagwat et al., 2026 — LLM multimodali generalisti, fototipo e diagnosi

- **Rivista:** *Bioengineering (Basel)* 13(8):932 (2026) · [DOI 10.3390/bioengineering13080932](https://doi.org/10.3390/bioengineering13080932) · PMID 42649821 · PMC13509600
- **Testo letto:** **solo abstract**. Scelto come esempio recente e ben costruito di valutazione di LLM generalisti (ChatGPT, Gemini) su immagini dermatologiche, perché usa un dataset con **biopsia** (DDI, vedi §4).

## In una frase
Due LLM multimodali commerciali, messi alla prova su 656 foto con diagnosi confermata da biopsia, **non** sono adatti a un uso diagnostico autonomo: sovrastimano spesso il tumore, e dire al modello il fototipo del paziente **non aiuta**.

## Cosa hanno fatto
- **Dati:** le **656 immagini del dataset DDI** (tutte con biopsia, fototipi I–VI).
- **Modelli:** ChatGPT 5.2 Edu e Gemini 3.1 Pro, usati dal browser.
- **Quattro condizioni di prompt** per ogni immagine:
  - nessun fototipo;
  - il fototipo **corretto**;
  - due fototipi **sbagliati** (uno lontanissimo dal vero).
- In totale **5.248 valutazioni**. Esito esplorativo: il **"lethal miss"**, cioè un tumore confermato che non compare tra le **prime 3 diagnosi** del modello.

## Risultati (dall'abstract)
- Gemini è più accurato di ChatGPT (odds ratio 2,32).
- Indicare il fototipo **non migliora** l'accuratezza in nessuna condizione.
- Con un fototipo **molto sbagliato**, ChatGPT ha **più lethal miss** (odds ratio appaiato 5,0; p = 0,043). Gemini no.
- Benigno/maligno senza fototipo: **specificità molto bassa**, 42,5% ChatGPT e **22,9%** Gemini. I modelli chiamano "maligno" troppe lesioni benigne.
- Gemini va peggio sulle lesioni maligne dei fototipi **V–VI** che su quelli più chiari.
- Conclusione degli autori: nessuna delle due configurazioni giustifica un **uso autonomo**.

## Messaggi chiave per la tesi
1. Gli LLM generalisti **non sono classificatori affidabili**: molti falsi positivi e risultati che cambiano con dettagli del prompt.
2. Anche gli LLM mostrano il **divario per fototipo** già visto nelle CNN (DDI 2022).
3. Il prompt può **peggiorare** la diagnosi se contiene un'informazione sbagliata: rischio concreto in un sistema ad agenti.

## Cosa porto in Neo Helper
- Conferma la regola di progetto: **l'LLM non classifica**. Le probabilità vengono dai modelli di visione.
- L'agente non deve passare **metadati non verificati** come se fossero certi; meglio segnalarli come "dichiarati dall'utente".
- Usare DDI anche per testare **l'agente completo**, non solo il classificatore, con la metrica "lethal miss" nelle prime 3 diagnosi.
- ⚠️ Recuperare il testo completo (MDPI, open access) per le accuratezze esatte per fototipo.
