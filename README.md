# ArabicPersian

Multilingual Arabic-script Qur'an renderings with a scope that can grow across Turkish, Azerbaijani, Kazakh, and future languages.

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

## Project goal

Render modern Turkish, Azeri, and Kazakh Qur'an translations into readable Arabic/Perso-Arabic script, with dictionaries, search indexes, QA reports, and app-ready JSON.

## Important claim policy

Do **not** market these as official or definitive historical editions.

Recommended labels:

- Turkish Arabic-Script Transliteration
- Azerbaijani Qur'an Arabic-Script Rendering
- Kazakh Qur'an Arabic-Script Digital Edition

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

See:

- `docs/CODEX_EXPORT_GUIDE.md`
- `docs/APP_BUILD_GUIDE.md`
- `docs/PROJECT_STATUS.md`
- `docs/REPO_STRUCTURE.md`
