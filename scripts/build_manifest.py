#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, argparse, datetime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("--out", default="manifest.json")
    args = parser.parse_args()

    root = Path(args.path)
    manifest = []
    for p in sorted(root.rglob("*")):
        if p.is_file():
            manifest.append({
                "path": str(p.relative_to(root)),
                "size_bytes": p.stat().st_size,
                "sha256": hashlib.sha256(p.read_bytes()).hexdigest()
            })

    Path(args.out).write_text(json.dumps({
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "root": str(root),
        "files": manifest
    }, indent=2), encoding="utf-8")
    print(f"Wrote {args.out}")

if __name__ == "__main__":
    main()
