# §8 — Introduzione: prodotti sul mercato e regole

> Issue #8 (M1.8) · Fonti: PubMed, più alcune fonti web per le notizie regolatorie (segnate con ⚠️). Ogni scheda dice cosa è stato letto.

Le sezioni precedenti parlavano di ricerca. Questa guarda **cosa esiste davvero** sul mercato e **quali regole** valgono quando un software aiuta a diagnosticare un tumore della pelle.

**1. Le app per il pubblico: poche prove.**
- **Freeman 2020** (*BMJ*, revisione sistematica): 9 studi su 6 app, piccoli e di bassa qualità.
  - **SkinVision** (marchio CE): sensibilità 80% e specificità 78%, ma su lesioni scelte e fotografate da medici.
  - Due app ritirate dopo sanzioni americane.
  - Conclusione: la marcatura CE **non protegge** abbastanza il pubblico.
- **Wongvibulsin 2024** (*JAMA Dermatology*): delle 41 app con AI negli store, **nessuna** approvata dalla FDA, quasi nessuna con prove, dermatologi coinvolti, trasparenza o privacy.

**2. I prodotti per i medici: prove migliori, regole più severe.**
- **DermaSensor** (USA): non usa foto ma la **spettroscopia**.
  - È il primo dispositivo con AI per i tumori della pelle autorizzato dalla **FDA** per i non specialisti (De Novo, 12 gennaio 2024, classe II, verificato), per i **medici di base**.
  - Molto sensibile (95,5%), poco specifico (20,7%) nello studio registrativo (Venkatesh 2024).
  - Con il suo aiuto i medici di base passano dal 67% all'88% di sensibilità su immagini (Jaklitsch 2023).
- **DERM** di Skin Analytics (Regno Unito): dermoscopia con smartphone, dentro i percorsi del servizio sanitario inglese, con più di 81.000 pazienti.
  - In uno studio prospettico trova i tumori quanto i teledermatologi, ma evita **più invii inutili** (Marsden 2024).
  - UKCA classe IIa nel 2022; **marchio CE di classe III** con uso autonomo nel 2025 (fonte aziendale ⚠️).

**3. Le regole in Europa.**
- **MDR** (regolamento UE 2017/745, dal 2021): un software che aiuta la diagnosi è un **dispositivo medico**, di solito almeno di classe IIa, con organismo notificato, valutazione clinica e sorveglianza dopo la vendita (Malvehy 2022).
- **AI Act** (regolamento UE 2024/1689): l'AI nei dispositivi medici è **ad alto rischio**, con obblighi su dati, gestione del rischio, trasparenza, supervisione umana e monitoraggio. Nel 2025–2026 la UE discute di **togliere molte di queste tutele** ai dispositivi medici. Il compromesso del luglio 2026 sul Digital Omnibus le ha mantenute, ma l'Health Innovation Package è ancora aperto (Van Kolfschooten 2026).
- **USA:** la FDA autorizza con le procedure 510(k), De Novo o PMA. Nessuna app per il pubblico è autorizzata.

**Il filo conduttore per Neo Helper:**
- Neo Helper è un **prototipo di ricerca**, non un dispositivo medico: nessun uso clinico, nessuna diagnosi al paziente, avvisi ben visibili.
- Il pubblico scelto (**medici, soprattutto non specialisti**) è lo stesso di DermaSensor e DERM: un uso realistico.
- Le licenze non commerciali (PanDerm, MONET, HAM10000) **e** le regole (MDR classe IIa o superiore, AI Act alto rischio) dicono la stessa cosa: un prodotto richiederebbe dati, modelli, prove cliniche e certificazioni diversi.
- I requisiti dell'AI Act sono una buona **lista di controllo volontaria**: data card, model card, supervisione del medico, catena di prove, registro delle versioni.

| Prodotto | Tecnologia | Per chi | Stato regolatorio | Prove |
|----------|-----------|---------|-------------------|-------|
| SkinVision | Foto smartphone + algoritmo | Pubblico | CE (prima dell'MDR) | Sens. 80%, spec. 78% su lesioni scelte da medici |
| DermaSensor | Spettroscopia + ML | Medici di base | FDA De Novo 2024, classe II | Sens. 95,5%, spec. 20,7% |
| DERM (Skin Analytics) | Dermoscopia smartphone + ensemble CNN | Servizio sanitario, triage | UKCA IIa 2022; CE classe III 2025 ⚠️ | Prospettico: meno invii a pari sensibilità |
| App AI negli store (41) | Varie | Pubblico | Nessuna FDA | Quasi nessuna prova |

**Da leggere in seguito:** la decisione De Novo della FDA su DermaSensor; il testo dell'MDR (regola 11) e dell'AI Act (articolo 6 e Allegato I); Moleanalyzer Pro (FotoFinder) ⚠️.
