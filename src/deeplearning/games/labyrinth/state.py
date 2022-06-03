from deeplearning.environment.state import StateBase


class StateLabyrinth(StateBase):

    def __init__(self, number, current_tile, current_targets):
        super().__init__(number)
        self.current_tile = current_tile
        self.current_targets = current_targets

    def get_current_tile(self):
        return self.current_tile

    def get_current_targets(self):
        return self.current_targets
