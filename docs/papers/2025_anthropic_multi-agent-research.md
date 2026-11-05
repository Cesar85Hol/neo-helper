# Anthropic, 2025 — Come abbiamo costruito il nostro sistema di ricerca multi-agente

- **Fonte:** blog di ingegneria di Anthropic, 13 giugno 2025 · J. Hadfield, B. Zhang, K. Lien, F. Scholz, J. Fox, D. Ford · [anthropic.com/engineering/multi-agent-research-system](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Testo letto:** pagina completa, tramite estrazione automatica (2026-11-04).

## In una frase
Un agente capo che divide la ricerca tra più sottoagenti in parallelo funziona molto meglio di un agente solo. Però consuma molti più token, e conviene solo per compiti davvero parallelizzabili.

## Architettura (orchestratore–lavoratori)
- **Agente capo:** analizza la domanda, scrive un piano e lo salva in **memoria** (oltre 200.000 token il contesto viene tagliato).
- **Sottoagenti:** lanciati in parallelo, ognuno con il suo contesto. Cercano, valutano i risultati e restituiscono una sintesi compressa.
- **Agente delle citazioni:** alla fine collega ogni affermazione del report alla sua fonte.

## Numeri chiave
- Il sistema multi-agente (Claude Opus 4 come capo, Claude Sonnet 4 come sottoagenti) supera un singolo Claude Opus 4 del **90,2%** nella valutazione interna di ricerca.
- **I token spiegano l'80%** della variabilità delle prestazioni (BrowseComp). Insieme al numero di chiamate ai tool e alla scelta del modello si arriva al 95%.
- **Costo:** un agente usa circa **4 volte** i token di una chat; un sistema multi-agente circa **15 volte**.
- La chiamata ai tool in parallelo riduce i tempi fino al 90% sulle domande complesse.

## Quando il multi-agente NON conviene
- Il valore del compito non giustifica il costo.
- Gli agenti devono condividere molto contesto o dipendono molto l'uno dall'altro.
- La maggior parte dei compiti di programmazione (poco parallelizzabili).
- Coordinamento in tempo reale.

## Principi di prompt
1. "Pensare come i propri agenti": simularli passo passo con gli stessi prompt e tool.
2. Insegnare al capo a **delegare bene**: obiettivo, formato di uscita, tool da usare, confini chiari.
3. Adattare lo sforzo alla complessità: 1 agente con 3–10 chiamate per un fatto semplice, fino a più di 10 sottoagenti per ricerche complesse.
4. Tool con scopo distinto e descrizione chiara. Un agente che migliora le descrizioni dei tool ha ridotto del 40% il tempo dei compiti.
5. Partire largo, poi restringere.

## Valutazione
- **Partire piccoli:** circa 20 domande reali bastano all'inizio, perché gli effetti sono grandi.
- **LLM come giudice** con una griglia: accuratezza dei fatti, delle citazioni, completezza, qualità delle fonti, efficienza dei tool.
- **Valutazione umana** per i casi che l'automatico non vede. Per esempio, i primi agenti preferivano siti ottimizzati per i motori di ricerca invece di fonti autorevoli.

## Affidabilità in produzione
- Gli errori si accumulano negli agenti che durano a lungo: servono **checkpoint** e ripartenze, non ricominciare da capo.
- **Tracciamento completo** delle decisioni per il debug.
- Esecuzione sincrona: il capo aspetta tutti i sottoagenti, ed è un collo di bottiglia.

## Cosa porto in Neo Helper
- La diagnosi di una lesione **non** è un compito molto parallelizzabile. Le dipendenze sono forti: qualità → segmentazione → classificazione → spiegazione. Quindi **v2 (agente singolo + tool)** è probabilmente sufficiente.
- Il multi-agente (v3) va giustificato con una misura. Candidati naturali per il parallelo:
  - spiegazione con Grad-CAM, concetti MONET e casi simili insieme;
  - un **Critic** che verifica il report.
- **Domanda di ricerca possibile:** "v3 multi-agente migliora davvero rispetto a v2, e a quale costo in token e tempo?". È la issue M4.4.
- Valutazione dei report con **LLM come giudice + griglia**, più una piccola verifica umana.
- Un **agente delle citazioni** ha senso anche da noi: ogni frase del report deve rimandare all'uscita di un tool.
