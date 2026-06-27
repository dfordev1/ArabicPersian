#!/usr/bin/env python3
"""Build a lightweight JSON search index from verse lookup data.

This is intentionally simple so it can be adapted later for Elasticsearch,
SQLite FTS, or a frontend search cache.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def iter_text(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_text(item)
    elif isinstance(value, list):
        for item in value:
            yield from iter_text(item)


def build_index(data):
    index = []
    for key, value in data.items():
        text = " ".join(part for part in iter_text(value) if part).strip()
        index.append({"key": key, "text": text})
    return index


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    parser.add_argument("output_json")
    args = parser.parse_args()

    data = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    index = build_index(data)
    Path(args.output_json).write_text(
        json.dumps(index, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {args.output_json}")


if __name__ == "__main__":
    main()
