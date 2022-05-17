from environment.state import StateBase


class StateLabyrinth(StateBase):

    def __init__(self, number):
        """
        The State is a Combination of the current Figure on top of the stack and the current Face of the cube
        in game.
        :param current_figure:
        :param current_face:
        :param prev:
        """
        super().__init__(number)
        self.current_face = current_face
        self.current_fig = current_fig

    def get_current_face(self):
        return self.current_face

    def get_current_figure(self):
        return self.current_fig
