# Haenssle et al., 2018 — "Man against machine": rete neurale contro 58 dermatologi sul melanoma in dermatoscopia

- **Rivista:** *Annals of Oncology* 29(8):1836–1842 (2018) · [DOI 10.1093/annonc/mdy166](https://doi.org/10.1093/annonc/mdy166) · PMID 29846502
- **Gruppo:** Università di Heidelberg, con collaboratori internazionali (incluso Memorial Sloan Kettering)
- **Testo letto:** abstract strutturato (PubMed). Il testo completo non è su PubMed Central.
- **Tipo di immagini:** **dermatoscopiche**, lesioni melanocitiche

## In una frase
Una rete neurale addestrata su immagini dermatoscopiche ha battuto la maggior parte di **58 dermatologi di 17 Paesi**, inclusi 30 esperti, nel distinguere il melanoma dai nevi.

## Il problema
Esteva 2017 aveva usato soprattutto foto cliniche e un gruppo di dermatologi di un solo centro. Mancava un confronto con un **gruppo ampio e internazionale** di dermatologi, sulle immagini dermatoscopiche che si usano davvero in ambulatorio.

## Cosa hanno fatto
- **Rete:** Google **Inception v4**, addestrata e validata su immagini dermatoscopiche con diagnosi.
- **Test set:** 100 immagini.
- **Lettori:** 58 dermatologi internazionali, di cui 30 esperti.
- **Studio in due livelli:**
  - **Livello I:** solo l'immagine dermatoscopica.
  - **Livello II:** immagine più informazioni cliniche e foto d'insieme, come in una visita reale.
- Confronto anche con i migliori 5 algoritmi della challenge **ISBI 2016**.
- Studio registrato nel registro tedesco degli studi clinici (DRKS00013570).

## Risultati
| | Sensibilità | Specificità |
|--|-------------|-------------|
| Dermatologi, livello I | 86,6% | 71,3% |
| Dermatologi, livello II | 88,9% | 75,7% |
| **CNN**, alla stessa sensibilità dei dermatologi | 86,6% / 88,9% | **82,5%** |

- **AUC: CNN 0,86 vs dermatologi 0,79** (p < 0,01).
- Le **informazioni cliniche** aiutano i dermatologi (la specificità sale in modo significativo), ma non bastano a raggiungere la rete.
- La CNN è vicina ai migliori 3 algoritmi della challenge ISBI 2016.
- Conclusione degli autori: i medici, **a prescindere dall'esperienza**, potrebbero beneficiare dell'assistenza di una CNN.

## Come leggere questi numeri
- A parità di melanomi riconosciuti, la rete fa **meno falsi allarmi**: 82,5% di specificità contro 71–76%. In pratica significa meno nei benigni asportati inutilmente.
- Il test set è piccolo (100 immagini) e scelto dai ricercatori: i numeri vanno presi con prudenza.

## Limiti
- Test **retrospettivo** su un set ridotto e "arricchito" di casi difficili.
- Solo lesioni **melanocitiche** (melanoma vs nevi), non le altre classi.
- Il titolo "uomo contro macchina" ha generato critiche: la rivista ha pubblicato una lettera ("What type of man against machine?") e una risposta degli autori (PMID 29992324). Il vero scenario clinico è **uomo + macchina**.
- ⚠️ Pochi dati sulla diversità dei fototipi.

## Cosa porto in Neo Helper
- Lo schema a **livelli di informazione** (solo immagine → immagine + dati clinici) è un'ottima idea per i nostri esperimenti: misurare quanto aiutano i metadati (età, sede).
- La metrica clinica "**specificità a sensibilità fissata**" (quella dei dermatologi) è più parlante dell'accuratezza.
- Il paper prepara la domanda chiave che Tschandl 2020 affronterà: non chi vince, ma **come collaborano**.
