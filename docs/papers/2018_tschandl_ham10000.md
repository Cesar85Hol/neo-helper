# Tschandl, Rosendahl, Kittler, 2018 — Il dataset HAM10000

- **Rivista:** *Scientific Data* 5:180161 (2018) · [DOI 10.1038/sdata.2018.161](https://doi.org/10.1038/sdata.2018.161) · PMID 30106392
- **Gruppo:** ViDIR Group, Università di Medicina di Vienna + studio di Cliff Rosendahl (Queensland, Australia)
- **Testo letto:** completo (PubMed Central PMC6091241)
- **Dati:** Harvard Dataverse e archivio ISIC

## In una frase
HAM10000 ("Human Against Machine with 10000 training images") è il dataset di **10.015 immagini dermatoscopiche** in 7 classi su cui si basa gran parte della ricerca dal 2018: sarà quasi certamente **il nostro primo dataset**.

## Il problema
Prima di HAM10000 i dataset dermatoscopici erano:
- **piccoli** (es. PH2: 200 immagini, 160 nevi e 40 melanomi);
- **sbilanciati** verso nevi e melanomi (archivio ISIC 2018: 12.893 su 13.786 immagini);
- poco **accessibili** (es. atlante su CD-ROM a pagamento).

Così i sistemi andavano bene in laboratorio e male in clinica, dove molte lesioni pigmentate **non sono melanocitiche**.

## Come è stato costruito
- **Due fonti, vent'anni di immagini:**
  - **Vienna** (centro di riferimento terziario): pazienti ad alto rischio, molti nevi, storia personale o familiare di melanoma. Diapositive digitalizzate, database DermLite, sistema MoleMax HD di follow-up.
  - **Queensland, Australia** (cure primarie, alta incidenza di tumori cutanei): pelle con **forte danno solare cronico**. Immagini estratte da 122 file PowerPoint con uno script Python.
- **Filtro automatico:** una rete InceptionV3 addestrata su 1.501 immagini etichettate a mano separa le immagini dermatoscopiche da quelle cliniche (accuratezza 98,68%), seguita da revisione manuale.
- **Pulizia:**
  - esclusi i casi con diagnosi istologica ambigua;
  - escluse le immagini identificabili (vestiti, gioielli, tatuaggi), quelle sfuocate o con bolle di gel, le lesioni non pigmentate, ungueali, mucose, oculari;
  - i **peli sono stati lasciati**, perché sono realistici;
  - correzioni di colore solo per immagini sottoesposte o con dominante giallo/verde.

## Le 7 classi ⚠️ (numeri dalla tabella del paper, da ricontrollare)
| Classe | Immagini (circa) |
|--------|------------------|
| nv — nevi | 6.705 |
| mel — melanoma | 1.113 |
| bkl — cheratosi benigne | 1.099 |
| bcc — carcinoma basocellulare | 514 |
| akiec — cheratosi attinica / Bowen | 327 |
| vasc — lesioni vascolari | 142 |
| df — dermatofibroma | 115 |

Il dataset è **fortemente sbilanciato**: circa due terzi sono nevi.

## Ground truth
- **Istopatologia** per oltre il 50% delle lesioni.
- **Follow-up** dermatoscopico (nessun cambiamento in 1,5 anni o 3 visite), solo per i nevi.
- **Consenso** di due esperti per lesioni benigne tipiche.
- **Microscopia confocale** per alcune cheratosi del viso.

## Avvertenze importanti per chi lo usa
- **Più immagini della stessa lesione** (ingrandimenti, angoli, fotocamere diverse): c'è un identificativo di lesione (`lesion_id`) e **lo split va fatto per lesione**, altrimenti il test è "contaminato" dal training.
- Le immagini sono più "pulite" di quelle che farebbe un utente reale: mancano foto sfuocate o poco ingrandite.
- **Licenza:** rilasciato per **scopi accademici di machine learning** (⚠️ verificare la licenza esatta, CC BY-NC).
- HAM10000 è stato il **training set della challenge ISIC 2018** ed è incluso anche in ISIC 2019: attenzione a non usarlo come test di un modello addestrato su ISIC 2019.

## Cosa porto in Neo Helper
- È il **primo dataset** per la baseline (issue #12 e #13).
- Split per `lesion_id`, gestione dello **sbilanciamento**, analisi per **sorgente** (Vienna vs Australia) come primo test di generalizzazione.
- Leggere i metadati: tipo di ground truth, età, sesso, sede anatomica.
