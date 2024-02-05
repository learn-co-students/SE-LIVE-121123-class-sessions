import ipdb
from classes.game import Game
from classes.player import Player
from classes.result import Result

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    game1 = Game("Baldur's Gate 3")
    player1 = Player("Susan")
    player_names = ["Isaiah", "Cecilia", "Nuburooj"]
    new_players = [Player(name) for name in player_names]

    result1 = Result(player1, game1, 300)

    ipdb.set_trace()
