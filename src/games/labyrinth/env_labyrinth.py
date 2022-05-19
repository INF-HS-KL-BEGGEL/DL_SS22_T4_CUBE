from turtle import position
from environment.environment import Environment
from games.labyrinth.labyrinth import Direction
from games.labyrinth.actions import GoAction
from games.labyrinth.state import StateLabyrinth


class EnvLabyrinth(Environment):

    def __init__(self, game):
        super().__init__(game)

    def calc_observation_space(self):
        statecounter = 0
        accessible_tiles = self.game.get_labyrinth().get_all_accessible_tiles()
        targets = self.game.get_targets()

        states = []
        for tile in accessible_tiles:
            for target in targets:
                states.append(StateLabyrinth(statecounter, tile, target))
                statecounter += 1

        return states

    def calc_action_space(self):
        action_space = [GoAction(0, self.game, Direction.NORTH), GoAction(1, self.game, Direction.EAST),
                        GoAction(2, self.game, Direction.SOUTH), GoAction(3, self.game, Direction.WEST)]
        return action_space

    def get_current_state(self):
        for state in self.observation_space:
            if state.get_current_tile() == self.game.get_current_tile() and \
                    state.get_current_target() == self.game.get_current_target():
                return state

        return None
