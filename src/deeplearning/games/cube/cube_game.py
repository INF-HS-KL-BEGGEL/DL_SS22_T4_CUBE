import random

from deeplearning.games.cube.cube import Cube
from deeplearning.games.cube.face import Face
from deeplearning.games.cube.figure import Direction, Figure
from deeplearning.games.game import Game


class CubeGame(Game):

    def __init__(self, cube: Cube, figures: list):
        """Initializes the game with the given cube and figures"""
        super().__init__()
        self.cube = cube
        self.current_face = 0
        self.faces = cube.get_faces()
        self.figure_stack = figures

        self.figure_stack_copy = figures.copy()

    def turn_left(self, steps=1):
        """Turns the cube left by the given number of steps, default is 1"""
        length = len(self.cube.get_faces())
        if (self.current_face - steps) < 0:
            while steps > 0:
                if self.current_face == 0:
                    self.current_face = length - 1
                else:
                    self.current_face -= 1
                steps -= 1
        else:
            self.current_face -= steps

    def turn_right(self, steps=1):
        """Turns the cube right by the given number of steps, default is 1"""
        length = len(self.cube.get_faces())
        if (self.current_face + steps) >= (length - steps):
            while steps > 0:
                if self.current_face == (length - 1):
                    self.current_face = 0
                else:
                    self.current_face += 1
                steps -= 1
        else:
            self.current_face += steps

    def try_fit(self):
        """Try to fit the given figure on the current face"""
        if len(self.figure_stack) == 0:
            return False

        figure = self.figure_stack[-1]
        fits = self.cube.fits(figure, self.current_face)
        if fits:
            self.figure_stack.pop()
        return fits

    def rotate_figure(self):
        """Rotates the given figure"""
        self.get_top_of_figure_stack().rotate()

    def get_current_face(self):
        """Returns the current face"""
        return self.cube.get_faces()[self.current_face]

    def get_current_face_index(self):
        """Returns the current face index"""
        return self.current_face

    def get_figure_stack(self):
        return self.figure_stack

    def get_top_of_figure_stack(self):
        if len(self.figure_stack) == 0:
            return None

        return self.figure_stack[-1]

    def get_cube(self):
        return self.cube

    def reset_game(self):
        """Resets the game"""
        self.figure_stack = self.figure_stack_copy.copy()
        random.shuffle(self.figure_stack)
        self.current_face = random.randint(0, len(self.faces) - 1)

    def is_done(self):
        return len(self.figure_stack) == 0

    def print_game(self):
        """Prints the game"""
        print("Figures: %s" % self.figure_stack)
        print("Current face: %s" % self.get_current_face())
        print("Cube: %s" % self.get_cube())

    @staticmethod
    def setup_game(n=6):
        """Creates a game"""

        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        figures = []
        cube = Cube()
        for i in range(n):
            fig = Figure("figure" + str(i), random.choice(directions))
            face = Figure("figure" + str(i), random.choice(directions))
            figures.append(fig)
            cube.add_face(Face.create(face))

        return CubeGame(cube, figures)
