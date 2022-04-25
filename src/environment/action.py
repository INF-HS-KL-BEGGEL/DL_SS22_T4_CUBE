# Noch keine Idee wie wir Actionen am besten wegabstrahieren können

class Action():

    def __init__(self, name, game):
        self.game = game
        self.name = name

    def execute(self):
        pass


class TurnLeftAction(Action):
    """
        
    """
    def __init__(self, name, game):
        super().__init__(name, game)

    def execute(self):
        self.game.turn_left()


class TurnRightAction(Action):

    def __init__(self, name, game):
        super().__init__(name, game)

    def execute(self):
        self.game.turn_right()


class TryFitAction(Action):

    def __init__(self, name, game, figure):
        super().__init__(name, game)
        self.figure = figure

    def get_figure(self):
        return self.figure

    def execute(self):
        self.game.try_fit(self.figure)