# Universal App Data Spec

Each language folder:

metadata.json
verse_lookup.json
dictionary.json
search_index.json
glossary.csv
qa_report.json

For single translation:
{
  "1:1": {"source":"...", "arabic_script":"...", "footnotes":"..."}
}

For multiple translations:
{
  "1:1": {
    "translations": {
      "source_name": {"source":"...", "arabic_script":"..."}
    },
    "footnotes": {}
  }
}
