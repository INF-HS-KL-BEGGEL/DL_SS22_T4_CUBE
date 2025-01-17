from deeplearning.environment.action import Action


class TurnLeftAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, id, game, step=1):
        super().__init__(id, game)
        self.step = step

    def execute(self) -> int:
        self.game.turn_left(self.step)
        # return -len(self.game.faces)
        return -1


class TurnRightAction(Action):
    """Class representing the action to turn the cube right"""

    def __init__(self, id, game, step):
        super().__init__(id, game)
        self.step = step

    def execute(self):
        self.game.turn_right(self.step)
        # return -len(self.game.faces)
        return -1


class TryFitAction(Action):
    """
    Class representing the action to try
    to fit a figure on the current face
    """

    def __init__(self, id, game):
        super().__init__(id, game)

    def execute(self):
        """
        :return: reward
        """
        fits = self.game.try_fit()
        if fits:
            # Square the length as reward plus give back negative reward from turn action
            # np.power(len(self.game.faces), 2) + len(self.game.faces)
            return 20
        # return -len(self.game.faces)
        return -2


class RotateFigureAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, id, game):
        super().__init__(id, game)

    def execute(self) -> int:
        self.game.rotate_figure()

        # return -len(self.game.faces)
        return -1
