
class Cube:
    """The Cube on which the game will be played"""

    def __init__(self):
        """Initializes the Cube with no faces"""
        self.faces = []

    def add_face(self, face):
        """Adds a face to the cube"""
        self.faces.append(face)

    def remove_face(self, pos):
        """Removes the face at the given position"""
        del self.faces[pos]

    def get_faces(self):
        """Returns the faces of the cube"""
        return self.faces

    def get_face(self, pos):
        """Returns the face at the given position"""
        return self.faces[pos]

    def fits(self, figure, pos):
        """Returns True if the figure fits on the face at the given position"""
        return self.faces[pos].fits(figure)

    def __repr__(self):
        """Returns a string representation of the cube"""
        return " faces: %s" % self.faces
