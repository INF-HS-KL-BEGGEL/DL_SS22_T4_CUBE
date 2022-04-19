# Noch keine Idee wie wir Actionen am besten wegabstrahieren können

class Action():

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class TurnAction(Action):

    def __init__(self, name, figure):
        super().__init__(name)
        self.figure = figure

    def get_figure(self):
        return self.figure


class FigureFitAction(Action):

    def __init__(self, name, figure):
        super().__init__(name)
        self.figure = figure

    def get_figure(self):
        return self.figure
