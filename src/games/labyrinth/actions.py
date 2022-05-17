from environment.action import Action


class GoAction(Action):
    """Class representing the action to move the agent in a given direction"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        result = self.game.go(self.direction)
        if result == -1:
            return -5
        elif result == 0:
            return -1
        elif result == 1:
            return 50
