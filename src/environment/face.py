from environment.figure import Figure

class Face():

    def __init__(self):
        self.matching_figures = []

    def add_available_figure(self, figure):
        self.matching_figures.append(figure)

    def get_figures(self):
        return self.matching_figures

    def fits(self, figure):

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

        face = Face()
        face.add_available_figure(Figure(figure_name))
        return face