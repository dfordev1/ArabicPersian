# Codex Prompt — Organize GitHub Repository

You are working inside a GitHub repository containing Arabic-script Qur'an rendering data for Turkish, Azerbaijani, and Kazakh.

## Goal

Turn this handoff folder into a clean, maintainable open-source repository.

## Tasks

1. Keep all existing release ZIPs under `data/releases/`.
2. Keep intermediate pipeline ZIPs under `data/intermediate/`.
3. Create clear docs:
   - project overview
   - data formats
   - app integration
   - QA workflow
   - release checklist
4. Add scripts to:
   - inspect bundles
   - extract bundles
   - validate JSON
   - split verse lookup by surah
   - build a simple search index
5. Do not change the actual text data unless explicitly asked.
6. Add `.gitignore`.
7. Add a basic Python project structure if helpful.
8. Make README professional and clear.
9. Add warnings that outputs are Arabic-script renderings, not official scholarly editions.
10. Prepare the repo for GitHub Releases.

## Important

Do not invent missing data.

Do not delete release ZIPs.

Do not rename files inside ZIP bundles unless creating derived app-optimized copies.
