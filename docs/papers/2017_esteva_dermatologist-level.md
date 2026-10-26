# Esteva et al., 2017 — Classificazione del cancro della pelle "a livello di dermatologo" con reti neurali profonde

- **Rivista:** *Nature* 542:115–118 (2017) · [DOI 10.1038/nature21056](https://doi.org/10.1038/nature21056) · PMID 28117445
- **Gruppo:** Stanford University (ingegneria, dermatologia, informatica — tra gli autori Sebastian Thrun)
- **Testo letto:** completo (PubMed Central PMC8382232)
- **Tipo di immagini:** soprattutto **cliniche** (foto), più una parte dermatoscopica

## In una frase
È il paper che ha acceso l'interesse mondiale: una sola rete neurale, addestrata su circa 130.000 foto, distingue tumori della pelle da lesioni benigne **bene quanto 21 dermatologi**.

## Il problema
Prima del 2017 i sistemi automatici usavano **pochi dati** (spesso meno di mille immagini), lavoravano solo su immagini dermatoscopiche standardizzate e richiedevano passaggi fatti a mano (segmentare la lesione, estrarre caratteristiche come bordi e colori). Generalizzavano male.

## Cosa hanno fatto
1. **Dataset enorme:** 129.450 immagini cliniche di **2.032 malattie**, da 18 archivi online curati da medici e dall'ospedale di Stanford. Tra queste, 3.374 dermatoscopiche.
2. **Tassonomia ad albero:** i dermatologi hanno organizzato le 2.032 malattie in un albero con tre radici: benigne, maligne, non neoplastiche.
3. **Algoritmo di partizione:** l'albero viene "tagliato" in **757 classi di addestramento**, ciascuna con al massimo circa 1.000 immagini. Le classi fini (es. melanoma amelanotico) hanno abbastanza dati senza diventare troppo grandi.
4. **Rete:** Google **Inception v3** pre-addestrata su ImageNet (1,28 milioni di foto di oggetti comuni), poi riaddestrata su tutte le immagini mediche (*transfer learning*). Immagini ridotte a 299×299 pixel, con aumenti di dati (rotazioni casuali, ritagli, ribaltamenti).
5. **Inferenza:** per sapere la probabilità di "melanoma" si **sommano** le probabilità di tutte le classi fini che stanno sotto "melanoma" nell'albero.
6. **Attenzione al leakage:** le immagini della stessa lesione (o molto simili) sono state collegate in un grafo e tenute sempre dalla stessa parte dello split tra training e validation.

## Come l'hanno valutato
- Validazione interna con 9 fold: accuratezza **72,1%** su 3 classi (due dermatologi: 65,6% e 66,0%) e **55,4%** su 9 classi (dermatologi: 53,3% e 55,0%). Addestrare sulle classi fini e poi sommare funziona meglio che addestrare direttamente su 3 o 9 classi.
- **Test decisivo** solo su lesioni con **biopsia**, tre compiti:
  - carcinomi cheratinocitari vs cheratosi seborroiche (135 immagini);
  - melanoma vs nevo su foto cliniche (130 immagini);
  - melanoma vs nevo su immagini dermatoscopiche (111 immagini).
- Ai dermatologi (almeno 21 per compito) è stato chiesto: **"biopsia/tratteresti o rassicureresti il paziente?"**, cioè la decisione clinica reale.

## Risultati
- In tutti e tre i compiti l'**AUC supera 0,91**.
- Quasi tutti i dermatologi stanno **sotto la curva** sensibilità-specificità della rete: la rete eguaglia o supera la media degli esperti.
- Sul test set completo (fino a 1.010 immagini dermatoscopiche) l'AUC cambia meno di 0,03: risultato stabile.
- Le **mappe di salienza** mostrano che la rete guarda la lesione e ignora la pelle sana circostante.
- Errori simili a quelli umani: nevi benigni e melanomi vengono confusi tra loro sia dalla rete sia dai dermatologi.

## Limiti
- Confronto **solo sull'immagine**: il dermatologo reale usa anche storia clinica, palpazione, confronto con gli altri nei.
- Il dataset di training **non è pubblico**: lo studio non è riproducibile.
- Test **retrospettivo** su immagini selezionate, non in clinica reale. Gli autori stessi chiedono validazione sul campo.
- Le immagini sfocate sono state tolte dal test: nella realtà (smartphone) non sarà così.
- ⚠️ Studi successivi hanno criticato la scarsa presenza di pelli scure nei dati.

## Cosa porto in Neo Helper
- La **tassonomia gerarchica**: addestrare su classi fini e aggregare in "benigno/maligno" è un'idea semplice ed efficace.
- La **domanda giusta** nei test: "asportare o rassicurare?" e non solo "che diagnosi è?".
- Lo **split per lesione** (raggruppare immagini simili) è obbligatorio anche per noi.
- Il sogno "diagnosi da smartphone" nasce qui, ma con molti limiti da discutere nella tesi.
