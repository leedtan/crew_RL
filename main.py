from the_crew.game import Game
from the_crew.mission import Mission

@dataclass

def dummy_win_condition(game_state):
    return game_state.current_round >= 3

def player_wins_0_rounds(game_state):
    return game_state.current_round >= 3



def main():
    num_players = 3
    mission = Mission("Complete three rounds", {"rounds": dummy_win_condition})
    game = Game(num_players)
    game.setup(mission)
    game.play_game()

if __name__ == "__main__":
    main()
