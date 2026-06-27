#!/usr/bin/env python3
from pathlib import Path
import json, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument("output_dir")
    args = parser.parse_args()

    data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    surahs = {}
    for key, value in data.items():
        surah = str(key).split(":")[0].zfill(3)
        surahs.setdefault(surah, {})[key] = value

    for surah, verses in surahs.items():
        (out / f"{surah}.json").write_text(
            json.dumps(verses, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8"
        )

    print(f"Wrote {len(surahs)} surah files to {out}")

if __name__ == "__main__":
    main()
