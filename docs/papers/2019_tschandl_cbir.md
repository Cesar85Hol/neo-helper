# Tschandl et al., 2019 — Ricerca di immagini simili (CBIR) in dermoscopia

- **Rivista:** *British Journal of Dermatology* 181(1):155–165 (2019) ⚠️ volume e pagine da verificare · [DOI 10.1111/bjd.17189](https://doi.org/10.1111/bjd.17189) · PMID 30207594 · PMC7379719
- **Gruppo:** Medical University of Vienna (Tschandl, Kittler) con Argenziano e Zalaudek
- **Testo letto:** **completo** (PMC).

## In una frase
Mostrare al medico le **16 immagini più simili** dall'archivio, ognuna con la sua diagnosi, è accurato quanto le probabilità della rete. In più, funziona meglio su classi che la rete non ha mai visto.

## Cosa hanno fatto
- **Tre dataset dermoscopici:**
  - EDRA, 888 immagini, 3 classi;
  - ISIC 2017, 2.750 immagini, 3 classi;
  - PRIV, archivio di Reggio Emilia, 16.691 immagini, 8 classi.
  
  Le immagini della stessa lesione non sono mai divise tra training e test.
- **Rete:** ResNet-50 pre-addestrata su ImageNet e poi riaddestrata. Ogni immagine diventa un vettore di 2.048 numeri ("deep features", strato pool5).
- **CBIR:** per un'immagine nuova si cercano le più simili nell'archivio di training con la similarità del coseno. La diagnosi prevista è la più frequente tra le k immagini recuperate.
- Confronto con la classica uscita softmax della stessa rete.

## Risultati
- **Rilevare un tumore** (AUC, con 16 immagini recuperate):

  | Dataset | CBIR | Softmax |
  |---------|------|---------|
  | EDRA | 0,842 | 0,830 |
  | ISIC 2017 | 0,806 | 0,810 |
  | PRIV | 0,852 | 0,847 |

  Nessuna differenza significativa.
- **Con sole 2 immagini** l'accuratezza cala. Oltre 16 non migliora in modo consistente: **16 è un buon numero**.
- **Soglia pratica:** "maligno se almeno il 25% delle 16 immagini è maligno". In PRIV dà sensibilità 87,4% e specificità 63,9%.
- **Classi mai viste:** una rete addestrata su 3 classi ottiene una mAP di circa 0,18–0,20 su PRIV, che ne ha 8. Con il CBIR sull'archivio di PRIV sale a 0,37–0,40. Dagli esempi simili si ritrovano diagnosi che la rete non conosce.

## Messaggi chiave per la tesi
1. Il CBIR è una **spiegazione naturale** per il dermatologo: "assomiglia a questi casi, e questi erano…". Se i casi recuperati non assomigliano affatto alla lesione, il medico capisce da solo che la rete non lo può aiutare.
2. Un archivio di casi si può **aggiornare** senza riaddestrare la rete: basta aggiungere immagini diagnosticate.
3. In Tschandl 2020 il CBIR non ha aumentato l'accuratezza dei medici quanto le probabilità multiclasse. Nella meta-analisi di Krakowski 2024 è l'**unico** metodo di spiegazione testato con medici (2 studi).

## Limiti
- Studio pilota, senza calcolo della numerosità. Non misura l'effetto sui medici.
- Bias di selezione e di verifica: sono immagini che un medico ha ritenuto degne di fotografare.

## Cosa porto in Neo Helper
- **Tool `similar_cases`:** con gli embedding di PanDerm (o di DINOv2) e una ricerca del coseno su HAM10000 (training), restituisce le k = 16 immagini più simili con diagnosi, `label_source` e somiglianza.
- Nel report per il medico: mostrare i **primi 4–8 casi**, e segnalare quando la somiglianza è bassa. È un altro segnale di "fuori distribuzione".
- Gli embedding sono già calcolati per la testa lineare, quindi il costo è quasi zero.
- Collegamento con il §4 del documento delle scelte: se arrivano dati dall'ospedale, entrano subito nell'archivio del CBIR.
