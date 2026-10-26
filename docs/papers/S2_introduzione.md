# §2 — Introduzione: dal "chi vince" al "come collaboriamo"

> Issue #2 · Fonti: PubMed. Ogni scheda riporta DOI e se è stato letto il testo completo o solo l'abstract.

I sei lavori di questa sezione raccontano una storia in tre atti, tra il 2017 e il 2020.

**Atto 1 — "La macchina vede come il dermatologo" (2017–2019).**
- **Esteva 2017** dimostra che una rete neurale, addestrata su circa 130.000 foto, eguaglia 21 dermatologi.
- **Haenssle 2018** e **Brinker 2019** ripetono il confronto sulle immagini **dermatoscopiche**, con 58 e 157 dermatologi: la rete batte la maggioranza.

**Atto 2 — "Dati aperti e confronto onesto" (2018–2019).**
- **HAM10000 (Tschandl 2018)** mette a disposizione di tutti 10.015 immagini in 7 classi.
- **Tschandl 2019** organizza la sfida più grande: 511 medici contro 139 algoritmi. Gli algoritmi vincono, ma sulle immagini di **centri mai visti** il vantaggio si riduce molto.

**Atto 3 — "Uomo + macchina" (2020).**
- **Tschandl 2020** cambia domanda: l'AI aiuta davvero il medico? Sì, soprattutto i meno esperti. Ma un'AI sbagliata inganna anche gli esperti, e **la forma** in cui l'AI presenta il risultato conta.

**Il filo conduttore per Neo Helper:** non basta un modello accurato. Servono:
- dati aperti e split corretti;
- test su dati esterni;
- metriche cliniche (sensibilità a specificità fissata);
- un'interfaccia pensata per la **collaborazione**, con incertezza visibile.

| Anno | Paper | Immagini | Confronto | Messaggio |
|------|-------|----------|-----------|-----------|
| 2017 | Esteva (*Nature*) | 129.450 cliniche | 21 dermatologi | AI a livello di dermatologo |
| 2018 | Haenssle (*Ann Oncol*) | dermatoscopiche, test su 100 | 58 dermatologi | CNN AUC 0,86 vs 0,79 |
| 2018 | Tschandl (*Sci Data*) | 10.015 dermatoscopiche | — | Il dataset HAM10000 |
| 2019 | Brinker (*Eur J Cancer*) | 12.378 pubbliche, test su 100 | 157 dermatologi | Battuti 136 su 157 |
| 2019 | Tschandl (*Lancet Oncol*) | 1.511 di test, 7 classi | 511 lettori vs 139 algoritmi | Algoritmi migliori, ma calano sui dati esterni |
| 2020 | Tschandl (*Nat Med*) | dermatoscopiche, 7 classi | medici con e senza AI | La collaborazione batte entrambi |
