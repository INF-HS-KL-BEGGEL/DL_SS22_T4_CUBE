from cube import Cube
from state import State

class Environment():

    def __init__(self):

        self.cube = Cube()

        self.cmd_mapping = {
            "turn_left": self.cube.turn_left,
            "turn_right": self.cube.turn_right,
            "fits": self.cube.fits
        }

    def act(self, action):
        """
        (s')
        :param action:
        :return:
        """
        return State()

    @staticmethod
    def get_random_action():
        pass
