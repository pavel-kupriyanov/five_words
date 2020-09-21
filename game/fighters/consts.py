from enum import Enum


class CollectionNames(str, Enum):
    HAND = 'HAND'
    RESERVE = 'RESERVE'
    DISCARD = 'DISCARD'
