from environment.state import StateBase


class StateLabyrinth(StateBase):

    def __init__(self, number, current_tile, current_target):
        super().__init__(number)
        self.current_tile = current_tile
        self.current_target = current_target

    def get_current_tile(self):
        return self.current_tile
    
    def get_current_target(self):
        return self.current_target
    
