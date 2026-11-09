# Tu et al., 2025 — AMIE: verso un'AI che fa diagnosi conversando

- **Rivista:** *Nature* (2025) · [DOI 10.1038/s41586-025-08866-7](https://doi.org/10.1038/s41586-025-08866-7) · PMID 40205050 · PMC12158756
- **Seguito:** Liévin et al., *Towards conversational artificial intelligence for disease management*, *Nature* (2026) · [DOI 10.1038/s41586-026-10764-5](https://doi.org/10.1038/s41586-026-10764-5) · PMID 42310463 · PMC13421318
- **Gruppo:** Google Research e Google DeepMind
- **Testo letto:** abstract e discussione del paper del 2025; abstract, limiti e conclusioni di quello del 2026. Il testo completo è in PMC, ma non l'ho letto tutto ⚠️.

## In una frase
AMIE è un LLM addestrato per fare l'**anamnesi in chat** e proporre una diagnosi differenziale. In visite simulate con pazienti-attori ha fatto meglio dei medici di base, ma gli autori dicono chiaramente che **non è pronto** per la clinica.

## Cosa hanno fatto (2025)
- LLM ottimizzato per il **dialogo diagnostico**. Si addestra in un **ambiente simulato in cui gioca contro sé stesso** (paziente, medico, critico), con feedback automatico.
- Valutazione in stile **OSCE**, l'esame clinico a stazioni:
  - studio randomizzato in doppio cieco e crossover;
  - **159 casi** da Canada, Regno Unito e India;
  - **20 medici di base** contro AMIE;
  - pazienti-attori, consultazioni in **chat testuale**.
- Giudicano medici specialisti e pazienti-attori, su molti assi: anamnesi, accuratezza diagnostica, gestione, comunicazione, empatia.

## Risultati (2025)
- Diagnosi differenziali **più accurate e complete** di quelle dei medici.
- Migliore su **30 assi su 32** secondo gli specialisti e su **25 su 26** secondo i pazienti-attori.
- Raccoglie le informazioni bene quanto i medici. A parità di informazioni raccolte, forma una diagnosi differenziale più completa.

## Il seguito (2026): gestione della malattia
- AMIE diventa un **sistema agentico per più visite**, ancorato alle **linee guida cliniche** (NICE, BMJ Best Practice) e ai **prontuari dei farmaci**.
- Contro 21 medici di base su 100 scenari con più visite:
  - **non inferiore** nel ragionamento sulla gestione;
  - migliore per precisione delle terapie e degli esami, e per aderenza alle linee guida.
- Nuovo benchmark **RxQA** sui farmaci: AMIE fa meglio dei medici sulle domande difficili.

## Limiti dichiarati dagli autori
- **Chat testuale sincrona**: non è il modo in cui i medici lavorano di solito, e penalizza i medici.
- Scenari **simulati** con attori, non pazienti reali.
- Il sistema "**non è pronto** per l'uso clinico". Servono studi prospettici con supervisione etica e di sicurezza.

## Messaggi chiave per la tesi
1. Lo stato dell'arte dei sistemi conversazionali medici è **studiato con rigore** (randomizzazione, cieco, molti assi di valutazione), ma resta in simulazione.
2. Il passo avanti del 2026 è l'**ancoraggio a fonti autorevoli** (linee guida, prontuari). È la stessa idea del RAG di DermAgent e delle "citazioni" di Anthropic.
3. AMIE lavora sul **testo**. Neo Helper parte dall'**immagine**, che è un problema diverso. Qui la parte visiva resta ai modelli specialistici (Bhagwat 2026).

## Cosa porto in Neo Helper
- **Griglia di valutazione del report** ispirata ad AMIE: completezza, correttezza, chiarezza, adeguatezza delle raccomandazioni, comunicazione dell'incertezza. Va giudicata da medici, o da un LLM giudice verificato su un campione.
- Il report deve citare **fonti cliniche** (criteri dermoscopici, raccomandazioni di invio) prese da un piccolo archivio controllato, non dalla memoria del modello.
- Lessico prudente: come AMIE, dichiarare sempre che è uno strumento **di ricerca**.
