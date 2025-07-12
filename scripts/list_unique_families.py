#!/usr/bin/env python3
"""
list_unique_families.py

📜 Outputs all unique 'families' from the vault as:
"family-name"
Each on its own line, lowercased, quoted.

🗂 File written to: ref/families.text
"""

import json
from pathlib import Path

VAULT_FILE = Path("../data/ivault_master.json")
REF_DIR = Path("../ref")
OUTPUT_FILE = REF_DIR / "families.txt"

def main():
    data = json.loads(VAULT_FILE.read_text(encoding="utf-8"))
    families_set = set()

    for entry in data:
        families = entry.get("families", [])
        for fam in families:
            if isinstance(fam, str):
                families_set.add(fam.lower())

    REF_DIR.mkdir(exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(f'"{fam}"' for fam in sorted(families_set)), encoding="utf-8")

    print(f"✅ Families list written to: {OUTPUT_FILE}")

    # Optional count output — uncomment when needed
    # print(f"\nTotal unique families: {len(families_set)}")

if __name__ == "__main__":
    main()