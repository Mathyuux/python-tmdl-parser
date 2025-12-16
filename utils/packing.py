import os
from typing import Dict
from pathlib import Path
from utils.parser import TMDLParser

class TMDLPacking:
    def __init__(self, path: Path):
        self.path = path
        self.pbip = os.path.splitext(next(f for f in os.listdir(self.path) if f.endswith('.pbip')))[0]

    def pack_table(self) -> Dict:
        tables = {}

        for file in Path(f"{self.path}\\{self.pbip}.SemanticModel\\definition\\tables").glob("*.tmdl"):
            content = TMDLParser(file.read_text(encoding="utf-8"))
            table_parsed = content.parse("table", r"table\s+([^\n]+)")

            # Check if tables exists
            if not table_parsed: continue

            source_parsed = content.parse("source", r"Source\s*=\s*([^\n]+)")
            source_type = content.parse_source_type(source_parsed["source"])
            columns_parsed = content.parse("columns", r"column\s+([^\n]+)\s*dataType:\s*([A-Za-z0-9_]+)")

            tables[table_parsed["table"]] = {
                "source": source_parsed["source"],
                "source_type" : source_type,
                "columns": columns_parsed["columns"],
            }

        return tables