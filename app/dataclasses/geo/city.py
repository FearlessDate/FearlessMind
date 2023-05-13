from typing import List
from dataclasses import dataclass

@dataclass
class City:
    name: 'MultilingualStr'
    population: int
    country: 'Country'
    region: str
    languages: List[tuple['Language', float]]
