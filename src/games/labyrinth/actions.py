from environment.action import Action


class GoAction(Action):
    """Class representing the action to move the agent in a given direction"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        if self.game.go(self.direction) == 1:
            return 50
        if self.game.go(self.direction) == 0:
            return -1
        return -5
