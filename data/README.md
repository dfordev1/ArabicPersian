# Data Layout

The repository keeps the source bundles intact and uses them as the canonical
inputs for derived app assets.

## `data/releases/`

Published ZIP bundles for each language.

- `turkish_quran_arabic_script_v4_0_consistency_usability.zip`
- `azeri_quran_arabic_script_production_v1.zip`
- `kazakh_quran_arabic_script_production_v1.zip`

## `data/intermediate/`

Pipeline artifacts, QA bundles, and working ZIPs from the source workflows.

These are useful for inspection and future regeneration, but they should not be
treated as final user-facing releases.

## Derived data

If you generate app-ready JSON, search indexes, or per-surah files, write them
to a derived path such as:

```text
app/public/data/
build/
```

Keep those derived files separate from the release ZIPs.

