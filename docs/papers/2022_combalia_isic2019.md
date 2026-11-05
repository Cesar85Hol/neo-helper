# Combalia et al., 2022 — La challenge ISIC 2019: cosa succede fuori dal laboratorio

- **Rivista:** *The Lancet Digital Health* 4(5):e330–e339 (2022) · [DOI 10.1016/S2589-7500(22)00021-8](https://doi.org/10.1016/S2589-7500(22)00021-8) · PMID 35461690 · PMC9295694
- **Gruppo:** Hospital Clínic de Barcelona (Malvehy, Puig), Memorial Sloan Kettering (Rotemberg, Halpern), IBM, Vienna
- **Testo letto:** **completo** (PMC): abstract, metodi e risultati principali; non le appendici.

## In una frase
Messi davanti a immagini **difficili**, a **centri nuovi** e a **malattie mai viste**, i migliori algoritmi del 2019 crollano: l'accuratezza bilanciata passa dall'82% al 59%, e quasi metà delle lesioni sconosciute viene chiamata **maligna**.

## Come era fatta
- **Training:** **25.331 immagini dermoscopiche** in **8 classi** (le 7 di HAM10000 più il carcinoma squamocellulare), da Vienna (HAM10000) e da Barcellona (**BCN20000**).
- **Test:** **8.238 immagini**, che contengono:
  - tutte le 8 classi;
  - una classe **"non addestrata"** (NT), cioè diagnosi che non c'erano nel training;
  - immagini da paesi assenti nel training (Turchia, Nuova Zelanda, Svezia, Argentina).
- **Due compiti:** solo immagini, oppure immagini più metadati (età, sesso, sede).
- **Artefatti annotati a mano:** peli, segni di penna, ulcerazione, crosta, pigmentazione.
- **Confronto con 18 dermatologi:** 2.460 valutazioni su 1.269 immagini.
- Hanno partecipato **64 squadre** con **129 algoritmi**.

## Risultati
| Test | Accuratezza bilanciata del migliore |
|------|-------------------------------------|
| HAM10000 (come nei benchmark pubblicati) | **82,0%** |
| BCN20000 (più vicino alla clinica reale) | **58,8%** |

- **Distribuzioni diverse e classi non addestrate** fanno calare l'accuratezza.
- **Artefatti e centro di provenienza** (peli, penna, ulcerazione) peggiorano i risultati in modo complesso, diverso per ogni diagnosi.
- **Contro i dermatologi:**
  - gli algoritmi sono migliori nella maggior parte delle categorie;
  - sono simili sulle cheratosi attiniche;
  - sono molto peggiori sulle **diagnosi mai viste**: gli esperti ne riconoscono il **26%**, gli algoritmi il **6%**.
- **Il dato sulla sicurezza:** nei primi 25 algoritmi, il **47,1%** delle lesioni "mai viste" viene classificato come **maligno**. Più spesso come basocellulare (32,4%), poi come melanoma (7,8%) e squamocellulare (6,9%). In clinica significherebbe molte biopsie inutili.
- **Come hanno provato a riconoscere l'ignoto:**
  - la squadra migliore ha raccolto da sola immagini esterne (pelle sana, verruche, cisti) e le ha usate per addestrare la classe "altro";
  - altre squadre hanno usato modelli a 8 classi con la possibilità di "nessuna", oppure l'entropia delle probabilità.
  
  Nessuno ci è riuscito bene.

## Messaggi chiave per la tesi
1. Le alte accuratezze su HAM10000 **sovrastimano** le prestazioni reali. Il test su BCN20000 è molto più severo.
2. Un classificatore chiuso **non sa dire "non so"**: assegna ogni immagine a una classe conosciuta, spesso maligna.
3. Gli autori lo dicono esplicitamente: nei protocolli di valutazione servono test con **classi sconosciute** e **centri diversi**.

## Cosa porto in Neo Helper
- **Conferma forte** della scelta P8 ("non so" con conformal e controllo fuori distribuzione) e della scelta di usare BCN20000 come **test esterno** (ISIC 2019 dopo la baseline).
- **Test "classe sconosciuta":** valutare quante lesioni di diagnosi non presenti in HAM10000 Neo Helper riconosce come "non so" invece di dare una diagnosi. Le immagini "unknown" del test di BCN20000 servono a questo, se le etichette sono disponibili ⚠️.
- Riportare la **matrice di confusione** delle lesioni sconosciute: quante vanno verso classi maligne.
- Analisi per **artefatto** (peli, penna) come in questo studio.
