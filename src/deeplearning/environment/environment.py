from abc import ABC, abstractmethod
from deeplearning.environment.state import StateBase
import random


class Environment(ABC):

    def __init__(self, game):
        """Initializes the environment with a random Game"""

        self.game = game
        self._observation_space = self.calc_observation_space()
        self._action_space = self.calc_action_space()
        self.current_state = self.reset_state()

    @abstractmethod
    def get_current_state(self):
        pass

    @abstractmethod
    def calc_observation_space(self):
        pass

    @abstractmethod
    def calc_action_space(self):
        pass

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
        self.game.reset_game()
        return self._observation_space[0]

    def reset_environment(self):
        self.game.reset_game()
        self.current_state = self.reset_state()

    def get_random_action(self):
        return random.choice(self.action_space)
