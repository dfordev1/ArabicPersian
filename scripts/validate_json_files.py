#!/usr/bin/env python3
from pathlib import Path
import json, argparse, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()

    root = Path(args.path)
    files = list(root.rglob("*.json"))
    failed = []
    for p in files:
        try:
            json.loads(p.read_text(encoding="utf-8"))
            print(f"OK {p}")
        except Exception as e:
            print(f"FAIL {p}: {e}")
            failed.append(str(p))
    if failed:
        sys.exit(1)

if __name__ == "__main__":
    main()
