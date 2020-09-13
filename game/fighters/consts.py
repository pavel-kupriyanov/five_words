from enum import Enum


class TempCardDestination(str, Enum):
    HAND = 'HAND'
    RESERVE = 'RESERVE'
    DISCARD = 'DISCARD'
