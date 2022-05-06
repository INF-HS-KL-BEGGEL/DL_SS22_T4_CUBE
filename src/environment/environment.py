from environment.game import Game
from environment.action import TurnRightAction, TurnLeftAction, TryFitAction
from environment.state import State


class Environment:
    
    def __init__(self):
        """Initializes the environment with a random Game"""

        self.game = Game.setup_game_random()
        self._observation_space = self.calc_observation_space()
        self.current_state = self.reset()
        self._action_space = [TurnRightAction(self.game), TurnLeftAction(self.game), TryFitAction(self.game)]

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
    
    def pick_random_action(self):
        return self.action_space.get_random_action()
    
    def execute_random_action(self):
        return self.pick_random_action().execute()

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

    def reset(self) -> State:
        return self._observation_space[0]

    def get_state_from(self, current_face, current_figure):
        for state in self.observation_space:

            if state.current_fig == current_figure and state.current_face == current_face:
                return state

        return None

    @staticmethod
    def create_sample():
        return Environment()
