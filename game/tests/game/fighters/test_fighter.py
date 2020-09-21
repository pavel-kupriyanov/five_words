import pytest

from game.types import Cards, Fighter
from game.fighters import get_some_cards, CollectionNames


@pytest.fixture(name='cards')
def get_cards() -> Cards:
    return get_some_cards()


def test_draw_cards(cards: Cards):
    giacomo = Fighter('Giacomo Vonzazzo', cards)
    collections = {
        CollectionNames.HAND: [],
        CollectionNames.RESERVE: [],
        CollectionNames.DISCARD: []
    }
    for i in range(5):
        for destination, destination_cards in collections.items():
            giacomo.draw()
            destination_cards.append(giacomo.temp_card)
            giacomo.place_card_into(destination)

    assert all(map(len, collections.values()))
    number_of_cards = list(map(len, [giacomo.reserve, giacomo.hand, giacomo.discard]))
    assert all(number_of_cards)
    assert len(giacomo.deck) == len(cards) - sum(number_of_cards)
    assert giacomo.temp_card is None
