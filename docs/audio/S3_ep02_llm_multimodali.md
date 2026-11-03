# Episodio 9 — Gli LLM che guardano la pelle: SkinGPT-4 e i modelli generalisti

Nell'episodio precedente abbiamo parlato di reti che vedono. Oggi parliamo di modelli che vedono e parlano: i grandi modelli linguistici multimodali. Sono la stessa famiglia di ChatGPT, Gemini e Claude, ma capaci di ricevere un'immagine.

Primo lavoro: SkinGPT-4, pubblicato su Nature Communications nel duemilaventiquattro. L'ho letto per intero. L'idea è semplice: si prende un modello che vede, un modello che parla, Llama due, e si costruisce un piccolo ponte tra i due. Si addestra solo il ponte. In due tappe. Nella prima, il modello impara i concetti clinici: papula, placca, crosta, eritema. Quarantotto concetti in tutto. Nella seconda impara le diagnosi, da circa cinquantamila immagini e dalle note dei medici.

Il risultato è un sistema che ricevi una foto e ti risponde come un medico di famiglia: descrive la lesione, propone una diagnosi, suggerisce le cause e i possibili trattamenti. E puoi fargli domande.

Ma attenzione a come è stato valutato. Centocinquanta casi. Cinque dermatologi leggono le risposte e dicono se sono d'accordo. L'ottanta per cento delle diagnosi viene giudicato corretto o pertinente. Sembra tanto, ma non è una misura di accuratezza: i medici sanno che la risposta viene da una macchina, la leggono dopo, e danno un voto di gradimento. Mancano sensibilità, specificità, un test indipendente. E il sistema è pensato anche per l'autodiagnosi dei pazienti, che è lo scenario più rischioso di tutti. Gli autori stessi ammettono il problema delle allucinazioni: il modello può inventare con sicurezza.

Secondo lavoro, molto recente: Bhagwat e colleghi, duemilaventisei. Di questo ho letto solo il riassunto. Hanno preso due modelli commerciali, ChatGPT e Gemini, e li hanno messi alla prova su seicentocinquantasei foto con diagnosi confermata dalla biopsia, di pazienti con ogni colore di pelle. In più, hanno fatto un esperimento furbo: nel messaggio al modello hanno scritto il fototipo del paziente. A volte quello giusto, a volte uno sbagliato.

I risultati. Primo: dire il fototipo al modello non serve a niente. Secondo: se il fototipo scritto è molto sbagliato, ChatGPT dimentica più spesso un tumore vero tra le sue prime tre ipotesi. Gli autori lo chiamano lethal miss, l'errore che può costare la vita. Terzo: entrambi i modelli dicono "maligno" troppo spesso. Gemini riconosce come benigne poco più di una lesione benigna su cinque. Quarto: sulle pelli scure le lesioni maligne vengono riconosciute meno. Conclusione degli autori: nessuno dei due è adatto a un uso autonomo.

Che cosa ci portiamo a casa per Neo Helper? Una regola che avevamo già deciso, e che ora ha due prove in più. Il modello linguistico non deve classificare. Deve orchestrare: chiamare i modelli di visione, raccogliere i numeri, e scriverli in un report chiaro e onesto. Le probabilità vengono sempre da un modello misurato, e il report deve dire da dove vengono.

E un'idea da SkinGPT-4 che vale la pena tenere: insegnare prima i concetti clinici e poi la diagnosi. I quarantotto concetti possono diventare il vocabolario del nostro report. Un'ultima cosa: le informazioni che l'utente scrive, come il fototipo o l'età, non vanno trattate come certe. Un dato sbagliato nel prompt può peggiorare la diagnosi.
