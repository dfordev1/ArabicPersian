# Codex Prompt — Continue Kazakh v2

The Kazakh pipeline has reached Step 5.5.

Use these files:

- `data/intermediate/kazakh/kazakh_step1_language_model.zip`
- `data/intermediate/kazakh/kazakh_step2_master_dictionary.zip`
- `data/intermediate/kazakh/kazakh_step3_morphology.zip`
- `data/intermediate/kazakh/kazakh_step4_quran_rebuild.zip`
- `data/intermediate/kazakh/kazakh_step5_quality_assurance.zip`
- `data/intermediate/kazakh/kazakh_step5_5_quranic_vocab_lock.zip`
- `data/intermediate/kazakh/kazakh_final_consistency_checker.zip`

## Goal

Create `kazakh_quran_arabic_script_production_v2_beta.zip`.

## Required final files

- `kazakh_quran_arabic_script_final.json`
- `kazakh_verse_lookup_final.json`
- `kazakh_master_dictionary_final.json`
- `kazakh_search_index_final.json`
- `kazakh_quranic_locked_glossary.csv`
- `kazakh_review_candidates.csv`
- `kazakh_confidence_report.csv`
- `metadata.json`
- `README.md`
- `LICENSE_NOTES.md`
- `manifest.json`

## Rules

- Use Step 5.5 locked files as the final text source.
- Do not change Qur'an wording.
- Do not invent review approvals.
- Label as beta unless human review has been performed.
