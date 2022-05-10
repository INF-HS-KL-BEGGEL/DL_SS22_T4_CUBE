

class State:

    def __init__(self, current_face, current_fig, number, prev=None):
        """
        The State is a Combination of the current Figure on top of the stack and the current Face of the cube
        in game.
        :param current_figure:
        :param current_face:
        :param prev:
        """
        self.current_face = current_face
        self.current_fig = current_fig
        self.number = number

    def get_current_face(self):
        return self.current_face

    def get_current_figure(self):
        return self.current_fig

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        print("ACHTUNG HIER WURDE __ne__ aufgerufen")
        return not self == other

    def get_number(self):
        return self.number
