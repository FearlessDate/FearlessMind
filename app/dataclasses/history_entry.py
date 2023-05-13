from datetime import date
from typing import Optional
from dataclasses import dataclass

@dataclass
class HistoryEntry:
    location: Optional['Location'] = None
    date: date
    text: str
