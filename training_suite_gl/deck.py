#


class Card:
    _suites = ("\u2660", "\u2663", "\u2666", "\u2665")
    _values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")

    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def __str__(self):
        return self._suites[self.suite] + " " + self._values[self.value]


class JokerCard:
    def __str__(self):
        return "JOKER"


class Deck:
    def __init__(self):
        self.cards = [Card(i, x) for i in range(0, 4) for x in range(0, 13)]

    def shuffle(self):
        from random import shuffle

        shuffle(self.cards)

    def pop(self, num=-1):
        try:
            return self.cards.pop(num)
        except IndexError:
            return "Deck does not hold the card"

    def random(self):
        from random import choice

        return choice(self.cards)

    def get_card(self, num):
        try:
            return self.cards[num]
        except IndexError:
            return "Deck does not hold the card"

    def compare(self, card1, card2):
        try:
            if card1.suite > card2.suite and card1.value > card2.value:
                return "{} > {}".format(card1, card2)
            if card1.suite == card2.suite and card1.value == card2.value:
                return "{} == {}".format(card1, card2)
            return "{} < {}".format(card1, card2)
        except AttributeError:
            return "Deck does not hold the card"


def run_some_tests():
    "Define a deck and run some tests!"

    deck = Deck()
    print(deck.pop())
    deck.cards.append(JokerCard())
    print(deck.pop())
    print([str(deck.get_card(i)) for i in range(13)])
    print([str(deck.get_card(i)) for i in range(13, 26)])
    print(deck.compare(deck.get_card(1), deck.get_card(223)))
    deck.shuffle()
    print(deck.pop())
    print(deck.pop(23))
    print([str(deck.get_card(i)) for i in range(13)])
    print([str(deck.random()) for i in range(5)])


run_some_tests()
