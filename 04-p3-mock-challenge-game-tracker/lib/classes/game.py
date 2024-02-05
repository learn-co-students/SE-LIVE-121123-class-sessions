class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "title"):
            self._title = value
        else:
            raise Exception

    def results(self):
        from classes.result import Result

        return [result for result in Result.all if result.game == self]  # like a filter

    def players(self):
        return list(set([result.player for result in self.results()]))

    def average_score(self, player):
        player_scores = [
            result.score for result in self.results() if result.player == player
        ]
        if player_scores:
            return sum(player_scores) / len(player_scores)
        return 0
