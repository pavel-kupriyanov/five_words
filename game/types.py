"""
Shortcut for class imports
"""

from typing import List

from .cards import Card
from .fighters import Fighter

Cards = List[Card]

__all__ = [
    Card,
    Cards,
    Fighter
]
