from environment.cube import Cube
from environment.face import Face

class Game():

    def __init__(self, cube: Cube, figures: list):

        self.cube = cube
        self.front_face = 0
        self.figures = figures

    def turn_left(self, steps=1):

        if (self.front_face - steps) < 0:
            self.front_face = len(self.cube.get_faces())
        else:
            self.front_face -= steps

    def turn_right(self, steps=1):

        if self.front_face >= len(self.cube.get_faces()) - steps:
            self.front_face = 0
        else:
            self.front_face += 1

    def try_fit(self, figure):
        """
        Versuch ob übergebene figur PASST
        :return:
        """
        return self.cube.fits(figure, self.front_face)

    def get_current_face(self):
        return self.cube.get_faces()[self.front_face]

    def reset_game(self):
        """
        Spiel auf Anfang zurücksetzen
        :return:
        """


    @staticmethod
    def setupGameRandom():
        cube = Cube()
        cube.add_face(Face.create("figure1"))
        cube.add_face(Face.create("figure2"))
        cube.add_face(Face.create("figure3"))

        figures = []

        return Game(cube, figures)