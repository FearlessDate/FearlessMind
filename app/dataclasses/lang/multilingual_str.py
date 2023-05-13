from dataclasses import dataclass

@dataclass
class MultilingualStr:
    english: str
    native: str
    secondary: str
