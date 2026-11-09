# Jaklitsch et al., 2023 — DermaSensor: uno strumento per i medici di base

- **Rivista:** *Journal of Primary Care & Community Health* 14 (2023) · [DOI 10.1177/21501319231205979](https://doi.org/10.1177/21501319231205979) · PMID 37933569 · PMC10631325
- **Gruppo:** sei autori, tra cui Laura Ferris (University of Pittsburgh) ⚠️ verificare affiliazioni e conflitti d'interesse con l'azienda
- **Testo letto:** abstract e parti di introduzione e discussione (PMC).
- **Dati sull'autorizzazione FDA:** verificati il 2026-11-09 sulla banca dati De Novo della FDA e su Venkatesh et al., *npj Digit Med* 7:156 (2024), [DOI 10.1038/s41746-024-01161-1](https://doi.org/10.1038/s41746-024-01161-1).

## In una frase
DermaSensor **non guarda una foto**: misura come la luce viene diffusa dalla lesione (spettroscopia) e un algoritmo dice "indagare" o "monitorare". Con il suo aiuto, i medici di base riconoscono più tumori.

## Il dispositivo
- **Portatile**, appoggiato sulla lesione. Usa la **spettroscopia a diffusione elastica** (ESS) e un algoritmo di machine learning.
- Pensato per i **medici di base**, non per i dermatologi né per i pazienti.
- **FDA:** autorizzazione **De Novo DEN230008**, decisione del 12 gennaio 2024, **classe II**. È il primo dispositivo con AI per i tumori della pelle indicato per **medici non dermatologi**, in pazienti di 40 anni o più. La FDA ha chiesto studi dopo l'autorizzazione nelle popolazioni poco rappresentate (nello studio registrativo il 97,1% dei pazienti era bianco).
- **Studio registrativo DERM-SUCCESS** (Venkatesh 2024): 1.579 lesioni di 1.005 pazienti in 22 centri di medicina generale.
  - sensibilità **95,5%** (medici di base 83%);
  - specificità **20,7%**, cioè molti falsi positivi;
  - valore predittivo negativo 96,6%.

## Lo studio letto: utilità per i medici di base
- **57 medici di base** valutano **50 immagini cliniche** (25 maligne, 25 benigne), prima senza e poi con il risultato del dispositivo.

| | Senza dispositivo | Con dispositivo |
|---|---|---|
| Sensibilità diagnostica | 67% | **88%** |
| Sensibilità nella gestione ("invio o biopsia") | 81% | **94%** |
| Specificità | — | nessuna differenza significativa |

- **Limiti dichiarati:**
  - immagini e non pazienti veri (niente palpazione);
  - medici interessati al tema (selezione);
  - metà delle lesioni maligne, molto più che nella realtà.

## Messaggi chiave per la tesi
1. Il primo prodotto autorizzato dalla FDA **non è un classificatore di immagini**, e punta tutto sulla **sensibilità** a scapito della specificità.
2. Il pubblico è lo stesso che la letteratura indica come quello che guadagna di più dall'AI: i **non dermatologi** (Krakowski 2024).
3. Studi su immagini con 50% di tumori **sovrastimano** l'utilità reale.

## Cosa porto in Neo Helper
- **Confronto nella discussione:** DermaSensor (spettroscopia, alta sensibilità, bassa specificità) contro Neo Helper (dermoscopia, soglia regolabile, insieme conformal).
- Il nostro pubblico principale (medici non specialisti) è lo stesso di un prodotto già autorizzato: è un uso **realistico**.
