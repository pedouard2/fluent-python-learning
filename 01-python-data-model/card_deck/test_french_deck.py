import pytest
from french_deck import Card, FrenchDeck


@pytest.fixture
def deck():
    return FrenchDeck()


def test_deck_length(deck):
    assert len(deck) == 52


@pytest.mark.parametrize(
    "rank,suit", [("A", "spades"), ("K", "hearts"), ("2", "diamonds")]
)
def test_card_creation(rank, suit):
    card = Card(rank, suit)
    assert card.rank == rank

    assert card.suit == suit
