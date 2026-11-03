# §4 — Introduzione: bias, equità e scorciatoie

> Issue #5 (M1.5) · Fonti: PubMed, alphaXiv. Ogni scheda riporta DOI e se è stato letto il testo completo o solo l'abstract.

Nelle sezioni precedenti abbiamo visto reti che eguagliano o superano i dermatologi. Questa sezione risponde a una domanda scomoda: **su chi** e **perché** funzionano? I quattro lavori mostrano tre modi in cui un modello può sembrare bravo e non esserlo.

**Problema 1 — La rete impara la cosa sbagliata (Winkler 2019).**
- Un segno di **penna chirurgica** vicino a un neo fa crollare la specificità di una rete certificata dall'84% al 46%. La rete aveva imparato "penna = melanoma". Si chiama **shortcut learning** (apprendimento per scorciatoie).

**Problema 2 — I dati non rappresentano tutti (Fitzpatrick17k 2021, DDI 2022).**
- **Fitzpatrick17k** etichetta il fototipo in 16.577 foto cliniche: le pelli scure sono 3,6 volte meno di quelle chiare, e una rete funziona meglio sui fototipi simili a quelli di addestramento.
- **DDI** testa tre modelli su foto con **biopsia** e pelli di tutti i colori: le AUC passano da circa 0,9 a 0,56–0,67, con risultati peggiori sulle pelli scure. Il divario si chiude **solo con dati diversi**. E anche i dermatologi che etichettano a vista sbagliano di più sulle pelli scure.

**Problema 3 — Come si valuta (CLEAR Derm 2022).**
- La checklist dell'ISIC mette in ordine tutto: descrivere immagini e artefatti, dichiarare il fototipo, separare bene i dati, testare fuori distribuzione, stratificare i risultati, dire chi userà il sistema e con quali rischi.

**Il filo conduttore per Neo Helper:**
- controllare la **qualità e gli artefatti** di ogni immagine prima di classificarla;
- valutare su **test esterni** con biopsia e diversi fototipi (DDI), riportando i risultati **per sottogruppo**;
- dichiarare onestamente che HAM10000 è fatto quasi solo di **pelli chiare** e non riporta il fototipo;
- usare **CLEAR Derm** come griglia del capitolo di valutazione.

Collegamento con la §3: anche gli LLM multimodali (Bhagwat 2026, su DDI) vanno peggio sulle pelli scure, e PanDerm dichiara prestazioni "stabili tra fototipi" solo con l'accuratezza complessiva.

| Anno | Lavoro | Dati | Messaggio |
|------|--------|------|-----------|
| 2019 | Winkler (*JAMA Dermatol*) | 130 lesioni, con e senza penna | Specificità 84% → 46% con i segni di penna |
| 2021 | Groh, Fitzpatrick17k (CVPR-W) | 16.577 foto cliniche, 114 malattie | Pelli scure poco rappresentate; la rete generalizza male tra fototipi lontani |
| 2022 | Daneshjou, DDI (*Sci Adv*) | 656 foto con biopsia, fototipi I–VI | AUC 0,56–0,67; peggio su pelli scure; si corregge con dati diversi |
| 2022 | Daneshjou, CLEAR Derm (*JAMA Dermatol*) | consenso di 19 esperti ISIC | 25 punti per sviluppare e valutare l'AI dermatologica |

**Da leggere in seguito** (non in questo pacchetto): Bissoto et al. sugli artefatti nei dataset ISIC (2019–2020) ⚠️.
