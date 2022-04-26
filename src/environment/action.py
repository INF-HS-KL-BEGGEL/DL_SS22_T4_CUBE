# Noch keine Idee wie wir Actionen am besten wegabstrahieren können

class Action:
    """Class representing the actions that can be used in the game"""
    def __init__(self, name, game):
        self.game = game
        self.name = name

    def execute(self):
        pass


class TurnLeftAction(Action):
    """Class representing the action to turn the cube left"""
    def __init__(self, name, game):
        super().__init__(name, game)

    def execute(self):
        self.game.turn_left()


class TurnRightAction(Action):
    """Class representing the action to turn the cube right"""
    def __init__(self, name, game):
        super().__init__(name, game)

    def execute(self):
        self.game.turn_right()


class TryFitAction(Action):
    """
    Class representing the action to try
    to fit a figure on the current face
    """
    def __init__(self, name, game, figure):
        super().__init__(name, game)
        self.figure = figure

    def get_figure(self):
        return self.figure

    def execute(self):
        self.game.try_fit(self.figure)
