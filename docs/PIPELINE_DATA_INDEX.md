# Pipeline Data Index

This index lists the mid-pipeline and app-ready datasets stored inside release and intermediate ZIP bundles.

The ZIP files remain the canonical bundled artifacts. This page makes their internal JSON, CSV, metadata, QA, dictionary, search-index, and review files discoverable without needing to download each bundle first.

## [data/intermediate/azeri/azeri_pass2_normalized.zip](../data/intermediate/azeri/azeri_pass2_normalized.zip)

- Type: Intermediate pipeline bundle
- Size: 3,832,842 bytes
- Internal files: 5

JSON files:
- `azeri_pass2_normalized/azeri_2_translations_arabic_script_pass2.json`
- `azeri_pass2_normalized/azeri_arabic_script_dictionary_pass2.json`
- `azeri_pass2_normalized/azeri_pass2_report.json`
- `azeri_pass2_normalized/azeri_verse_lookup_pass2.json`

CSV files:
- `azeri_pass2_normalized/azeri_pass2_unusual_characters.csv`

## [data/intermediate/azeri/azeri_pass3_frequency_analysis.zip](../data/intermediate/azeri/azeri_pass3_frequency_analysis.zip)

- Type: Intermediate pipeline bundle
- Size: 797,919 bytes
- Internal files: 5

JSON files:
- `azeri_pass3_frequency_analysis/azeri_pass3_statistics.json`

CSV files:
- `azeri_pass3_frequency_analysis/azeri_source_vocabulary_comparison_pass3.csv`
- `azeri_pass3_frequency_analysis/azeri_top_1000_words_review_pass3.csv`
- `azeri_pass3_frequency_analysis/azeri_variant_report_pass3.csv`
- `azeri_pass3_frequency_analysis/azeri_word_frequency_pass3.csv`

## [data/intermediate/azeri/azeri_pass4_quranic_terms.zip](../data/intermediate/azeri/azeri_pass4_quranic_terms.zip)

- Type: Intermediate pipeline bundle
- Size: 3,841,857 bytes
- Internal files: 5

JSON files:
- `azeri_pass4_quranic_terms/azeri_2_translations_arabic_script_pass4.json`
- `azeri_pass4_quranic_terms/azeri_arabic_script_dictionary_pass4.json`
- `azeri_pass4_quranic_terms/azeri_pass4_report.json`
- `azeri_pass4_quranic_terms/azeri_verse_lookup_pass4.json`

CSV files:
- `azeri_pass4_quranic_terms/azeri_pass4_normalized_terms.csv`

## [data/intermediate/azeri/azeri_pass5_morphology.zip](../data/intermediate/azeri/azeri_pass5_morphology.zip)

- Type: Intermediate pipeline bundle
- Size: 2,238,304 bytes
- Internal files: 4

JSON files:
- `azeri_pass5_morphology/azeri_2_translations_arabic_script_pass5.json`
- `azeri_pass5_morphology/azeri_arabic_script_dictionary_pass5.json`
- `azeri_pass5_morphology/azeri_pass5_morphology_report.json`

CSV files:
- `azeri_pass5_morphology/remaining_unresolved_tokens_pass5.csv`

## [data/intermediate/azeri/azeri_pass6_consensus_qa.zip](../data/intermediate/azeri/azeri_pass6_consensus_qa.zip)

- Type: Intermediate pipeline bundle
- Size: 4,850,572 bytes
- Internal files: 8

JSON files:
- `azeri_pass6_consensus_qa/azeri_2_translations_arabic_script_pass6.json`
- `azeri_pass6_consensus_qa/azeri_arabic_script_dictionary_pass6.json`
- `azeri_pass6_consensus_qa/azeri_pass6_report.json`
- `azeri_pass6_consensus_qa/azeri_search_index_pass6.json`
- `azeri_pass6_consensus_qa/azeri_verse_lookup_pass6.json`

CSV files:
- `azeri_pass6_consensus_qa/azeri_consensus_vocabulary_pass6.csv`
- `azeri_pass6_consensus_qa/azeri_coverage_pass6.csv`
- `azeri_pass6_consensus_qa/azeri_variant_review_pass6.csv`

## [data/intermediate/kazakh/kazakh_final_consistency_checker.zip](../data/intermediate/kazakh/kazakh_final_consistency_checker.zip)

- Type: Intermediate pipeline bundle
- Size: 724,127 bytes
- Internal files: 5

JSON files:
- `kazakh_final_consistency_checker_report.json`

CSV files:
- `kazakh_duplicate_arabic_spellings_review.csv`
- `kazakh_quranic_concept_consistency_summary.csv`
- `kazakh_quranic_term_occurrences.csv`
- `kazakh_unlocked_religious_term_candidates.csv`

## [data/intermediate/kazakh/kazakh_step1_language_model.zip](../data/intermediate/kazakh/kazakh_step1_language_model.zip)

- Type: Intermediate pipeline bundle
- Size: 2,335,425 bytes
- Internal files: 4

JSON files:
- `kazakh_language_model.json`
- `kazakh_step1_report.json`

CSV files:
- `kazakh_suffix_frequency.csv`
- `kazakh_word_frequency.csv`

## [data/intermediate/kazakh/kazakh_step2_master_dictionary.zip](../data/intermediate/kazakh/kazakh_step2_master_dictionary.zip)

- Type: Intermediate pipeline bundle
- Size: 2,182,549 bytes
- Internal files: 2

JSON files:
- `kazakh_master_dictionary.json`
- `kazakh_step2_report.json`

## [data/intermediate/kazakh/kazakh_step3_morphology.zip](../data/intermediate/kazakh/kazakh_step3_morphology.zip)

- Type: Intermediate pipeline bundle
- Size: 6,127,317 bytes
- Internal files: 5

JSON files:
- `kazakh_master_dictionary_v2.json`
- `kazakh_morphology.json`
- `kazakh_step3_morphology_report.json`

CSV files:
- `kazakh_morphology_families.csv`
- `kazakh_review_candidates.csv`

## [data/intermediate/kazakh/kazakh_step4_quran_rebuild.zip](../data/intermediate/kazakh/kazakh_step4_quran_rebuild.zip)

- Type: Intermediate pipeline bundle
- Size: 1,602,174 bytes
- Internal files: 5

JSON files:
- `kazakh_quran_arabic_script_v2.json`
- `kazakh_step4_report.json`
- `kazakh_verse_lookup_v2.json`

CSV files:
- `kazakh_low_confidence_tokens_step4.csv`
- `kazakh_step4_validation_issues.csv`

## [data/intermediate/kazakh/kazakh_step5_5_quranic_vocab_lock.zip](../data/intermediate/kazakh/kazakh_step5_5_quranic_vocab_lock.zip)

- Type: Intermediate pipeline bundle
- Size: 4,939,629 bytes
- Internal files: 7

JSON files:
- `kazakh_master_dictionary_locked.json`
- `kazakh_quran_arabic_script_v2_locked.json`
- `kazakh_step5_5_report.json`
- `kazakh_verse_lookup_v2_locked.json`

CSV files:
- `kazakh_quranic_locked_glossary.csv`
- `kazakh_step5_5_glossary_changes.csv`
- `kazakh_step5_5_validation_issues.csv`

## [data/intermediate/kazakh/kazakh_step5_quality_assurance.zip](../data/intermediate/kazakh/kazakh_step5_quality_assurance.zip)

- Type: Intermediate pipeline bundle
- Size: 5,247,394 bytes
- Internal files: 8

JSON files:
- `kazakh_master_dictionary_step5.json`
- `kazakh_quran_arabic_script_v2_qa.json`
- `kazakh_step5_report.json`
- `kazakh_verse_lookup_v2_qa.json`

CSV files:
- `kazakh_confidence_report_step5.csv`
- `kazakh_review_candidates_step5.csv`
- `kazakh_step5_qa_overrides.csv`
- `kazakh_step5_validation_issues.csv`

## [data/intermediate/kyrgyz/kyrgyz_quran_arabic_script_v1_beta.zip](../data/intermediate/kyrgyz/kyrgyz_quran_arabic_script_v1_beta.zip)

- Type: Intermediate pipeline bundle
- Size: 3,388,394 bytes
- Internal files: 12

JSON files:
- `kyrgyz_master_dictionary_final.json`
- `kyrgyz_quran_arabic_script_final.json`
- `kyrgyz_search_index_final.json`
- `kyrgyz_verse_lookup_final.json`
- `manifest.json`
- `metadata.json`

CSV files:
- `kyrgyz_quranic_locked_glossary.csv`
- `kyrgyz_review_candidates.csv`
- `kyrgyz_validation_issues.csv`
- `kyrgyz_word_frequency.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/intermediate/kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip](../data/intermediate/kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip)

- Type: Intermediate pipeline bundle
- Size: 3,082,591 bytes
- Internal files: 11

JSON files:
- `kyrgyz_master_dictionary_final.json`
- `kyrgyz_quran_arabic_script_final.json`
- `kyrgyz_search_index_final.json`
- `kyrgyz_verse_lookup_final.json`
- `manifest.json`
- `metadata.json`

CSV files:
- `kyrgyz_qa_glossary_expansion.csv`
- `kyrgyz_unlocked_religious_candidates.csv`
- `kyrgyz_validation_issues.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/intermediate/uzbek/uzbek_phase1_master_corpus.zip](../data/intermediate/uzbek/uzbek_phase1_master_corpus.zip)

- Type: Intermediate pipeline bundle
- Size: 9,031,727 bytes
- Internal files: 17

JSON files:
- `uzbek_phase1_master_corpus/manifest.json`
- `uzbek_phase1_master_corpus/raw_extracted/alauddin_mansour_simple/alauddin-mansour-simple.json`
- `uzbek_phase1_master_corpus/raw_extracted/alauddin_mansour_with_tags/alauddin-mansour-with-footnote-tags.json`
- `uzbek_phase1_master_corpus/raw_extracted/muhammad_sodik_inline_footnotes/muhammad-sodik-muhammad-yusuf-inline-footnotes.json`
- `uzbek_phase1_master_corpus/raw_extracted/muhammad_sodik_simple/muhammad-sodik-muhammad-yusuf-simple.json`
- `uzbek_phase1_master_corpus/raw_extracted/muhammad_sodik_with_tags/muhammad-sodik-muhammad-yusuf-with-footnote-tags.json`
- `uzbek_phase1_master_corpus/raw_extracted/rowwad_simple/uzbek-translation-rowwad-translation-center-simple.json`
- `uzbek_phase1_master_corpus/raw_extracted/sodik_inline_footnotes/quran-uz-sodik-inline-footnotes.json`
- `uzbek_phase1_master_corpus/raw_extracted/sodik_simple/quran-uz-sodik-simple.json`
- `uzbek_phase1_master_corpus/raw_extracted/sodik_with_tags/quran-uz-sodik-with-footnote-tags.json`
- `uzbek_phase1_master_corpus/uzbek_master_corpus_phase1.json`
- `uzbek_phase1_master_corpus/uzbek_phase1_report.json`
- `uzbek_phase1_master_corpus/uzbek_verse_lookup_phase1.json`

CSV files:
- `uzbek_phase1_master_corpus/uzbek_core_word_frequency_phase1.csv`
- `uzbek_phase1_master_corpus/uzbek_footnote_marker_report_phase1.csv`
- `uzbek_phase1_master_corpus/uzbek_translation_coverage_phase1.csv`

Docs/metadata notes:
- `uzbek_phase1_master_corpus/README.md`

## [data/intermediate/uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip](../data/intermediate/uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip)

- Type: Intermediate pipeline bundle
- Size: 9,320,793 bytes
- Internal files: 13

JSON files:
- `manifest.json`
- `metadata.json`
- `uzbek_master_dictionary_final.json`
- `uzbek_quran_arabic_script_final.json`
- `uzbek_search_index_final.json`
- `uzbek_verse_lookup_final.json`

CSV files:
- `uzbek_glossary_candidates_reviewed.csv`
- `uzbek_quranic_locked_glossary_final.csv`
- `uzbek_review_candidates_remaining.csv`
- `uzbek_validation_issues_remaining.csv`
- `uzbek_validation_issues_resolved.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/intermediate/uzbek/uzbek_v2_consensus_corpus.zip](../data/intermediate/uzbek/uzbek_v2_consensus_corpus.zip)

- Type: Intermediate pipeline bundle
- Size: 5,521,219 bytes
- Internal files: 8

JSON files:
- `manifest.json`
- `uzbek_master_consensus_corpus_v2.json`
- `uzbek_v2_consensus_report.json`
- `uzbek_verse_lookup_consensus_v2.json`

CSV files:
- `uzbek_consensus_word_frequency_v2.csv`
- `uzbek_footnote_inventory_v2.csv`
- `uzbek_translation_coverage_v2.csv`

Docs/metadata notes:
- `README.md`

## [data/releases/azeri/azeri_v2_perso_arabic_start.zip](../data/releases/azeri/azeri_v2_perso_arabic_start.zip)

- Type: Release bundle
- Size: 2,970,555 bytes
- Internal files: 9

JSON files:
- `azeri_arabic_script_dictionary_v2_perso_arabic.json`
- `azeri_search_index_v2_perso_arabic.json`
- `azeri_v2_start_report.json`
- `azeri_verse_lookup_v2_perso_arabic.json`
- `manifest.json`

CSV files:
- `azeri_v2_locked_terms.csv`
- `azeri_v2_validation_issues.csv`
- `azeri_v2_word_frequency.csv`

Docs/metadata notes:
- `README.md`

## [data/releases/azeri_quran_arabic_script_production_v1.zip](../data/releases/azeri_quran_arabic_script_production_v1.zip)

- Type: Release bundle
- Size: 4,531,336 bytes
- Internal files: 8

JSON files:
- `azeri_2_translations_arabic_script_final.json`
- `azeri_arabic_script_dictionary_final.json`
- `azeri_search_index_final.json`
- `azeri_verse_lookup_final.json`
- `manifest.json`
- `metadata.json`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/releases/kazakh/kazakh_app_final_bundle.zip](../data/releases/kazakh/kazakh_app_final_bundle.zip)

- Type: Release bundle
- Size: 8,492,822 bytes
- Internal files: 11

JSON files:
- `kazakh_final_report.json`
- `kazakh_master_dictionary_final.json`
- `kazakh_quran_arabic_script_final.json`
- `kazakh_search_index_final.json`
- `kazakh_verse_lookup_final.json`
- `manifest.json`
- `metadata.json`

CSV files:
- `kazakh_quranic_locked_glossary.csv`
- `kazakh_validation_issues.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/releases/kazakh_quran_arabic_script_production_v1.zip](../data/releases/kazakh_quran_arabic_script_production_v1.zip)

- Type: Release bundle
- Size: 2,533,618 bytes
- Internal files: 11

JSON files:
- `kazakh_production_v1/kazakh_arabic_script_dictionary.json`
- `kazakh_production_v1/kazakh_quran_arabic_script.json`
- `kazakh_production_v1/kazakh_search_index.json`
- `kazakh_production_v1/kazakh_verse_lookup.json`
- `kazakh_production_v1/manifest.json`
- `kazakh_production_v1/metadata.json`

CSV files:
- `kazakh_production_v1/kazakh_qc_remaining_script.csv`
- `kazakh_production_v1/kazakh_variant_review.csv`
- `kazakh_production_v1/kazakh_word_frequency.csv`

Docs/metadata notes:
- `kazakh_production_v1/LICENSE_NOTES.md`
- `kazakh_production_v1/README.md`

## [data/releases/kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip](../data/releases/kyrgyz/kyrgyz_quran_arabic_script_v1_qa_production.zip)

- Type: Release bundle
- Size: 3,082,591 bytes
- Internal files: 11

JSON files:
- `kyrgyz_master_dictionary_final.json`
- `kyrgyz_quran_arabic_script_final.json`
- `kyrgyz_search_index_final.json`
- `kyrgyz_verse_lookup_final.json`
- `manifest.json`
- `metadata.json`

CSV files:
- `kyrgyz_qa_glossary_expansion.csv`
- `kyrgyz_unlocked_religious_candidates.csv`
- `kyrgyz_validation_issues.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`

## [data/releases/turkish_quran_arabic_script_v4_0_consistency_usability.zip](../data/releases/turkish_quran_arabic_script_v4_0_consistency_usability.zip)

- Type: Release bundle
- Size: 6,739,520 bytes
- Internal files: 11

JSON files:
- `consistency_usability_v4_0/display_config_v4_0.json`
- `consistency_usability_v4_0/metadata_v4_0.json`
- `consistency_usability_v4_0/orthography_rules_v4_0.json`
- `consistency_usability_v4_0/turkish_5_translations_arabic_script_v4_0.json`
- `consistency_usability_v4_0/turkish_arabic_script_dictionary_v4_0_consistent.json`
- `consistency_usability_v4_0/turkish_wbw_arabic_script_v4_0.json`
- `consistency_usability_v4_0/validation_v4_0.json`
- `consistency_usability_v4_0/verse_lookup_v4_0.json`

CSV files:
- `consistency_usability_v4_0/consistency_changes_v4_0.csv`
- `consistency_usability_v4_0/same_spelling_multiple_lemmas_review_v4_0.csv`

Docs/metadata notes:
- `consistency_usability_v4_0/README.md`

## [data/releases/uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip](../data/releases/uzbek/uzbek_quran_arabic_script_v2_production_fixed.zip)

- Type: Release bundle
- Size: 9,320,793 bytes
- Internal files: 13

JSON files:
- `manifest.json`
- `metadata.json`
- `uzbek_master_dictionary_final.json`
- `uzbek_quran_arabic_script_final.json`
- `uzbek_search_index_final.json`
- `uzbek_verse_lookup_final.json`

CSV files:
- `uzbek_glossary_candidates_reviewed.csv`
- `uzbek_quranic_locked_glossary_final.csv`
- `uzbek_review_candidates_remaining.csv`
- `uzbek_validation_issues_remaining.csv`
- `uzbek_validation_issues_resolved.csv`

Docs/metadata notes:
- `LICENSE_NOTES.md`
- `README.md`
