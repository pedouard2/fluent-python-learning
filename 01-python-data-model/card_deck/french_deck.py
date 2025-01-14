import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JKQA")
    suits = "spades diamonds clubs hearts".split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __get__item__(self, position):
        return self._cards[position]

    def spades_high(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return (
            rank_value * len(FrenchDeck.suit_values) + FrenchDeck.suit_values[card.suit]
        )
