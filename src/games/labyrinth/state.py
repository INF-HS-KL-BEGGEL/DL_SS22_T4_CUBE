from environment.state import StateBase


class StateLabyrinth(StateBase):

    def __init__(self, number, current_tile):
        super().__init__(number)
        self.current_tile = current_tile

    def get_current_tile(self):
        return self.current_tile

    
