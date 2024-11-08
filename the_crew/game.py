from .deck import Deck
from .player import Player
from .mission import Mission

class Game:
    def __init__(self, num_players):
        self.deck = Deck()
        self.players = [Player(i) for i in range(num_players)]
        self.current_round = 0
        self.mission = None
        self.trick_winner = None  # To track round-by-round winner

    def setup(self, mission):
        self.mission = mission
        hands = self.deck.deal(len(self.players))
        for i, hand in enumerate(hands):
            self.players[i].set_hand(hand)
        print(f"Game set up with mission: {self.mission.description}")

    def play_round(self):
        # A round of play where each player plays one card in order
        cards_played = []
        for player in self.players:
            card = player.play_card(player.hand[0])  # Simple AI: play first card
            print(f"{player} plays {card}")
            cards_played.append((player, card))

        self.trick_winner = self.evaluate_trick(cards_played)
        self.current_round += 1

    def evaluate_trick(self, cards_played):
        # Determine who won the trick based on game rules
        winning_card = max(cards_played, key=lambda x: x[1].rank)  # Simplified example
        print(f"{winning_card[0]} wins the trick with {winning_card[1]}")
        return winning_card[0]

    def check_game_end(self):
        # Check for mission completion
        return self.mission.check_win_condition(self)

    def play_game(self):
        while not self.check_game_end():
            self.play_round()
        print("Mission Accomplished!")
