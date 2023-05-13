from typing import List
from dataclasses import dataclass
from typing import Optional

class Location:
    country: Optional['City'] = None
    city: Optional['Country'] = None
