# 04 — Etica, privacy, regolatorio

## Posizionamento
- Progetto **di ricerca/didattico**, open source. Nel README e in ogni interfaccia: *"Non è un dispositivo medico. Non usare per decisioni cliniche."*
- Utente target: **medico** (second opinion), non il paziente.

## Regolatorio (aggiornato il 2026-11-06, Pacchetto 4)
Fonti e dettagli: [S8_introduzione.md](papers/S8_introduzione.md) e le schede collegate.

- **UE — MDR 2017/745** (in applicazione da maggio 2021):
  - un software con finalità diagnostica è un **dispositivo medico**;
  - con la regola 11 è tipicamente almeno in **classe IIa**, con marcatura CE tramite **organismo notificato**;
  - servono valutazione clinica, gestione del rischio, sistema qualità e sorveglianza dopo l'immissione sul mercato;
  - fonte: [Malvehy 2022](papers/2022_malvehy_mdr-dermatology.md).
  
  Esempio: **DERM** (Skin Analytics) ha la **classe III** per l'uso autonomo (2025, fonte aziendale ⚠️). Il periodo di transizione per i dispositivi già esistenti è stato prorogato al 2027–2028 (reg. UE 2023/607 ⚠️ da verificare).
- **UE — AI Act** (reg. 2024/1689, in vigore da agosto 2024):
  - l'AI nei dispositivi medici è ad **alto rischio** (Allegato I);
  - obblighi su **dati** (qualità e rappresentatività), gestione del rischio, **documentazione e trasparenza**, **supervisione umana**, **monitoraggio**;
  - obblighi per l'Allegato I dal 2 agosto 2027 ⚠️ da verificare.
  
  **Il quadro è in movimento:** l'Health Innovation Package (dicembre 2025) proporrebbe di togliere quasi tutti questi obblighi ai dispositivi medici. Il compromesso sul Digital Omnibus (luglio 2026) li ha per ora mantenuti ([Van Kolfschooten 2026](papers/2026_vankolfschooten_ai-act.md)). Da ricontrollare prima della consegna della tesi.
- **USA — FDA:**
  - percorsi 510(k), De Novo, PMA;
  - **DermaSensor** è il primo dispositivo con AI per i tumori della pelle autorizzato (De Novo, gennaio 2024 ⚠️). È per i medici di base e usa la spettroscopia, non le foto;
  - nessuna app per il pubblico è autorizzata ([Freeman 2020](papers/2020_freeman_smartphone-apps.md), [Wongvibulsin 2024](papers/2024_wongvibulsin_ai-apps.md)).
- **GDPR:** le immagini cutanee sono **dati sanitari** (art. 9) e possono essere identificative (tatuaggi, volto). Nella demo pubblica: nessuna conservazione o consenso esplicito, oppure solo immagini dei dataset.

### Cosa significa per Neo Helper
- **Perché non è un dispositivo medico:** è un prototipo di ricerca. Non è immesso sul mercato, non è usato per decisioni cliniche e non dà diagnosi ai pazienti. Gli avvisi lo dicono in ogni interfaccia.
- **Cosa servirebbe per diventarlo**, da descrivere nella tesi:
  - dati e modelli con licenze adatte (oggi PanDerm, MONET e HAM10000 sono non commerciali);
  - sistema qualità;
  - valutazione clinica prospettica;
  - classe IIa o superiore con organismo notificato;
  - obblighi dell'AI Act;
  - sorveglianza dopo l'immissione sul mercato.
- **I requisiti dell'AI Act come lista di controllo volontaria:**
  - data card e limiti dei dati (fototipi, centri);
  - valutazione per sottogruppo;
  - **supervisione umana** (decide il medico);
  - trasparenza (model card, catena di prove nel report);
  - registro delle versioni e degli errori.
- **Demo pubblica (M5.1):** solo con immagini dei dataset o senza conservazione, con avviso ben visibile. Con PanDerm va prima chiarita la licenza (mail agli autori).

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
