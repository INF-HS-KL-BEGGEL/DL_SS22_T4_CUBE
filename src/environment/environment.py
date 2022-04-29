import random
from environment.cube import Cube
from environment.game import Game
from environment.action import Action, TurnRightAction, TurnLeftAction, TryFitAction
from environment.state import State

class Space():

    def __init__(self, space: list):
        self.space = space

    @property
    def n(self):
        return len(self.space)

    def sample(self):
        return random.choice(self.space)

    def append(self, object):
        self.space.append(object)

class Environment:


    def __init__(self):
        """Initializes the environment with a random Game"""
        self.game = Game.setupGameRandom()
        self._action_space = Space([TurnRightAction, TurnLeftAction, TryFitAction])
        self._observation_space = self.calc_observation_space()
        self.state_counter = 0

    def calc_observation_space(self):
        space = []
        for i, face in enumerate(self.game.get_cube().get_faces()):
            space.append(State(i))
        return Space(space)

    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space

    def step(self, action) -> (State, int, str):
        self.state_counter += 1
        reward = action.execute()
        return State(self.game.get_current_face()), reward, ""

    def reset(self) -> State:
        self.state_counter += 1
        return State(self.state_counter)