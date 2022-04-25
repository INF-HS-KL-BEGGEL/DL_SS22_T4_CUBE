
class Cube():

    def __init__(self):

        self.faces = []

    def add_face(self, face):
        self.faces.append(face)

    def get_faces(self):
        return self.faces

    def get_face(self, pos):
        return self.faces[pos]

    def fits(self, figure, pos):
        return self.faces[pos].fits(figure)

    def __repr__(self):
        return " faces: %s" % (self.faces)