from typing import Optional, Tuple
from datetime import date
from dataclasses import dataclass

@dataclass
class JobVacancy:
    company: 'Company'
    title: str
    text: str
    salary_range_usd: Optional[Tuple[int, int]] = None
    location: Optional['Location'] = None
    date_published: Optional[date] = None
