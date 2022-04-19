
class Cube():

    def __init__(self):

        self.faces = []
        self.front_face = 0

    def add_face(self, face):
        self.faces.append(face)

    def get_current_face(self):
        return self.faces[self.front_face]

    def turn_left(self, steps=1):

        if (self.front_face - steps) < 0:
            self.front_face = len(self.faces)
        else:
            self.front_face -= steps

    def turn_right(self, steps=1):

        if self.front_face >= len(self.faces) - steps:
            self.front_face = 0
        else:
            self.front_face += 1

    def fits(self, figure):
        return self.faces[self.front_face].fits(figure)


    def __repr__(self):
        return "front %s faces: %s" % (self.front_face, self.faces)