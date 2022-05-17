from environment.action import Action


class GoAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        return -1


class IsExecutableAction(Action):
    """Class representing the action to turn the cube left"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        return -1
