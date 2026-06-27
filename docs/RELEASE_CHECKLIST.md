# Release Checklist

Before publishing a language bundle:

- [ ] Confirm the language scope and label are accurate for the bundle.
- [ ] Verify source translation license.
- [ ] Verify dictionary/corpus license.
- [ ] Confirm label says "rendering" or "transliteration", not official edition.
- [ ] Run JSON validation.
- [ ] Run repository smoke tests.
- [ ] Confirm any raw source JSON inputs are documented under `data/source/`.
- [ ] Confirm new source inputs are listed in the repository description.
- [ ] Confirm short code labels like `dv` remain mapped to a canonical name in docs.
- [ ] Generate manifest.
- [ ] Attach ZIP to GitHub Release.
- [ ] Add version tag.
- [ ] Note known limitations.
- [ ] Include review status.
- [ ] Include contact/correction method.
- [ ] Mention which other languages are planned or already supported.
