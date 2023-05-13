from datetime import date
from typing import Optional
from dataclasses import dataclass

from .history_entry import HistoryEntry



@dataclass
class JobHistoryEntry(HistoryEntry):
    company: 'Company'
    title: str
    finish_date: Optional[date] = None
