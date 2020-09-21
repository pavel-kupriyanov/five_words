from typing import List, Optional, Dict
from random import shuffle

from game.cards.base import Card

from .collections import Hand, Deck, Reserve, Discard, Collection
from .consts import CollectionNames


class Fighter:

    def __init__(self, name: str, deck: List[Card]):
        self.name = name
        # maybe use descriptors?
        self.temp_card: Optional[Card] = None
        self.hand = Hand()
        self.reserve = Reserve()
        self.discard = Discard()
        self.deck = Deck(shuffle(deck))

    def draw(self):
        # TODO: think about error handling
        assert self.temp_card is None
        self.temp_card = self.deck.draw()

    def place_card_into(self, collection: CollectionNames):
        assert self.temp_card
        mapping: Dict[CollectionNames, Collection] = {
            CollectionNames.HAND: self.hand,
            CollectionNames.RESERVE: self.reserve,
            CollectionNames.DISCARD: self.discard
        }
        mapping[collection].append(self.temp_card)
        self.temp_card = None
