# Koh et al., 2020 — Concept Bottleneck Models

- **Conferenza:** ICML 2020 (PMLR 119) · [arXiv 2007.04612](https://arxiv.org/abs/2007.04612)
- **Gruppo:** Stanford (Percy Liang) e Google Research (Been Kim)
- **Testo letto:** sintesi strutturata del testo completo generata da alphaXiv, non il PDF ⚠️.

## In una frase
Invece di andare direttamente dall'immagine alla diagnosi, la rete passa da un "collo di bottiglia" di **concetti clinici** che un esperto può leggere e anche **correggere**.

## Come funziona
- Due stadi: **immagine → concetti** (rete g), poi **concetti → diagnosi** (modello f).
- I concetti sono annotati a mano. Per esempio, nelle radiografie del ginocchio: restringimento dello spazio articolare, osteofiti.
- Tre modi di addestrare:
  - **indipendente:** f impara dai concetti veri;
  - **sequenziale:** f impara dai concetti predetti da g;
  - **congiunto:** tutto insieme, con un peso λ tra la perdita sui concetti e quella sulla diagnosi.
- **Intervento al momento del test:** l'esperto sostituisce un concetto sbagliato con quello giusto e la diagnosi si aggiorna.

## Risultati
Su due dataset: **OAI**, radiografie del ginocchio con 10 concetti clinici, e **CUB**, 200 specie di uccelli con 112 attributi.
- **Accuratezza paragonabile** ai modelli "scatola nera". In alcuni casi è migliore: su OAI il modello sequenziale e quello congiunto battono quello standard.
- I concetti predetti sono **molto più fedeli** di quelli estratti a posteriori da una rete normale (linear probe).
- **Correggere pochi concetti migliora molto la diagnosi.** Su OAI, l'errore (RMSE) passa da più di 0,4 a circa 0,3 correggendone 2 ⚠️.
- Più **robusti alle scorciatoie:** nel dataset "TravelingBirds" lo sfondo è legato alla specie solo durante l'addestramento, e i CBM ne soffrono meno.
- Più efficienti con pochi dati (OAI).

## Limiti
- Servono **annotazioni dei concetti** per ogni immagine di addestramento. È il costo che MONET (Kim 2024) cerca di eliminare generando i concetti in automatico.
- Se i concetti scelti sono incompleti, il modello perde informazione.

## Cosa porto in Neo Helper
- Per la dermoscopia i concetti naturali sono i **criteri della 7-point checklist** e dell'ABCD. Le etichette ci sono in **Derm7pt** e, per melanoma e nevi di HAM10000, nelle annotazioni di Chanda 2024.
- Un piccolo CBM sopra gli embedding di PanDerm è un esperimento realistico per il capitolo di explainability (Fase 4).
- L'**intervento** si traduce bene in interfaccia: il medico dice "il velo blu-biancastro non c'è" e vede cambiare il punteggio di malignità.
