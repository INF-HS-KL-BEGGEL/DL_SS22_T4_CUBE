from deeplearning.environment.environment import Environment
from deeplearning.games.labyrinth.labyrinth import Direction
from deeplearning.games.labyrinth.actions import GoAction
from deeplearning.games.labyrinth.state import StateLabyrinth


class EnvLabyrinth(Environment):

    def __init__(self, game):
        super().__init__(game)

    @staticmethod
    def powerset(fullset):
        listrep = list(fullset)
        n = len(listrep)
        return [[listrep[k] for k in range(n) if i&1<<k] for i in range(2**n)]

    def calc_observation_space(self):
        statecounter = 0
        accessible_tiles = self.game.get_labyrinth().get_all_accessible_tiles()
        targets = self.game.get_targets()

        states = []
        target_combinations = EnvLabyrinth.powerset(targets)
        for tile in accessible_tiles:
            for targets in target_combinations:
                states.append(StateLabyrinth(statecounter, tile, targets))
                statecounter += 1

        # Empty Target States
        for tile in accessible_tiles:
            states.append(StateLabyrinth(statecounter, tile, []))
            statecounter += 1

        return states

    def calc_action_space(self):
        action_space = [GoAction(0, self.game, Direction.NORTH), GoAction(1, self.game, Direction.EAST),
                        GoAction(2, self.game, Direction.SOUTH), GoAction(3, self.game, Direction.WEST)]
        return action_space

    def get_current_state(self):
        for state in self.observation_space:
            if state.get_current_tile() == self.game.get_current_tile() and \
                    state.get_current_targets() == self.game.get_current_targets():
                return state

        return StateLabyrinth(-1, None, None)
