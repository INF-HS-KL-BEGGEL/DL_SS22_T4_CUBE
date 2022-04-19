import unittest
from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure

class TestCube(unittest.TestCase):

    def test_cube_turn_left_default(self):
        """ Turn left with one steps"""

        cube = Cube()

        f1 = Face.create("figure1")
        f2 = Face.create("figure2")
        f3 = Face.create("figure3")
        f4 = Face.create("figure4")

        cube.add_face(f1)
        cube.add_face(f2)
        cube.add_face(f3)
        cube.add_face(f4)

        cube.turn_left()

        self.assertEqual(cube.get_current_face(), f4)

        cube.turn_left()

        self.assertEqual(cube.get_current_face(), f3)

        cube.turn_left()
        cube.turn_left()
        cube.turn_left()

        self.assertEqual(cube.get_current_face(), f4)


    def test_cube_turn_right_default(self):
        """ Turn left with one steps"""

        cube = Cube()

        f1 = Face.create("figure1")
        f2 = Face.create("figure2")
        f3 = Face.create("figure3")
        f4 = Face.create("figure4")

        cube.add_face(f1)
        cube.add_face(f2)
        cube.add_face(f3)
        cube.add_face(f4)

        self.assertEqual(cube.get_current_face(), f1)

        cube.turn_right()
        cube.turn_right()
        cube.turn_right()
        cube.turn_right()
        cube.turn_right()

        self.assertEqual(cube.get_current_face(), f4)


    def test_turn_left_steps(self):
        """ Turn left with more steps"""

        cube = Cube()

        f1 = Face.create("figure1")
        f2 = Face.create("figure2")
        f3 = Face.create("figure3")
        f4 = Face.create("figure4")

        cube.add_face(f1)
        cube.add_face(f2)
        cube.add_face(f3)
        cube.add_face(f4)

        self.assertEqual(cube.get_current_face(), f1)

        cube.turn_left(5)

        self.assertEqual(cube.get_current_face(), f4)

        cube.turn_left(2)

        self.assertEqual(cube.get_current_face(), f2)


    def test_turn_right_steps(self):
        """ Turn left with more steps"""

        cube = Cube()

        f1 = Face.create("figure1")
        f2 = Face.create("figure2")
        f3 = Face.create("figure3")
        f4 = Face.create("figure4")

        cube.add_face(f1)
        cube.add_face(f2)
        cube.add_face(f3)
        cube.add_face(f4)

        self.assertEqual(cube.get_current_face(), f1)

        cube.turn_right(5)

        self.assertEqual(cube.get_current_face(), f2)

        cube.turn_right(2)

        self.assertEqual(cube.get_current_face(), f4)


    def test_cube_fits(self):

        cube = Cube()

        fig1 = Figure("figure1")
        face = Face()
        face.add_available_figure(fig1)
        cube.add_face(face)

        self.assertTrue(face.fits(fig1))
        self.assertFalse(face.fits(Figure("figureFalse")))


if __name__ == '__main__':
    unittest.main()