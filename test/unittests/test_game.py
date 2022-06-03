import unittest
from deeplearning.games.cube.cube_game import CubeGame


class TestCube(unittest.TestCase):

    def test_setup_game(self):
        game = CubeGame.setup_game()

        print(game.get_figure_stack())

        game = CubeGame.setup_game()

        print(game.get_figure_stack())

        game = CubeGame.setup_game()

        print(game.get_figure_stack())

    def test_try_fit(self):
        game = CubeGame.setup_game()

        print(game.get_top_of_figure_stack(), game.get_current_face_index(), game.get_current_face())
        game.turn_left()
        game.try_fit()
        print(game.get_top_of_figure_stack())

        print(game.get_top_of_figure_stack(), game.get_current_face_index(), game.get_current_face())
        game.turn_left()
        game.try_fit()
        print(game.get_top_of_figure_stack())

        print(game.get_top_of_figure_stack(), game.get_current_face_index(), game.get_current_face())
        game.turn_left()
        game.try_fit()
        print(game.get_top_of_figure_stack())

        print(game.get_top_of_figure_stack(), game.get_current_face_index(), game.get_current_face())
        game.turn_left()
        game.try_fit()
        print(game.get_top_of_figure_stack())


if __name__ == '__main__':
    unittest.main()
