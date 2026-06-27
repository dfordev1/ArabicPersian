from __future__ import annotations

import json
import zipfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class RepoSmokeTests(unittest.TestCase):
    def test_manifest_lists_expected_release_bundles(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        files = {item["path"] for item in manifest["files"]}
        self.assertIn("data/releases/turkish_quran_arabic_script_v4_0_consistency_usability.zip", files)
        self.assertIn("data/releases/azeri_quran_arabic_script_production_v1.zip", files)
        self.assertIn("data/releases/kazakh_quran_arabic_script_production_v1.zip", files)

    def test_release_archives_open_cleanly(self) -> None:
        release_dir = ROOT / "data" / "releases"
        for archive in release_dir.glob("*.zip"):
            with zipfile.ZipFile(archive) as zf:
                bad = zf.testzip()
                self.assertIsNone(bad, f"{archive.name} failed at {bad}")
                self.assertGreater(len(zf.namelist()), 0, archive.name)

    def test_app_scaffold_exists(self) -> None:
        self.assertTrue((ROOT / "app" / "index.html").exists())
        self.assertTrue((ROOT / "app" / "styles.css").exists())
        self.assertTrue((ROOT / "app" / "app.js").exists())

    def test_source_json_assets_are_valid(self) -> None:
        source_dir = ROOT / "data" / "source"
        for path in source_dir.rglob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertTrue(data, path.name)
            if path.name == "quranjawifinal.json":
                self.assertIsInstance(data, list)
                self.assertIn("jawiTranslation", data[0])
            if path.name == "bangaliurduquran.json":
                self.assertIsInstance(data, dict)
                self.assertIn("1:1:1", data)
            if path.name == "maltesequrandata.json":
                self.assertIsInstance(data, dict)
                self.assertIn("1. Al-Fatiha", data)
            if path.name == "dv-unknow-simple.json":
                self.assertIsInstance(data, dict)
                self.assertIn("1:1", data)


if __name__ == "__main__":
    unittest.main()
