class Mission:
    def __init__(self, description, target_conditions):
        self.description = description
        self.target_conditions = target_conditions  # dict of {suit, rank} pairs or other goals

    def check_win_condition(self, game_state):
        # Checks if conditions are met in the game state
        for condition in self.target_conditions:
            if not self.target_conditions[condition](game_state):
                return False
        return True
