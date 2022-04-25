from environment.figure import Figure


class Face:
    """Class representing a face of the Cube"""

    def __init__(self):
        """Initializes the face with no figures"""
        self.matching_figures = []

    def add_available_figure(self, figure):
        """Adds a figure to the face"""
        self.matching_figures.append(figure)

    def get_figures(self):
        """Returns the figures of the face"""
        return self.matching_figures

    def fits(self, figure):
        """Returns True if the figure fits on the face"""
        if figure in self.matching_figures:
            return True

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        for f in self.matching_figures:
            for o in other.matching_figures:
                if not f == o:
                    return False
        return True

    def __repr__(self):
        return str(self.matching_figures)

    @staticmethod
    def create(figure_name):
        """Creates a face with the given figure"""
        face = Face()
        face.add_available_figure(Figure(figure_name))
        return face
