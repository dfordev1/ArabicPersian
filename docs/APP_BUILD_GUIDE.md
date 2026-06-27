# App Build Guide

## Main JSON to use

For each language, prefer the `verse_lookup` JSON file inside its bundle.

The app should use:

- Verse lookup JSON: primary display database
- Dictionary JSON: word tap and dictionary screen
- Search index JSON: instant search

## Recommended app features

1. Language selector
2. Qur'an reader
3. Verse search
4. Dictionary search
5. Word tap panel
6. Translation comparison
7. Light/dark mode
8. RTL display support
9. Review feedback submission

## Performance recommendation

For production, split verse lookup by surah:

```text
public/data/kk/surah/001.json
public/data/kk/surah/002.json
...
public/data/kk/surah/114.json
```

This avoids loading the entire database on first page load.

## Lovable prompt

See:

```text
prompts/LOVABLE_MULTILINGUAL_APP_PROMPT.md
```
