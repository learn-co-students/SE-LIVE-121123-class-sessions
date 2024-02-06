class Result:

    all = []  # SSOT

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        # Result.all.append(self)
        self.__class__.all.append(self)
        """
        Using `self.__class__.all.append(self)` within the `__init__` method is generally considered better practice than directly referencing the class name `Result.all.append(self)`. Here's why:

        1. **Encapsulation**: Using `self.__class__` allows the code to remain encapsulated within the instance itself. This means that if the class name were to change, the code would still work correctly because it refers to the class through the instance (`self`).

        2. **Inheritance**: If you later decide to subclass `Result`, using `self.__class__` ensures that the subclass's static list is updated, rather than always appending to the base class's list. Directly referencing `Result.all` would not reflect this behavior and could lead to incorrect data being stored in the wrong list.

        3. **Readability**: While both forms are readable, using `self.__class__` makes it clear that the operation is being performed on the class of the instance, which can be helpful for understanding the code's intent.

        4. **Consistency**: Consistently using `self.__class__` throughout your codebase can help maintain a consistent coding style, making the code easier to read and understand.`

        By using `self.__class__.all.append(self)`, you ensure that the instance is added to the correct list associated with its class, regardless of whether it's the base class or a subclass.
        """

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
