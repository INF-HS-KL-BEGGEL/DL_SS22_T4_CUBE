import unittest
from environment.game import Game
from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure


class TestCube(unittest.TestCase):

    def test_setup_game(self):
        game = Game.setup_game()

        print(game.get_figure_stack())

        game = Game.setup_game()

        print(game.get_figure_stack())

        game = Game.setup_game()

        print(game.get_figure_stack())


if __name__ == '__main__':
    unittest.main()
