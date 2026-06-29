# Data Layout

The repository keeps the source bundles intact and uses them as the canonical
inputs for derived app assets.

## `data/releases/`

Published ZIP bundles for each language.

- `turkish_quran_arabic_script_v4_0_consistency_usability.zip`
- `azeri_quran_arabic_script_production_v1.zip`
- `azeri/azeri_v2_perso_arabic_start.zip`
- `kazakh_quran_arabic_script_production_v1.zip`
- `kazakh/kazakh_app_final_bundle.zip`
- `kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip`
- `uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip`
- `turkmen/Turkmen_PersoArabic_local.json`
- `turkmen/Turkmen_PersoArabic_local.csv`
- `turkmen/Turkmen_PersoArabic_local_qa_failures.json`

## `data/intermediate/`

Pipeline artifacts, QA bundles, and working ZIPs from the source workflows.

These are useful for inspection and future regeneration, but they should not be
treated as final user-facing releases.

Additional synchronized pipeline artifacts:

- `kyrgyz/kyrgyz_quran_arabic_script_v1_beta.zip`
- `kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip`
- `uzbek/uzbek_phase1_master_corpus.zip`
- `uzbek/uzbek_v2_consensus_corpus.zip`
- `uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip`

## Derived data

If you generate app-ready JSON, search indexes, or per-surah files, write them
to a derived path such as:

```text
app/public/data/
build/
```

Keep those derived files separate from the release ZIPs.

## Source JSON inputs

Some language projects may arrive as raw JSON instead of release ZIPs. Keep
those in `data/source/` so they stay easy to inspect and convert.

Current source inputs:

- `data/source/jawi/quranjawifinal.json`
- `data/source/bangali-urdu/bangaliurduquran.json`
- `data/source/turkmen/Turkmen_verse_only_corrected.json`
- `data/source/turkmen/Turkmen_verse_only_corrected.csv`
