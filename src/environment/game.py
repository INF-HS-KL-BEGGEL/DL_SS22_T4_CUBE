from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure


class Game:

    def __init__(self, cube: Cube, figures: list):
        """Initializes the game with the given cube and figures"""
        self.cube = cube
        self.current_face = 0
        self.faces = cube.get_faces()
        self.figures = figures

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

    def try_fit(self, figure):
        """Try to fit the given figure on the current face"""
        return self.cube.fits(figure, self.current_face)

    def get_current_face(self):
        """Returns the current face"""
        return self.cube.get_faces()[self.current_face]

    def get_cube(self):
        return self.cube

    def reset_game(self):
        """Resets the game"""
        self.current_face = 0

    def print_game(self):
        """Prints the game"""
        print("Figures: %s" % self.figures)
        print("Current face: %s" % self.get_current_face())
        print("Cube: %s" % self.get_cube())



    @staticmethod
    def setup_game_random():
        """Creates a random game"""
        cube = Cube()

        fig1 = Figure("figure1")
        fig2 = Figure("figure2")
        fig3 = Figure("figure3")

        face1 = Face().create("figure1")
        face2 = Face().create("figure2")
        face3 = Face().create("figure3")

        cube.add_face(face1)
        cube.add_face(face2)
        cube.add_face(face3)

        figures = [fig1, fig2, fig3]

        return Game(cube, figures)
