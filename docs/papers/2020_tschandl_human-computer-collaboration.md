# Tschandl et al., 2020 — La collaborazione uomo-computer nel riconoscimento del cancro della pelle

- **Rivista:** *Nature Medicine* 26(8):1229–1234 (2020) · [DOI 10.1038/s41591-020-0942-0](https://doi.org/10.1038/s41591-020-0942-0) · PMID 32572267
- **Gruppo:** Vienna (Kittler, Tschandl) con centri internazionali (Napoli, Modena, Trieste, Barcellona, Brisbane, New York…)
- **Testo letto:** **solo abstract** (PubMed). L'articolo completo è a pagamento.
  I numeri segnati con ⚠️ vengono da memoria di letture secondarie e **vanno verificati** sul testo completo (issue #9).
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
- Studio con **medici di diversi livelli di esperienza** (circa 300 lettori ⚠️; da meno di 1 anno a oltre 10 anni di esperienza) su immagini dermatoscopiche delle **7 classi** HAM10000/ISIC 2018.
- Il lettore dà una diagnosi, poi vede il supporto dell'AI e può cambiarla.
- **Rappresentazioni dell'AI confrontate:**
  1. **probabilità multiclasse** (un istogramma con la probabilità di ciascuna delle 7 diagnosi);
  2. **probabilità di malignità** (un solo numero: quanto è probabile che sia maligna);
  3. **CBIR** (*content-based image retrieval*): l'AI mostra **immagini simili** già diagnosticate.
- **Scenari clinici simulati:** supporto diretto, **second opinion**, **triage in telemedicina**.
- Esperimento con **AI volutamente difettosa**: cosa fanno i medici se l'AI sbaglia?
- Analisi delle **mappe di attivazione** (class activation maps) per capire dove guarda l'AI.

## Risultati (dall'abstract)
- L'AI di buona qualità **migliora l'accuratezza diagnostica** oltre quella dell'AI da sola e dei medici da soli.
- **I meno esperti guadagnano di più.**
- Su dispositivi mobili, le **probabilità multiclasse** funzionano **meglio del CBIR**.
- L'AI è utile anche come **second opinion** e per il **triage** in telemedicina.
- **L'AI difettosa inganna tutti**, esperti inclusi.
- Le mappe di attivazione hanno dato **indicazioni utili a migliorare la diagnosi umana**: guardando dove guarda l'AI, i medici possono imparare qualcosa.

### Numeri da verificare ⚠️
- Con le probabilità multiclasse, l'accuratezza dei lettori sarebbe passata da circa il **64% a circa il 77%** (circa +13 punti percentuali).
- Le mappe di attivazione avrebbero mostrato che per le cheratosi attiniche pigmentate l'AI usa anche la **pelle intorno alla lesione** (fotodanneggiata). Insegnarlo a studenti di medicina ne avrebbe migliorato la diagnosi.

## Messaggi chiave per la tesi
1. **Il valore sta nella collaborazione**, non nella gara uomo-macchina.
2. **La forma dell'output conta**: una distribuzione di probabilità su più diagnosi è più utile di un singolo numero o di immagini simili, almeno in questo studio.
3. **Automation bias**: se l'AI sbaglia con sicurezza, il medico tende a seguirla. Servono **incertezza** visibile e meccanismi per dire "non lo so".
4. L'AI può anche **insegnare**: l'explainability è anche uno strumento didattico.

## Limiti
- Studio su **immagini**, non su pazienti reali.
- Senza testo completo non posso riportare i dettagli di metodo. Da recuperare.

## Cosa porto in Neo Helper
- **Interfaccia:** mostrare la **distribuzione su tutte le classi**, non un solo verdetto. Il CBIR (casi simili) può restare come funzione secondaria.
- **Agente Critic/Safety** e **quantificazione dell'incertezza**: sono la risposta diretta al rischio di "AI difettosa".
- **Valutazione con utenti** (Fase 7): misurare il miglioramento del medico **con e senza** Neo Helper, non solo l'accuratezza del modello.
- **Heatmap** (Grad-CAM) come strumento di spiegazione **e** di formazione.
