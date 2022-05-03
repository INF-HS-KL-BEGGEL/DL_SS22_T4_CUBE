# Noch keine Idee wie wir Actionen am besten wegabstrahieren können
from environment.state import State

class Action:
    """Class representing the actions that can be used in the game"""
    def __init__(self, game):
        self.game = game

    def execute(self) -> (State, int):
        pass


class TurnLeftAction(Action):
    """Class representing the action to turn the cube left"""
    def __init__(self, game):
        super().__init__(game)

    def execute(self) -> (State, int):
        """
        :return: reward
        """
        self.game.turn_left()
        return State(self.game.get_current_face()), 1

class TurnRightAction(Action):
    """Class representing the action to turn the cube right"""
    def __init__(self, game):
        super().__init__(game)

    def execute(self) -> (State, int):
        """
        :return: reword
        """
        self.game.turn_right()
        return State(self.game.get_current_face()), 1

class TryFitAction(Action):
    """
    Class representing the action to try
    to fit a figure on the current face
    """
    def __init__(self, game):
        super().__init__(game)
        self.figure = None

    def get_figure(self):
        return self.figure

    def set_figure(self, figure):
        self.figure =figure

    def execute(self) -> (State, int):
        """
        :return: reward
        """
        self.game.try_fit(self.figure)
        return State(self.game.get_current_face()), 2