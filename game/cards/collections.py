from typing import  Optional

from .base import Card, Cards


# TODO: move into cards module
class Collection:
    LIMIT = 0

    def __init__(self, initial: Optional[Cards] = None, max_cards=LIMIT):
        if initial is None:
            initial = []
        self._collection = initial
        self.limit = max_cards

    def __len__(self):
        return len(self._collection)

    def __repr__(self) -> str:
        return f'{str(type(self))} with {len(self)} cards.'

    def append(self, card: Card):
        assert not self.limit or len(self) < self.limit
        self._collection.insert(0, card)


class Hand(Collection):
    LIMIT = 5


class Reserve(Collection):
    LIMIT = 5


class Deck(Collection):

    def draw(self) -> Card:
        assert len(self)
        return self._collection.pop()


class Discard(Collection):
    pass
