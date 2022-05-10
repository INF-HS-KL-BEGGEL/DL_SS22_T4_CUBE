import unittest
from environment.game import Game
from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure
from environment.environment import Environment

class TestEnv(unittest.TestCase):

    def test_setup_env(self):

        env = Environment.create_sample()

        print([(s.get_number(), s.current_face, s.current_fig) for s in env.observation_space])


if __name__ == '__main__':
    unittest.main()

