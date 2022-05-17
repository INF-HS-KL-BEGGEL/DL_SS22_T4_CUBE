from games.cube.cube_game import CubeGame
from games.cube.actions import TurnRightAction, TurnLeftAction, TryFitAction, RotateFigureAction
from games.cube.state import StateCube
from environment.state import StateBase
import random


class Environment:

    def __init__(self, game):
        """Initializes the environment with a random Game"""

        self.game = game
        self._observation_space = self.calc_observation_space()
        self._action_space = self.calc_action_space()
        self.current_state = self.reset_state()

    def add_action_space(self, actionspace: list):
        self._action_space = actionspace

    def add_observation_space(self, observation_space: list):
        self._observation_space = observation_space

    def calc_observation_space(self):
        statecounter = 0
        faces = self.game.get_cube().get_faces()
        figures = self.game.get_figure_stack()

        states = []
        for face in faces:
            for fig in figures:
                states.append(StateCube(face, fig, statecounter))
                statecounter += 1

        return states

    def calc_action_space(self):
        action_id = 0
        action_space = [TryFitAction(action_id, self.game)]
        length = len(self.game.faces)
        for i in range(length):
            action_id += 1
            action_space.append(TurnRightAction(action_id, self.game, i + 1))

            action_id += 1
            action_space.append(TurnLeftAction(action_id, self.game, i + 1))
        action_id += 1
        action_space.append(RotateFigureAction(action_id, self.game))
        return action_space

    @property
    def observation_space(self):
        return self._observation_space

    @property
    def action_space(self):
        return self._action_space

    def step(self, action):
        reward = action.execute()

        # Determine if the game is over
        done = self.game.is_done()

        if not done:
            current_state = self.get_current_state()

            return current_state, reward, done, {}

        return None, reward, done, {}

    def reset_state(self) -> StateBase:
        return self._observation_space[0]

    def reset_environment(self):
        self.game.reset_game()
        self.current_state = self.reset_state()

    def get_current_state(self):
        for state in self.observation_space:
            if state.get_current_figure() == self.game.get_top_of_figure_stack() and \
                    state.get_current_face() == self.game.get_current_face():
                return state

        return None

    @staticmethod
    def create_sample():
        return Environment(CubeGame.setup_game(6))

    def get_random_action(self):
        return random.choice(self.action_space)
