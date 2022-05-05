import random
from environment.cube import Cube
from environment.game import Game
from environment.action import Action, TurnRightAction, TurnLeftAction, TryFitAction
from environment.state import State
import numpy as np

class ActionSpace:

    def __init__(self, space: list):
        self.space = space

    @property
    def n(self):
        return len(self.space)

    def append(self, object):
        self.space.append(object)

    def get(self, index):
        return self.space[index]

    def get_random_action(self):
        return self.space[random.randint(0, len(self.space) - 1)]


class Environment:
    
    def __init__(self):
        """Initializes the environment with a random Game"""
        self.state_counter = 0

        self.game = Game.setup_game_random()
        self.state = self.reset()
        self._action_space = ActionSpace(
            [TurnRightAction(self.game), TurnLeftAction(self.game), TryFitAction(self.game)])
        self._observation_space = self.calc_observation_space()


    def calc_observation_space(self):
        return ActionSpace(self.game.get_cube().get_faces())

    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space
    
    def pick_random_action(self):
        return self.action_space.get_random_action()
    
    def execute_random_action(self):
        return self.pick_random_action().execute()

    def step(self, action):    
        reward = action.execute()

        self.game.print_game()
        
        # Determine if the game is over
        done = self.game.is_done()

        state = State(self.state_counter)
        self.state_counter += 1

        return state, reward, done, {}

    def reset(self) -> State:
        state = State(self.state_counter)
        self.state_counter += 1
        return state

    @staticmethod
    def create_sample():
        return Environment()
