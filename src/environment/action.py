
class Action:
    """Class representing the actions that can be used in the game"""

    def __init__(self, game):
        self.game = game

    def execute(self):
        pass


class TurnLeftAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, game):
        super().__init__(game)

    def id(self):
        return 0

    def execute(self) -> int:
        self.game.turn_left()
        return 1


class TurnRightAction(Action):
    """Class representing the action to turn the cube right"""

    def __init__(self, game):
        super().__init__(game)

    def id(self):
        return 1

    def execute(self):
        self.game.turn_right()
        return 1

class TryFitAction(Action):
    """
    Class representing the action to try
    to fit a figure on the current face
    """

    def __init__(self, game):
        super().__init__(game)

    def id(self):
        return 2

    def execute(self):
        """
        :return: reward
        """
        fits = self.game.try_fit()
        if fits:
            return 1
        return -1