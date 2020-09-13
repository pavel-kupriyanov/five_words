from typing import List, Optional

from game.cards.base import Card


class BaseCollection:
    LIMIT = 0

    def __init__(self, initial: Optional[List[Card]] = None, max_cards=LIMIT):
        if initial is None:
            initial = []
        self.__collection = initial
        self.limit = max_cards

    def __len__(self):
        return len(self.__collection)

    def append(self, card: Card):
        assert not self.limit or len(self) < self.limit
        self.__collection.insert(0, card)


class Hand(BaseCollection):
    LIMIT = 5


class Reserve(BaseCollection):
    LIMIT = 5


class Deck(BaseCollection):

    def draw(self) -> Card:
        assert not self
        return self.__collection.pop()


class Discard(BaseCollection):
    pass
