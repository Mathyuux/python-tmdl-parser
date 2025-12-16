import re
from typing import Dict

class TMDLParser:
    def __init__(self, content: str):
        self.content = content

    def parse(self, parsing: str, regex: str, exc: str = r"partition\s+[^\n]+=\s([^\n]+)") -> Dict:
        e = re.compile(exc).search(self.content)

        if not e: raise ValueError(f"[X][parser.py] Exception error.")
        if e.group(1) != 'm': return None

        m = re.findall(regex, self.content)

        if not m: raise ValueError(f"[X][parser.py] Find nothing like {regex}.")

        return {parsing: m[0] if len(m) == 1 else dict(m)}
    
    def parse_source_type(self, table_source: str) -> str:
        regexes = {
            "Csv": r"Csv",
            "Teradata": r"Teradata",
            "Sql": r"Sql",
            "Date": r"Date",
        }

        for name, pattern in regexes.items():
            if re.search(pattern, table_source):
                return name
            
        return 'Autre'