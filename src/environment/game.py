from environment.cube import Cube
from environment.face import Face
from environment.figure import Figure

class Game:

    def __init__(self, cube: Cube, figures: list):
        """Initializes the game with the given cube and figures"""
        self.cube = cube
        self.front_face = 0
        self.figures = figures

    def turn_left(self, steps=1):
        """Turns the cube left by the given number of steps, default is 1"""
        if (self.front_face - steps) < 0:
            self.front_face = len(self.cube.get_faces())
        else:
            self.front_face -= steps

    def turn_right(self, steps=1):
        """Turns the cube right by the given number of steps, default is 1"""
        if self.front_face >= len(self.cube.get_faces()) - steps:
            self.front_face = 0
        else:
            self.front_face += 1

    def try_fit(self, figure):
        """Try to fit the given figure on the current face"""
        return self.cube.fits(figure, self.front_face)

    def get_current_face(self):
        """Returns the current face"""
        return self.cube.get_faces()[self.front_face]

    def get_cube(self):
        return self.cube

    def reset_game(self):
        """Resets the game"""
        self.front_face = 0

    @staticmethod
    def setup_game_random():
        """Creates a random game"""
        cube = Cube()

        fig1 = Figure("figure1")
        fig2 = Figure("figure2")
        fig3 = Figure("figure3")

        cube.add_face(fig1)
        cube.add_face(fig2)
        cube.add_face(fig3)

        figures = [fig1, fig2, fig3]

        return Game(cube, figures)
