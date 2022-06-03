from abc import ABC, abstractmethod


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
