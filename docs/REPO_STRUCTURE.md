# Repository Structure

This repository keeps the original handoff bundles intact and adds a simple layout for GitHub usage.

## Top-level layout

```text
arabic_script_quran_project_github_handoff/
├── data/
│   ├── releases/
│   └── intermediate/
├── docs/
├── prompts/
├── scripts/
├── engine/
├── languages/
│   ├── tr/
│   ├── az/
│   └── kk/
├── app/
├── review/
├── tests/
└── README.md
```

## Folder purpose

- `data/releases/`: published ZIP bundles for each language
- `data/intermediate/`: pipeline artifacts and QA intermediates
- `docs/`: project overview, release notes, QA workflow, and usage guides
- `scripts/`: bundle inspection, extraction, validation, and derived-data helpers
- `engine/`: future processing or normalization code
- `languages/`: language-specific source or derived assets
- `app/`: app integration layer and client-ready data layout
- `review/`: reviewer worksheets, notes, and change logs
- `tests/`: automated validation checks

## Rule of thumb

Keep source bundles untouched. If you need app-optimized copies, write them to a separate derived path such as `app/public/data/` or a `build/` directory that is not committed.
