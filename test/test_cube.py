import unittest
from games.cube import Cube
from environment.face import Face
from environment.figure import Figure


class TestCube(unittest.TestCase):

    def test_create_face(self):
        face = Face.create("figure1")

        self.assertEqual(len(face.get_figures()), 1)

    def test_add_face(self):

        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_matching_figure(fig1)
        cube.add_face(face)

        self.assertEqual(len(cube.get_faces()), 1)

    def test_remove_face(self):

        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_matching_figure(fig1)
        cube.add_face(face)

        cube.remove_face(0)

        self.assertEqual(len(cube.get_faces()), 0)

    def test_get_face(self):
            
        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_matching_figure(fig1)
        cube.add_face(face)

        self.assertEqual(cube.get_face(0), face)

    def test_get_faces(self):
                    
        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_matching_figure(fig1)
        cube.add_face(face)

        self.assertEqual(cube.get_faces(), [face])

    def test_fits(self):
                
        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_matching_figure(fig1)
        cube.add_face(face)

        self.assertTrue(cube.fits(fig1, 0))

    # def test_cube_turn_left_default(self):
    #     """ Turn left with one steps"""

    #     f1 = Face.create("figure1")
    #     f2 = Face.create("figure2")
    #     f3 = Face.create("figure3")
    #     f4 = Face.create("figure4")

    #     cube = Cube()
    #     cube.add_face(f1)
    #     cube.add_face(f2)
    #     cube.add_face(f3)
    #     cube.add_face(f4)

    #     fig1 = f1.get_figures()
    #     fig2 = f1.get_figures()
    #     fig3 = f1.get_figures()
    #     fig4 = f1.get_figures()

    #     figures = fig1 + fig2 + fig3 + fig4

    #     game = Game(cube, figures)

    #     game.turn_left()

    #     self.assertEqual(game.get_current_face(), f4)

    #     game.turn_left()

    #     self.assertEqual(game.get_current_face(), f3)

    #     game.turn_left()
    #     game.turn_left()
    #     game.turn_left()

    #     self.assertEqual(game.get_current_face(), f4)

    # def test_cube_turn_right_default(self):
    #     """ Turn left with one steps"""

    #     f1 = Face.create("figure1")
    #     f2 = Face.create("figure2")
    #     f3 = Face.create("figure3")
    #     f4 = Face.create("figure4")

    #     cube = Cube()
    #     cube.add_face(f1)
    #     cube.add_face(f2)
    #     cube.add_face(f3)
    #     cube.add_face(f4)

    #     fig1 = f1.get_figures()
    #     fig2 = f1.get_figures()
    #     fig3 = f1.get_figures()
    #     fig4 = f1.get_figures()

    #     figures = fig1 + fig2 + fig3 + fig4

    #     game = Game(cube, figures)

    #     self.assertEqual(game.get_current_face(), f1)

    #     game.turn_right()
    #     game.turn_right()
    #     game.turn_right()
    #     game.turn_right()
    #     game.turn_right()

    #     self.assertEqual(game.get_current_face(), f4)

    # def test_turn_left_steps(self):
    #     """ Turn left with more steps"""

    #     f1 = Face.create("figure1")
    #     f2 = Face.create("figure2")
    #     f3 = Face.create("figure3")
    #     f4 = Face.create("figure4")

    #     cube = Cube()
    #     cube.add_face(f1)
    #     cube.add_face(f2)
    #     cube.add_face(f3)
    #     cube.add_face(f4)

    #     fig1 = f1.get_figures()
    #     fig2 = f1.get_figures()
    #     fig3 = f1.get_figures()
    #     fig4 = f1.get_figures()

    #     figures = fig1 + fig2 + fig3 + fig4

    #     game = Game(cube, figures)

    #     self.assertEqual(game.get_current_face(), f1)

    #     game.turn_left(5)

    #     self.assertEqual(game.get_current_face(), f4)

    #     game.turn_left(2)

    #     self.assertEqual(game.get_current_face(), f2)

    # def test_turn_right_steps(self):
    #     """ Turn left with more steps"""

    #     f1 = Face.create("figure1")
    #     f2 = Face.create("figure2")
    #     f3 = Face.create("figure3")
    #     f4 = Face.create("figure4")

    #     cube = Cube()
    #     cube.add_face(f1)
    #     cube.add_face(f2)
    #     cube.add_face(f3)
    #     cube.add_face(f4)

    #     fig1 = f1.get_figures()
    #     fig2 = f1.get_figures()
    #     fig3 = f1.get_figures()
    #     fig4 = f1.get_figures()

    #     figures = fig1 + fig2 + fig3 + fig4

    #     game = Game(cube, figures)

    #     self.assertEqual(game.get_current_face(), f1)

    #     game.turn_right(5)

    #     self.assertEqual(game.get_current_face(), f2)

    #     game.turn_right(2)

    #     self.assertEqual(game.get_current_face(), f4)

    # def test_cube_fits(self):

    #     cube = Cube()

    #     fig1 = Figure("figure1")
    #     face = Face()
    #     face.add_available_figure(fig1)
    #     cube.add_face(face)

    #     self.assertTrue(face.fits(fig1))
    #     self.assertFalse(face.fits(Figure("figureFalse")))


if __name__ == '__main__':
    unittest.main()
