#!/usr/bin/env python3
from pathlib import Path
import zipfile, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("zip_file")
    parser.add_argument("output_dir")
    args = parser.parse_args()

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.zip_file, "r") as z:
        z.extractall(out)
    print(f"Extracted {args.zip_file} to {out}")

if __name__ == "__main__":
    main()
