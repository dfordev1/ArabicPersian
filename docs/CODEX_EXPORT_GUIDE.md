# Codex Export Guide

Use this guide to move the project into GitHub with Codex.

## 1. Create a new repository

Suggested repository name:

```text
arabic-script-quran
```

Suggested description:

```text
Arabic-script renderings of Turkish, Azerbaijani, and Kazakh Qur'an translations with dictionaries, search indexes, and QA reports.
```

## 2. Upload this handoff folder

Unzip:

```bash
unzip arabic_script_quran_project_github_handoff.zip
cd arabic_script_quran_project_github_handoff
```

Initialize Git:

```bash
git init
git add .
git commit -m "Initial Arabic-script Qur'an project handoff"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/arabic-script-quran.git
git push -u origin main
```

## 3. Ask Codex to organize the repo

Use `prompts/CODEX_REPO_SETUP_PROMPT.md`.

## 4. Recommended GitHub layout after Codex cleanup

```text
arabic-script-quran/
├── data/
│   ├── releases/
│   └── intermediate/
├── engine/
├── languages/
│   ├── tr/
│   ├── az/
│   └── kk/
├── scripts/
├── docs/
├── app/
├── review/
├── tests/
└── README.md
```

## 5. Git LFS warning

Some ZIP/JSON files may be large. If GitHub rejects them, use Git LFS:

```bash
git lfs install
git lfs track "*.zip"
git lfs track "*.json"
git add .gitattributes
git add .
git commit -m "Track large data files with Git LFS"
git push
```

## 6. Release strategy

Create GitHub Releases:

- `turkish-v4.0`
- `azeri-v1.0`
- `kazakh-v1.0`
- `kazakh-v2-beta`

Attach ZIP bundles to releases.
