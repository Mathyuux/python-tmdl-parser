import json
from pathlib import Path
from typing import Dict

def save(dict: Dict, output_file: str, format: str = "json"):
    if format == "json":
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(dict, f, indent=2, ensure_ascii=False)
        return