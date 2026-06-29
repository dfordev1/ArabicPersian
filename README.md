# ArabicPersian

Multilingual Arabic-script Qur'an renderings with a scope that can grow across Turkish, Azerbaijani, Kazakh, Jawi, Bangali-Urdu, Maltese, DV, and future languages.

This repository keeps the project broad on purpose: the same structure can hold more languages as you add them, without changing the overall layout.

The starter app in `app/` is intentionally simple: it gives you a reader/search shell now, and it can later point at language-specific bundles without changing the foundation.

Additional source JSON assets can live under `data/source/` for languages that are still being organized into release bundles.

## Repository structure

See [docs/REPO_STRUCTURE.md](docs/REPO_STRUCTURE.md) for the GitHub-ready layout this handoff is organized around.

## Current language bundles

| Language | Status | Bundle |
|---|---:|---|
| Turkish | Mature production candidate | `data/releases/turkish_quran_arabic_script_v4_0_consistency_usability.zip` |
| Azeri/Azerbaijani | Production v1 | `data/releases/azeri_quran_arabic_script_production_v1.zip` |
| Kazakh | Production v1 + v2 pipeline intermediates | `data/releases/kazakh_quran_arabic_script_production_v1.zip` |
| Turkmen | Release candidate; Roman source + Afghan Turkmen Perso-Arabic transliteration | [Roman JSON](data/source/turkmen/Turkmen_verse_only_corrected.json) / [Roman CSV](data/source/turkmen/Turkmen_verse_only_corrected.csv) / [Perso-Arabic JSON](data/releases/turkmen/Turkmen_PersoArabic_local.json) / [Perso-Arabic CSV](data/releases/turkmen/Turkmen_PersoArabic_local.csv) / [QA notes](docs/turkmen/README.md) |
| Jawi | Source JSON input, safe-cleaned working baseline refreshed | `data/source/jawi/quranjawifinal.json` |
| Bangali-Urdu | Source JSON input | `data/source/bangali-urdu/bangaliurduquran.json` |
| Maltese | Source JSON input | `data/source/maltese/maltesequrandata.json` |
| DV | Source JSON input | `data/source/dv/dv-unknow-simple.json` |

## Project goal

Render modern Turkish, Azeri, and Kazakh Qur'an translations into readable Arabic/Perso-Arabic script, while also organizing new source inputs such as Jawi, Bangali-Urdu, Maltese, and DV into the same expandable workflow, with dictionaries, search indexes, QA reports, and app-ready JSON.

The Turkmen bundle adds both a corrected Roman-script source and an Afghan Turkmen Perso-Arabic transliteration release candidate. Start from [docs/turkmen/README.md](docs/turkmen/README.md) for exact file links and QA status.

## Important claim policy

Do **not** market these as official or definitive historical editions.

Recommended labels:

- Turkish Arabic-Script Transliteration
- Azerbaijani Qur'an Arabic-Script Rendering
- Kazakh Qur'an Arabic-Script Digital Edition
- Turkmen Qur'an Afghan Turkmen Perso-Arabic Transliteration
- Jawi Qur'an Arabic-Script Rendering
- Bangali-Urdu Qur'an Arabic-Script Rendering
- Maltese Qur'an Arabic-Script Rendering
- DV Qur'an Arabic-Script Rendering

Avoid:

- Official Ottoman Qur'an
- Definitive Kazakh Arabic-script Qur'an
- Scholarly verified edition

until reviewed by qualified native/scholarly reviewers.

## Quick start

1. Clone this repo.
2. Unzip the release bundle for the language you need.
3. Use the `verse_lookup` JSON as the primary app database.
4. Use dictionary/search-index JSON files for search and word tap features.
5. Prefer derived copies for app packaging and keep the source ZIPs under `data/releases/`.
6. Keep raw source JSON inputs under `data/source/` until they are converted into a release format.

### Jawi source note

The Jawi source JSON at `data/source/jawi/quranjawifinal.json` was refreshed from a
safe-cleaned working baseline that only applies conservative Unicode and spacing
normalization. It remains source material rather than a finalized scholarly edition.

### Maltese source note

The Maltese source JSON at `data/source/maltese/maltesequrandata.json` is kept as
raw source material and should be converted into app-ready data only after the
structure is reviewed and mapped.

### DV source note

The `dv` source JSON at `data/source/dv/dv-unknow-simple.json` is preserved as
source material under a short code label until the canonical project name is
confirmed.

See:

- `docs/CODEX_EXPORT_GUIDE.md`
- `docs/APP_BUILD_GUIDE.md`
- `docs/PROJECT_STATUS.md`
- `docs/REPO_STRUCTURE.md`
