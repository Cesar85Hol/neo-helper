# Yan et al., 2025 — PanDerm: un foundation model multimodale per la dermatologia clinica

- **Rivista:** *Nature Medicine* 31(8):2691–2702 (2025) · [DOI 10.1038/s41591-025-03747-y](https://doi.org/10.1038/s41591-025-03747-y) · PMID 40481209 · PMC12353815
- **Gruppo:** Monash University e centri australiani (Alfred Hospital, Queensland), con Vienna e altri centri internazionali
- **Testo letto:** **completo** (PMC), senza materiale supplementare. Pesi e licenza verificati sul repository ufficiale ([github.com/SiyuanYan1/PanDerm](https://github.com/SiyuanYan1/PanDerm)).

## In una frase
Un'unica rete, pre-addestrata **senza etichette** su più di **2 milioni di immagini** di 4 tipi diversi, che con poco addestramento aggiuntivo supera i modelli precedenti su **28 compiti** dermatologici e **aiuta i medici** nei test con lettori.

## Che cos'è un foundation model (in breve)
- Una grande rete addestrata su moltissimi dati **senza etichette** (apprendimento auto-supervisionato).
- Impara una "rappresentazione" generale delle immagini, che poi si adatta a compiti specifici con **poche etichette**.
- Prima di PanDerm, in dermatologia si partiva quasi sempre da reti addestrate su foto generiche (ImageNet).

## Cosa hanno fatto
- **Dati di pre-addestramento:** **2.149.706 immagini** da **11 fonti**, in 4 modalità:
  - total body photography (TBP): 757.890 riquadri (35,3%);
  - dermatopatologia (vetrini istologici): 537.047 riquadri (25,4%);
  - immagini cliniche: 460.328 (21,4%);
  - immagini dermoscopiche: 384.441 (17,9%).
  Fonti soprattutto **interne** (Australia, Nuova Zelanda) più alcune pubbliche (ISIC 2024, TCGA). Gli autori evitano le immagini prese dal web per **non contaminare** i test set pubblici.
- **Modello:** **ViT-Large** (24 blocchi). Addestramento con **mascheramento**: la rete vede metà dell'immagine e deve prevedere la rappresentazione della parte nascosta. Il "maestro" che fornisce le rappresentazioni bersaglio è un modello **CLIP-Large**.
- **Valutazione:** 28 benchmark (screening, rischio, diagnosi di malattie comuni e rare, segmentazione, cambiamenti nel tempo, metastasi e prognosi) e **3 studi con lettori**.

## Risultati
**1. Diagnosi e generalizzazione.**
- Migliore su 9 dataset su 10 (4 modalità, 7 centri). Su HAM10000 supera il secondo modello del 4,7%; su PAD-UFES-20 (foto da smartphone) del 9,0%.
- Con solo il **10–30% delle etichette** ottiene risultati simili agli altri modelli addestrati su tutto.
- Su **7 centri esterni** per il melanoma mantiene il vantaggio, anche su foto cliniche mai viste.

**2. Non solo tumori.**
Su 74 malattie diverse (infiammatorie, infettive, tumori) il vantaggio cresce con il numero di classi (+8,2% di F1 pesato).

**3. Cambiamenti nel tempo.**
Su coppie di immagini dermoscopiche a 3 mesi di distanza riconosce le lesioni che cambiano; per quelle poi risultate maligne AUROC 0,840.

**4. Screening su total body photography.**
- 216 lesioni maligne tra quasi 198.000 benigne: sensibilità **0,893**.
- Trova il tumore in **79 pazienti su 80** e propone di esaminare **60,8% di lesioni in meno** rispetto agli esperti di imaging (3.498 contro 8.913).
- Le rappresentazioni separano le lesioni sospette come nel segno del **"brutto anatroccolo"**.

**5. Prognosi.**
Dalle immagini dermoscopiche di melanomi invasivi prevede le metastasi con AUROC 0,964 (370 pazienti); nella regressione di Cox è il predittore più forte di recidiva, più di spessore di Breslow e ulcerazione.

**6. Tre studi con lettori.**

| Studio | Lettori | Risultato |
|--------|---------|-----------|
| Melanoma precoce su immagini sequenziali | 12 (7 dermatologi, 5 specializzandi) | PanDerm +10,2% sulla media dei medici; riconosce al primo controllo il 77,5% dei melanomi contro il 32,6% |
| Collaborazione su 7 classi dermoscopiche | 41 medici | Accuratezza da **0,69 a 0,80** con le probabilità multiclasse di PanDerm; +17% per i meno esperti, +6% per i più esperti |
| 128 malattie su foto cliniche | 37 (20 area dermatologica, 17 generalisti) | Top-3 da 54% a 63,4%; generalisti +16,5%, area dermatologica +10,3% |

Dato importante: in entrambi gli studi di collaborazione **PanDerm da solo** va **come o meglio** di medico + PanDerm (0,81 contro 0,80 nel primo; nettamente meglio nel secondo). Gli autori lo spiegano con l'uso **selettivo** dei consigli da parte dei medici.

## Messaggi chiave per la tesi
1. Il foundation model specifico per la dermatologia batte quelli generici (DINOv2, ImageNet) e quelli biomedici generalisti (BiomedGPT, BiomedCLIP, MONET nei benchmark).
2. Il guadagno più grande è **con poche etichette**: proprio la situazione di una tesi.
3. Lo studio con 41 medici conferma Tschandl 2020: **probabilità multiclasse** e beneficio maggiore per i **meno esperti**.
4. Medico + AI non supera sempre l'AI da sola: il modo di presentare l'output resta un problema aperto.

## Limiti
- Circa 200 malattie valutate, contro oltre 1.000 diagnosi esistenti.
- **Equità:** prestazioni "stabili tra fototipi" dichiarate solo come accuratezza complessiva nel supplementare; gli autori stessi dicono che servono metriche di fairness più complete.
- Dati di pre-addestramento in gran parte **australiani** e interni, non condivisi.
- Studio realistico successivo (**Anriot 2026**, vedi scheda): in condizioni reali PanDerm non supera i dermatologi con più di 10 anni di esperienza.

## Disponibilità dei pesi (verificata sul repository, 2026-11-03)
- **PanDerm** (ViT-L/16, il modello del paper) e **PanDerm_Base** (ViT-B/16): Google Drive.
- **DermLIP_PanDerm** (ViT-B/16, versione immagine-testo): Hugging Face.
- **Licenza CC-BY-NC-ND 4.0:** solo **ricerca accademica non commerciale**. Va bene per la tesi; non per un prodotto.

## Cosa porto in Neo Helper
- **Backbone principale candidato** (Fase 3): estrarre le rappresentazioni di PanDerm e addestrare sopra un classificatore leggero (*linear probe*) su HAM10000. Confronto con un baseline ImageNet.
- **Tool MCP "embedding"** riutilizzabile per classificazione, casi simili (CBIR) e controllo di qualità.
- Interfaccia: mostrare le **probabilità sulle 7 classi** (conferma di Tschandl 2020).
- Attenzione alla **licenza NC-ND** in tutti i documenti e nel README.
