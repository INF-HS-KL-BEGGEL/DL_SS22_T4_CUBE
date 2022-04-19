from environment.figure import Figure

class Face():

    def __init__(self):
        self.figures = []

    def add_available_figure(self, figure):
        self.figures.append(figure)

    def fits(self, figure):

        if figure in self.figures:
            return True

        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        for f in self.figures:
            for o in other.figures:
                if not f == o:
                    return False
        return True

    def __repr__(self):
        return str(self.figures)

    @staticmethod
    def create(figure_name):

        face = Face()
        face.add_available_figure(Figure(figure_name))
        return face