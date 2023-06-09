import random

class Card:
    """ Karta do gry. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep

class Hand:
    """ Ręka. """
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ Talia kart do gry. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać, bo nie ma kart.")

##czes głowna
deck1 = Deck()
deck1.populate()
deck1.shuffle()
print(f'Talia: {deck1}')
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]

deck1.deal(hands, per_hand=5)
print(f'Ręka moja: {my_hand}')
print(f'Ręka Twoja: {your_hand}')
print(f'Talia: {deck1}')

my_hand.clear()
your_hand.clear()