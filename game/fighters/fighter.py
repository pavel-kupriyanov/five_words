from typing import List
from random import shuffle

from game.cards.base import Card


class Fighter:

    def __init__(self, name: str, deck: List[Card]):
        self.name = name
        self.deck = shuffle(deck)
