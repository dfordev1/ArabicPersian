#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from pathlib import Path


SOURCE = Path("data/source/maltese/maltesequrandata.json")
OUT_DIR = Path("data/releases/maltese")
OUT_JSON = OUT_DIR / "maltese_quran_arabic_script.json"
OUT_CSV = OUT_DIR / "maltese_quran_arabic_script.csv"
OUT_QA = OUT_DIR / "maltese_quran_arabic_script_qa.json"


OVERRIDES = {
    "Alla": "الله",
    "Allah": "الله",
    "IsemAlla": "يسېم الله",
    "Qoran": "قرآن",
    "Koran": "قرآن",
    "Islam": "اسلام",
    "Muħammad": "محمد",
    "Muhammad": "محمد",
    "Ibrahim": "ابراهيم",
    "Musa": "موسى",
    "Mosc": "موسى",
    "Iblis": "ابليس",
    "Adam": "آدم",
}


DIGRAPHS = {
    "għ": "ع",
    "ie": "يه",
}


CHARS = {
    "a": "ا",
    "b": "ب",
    "ċ": "چ",
    "c": "ك",
    "d": "د",
    "e": "ې",
    "f": "ف",
    "ġ": "ج",
    "g": "گ",
    "h": "ه",
    "ħ": "ح",
    "i": "ي",
    "j": "ي",
    "k": "ك",
    "l": "ل",
    "m": "م",
    "n": "ن",
    "o": "و",
    "p": "پ",
    "q": "ق",
    "r": "ر",
    "s": "س",
    "t": "ت",
    "u": "و",
    "v": "ڤ",
    "w": "و",
    "x": "ش",
    "ż": "ز",
    "z": "ز",
}


PUNCT = {
    ",": "،",
    ";": "؛",
    "?": "؟",
}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def transliterate_word(word: str) -> str:
    if not word:
        return word
    if word in OVERRIDES:
        return OVERRIDES[word]
    if word.lower() in {k.lower(): k for k in OVERRIDES}:
        key = {k.lower(): k for k in OVERRIDES}[word.lower()]
        return OVERRIDES[key]

    out: list[str] = []
    i = 0
    lower = word.lower()
    while i < len(word):
        pair = lower[i : i + 2]
        if pair in DIGRAPHS:
            out.append(DIGRAPHS[pair])
            i += 2
            continue
        ch = lower[i]
        out.append(CHARS.get(ch, word[i]))
        i += 1
    return "".join(out)


WORD_RE = re.compile(r"[A-Za-zĊċĠġĦħŻż]+", re.UNICODE)


def transliterate_text(text: str) -> str:
    text = clean_text(text)
    text = WORD_RE.sub(lambda match: transliterate_word(match.group(0)), text)
    for src, dst in PUNCT.items():
        text = text.replace(src, dst)
    return text.strip()


def main() -> None:
    data = json.loads(SOURCE.read_text(encoding="utf-8-sig"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    converted: dict[str, dict[str, dict[str, str]]] = {}
    rows: list[dict[str, str | int]] = []
    qa = {
        "source": str(SOURCE),
        "output_json": str(OUT_JSON),
        "output_csv": str(OUT_CSV),
        "surahs": len(data),
        "verses": 0,
        "empty_outputs": [],
        "latin_letters_remaining": [],
        "notes": [
            "Deterministic phonetic Maltese Latin-script to Arabic/Perso-Arabic script rendering.",
            "This is not an Arabic translation and is not a scholarly Maltese Arabic-script orthography.",
        ],
    }

    for surah_key, ayahs in data.items():
        surah_no_text, _, surah_name = surah_key.partition(". ")
        surah_no = int(surah_no_text)
        converted[surah_key] = {}
        for ayah_no_text, payload in ayahs.items():
            ayah_no = int(ayah_no_text)
            latin = clean_text(payload.get("Translation", ""))
            arabic_script = transliterate_text(latin)
            converted[surah_key][ayah_no_text] = {
                "Translation": latin,
                "ArabicScript": arabic_script,
            }
            rows.append(
                {
                    "surah_number": surah_no,
                    "surah_name": surah_name,
                    "ayah_number": ayah_no,
                    "text_latin": latin,
                    "text_arabic_script": arabic_script,
                }
            )
            qa["verses"] += 1
            if not arabic_script:
                qa["empty_outputs"].append(f"{surah_no}:{ayah_no}")
            if re.search(r"[A-Za-zĊċĠġĦħŻż]", arabic_script):
                qa["latin_letters_remaining"].append(f"{surah_no}:{ayah_no}")

    OUT_JSON.write_text(json.dumps(converted, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "surah_number",
                "surah_name",
                "ayah_number",
                "text_latin",
                "text_arabic_script",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    OUT_QA.write_text(json.dumps(qa, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_QA}")


if __name__ == "__main__":
    main()
