from dataclasses import dataclass
from decimal import Decimal

@dataclass
class ItemDTO:
    name: str
    description: str
    price: Decimal
