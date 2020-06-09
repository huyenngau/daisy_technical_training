import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Deck:
    suits = ("Hearts", "Diamonds", "Clubs", "Spades")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = []

    def __str__(self):
        for card in self.cards:
            print(f"{card.suit} {card.value}")
        return "Cards remaining in deck: {}".format(len(self.cards))

    def shuffle(self):
        self.cards = []
        for suit in self.suits:
            for value in self.values:
                self.cards.append(Card(suit, value))

        if len(self.cards) < 52:
            raise Exception("Only deck full 52 cards can be shuffled!")
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            raise Exception("There are no cards to deal!")
        return self.cards.pop()


# Testing
deck = Deck()
deck.shuffle()
print("-----------------------------------")
print(deck)

deal_card = deck.deal()
print("-----------------------------------")
print(f"Deal card: {deal_card.suit} {deal_card.value}")
print(deck)

deck.shuffle()    
