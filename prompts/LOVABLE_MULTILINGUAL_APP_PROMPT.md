# Lovable Prompt — Multilingual Arabic-Script Qur'an App

I have attached a ZIP/repository containing Arabic-script Qur'an data for Turkish, Azerbaijani, and Kazakh.

Build a production-quality web app.

## Stack

- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui
- App Router
- Mobile-first
- Dark and light mode
- No backend initially
- Load JSON files from `/public/data`

## Data

Use the real files from the bundles.

Languages:

- Turkish
- Azerbaijani
- Kazakh

For each language, use:

- verse lookup JSON
- dictionary JSON
- search index JSON if available

Do not create mock data.

## Pages

1. Home
2. Language selector
3. Qur'an reader
4. Search
5. Dictionary
6. Compare translations
7. About
8. Review feedback page

## Qur'an reader

Display:

- Surah / ayah selector
- Arabic-script rendered translation
- original source script/Latin/Cyrillic
- optional dictionary tap panel

## Word tap

When a word is clicked, show:

- word
- Arabic-script spelling
- frequency
- source/confidence if available
- related search results

## Search

Support:

- Arabic script
- Latin/Cyrillic source text
- verse numbers
- dictionary terms

## Performance

Split large verse lookup files by surah if needed.

Use lazy loading and memoized search.

## Design

Modern Islamic style.

Clean typography.

Readable Arabic-script display.

Large mobile tap targets.

## Important labeling

Do not call the data official or definitive.

Use labels like:

- Arabic-script rendering
- digital transliteration
- beta edition
