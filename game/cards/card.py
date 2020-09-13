from .base import (
    FencingCard,
    WarCard,
    GrappleCard,
    SpecialCard,
)


class Absetzen(FencingCard):
    number = 1


class Zornhau1(FencingCard):
    number = 10


class Zornhau2(FencingCard):
    number = 14


class Zwerhau(FencingCard):
    number = 16


class Schielhau(FencingCard):
    number = 8


class Streichen1(FencingCard):
    number = 12


class Streichen2(FencingCard):
    number = 13


class ObenAbgenomen(WarCard):
    number = 30


class BrunchObenAbgenomen(WarCard):
    number = 31


class Winden(WarCard):
    number = 34


class Zornort(WarCard):
    number = 38


class ZwerhauStuck1(WarCard):
    number = 40


class BrunchZwerhauStuck1(WarCard):
    number = 17


class Duplieren(WarCard):
    number = 26


class Knopfstoss1(GrappleCard):
    number = 49


class Knopfstoss2(GrappleCard):
    number = 50


class Knetritt(GrappleCard):
    number = 48


class Daggerstoss(GrappleCard):
    number = 47


class Durchwechsel(SpecialCard):
    number = 54


class LengUndMasse(SpecialCard):
    number = 60
