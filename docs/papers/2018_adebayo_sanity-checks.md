# Adebayo et al., 2018 — Test di sanità per le mappe di salienza

- **Conferenza:** NeurIPS 2018 · [arXiv 1810.03292](https://arxiv.org/abs/1810.03292)
- **Gruppo:** Google Brain e UC Berkeley (Been Kim, Ian Goodfellow, Moritz Hardt)
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF ⚠️.

## In una frase
Molte mappe di salienza **sembrano** convincenti, ma restano quasi uguali anche quando la rete non ha imparato niente. Quindi non spiegano il modello.

## I due test proposti
1. **Randomizzazione dei pesi.** Si distruggono i pesi appresi della rete, strato dopo strato dall'alto verso il basso. Se la mappa non cambia, non dipende da ciò che la rete ha imparato.
2. **Randomizzazione delle etichette.** Si addestra la rete su etichette mescolate a caso, così impara a memoria il rumore. Se la mappa resta simile a quella della rete vera, non riflette il legame tra immagine e diagnosi.

Metodi testati: gradiente semplice, Gradient×Input, Integrated Gradients, Guided Backpropagation, Grad-CAM, Guided Grad-CAM, SmoothGrad, VarGrad. Su ImageNet (Inception v3), MNIST e Fashion-MNIST.

## Risultati
- **Superano i test:** gradiente, SmoothGrad e **Grad-CAM**. Le loro mappe cambiano quando la rete perde ciò che ha imparato.
- **Non superano i test:** **Guided Backpropagation** e **Guided Grad-CAM**. Restano quasi identiche anche con pesi casuali, e assomigliano a un **rilevatore di bordi** classico.
- Gradient×Input e Integrated Gradients sono dominati dalla struttura dell'immagine stessa.
- Messaggio generale: **giudicare una spiegazione a occhio è fuorviante**.

## Messaggi chiave per la tesi
1. Una heatmap "bella" non è una prova. Prima di mostrarla a un medico va verificato che dipenda davvero dal modello.
2. È un argomento forte per non affidarsi solo alle mappe di salienza in medicina, e per affiancarle a spiegazioni a concetti o a casi simili.

## Cosa porto in Neo Helper
- **Test di sanità obbligatorio** nel capitolo di explainability: randomizzare i pesi della testa e degli ultimi blocchi, poi misurare quanto cambia la mappa (correlazione di Spearman, SSIM).
- Escludere Guided Grad-CAM dal report.
