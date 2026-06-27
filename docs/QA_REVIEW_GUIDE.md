# QA Review Guide

## Review priority

Do not review every verse manually first.

Review in this order:

1. Locked Qur'anic glossary
2. Top 500 low-confidence tokens
3. Top 1,000 frequency tokens
4. Proper names
5. Religious terms
6. Duplicate spelling groups

## Kazakh files to review

From the Kazakh intermediate ZIPs:

- `kazakh_review_candidates_step5.csv`
- `kazakh_confidence_report_step5.csv`
- `kazakh_quranic_locked_glossary.csv`
- `kazakh_unlocked_religious_term_candidates.csv`
- `kazakh_duplicate_arabic_spellings_review.csv`

## Reviewer fields

Use:

```text
token
current_arabic_script
suggested_arabic_script
decision
notes
reviewer
date
```

## Release rule

Only call a version "reviewed" after a native speaker or scholar has approved the top terms.
