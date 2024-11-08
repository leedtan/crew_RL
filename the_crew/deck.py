import random
from enum import Enum
NUM_CARDS = 40
class Suit(Enum):
    PINK = auto()
    YELLOW = auto()
    GREEN = auto()
    BLUE = auto()




    ROCKET = auto()

class Card:
    def __init__(self, suit: Suit, rank: int):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.suit.name} {self.rank}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in range(1, 10) if suit != Suit.rocket]
        # Add rocket cards or other special cards if needed
        random.shuffle(self.cards)

    def deal(self, num_players):

        hands = [[] for _ in range(num_players)]

        while self.cards:
            for hand in hands:
                if self.cards:
                    hand.append(self.cards.pop())
        return hands
