class Result:

    all = []  # SSOT

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        # Result.all.append(self)
        self.__class__.all.append(self)

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        from classes.player import Player

        if isinstance(value, Player):
            self._player = value
        else:
            raise Exception

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, value):
        from classes.game import Game

        if isinstance(value, Game):
            self._game = value
        else:
            raise Exception

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, int) and 1 <= value <= 5000 and not hasattr(self, "score"):
            self._score = value
        else:
            raise Exception
