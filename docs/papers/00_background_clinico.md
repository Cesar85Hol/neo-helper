# §1 — Background clinico: melanoma, nevi e dermatoscopia

> Issue #1 · Fonti principali recuperate da PubMed: Argenziano 1998 ([DOI](https://doi.org/10.1001/archderm.134.12.1563)), Argenziano 2003 ([DOI](https://doi.org/10.1067/mjd.2003.281)), Tschandl 2018 ([DOI](https://doi.org/10.1038/sdata.2018.161)), Esteva 2017 ([DOI](https://doi.org/10.1038/nature21056)).
> Le parti segnate con ⚠️ vengono da conoscenza generale e vanno verificate su un manuale o una linea guida.

## In una frase
Il melanoma è raro rispetto agli altri tumori della pelle, ma è quello che uccide di più; se lo si prende presto si guarisce quasi sempre con una semplice asportazione. Tutto il lavoro di Neo Helper serve a **riconoscerlo prima**, distinguendolo dai nei benigni e dalle altre lesioni che gli somigliano.

## 1. Perché la diagnosi precoce conta
- Negli Stati Uniti i melanomi sono meno del 5% dei tumori cutanei ma causano circa il **75% dei decessi** per tumore della pelle (dati citati da Esteva 2017).
- La sopravvivenza a 5 anni passa da **oltre il 99%** se il melanoma è scoperto in fase iniziale a **circa il 14%** in fase avanzata (Esteva 2017).
- Un melanoma asportato in fase precoce "può essere curato con una semplice escissione chirurgica" (Tschandl 2018).

## 2. Le lesioni che un sistema deve distinguere
Le 7 classi del dataset HAM10000, che coprono **oltre il 95%** delle lesioni pigmentate viste in pratica clinica (Tschandl 2018):

| Sigla | Nome | Benigna/Maligna | Come appare (in breve) |
|-------|------|-----------------|------------------------|
| **nv** | Nevo melanocitico ("neo") | Benigno | Di solito **simmetrico** per colori e strutture; moltissime varianti |
| **mel** | Melanoma | **Maligno** | Spesso "caotico": asimmetria di forma, colori e strutture. Include il melanoma in situ |
| **bcc** | Carcinoma basocellulare | Maligno (raramente metastatizza) | Cresce in modo distruttivo se non trattato; varianti piatte, nodulari, pigmentate |
| **akiec** | Cheratosi attinica / malattia di Bowen | Pre-maligna / carcinoma intraepiteliale | Indotte da UV, su pelle fotodanneggiata; possono evolvere in carcinoma squamocellulare |
| **bkl** | Cheratosi benigne (seborroica, lentigo solare, LPLK) | Benigne | Le LPLK possono **imitare il melanoma** e spesso vengono asportate per dubbio |
| **df** | Dermatofibroma | Benigno | Reticolo periferico con **chiazza bianca centrale** |
| **vasc** | Lesioni vascolari (angiomi…) | Benigne | Rosse/viola, "lacune" ben delimitate; pigmentate da emoglobina, non melanina |

Da ricordare: quasi tutte queste lesioni hanno anche varianti **senza pigmento** (es. melanoma amelanotico), che sono più difficili e non sono incluse in HAM10000.

## 3. L'esame a occhio nudo: la regola ABCDE ⚠️
Regola mnemonica per pazienti e medici non specialisti:
- **A**simmetria — le due metà non coincidono
- **B**ordi irregolari, frastagliati
- **C**olore non uniforme (più tonalità di marrone, nero, rosso, blu, bianco)
- **D**iametro > 6 mm
- **E**voluzione — il neo cambia nel tempo (forma, colore, dimensione, sintomi)

La "E" è considerata il criterio più importante: un neo che cambia merita sempre attenzione.

**Il segno del "brutto anatroccolo"** (ugly duckling) ⚠️: in un paziente con molti nei, quelli simili tra loro sono probabilmente benigni; il neo che "non somiglia agli altri" è sospetto. Tschandl 2019 nota che questo confronto **migliora sensibilità e specificità** ma richiede di vedere l'intero paziente, non una lesione isolata: un limite di quasi tutti gli studi di AI.

## 4. La dermatoscopia
Il **dermatoscopio** è una lente con illuminazione (polarizzata o con liquido a immersione) che permette di vedere strutture sotto la superficie della pelle, invisibili a occhio nudo. Migliora la diagnosi rispetto all'occhio nudo, ma **richiede formazione ed esperienza** (Tschandl 2019).

Le immagini dermatoscopiche sono molto più **standardizzate** delle foto cliniche (stessa distanza, luce controllata). Per questo la maggior parte dei dataset e degli algoritmi lavora su immagini dermatoscopiche.

## 5. Gli algoritmi diagnostici dermatoscopici
Sono "ricette" per trasformare l'osservazione in una decisione.

### 5.1 Pattern analysis
Il metodo classico degli esperti: si riconosce il **pattern globale** (reticolare, globulare, omogeneo…) e le **strutture locali**. È il più accurato ma il più difficile da imparare.

### 5.2 Regola ABCD della dermatoscopia (Stolz, 1994) ⚠️
Da non confondere con l'ABCDE clinico. Si assegna un punteggio a:
- **A**symmetry (0–2), **B**order (0–8 segmenti con interruzione brusca), **C**olor (1–6 colori), **D**ifferential structures (1–5 strutture).

Il **TDS (Total Dermoscopy Score)** = A×1,3 + B×0,1 + C×0,5 + D×0,5.
- TDS < 4,75 → probabilmente benigno
- 4,75–5,45 → sospetto
- \> 5,45 → altamente sospetto per melanoma

Interessante per Neo Helper: è **calcolabile in parte automaticamente** da una segmentazione (asimmetria, bordi, numero di colori).

### 5.3 La 7-point checklist (Argenziano, 1998)
Pubblicata su *Archives of Dermatology* da un gruppo di Napoli ([DOI](https://doi.org/10.1001/archderm.134.12.1563)).
- **Criteri maggiori** (2 punti ciascuno) ⚠️: reticolo pigmentario atipico, velo blu-biancastro, pattern vascolare atipico.
- **Criteri minori** (1 punto ciascuno) ⚠️: strie irregolari, punti/globuli irregolari, chiazze (blotches) irregolari, strutture di regressione.
- Un punteggio **≥ 3** indica melanoma ⚠️.

Risultati dello studio originale (342 lesioni melanocitiche con istologia):

| Metodo | Sensibilità | Specificità |
|--------|-------------|-------------|
| 7-point checklist | **95%** | 75% |
| Regola ABCD | 85% | 66% |
| Pattern analysis (esperti) | 91% | **90%** |

Con la 7-point checklist, gli osservatori **meno esperti** ottenevano un'accuratezza migliore che con la regola ABCD.

### 5.4 Il Consensus Net Meeting (Argenziano, 2003)
40 dermatoscopisti esperti hanno valutato via Internet 108 lesioni con 4 algoritmi ([DOI](https://doi.org/10.1067/mjd.2003.281)). Messaggi chiave:
- Procedura in **due passi**: prima "melanocitica o no?", poi "melanoma o benigna?".
- **Accordo tra osservatori** discreto-buono sulla diagnosi finale, ma **scarso sui singoli criteri** dermatoscopici: esperti diversi vedono strutture diverse nella stessa immagine.
- La pattern analysis ha dato la performance migliore (rapporto di verosimiglianza positivo 5,1); gli altri algoritmi hanno sensibilità simile ma specificità più bassa.

**Perché importa per noi:** se gli esperti non sono d'accordo sui singoli criteri, anche le **etichette** dei dataset sui criteri (es. Derm7pt) sono rumorose. Un agente che calcola i criteri va presentato come "aiuto", non come verità.

## 6. Come si stabilisce la "verità" (ground truth)
In HAM10000 la diagnosi di riferimento viene da quattro fonti (Tschandl 2018):
1. **Istopatologia** (>50% dei casi): la lesione è stata asportata e analizzata al microscopio. È lo standard migliore.
2. **Follow-up**: nevi monitorati con dermatoscopia digitale senza cambiamenti per 1,5 anni o 3 visite.
3. **Consenso di esperti**: per lesioni benigne tipiche non asportate.
4. **Microscopia confocale** in vivo per alcune cheratosi.

Da ricordare per la tesi: dataset fatti solo di lesioni **asportate** soffrono di *verification bias* (si asporta solo ciò che sembra sospetto).

## Cosa porto in Neo Helper
- Le **7 classi HAM10000** come tassonomia di partenza, più l'aggregazione **benigno/maligno** per la decisione clinica (asportare/rassicurare).
- Un **agente "criteri dermoscopici"** (ABCD/TDS e 7-point) come spiegazione strutturata, sapendo che l'accordo umano su questi criteri è basso.
- L'idea del **brutto anatroccolo**: in futuro, confrontare più nei dello stesso paziente.
- Il campo **"tipo di ground truth"** (istologia, follow-up, consenso) va mostrato e usato nelle analisi.
