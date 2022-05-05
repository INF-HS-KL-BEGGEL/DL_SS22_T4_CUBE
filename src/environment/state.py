

class State:

    def __init__(self, number, prev=None):
        """
        The State is a Combination of the current Figure on top of the stack and the current Face of the cube
        in game.
        :param current_figure:
        :param current_face:
        :param prev:
        """
        self.number = number
        self.prev = prev

    def get_prev(self):
        return self.prev

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        print("ACHTUNG HIER WURDE __ne__ aufgerufen")
        return not self == other

    def get_number(self):
        return self.number
