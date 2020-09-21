from typing import List
from game.cards.base import Card
# TODO, remove wildcard
from game.cards.card import *


def get_some_cards() -> List[Card]:
    return [
        Absetzen(),
        Zornhau1(),
        Zornhau2(),
        Zwerhau(),
        Schielhau(),
        Streichen1(),
        Streichen2(),
        ObenAbgenomen(),
        BrunchObenAbgenomen(),
        Winden(),
        Zornort(),
        ZwerhauStuck1(),
        BrunchZwerhauStuck1(),
        Duplieren(),
        Knopfstoss1(),
        Knopfstoss2(),
        Knetritt(),
        Daggerstoss(),
        Durchwechsel(),
        LengUndMasse(),
    ]
