from abc import ABC, abstractmethod


class Game(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def reset_game(self):
        pass

    @abstractmethod
    def is_done(self):
        pass
