from cube import Cube
from game import Game
from action import Action, TurnRightAction, TurnLeftAction, TryFitAction

class Environment():

    def __init__(self):

        self.game = Game.setupGameRandom()

    def act(self, action_str):

        actions = {
            ""
        }

    @staticmethod
    def get_random_action():
        pass
