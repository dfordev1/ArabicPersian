const bundles = {
  tr: {
    label: "Turkish",
    title: "Surah 1",
    reference: "1:1",
    verse: "Bismillahirrahmanirrahim",
    translation: "Starter copy for Turkish bundle browsing.",
    results: [
      { ref: "1:1", text: "Bismillahirrahmanirrahim", note: "Opening verse" },
      { ref: "1:2", text: "Elhamdulillahi rabbil alemin", note: "Sample result" }
    ]
  },
  az: {
    label: "Azerbaijani",
    title: "Surah 1",
    reference: "1:1",
    verse: "Bismillahirrahmanirrahim",
    translation: "Starter copy for Azerbaijani bundle browsing.",
    results: [
      { ref: "1:1", text: "Bismillahirrahmanirrahim", note: "Opening verse" }
    ]
  },
  kk: {
    label: "Kazakh",
    title: "Surah 1",
    reference: "1:1",
    verse: "Bismillahirrahmanirrahim",
    translation: "Starter copy for Kazakh bundle browsing.",
    results: [
      { ref: "1:1", text: "Bismillahirrahmanirrahim", note: "Opening verse" }
    ]
  }
};

const languageSelect = document.getElementById("language-select");
const searchInput = document.getElementById("search-input");
const languageLabel = document.getElementById("language-label");
const surahTitle = document.getElementById("surah-title");
const verseReference = document.getElementById("verse-reference");
const verseText = document.getElementById("verse-text");
const verseTranslation = document.getElementById("verse-translation");
const resultsList = document.getElementById("results-list");
const resultCount = document.getElementById("result-count");

function renderResults(items) {
  resultsList.innerHTML = "";
  resultCount.textContent = `${items.length} result${items.length === 1 ? "" : "s"}`;
  items.forEach((item) => {
    const entry = document.createElement("div");
    entry.className = "results-item";
    entry.innerHTML = `<strong>${item.ref}</strong><span>${item.text}</span><small>${item.note}</small>`;
    resultsList.appendChild(entry);
  });
}

function renderLanguage(code) {
  const bundle = bundles[code];
  languageLabel.textContent = bundle.label;
  surahTitle.textContent = bundle.title;
  verseReference.textContent = bundle.reference;
  verseText.textContent = bundle.verse;
  verseTranslation.textContent = bundle.translation;
  renderResults(bundle.results);
}

languageSelect.addEventListener("change", (event) => {
  renderLanguage(event.target.value);
});

searchInput.addEventListener("input", (event) => {
  const bundle = bundles[languageSelect.value];
  const query = event.target.value.trim().toLowerCase();
  const filtered = !query
    ? bundle.results
    : bundle.results.filter((item) =>
        `${item.ref} ${item.text} ${item.note}`.toLowerCase().includes(query)
      );
  renderResults(filtered);
});

renderLanguage(languageSelect.value);
