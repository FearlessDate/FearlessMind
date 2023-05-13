from typing import List
from dataclasses import dataclass

@dataclass
class Country:
    name: 'MultilingualStr'
    languages: List[tuple['Language', float]]
    continent: str
