from typing import List, Optional, Dict
from random import shuffle

from game.cards.base import Card

from .collections import Hand, Deck, Reserve, Discard, BaseCollection
from .consts import TempCardDestination


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

    def temp_to(self, destination: TempCardDestination):
        assert self.temp_card
        mapping: Dict[TempCardDestination, BaseCollection] = {
            TempCardDestination.HAND: self.hand,
            TempCardDestination.RESERVE: self.reserve,
            TempCardDestination.DISCARD: self.discard
        }
        mapping[destination].append(self.temp_card)
        self.temp_card = None
