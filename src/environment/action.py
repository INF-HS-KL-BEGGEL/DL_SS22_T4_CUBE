from abc import ABC, abstractmethod

import numpy as np


class Action(ABC):
    """Class representing the actions that can be used in the game"""

    def __init__(self, id, game):
        self.game = game
        self._id = id

    @abstractmethod
    def execute(self):
        pass

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return "<ActionId %s , %s>" % (self.id, self.__class__.__name__)


class TurnLeftAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, id, game, step=1):
        super().__init__(id, game)
        self.step = step

    def execute(self) -> int:
        self.game.turn_left(self.step)
        return -len(self.game.faces)


class TurnRightAction(Action):
    """Class representing the action to turn the cube right"""

    def __init__(self, id, game, step):
        super().__init__(id, game)
        self.step = step

    def execute(self):
        self.game.turn_right(self.step)
        return -len(self.game.faces)


class TryFitAction(Action):
    """
    Class representing the action to try
    to fit a figure on the current face
    """

    def __init__(self, id, game):
        super().__init__(id, game)

    def execute(self):
        """
        :return: reward
        """
        fits = self.game.try_fit()
        if fits:
            # Square the length as reward plus give back negative reward from turn action
            return np.power(len(self.game.faces), 2) + len(self.game.faces)
        return -len(self.game.faces)
