class Player:
    def __init__(self, id):
        self.id = id
        self.hand = []

    def set_hand(self, hand):
        self.hand = hand

    def play_card(self, card):
        self.hand.remove(card)
        return card

    def __repr__(self):
        return f"Player {self.id} with hand {self.hand}"
