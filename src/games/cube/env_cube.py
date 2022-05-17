from environment.environment import Environment
from games.cube.actions import TurnRightAction, TurnLeftAction, TryFitAction, RotateFigureAction
from games.cube.state import StateCube


class EnvCube(Environment):

    def __init__(self, game):
        super().__init__(game)

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

    def get_current_state(self):
        for state in self.observation_space:
            if state.get_current_figure() == self.game.get_top_of_figure_stack() and \
                    state.get_current_face() == self.game.get_current_face():
                return state

        return None