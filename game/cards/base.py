from typing import List

class Card:
    number: int


class FencingCard(Card):
    pass


class WarCard(Card):
    pass


class GrappleCard(Card):
    pass


class SpecialCard(Card):
    pass


Cards = List[Card]
