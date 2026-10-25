# 04 — Etica, privacy, regolatorio

## Posizionamento
- Progetto **di ricerca/didattico**, open source. Nel README e in ogni interfaccia: *"Non è un dispositivo medico. Non usare per decisioni cliniche."*
- Utente target: **medico** (second opinion), non il paziente.

## Regolatorio (da approfondire nella Fase 1)
- **UE — MDR 2017/745**: software con finalità diagnostica = dispositivo medico; la regola 11 lo porta tipicamente in classe IIa o superiore → marcatura CE con organismo notificato. Fuori scope per noi, ma da descrivere nella tesi.
- **UE — AI Act (Reg. 2024/1689)**: AI in dispositivi medici = **alto rischio** (obblighi su dati, documentazione, supervisione umana, trasparenza). Applicazione graduale 2025–2027 ⚠️.
- **USA — FDA**: SaMD, 510(k)/De Novo; esempio DermaSensor (2024).
- **GDPR**: le immagini cutanee sono **dati sanitari** (art. 9) e possono essere identificative (tatuaggi, volto). Nella demo pubblica: nessuna conservazione o consenso esplicito, oppure solo immagini dei dataset.

## Bias e fairness
- I dataset ISIC sono prevalentemente fototipi chiari → valutare per sottogruppi (Fitzpatrick, età, sede anatomica, sesso) e dichiarare i limiti.
- Artefatti/shortcut (inchiostro chirurgico, righelli) → test di robustezza.

## Documentazione responsabile
- **Model card** (Mitchell et al. 2019) e **datasheet for datasets** (Gebru et al. 2021)
- Checklist **CLEAR Derm** (Daneshjou 2022), **TRIPOD+AI** (2024), **CONSORT-AI / DECIDE-AI** per studi con utenti

## Rischi specifici degli LLM/agenti
- Allucinazioni nel report → l'LLM può citare solo valori presenti nell'output dei tool (validazione schema + controllo automatico).
- Overconfidence/automation bias del medico → mostrare incertezza, casi simili, e mai un singolo "verdetto".
- Prompt injection tramite metadati/testo nell'immagine → sanificare input.
