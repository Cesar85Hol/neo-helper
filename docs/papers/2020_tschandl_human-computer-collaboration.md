# Tschandl et al., 2020 — La collaborazione uomo-computer nel riconoscimento del cancro della pelle

- **Rivista:** *Nature Medicine* 26(8):1229–1234 (2020) · [DOI 10.1038/s41591-020-0942-0](https://doi.org/10.1038/s41591-020-0942-0) · PMID 32572267
- **Gruppo:** Vienna (Kittler, Tschandl) con centri internazionali (Napoli, Modena, Trieste, Barcellona, Brisbane, New York…)
- **Testo letto:** **completo**, nella versione post-print peer reviewed dell'archivio dell'Università di Trieste (ArTS, handle 11368/2968193). Contiene articolo, metodi ed Extended Data.
- **Perché è il paper più importante per Neo Helper:** studia proprio **come presentare l'AI al medico**.

## In una frase
L'AI di buona qualità **migliora i medici** più di quanto facciano l'AI o i medici da soli; ne beneficiano soprattutto i **meno esperti**. Ma un'**AI sbagliata inganna tutti, anche gli esperti**, e il **modo** in cui l'AI presenta il risultato cambia l'efficacia.

## Il problema
Fino al 2019 la domanda era "chi vince, uomo o macchina?". Nella realtà l'AI sarà usata **da un medico**. Le domande diventano:
- quanto migliora il medico con l'AI?
- chi ne beneficia di più?
- quale **forma di supporto** funziona meglio?
- cosa succede se l'AI sbaglia?

## Cosa hanno fatto
- **La rete:** una **ResNet34** pre-addestrata su ImageNet e riaddestrata su **HAM10000**, 7 classi. Sul test set ISIC 2018 ha un richiamo medio del **77,7%** e un'accuratezza dell'**80,3%**. Si colloca nel primo quartile degli algoritmi della challenge e supera la maggior parte dei lettori umani.
- **I lettori:** **302 medici da 41 Paesi**: 169 dermatologi (56%), 77 specializzandi (25,5%), 38 medici di base (12,6%). L'esperienza va da meno di 1 anno a più di 10.
- **Il compito:** batch di **28 immagini** dal test set ISIC 2018. Il medico dà la diagnosi **prima senza e poi con** un tipo di supporto, e può cambiarla. In totale 512 test e 13.428 valutazioni.
- **Quattro forme di supporto confrontate:**
  1. **probabilità multiclasse** dell'AI: un grafico a barre sulle 7 diagnosi;
  2. **probabilità di malignità** dell'AI: un solo numero;
  3. **CBIR** (*content-based image retrieval*): l'AI mostra **immagini simili** già diagnosticate;
  4. **probabilità multiclasse "della folla"**: le risposte di 511 medici raccolte in uno studio precedente.
- **Esperimenti aggiuntivi:**
  - **AI difettosa** (155 lettori): le probabilità vengono scambiate apposta, così la classe più probabile diventa una diagnosi sbagliata;
  - **triage in telemedicina:** 1.521 foto fatte dai pazienti con lo smartphone e il dermatoscopio, 596 lesioni di 93 pazienti ad alto rischio;
  - **second opinion:** dermatologi che rivedono casi che avevano già gestito di persona, senza saperlo;
  - **didattica con l'explainability:** 189 studenti di medicina.

## Risultati
**1. La forma del supporto conta.**
- Con le **probabilità multiclasse** l'accuratezza passa dal **63,6% al 77,0%**: **+13,3 punti** (IC 95% 11,5–15,2).
- La **probabilità di malignità** e il **CBIR** non danno **nessun miglioramento**.
- Il CBIR richiede anche molto più tempo (16,5 secondi contro 4,6 per il grafico) e col tempo i medici **smettono di guardarlo**.
- Spiegazione degli autori: per un problema a 7 classi serve un supporto a 7 classi. Il singolo numero di malignità va bene per decisioni semplici come "biopsia sì/no".

**2. Chi ne beneficia.**
- I **meno esperti** cambiano la diagnosi più spesso (26,0% delle volte, contro il 14,7% degli esperti) e guadagnano di più.
- Gli **esperti** guadagnano solo quando **non sono sicuri** (+13,4%). Quando sono sicuri il beneficio è nullo (−0,7%).
- Regola pratica che ne deriva: *se sei un esperto ed è un caso in cui sei sicuro, puoi ignorare l'AI*.
- I medici cambiano idea quasi sempre a favore della **prima scelta dell'AI**, e soprattutto quando l'AI è molto più sicura della loro diagnosi iniziale.

**3. L'AI difettosa inganna tutti.**
- Con l'AI corretta il guadagno mediano è **+9,5%**.
- Con l'AI sbagliata diventa una **perdita mediana del −6,3%**.
- Succede in **tutti i gruppi**, esperti compresi. Più ti fidi, più sei vulnerabile.

**4. Il guadagno dipende dalla malattia.**
Il beneficio più grande riguarda le **cheratosi attiniche e i carcinomi intraepiteliali pigmentati**: +31,5%.

**5. Folla + AI.**

| Chi decide | Accuratezza media |
|------------|-------------------|
| Singolo medico | 64,8% |
| Piccolo gruppo di medici (voto di maggioranza) | 73,7% |
| AI da sola | 76,9% |
| **Gruppo di medici + probabilità dell'AI** | **81,0%** |

**6. Telemedicina.**
- Sulle foto fatte dai pazienti l'accuratezza della rete cala molto (53,9% contro 76,2%), perché sono immagini diverse da quelle di addestramento.
- Però, a livello di **paziente**, la rete riconosce il **95,2% dei pazienti con tumore**, con specificità 59,2%. Questo la rende utile per il **triage**.
- Limite: il campione non conteneva melanomi.

**7. Second opinion.**
- Con il supporto dell'AI i dermatologi passano da "asportare" a "controllare nel tempo" nel **15,5%** delle lesioni benigne (7 su 45), **senza** rinunciare ad asportare lesioni maligne.
- Le diagnosi specifiche corrette salgono dal 55,6% al 75,0% (11 dermatologi).

**8. L'AI che insegna.**
- Le mappe **Grad-CAM** mostrano che, per le cheratosi attiniche, la rete guarda **più della media la pelle intorno alla lesione**, cioè il danno solare cronico.
- Gli autori lo trasformano in un consiglio per gli studenti: "guardate anche la pelle intorno".
- Le diagnosi corrette di cheratosi attinica salgono dal **32,5% al 47,3%**; quelle complessive dal 55,2% al 59,1%.

**9. Bonus: la soglia scelta dai medici.**
Quando vedono la probabilità di malignità, i medici cambiano idea già intorno al **17%** e non al 50%. Questa soglia "istintiva" è molto vicina a quella ottimale per sensibilità e specificità (indice di Youden).

## Messaggi chiave per la tesi
1. **Il valore sta nella collaborazione**, non nella gara uomo-macchina.
2. **La forma dell'output conta**: per la diagnosi multiclasse funziona la distribuzione su tutte le classi; il CBIR, in questa forma, viene ignorato.
3. **Automation bias**: un'AI che sbaglia con sicurezza peggiora anche gli esperti. Servono **incertezza** visibile e meccanismi per dire "non lo so".
4. Gli esperti sicuri non hanno bisogno dell'AI: il supporto va **adattato all'utente e al compito**.
5. L'AI può anche **insegnare**: l'explainability è anche uno strumento didattico.
6. Gli autori concludono che le AI andrebbero valutate **nelle mani degli utenti finali**, in condizioni reali, non come dispositivi da soli.

## Limiti
- Studio su **immagini**, non su pazienti visitati di persona.
- Campioni piccoli negli scenari clinici: 11 dermatologi nella second opinion; nessun melanoma nel campione di telemedicina.
- Una sola rete (ResNet34) e una sola implementazione di CBIR. Gli autori notano che altre forme di CBIR potrebbero funzionare meglio.

## Cosa porto in Neo Helper
- **Interfaccia:** mostrare la **distribuzione su tutte le 7 classi**, non un solo verdetto. I casi simili (CBIR) possono restare come funzione secondaria e opzionale.
- **Soglie:** per una decisione "asportare/controllare" usare una soglia di malignità **bassa** (intorno al 17–20%), non il 50%.
- **Agente Critic/Safety** e **quantificazione dell'incertezza**: sono la risposta diretta al rischio di "AI difettosa".
- **Valutazione con utenti** (Fase 7): misurare il miglioramento del medico **con e senza** Neo Helper, separando esperti e non esperti, sicuri e non sicuri.
- **Heatmap** (Grad-CAM) come strumento di spiegazione **e** di formazione.
- **Triage** a livello di paziente, non di singola immagine, come scenario per l'app mobile.
