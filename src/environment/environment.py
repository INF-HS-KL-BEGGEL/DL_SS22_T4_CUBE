from environment.game import Game
from environment.action import TurnRightAction, TurnLeftAction, TryFitAction
from environment.state import State
import random

class Environment:
    
    def __init__(self):
        """Initializes the environment with a random Game"""

        self.game = Game.setup_game()
        self._observation_space = self.calc_observation_space()
        self.current_state = self.reset_state()
        self._action_space = [
            TurnRightAction(0, self.game, 1),
            TurnRightAction(1, self.game, 2),
            TurnLeftAction(2, self.game, 1),
            TurnLeftAction(3, self.game, 2),
            TryFitAction(4, self.game)]

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

            if state.current_fig == current_figure and state.current_face == current_face:
                return state

        return None

    @staticmethod
    def create_sample():
        return Environment()

    def get_random_action(self):
        return random.choice(self.action_space)
