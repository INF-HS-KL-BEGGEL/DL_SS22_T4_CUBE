from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure


class Game:

    def __init__(self, cube: Cube, figures: list):
        """Initializes the game with the given cube and figures"""
        self.cube = cube
        self.current_face = 0
        self.faces = cube.get_faces()
        self.figure_stack = figures

        self.figure_stack_copy = figures.copy()

    def turn_left(self, steps=1):
        """Turns the cube left by the given number of steps, default is 1"""
        if (self.current_face - steps) < 0:
            self.current_face = len(self.cube.get_faces()) - 1
        else:
            self.current_face -= steps

    def turn_right(self, steps=1):
        """Turns the cube right by the given number of steps, default is 1"""
        if (self.current_face + 1) >= len(self.cube.get_faces()) - steps:
            self.reset_game()
        else:
            self.current_face += 1

    def try_fit(self):
        """Try to fit the given figure on the current face"""
        if len(self.figure_stack) == 0:
            return False

        figure = self.figure_stack[-1]
        fits = self.cube.fits(figure, self.current_face)
        if fits:
            self.figure_stack.pop()
        return fits

    def get_current_face(self):
        """Returns the current face"""
        return self.cube.get_faces()[self.current_face]

    def get_current_face_index(self):
        """Returns the current face index"""
        return self.current_face

    def get_figure_stack(self):
        return self.figure_stack

    def get_top_of_figure_stack(self):
        """
        :return:
        """

        return self.figure_stack[-1]

    def get_cube(self):
        return self.cube

    def reset_game(self):
        """Resets the game"""
        self.figure_stack = self.figure_stack_copy.copy()
        self.current_face = 0

    def is_done(self):
        return len(self.figure_stack) == 0

    def print_game(self):
        """Prints the game"""
        print("Figures: %s" % self.figure_stack)
        print("Current face: %s" % self.get_current_face())
        print("Cube: %s" % self.get_cube())


    @staticmethod
    def setup_game():
        """Creates a random game"""
        cube = Cube()

        fig1 = Figure("figure1")
        fig2 = Figure("figure2")
        fig3 = Figure("figure3")
        fig4 = Figure("figure4")

        face1 = Face.create("figure1")
        face2 = Face.create("figure2")
        face3 = Face.create("figure3")
        face4 = Face.create("figure4")

        cube.add_face(face1)
        cube.add_face(face2)
        cube.add_face(face3)
        cube.add_face(face4)

        figures = [fig1, fig2, fig3, fig4]

        return Game(cube, figures)
