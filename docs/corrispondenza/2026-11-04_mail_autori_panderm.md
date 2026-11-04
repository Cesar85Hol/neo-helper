# Mail agli autori di PanDerm / DermFM-Zero sulla licenza

> Bozza del 2026-11-04 · **Stato: non inviata.** La mail la invia Cesar; questo file tiene traccia del testo e della risposta.
> Contesto: [05_scelte_e_pipeline.md §1.2](../05_scelte_e_pipeline.md).

## Destinatari
- Autore corrispondente di PanDerm (Nature Medicine 2025): gruppo di **Zongyuan Ge**, Monash University. ⚠️ Prendere l'indirizzo dalla sezione *Correspondence* dell'articolo o dalla pagina Monash; non indovinarlo.
- In copia: **Siyuan Yan** (primo autore, maintainer del repository `SiyuanYan1/PanDerm`).
- Alternativa se non rispondono entro 2–3 settimane: aprire una *Discussion* o una issue pubblica sul repository GitHub (senza dettagli sull'ospedale).

## Cosa chiediamo, in breve
1. Conferma che il fine-tuning per esperimenti interni della tesi è permesso.
2. Se si può pubblicare la **sola testa** addestrata sugli embedding di PanDerm (la zona grigia).
3. Se si può fare una **demo di ricerca pubblica**, non commerciale (es. Hugging Face Space), che scarica i pesi ufficiali.
4. Quale licenza vale per **DermFM-Zero**: GitHub dice CC BY-NC 4.0, Hugging Face CC BY-NC-ND 4.0.
5. Se un eventuale **studio di ricerca in ospedale** (non clinico, con comitato etico) rientra nella "ricerca accademica".

## Testo della mail (in inglese)

**Subject:** PanDerm / DermFM-Zero license – questions for a non-commercial academic project

Dear Prof. Ge, dear Dr. Yan,

I am working on **Neo Helper**, a non-commercial academic project (thesis) on decision support for skin lesion assessment. Thank you for releasing PanDerm. Based on your Nature Medicine paper, it is the backbone we would like to use.

Our plan is to use PanDerm as a frozen feature extractor with a light classification head on HAM10000. As a second experiment we would fine-tune it. We will compare it with DINOv2 and Derm Foundation. Our code is MIT-licensed and public; it will download the official weights from your repository and will not redistribute them.

We have read the CC BY-NC-ND 4.0 license and the README ("non-commercial academic research purposes"). We want to stay within them, and would be grateful if you could clarify a few points:

1. **Fine-tuning.** We understand that fine-tuning PanDerm for internal, non-commercial research is allowed, as long as the adapted weights are not shared. Is that correct?
2. **Classification head.** May we publish only the small head trained on PanDerm embeddings (without any PanDerm weights), so that others can reproduce our results using the official checkpoint?
3. **Research demo.** May we host a public, non-commercial research demo, clearly labelled as not a medical device, that loads the official PanDerm weights at runtime?
4. **DermFM-Zero.** The GitHub repository states CC BY-NC 4.0, while the Hugging Face model card states CC BY-NC-ND 4.0. Which license applies?
5. **Hospital research study.** If a partner hospital later joins with ethics approval, would a retrospective research evaluation, with no clinical use, fall within "academic research"?

On a related note, we could only access the abstract of Anriot et al., JAMA Dermatology 2026, "Limits of AI models for skin cancer diagnosis in realistic settings". If an author copy is available, we would be glad to read the full methods, in particular how the metadata were used in the multimodal model.

We will of course cite PanDerm and acknowledge your group in all outputs. If written permission beyond the license is needed for any of these points, we would be happy to follow whatever conditions you set.

Thank you very much for your time.

Kind regards,
Cesar Seminario Yrigoyen
Neo Helper — https://github.com/Cesar85Hol/neo-helper

## Risposta
_(da compilare quando arriva: data, chi risponde, cosa permette, cosa no)_
