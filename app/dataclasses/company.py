from datetime import date
from typing import Optional
from dataclasses import dataclass

@dataclass
class Company:
    location: Optional['Location'] = None
    founding_date: date
    description: str
    name: str