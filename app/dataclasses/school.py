from datetime import date
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class Company:
    location: Optional['Location'] = None
    founding_date: date
    description: str
    name: 'MultilingualStr'
    faculties: Optional[List[str]] = None
