from games.cube.cube_game import CubeGame
from environment.action import TurnRightAction, TurnLeftAction, TryFitAction, RotateFigureAction
from environment.state import State
import random


class Environment:

    def __init__(self):
        """Initializes the environment with a random Game"""

        self.game = CubeGame.setup_game(6)
        self._observation_space = self.calc_observation_space()
        self._action_space = self.calc_action_space()
        self.current_state = self.reset_state()


    def calc_observation_space(self):
        statecounter = 0
        faces = self.game.get_cube().get_faces()
        figures = self.game.get_figure_stack()

        states = []
        for face in faces:
            for fig in figures:
                states.append(State(face, fig, statecounter))
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

    def get_current_state(self):
        return self.current_state

    def step(self, action):
        reward = action.execute()

        # Determine if the game is over
        done = self.game.is_done()

        if not done:
            current_state = self.get_state_from(self.game.get_current_face(), self.game.get_top_of_figure_stack())
            next_state = self.observation_space[current_state.get_number()]
            return next_state, reward, done, {}

        return None, reward, done, {}

    def reset_state(self) -> State:
        return self._observation_space[0]

    def reset_environment(self):
        self.game.reset_game()
        self.current_state = self.reset_state()

    def get_state_from(self, current_face, current_figure):
        for state in self.observation_space:
            if state.get_current_figure() == current_figure and state.get_current_face() == current_face:
                return state

        return None

    @staticmethod
    def create_sample():
        return Environment()

    def get_random_action(self):
        return random.choice(self.action_space)
