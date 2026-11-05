# Kurtansky et al., 2024 — ISIC 2020: le altre lesioni del paziente aiutano?

- **Rivista:** *Journal of the European Academy of Dermatology and Venereology* 39(8):1489–1499 (2025; online dicembre 2024) · [DOI 10.1111/jdv.20479](https://doi.org/10.1111/jdv.20479) · PMID 39648687 · PMC12145458
- **Gruppo:** Memorial Sloan Kettering (Kurtansky, Rotemberg), University of Queensland (Soyer, Primiero), Barcellona (Combalia)
- **Testo letto:** abstract (strutturato) e parte dell'introduzione (PMC).

## In una frase
Nella gara ISIC 2020 vedere **altre lesioni dello stesso paziente** non ha aiutato né gli algoritmi né i medici. Forse perché 7 immagini dermoscopiche non bastano a ricostruire il "brutto anatroccolo".

## Cosa hanno fatto
- **Gara online (2020):** classificare immagini dermoscopiche come melanoma o benigne, con immagini raggruppate per paziente (dataset di Rotemberg 2021). Erano ammessi dati pubblici esterni. Classifica in base all'**AUROC** sul test privato.
- **Studio con lettori umani:** su una parte del test, prima la diagnosi della lesione da sola, poi la stessa diagnosi dopo aver visto **7 altre lesioni** dello stesso paziente.

## Risultati
- **3.308 invii:** i primi 50 hanno AUROC tra **0,943 e 0,949**.
- **Pochi algoritmi** hanno usato i confronti tra le lesioni dello stesso paziente: quasi tutti valutavano ogni immagine da sola.
- **Lettori umani:** sensibilità e specificità mediane erano 60,0% e 86,7% senza contesto, 60,0% e 85,7% con contesto. **Nessun miglioramento.**
- Le prestazioni di algoritmi e medici **cambiano con la fonte delle immagini** (il centro).
- Gli autori ipotizzano che servirebbe un'immagine **di tutto il corpo**, non 7 lesioni scelte. È proprio quello che fa ISIC 2024 (Kurtansky 2025).

## Messaggi chiave per la tesi
1. Un'idea clinica sensata non migliora automaticamente un algoritmo: va **misurata**.
2. Anche qui le prestazioni dipendono dal **centro**: il domain shift è ovunque.

## Cosa porto in Neo Helper
- Il "contesto del paziente" resta una **possibile estensione futura**, ma non è una priorità per la tesi.
- Riportare i risultati **per centro di provenienza** quando i dati lo permettono.
