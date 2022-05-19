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
        tiles = self.game.get_labyrinth().get_all_tiles()

        states = []
        for tile in tiles:
            states.append(StateLabyrinth(statecounter, tile))
            statecounter += 1
          
        return states

    def calc_action_space(self):
        action_space = [GoAction(0, self.game, Direction.NORTH), GoAction(1, self.game, Direction.EAST),
                        GoAction(2, self.game, Direction.SOUTH), GoAction(3, self.game, Direction.WEST)]
        return action_space

    def get_current_state(self):
        for state in self.observation_space:
            if state.get_current_tile() == self.game.get_current_tile():
                return state
        return None
