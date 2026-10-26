# Tschandl et al., 2019 — Lettori umani contro algoritmi nella classificazione delle lesioni pigmentate (ISIC 2018)

- **Rivista:** *The Lancet Oncology* 20(7):938–947 (2019) · [DOI 10.1016/S1470-2045(19)30333-X](https://doi.org/10.1016/S1470-2045(19)30333-X) · PMID 31201137
- **Gruppo:** Vienna (Kittler, Tschandl) con l'International Dermoscopy Society, molti centri internazionali (anche Napoli, Modena, Trieste)
- **Testo letto:** completo (PubMed Central PMC8237239)
- **Tipo di immagini:** dermatoscopiche, **7 classi** (le classi di HAM10000)

## In una frase
Il più grande confronto aperto uomo-macchina: **511 lettori** di 63 Paesi contro **139 algoritmi** della challenge ISIC 2018, su tutte le lesioni pigmentate e non solo sul melanoma. I migliori algoritmi vincono nettamente, ma perdono terreno sulle immagini "nuove".

## Il problema
Gli studi precedenti (Esteva, Haenssle, Brinker) confrontavano soprattutto **melanoma vs nevo**. Nella pratica, però, in pazienti con forte danno solare fino al **50%** delle lesioni pigmentate asportate **non sono melanocitiche**. Serviva un confronto **multiclasse**, su dati pubblici, con i migliori algoritmi del mondo.

## Come hanno fatto
- **Training set:** HAM10000 (10.015 immagini), dato ai partecipanti della challenge ISIC 2018.
- **Test set:** 1.511 immagini:
  - 1.195 dalle stesse fonti di HAM10000;
  - **316 da centri esterni** (Turchia, Nuova Zelanda, Svezia, Argentina) per avere più tipi di pelle.
- **Algoritmi:** 139, da 77 laboratori. Per ogni immagine conta la classe con probabilità più alta.
- **Lettori umani:**
  - piattaforma web, batch casuali di 30 immagini;
  - prima 4 test di screening per verificare il livello;
  - 55% dermatologi, 23% specializzandi, 16% medici di base;
  - "esperti" = più di 10 anni di esperienza in dermatoscopia.
- **Tipi di batch:** bilanciato (stesso numero per classe), più benigni, più maligni, casuale.
- **Metrica principale:** numero di diagnosi corrette su 30, cioè l'**accuratezza bilanciata** (la media della sensibilità per classe). Così non conviene "dire sempre nevo".

## Risultati
- **Batch bilanciato:**
  - tutti i lettori: 17,91 corrette su 30;
  - **top 3 algoritmi: 25,85** (differenza 7,94).
- **Esperti contro top 3:** 18,78 vs 25,43 (differenza **6,65**).
- **Tutti gli algoritmi contro tutti i lettori:** +2,01 diagnosi corrette per gli algoritmi.
- **Unico caso in cui gli umani vincono:** nei batch **ricchi di casi maligni** gli esperti battono la media degli algoritmi (di circa 0,5 diagnosi).
- **Sensibilità media per classe:**
  - lettori 79,2%, esperti 81,2%;
  - top 3 algoritmi tra 84,5% e 88,5%.
- **Il caso più eclatante, i carcinomi intraepiteliali** (cheratosi attinica / Bowen):
  - esperti: sensibilità **51,2%**;
  - algoritmi: **90,7%**.
- **Benigno contro maligno**, voto di maggioranza dei lettori: AUC **0,958**, come i top 3 algoritmi (0,958–0,971, differenza non significativa).
- **Immagini da centri non presenti nel training** (out-of-distribution): il vantaggio delle macchine **si riduce molto**. Gli umani sono sotto del 3,6% invece che dell'11,4%.

## Messaggi chiave per la tesi
1. **Generalizzazione:** i modelli soffrono sulle immagini di centri mai visti. Serve **test esterno**.
2. **Metrica:** l'accuratezza bilanciata tratta tutti gli errori allo stesso modo, ma clinicamente scambiare un melanoma per un basocellulare è meno grave (entrambi si asportano) che scambiarlo per un nevo. Una metrica **benigno/maligno** o **asportare/rassicurare** è più rilevante.
3. **Il contesto manca:** né lettori né algoritmi avevano età, sede o confronto con altri nei ("brutto anatroccolo"). È uno scenario da **telemedicina**.
4. **"Saggezza della folla":** il voto di maggioranza dei lettori raggiunge l'AUC degli algoritmi.
5. Gli autori concludono che in futuro i classificatori saranno usati **sotto guida umana** e che bisogna testarli **nelle mani dei medici**. È l'introduzione esatta a Tschandl 2020.

## Limiti
- È una simulazione: 20 secondi circa per immagine, nessun paziente reale.
- Immagini da dispositivi e ingrandimenti diversi, a cui il lettore non è abituato.
- Il set australiano è più difficile (molte lesioni ambigue su pelle fotodanneggiata).

## Cosa porto in Neo Helper
- Usare l'**accuratezza bilanciata** per il multiclasse e affiancarla sempre all'**AUC benigno/maligno**.
- Prevedere un **test set esterno** fin dall'inizio (issue #19).
- Includere i **metadati** come input (età, sede), cosa che qui mancava.
- L'idea della **folla**: un **ensemble** di modelli (o di agenti) può essere più robusto di un singolo modello.
