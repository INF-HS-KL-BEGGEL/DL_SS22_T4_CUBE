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

    def sample(self):
        return random.choice(self.space)

    def append(self, object):
        self.space.append(object)

    def get(self, index):
        return self.space[index]

    def get_random_action(self):
        return self.space[random.randint(0, len(self.space) - 1)]


class Environment:
    
    def __init__(self):
        """Initializes the environment with a random Game"""
        self.game = Game.setup_game_random()
        self.state = self.reset()
        self._action_space = ActionSpace(
            [TurnRightAction(self.game), TurnLeftAction(self.game)])
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
        self.action_space.get(action).execute()
        fits = self.game.try_fit(self.game.figures[0])

        if fits:
            reward = 25
        else:
            reward = -1
        
        # Determine if the game is over
        done = False
        if self.state.state_position > 1:
            done = True

        # Update the state
        self.state.update_state(self.game.get_current_face())

        return self.state, reward, done, {}

    def reset(self) -> State:
        return State(0, self.game.get_current_face())

    @staticmethod
    def create_sample():
        return Environment()
