from deeplearning.environment.action import Action
from deeplearning.games.labyrinth.labyrinth import TileType


class GoAction(Action):
    """Class representing the action to move the agent in a given direction"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        result_tile = self.game.go(self.direction)
        if not result_tile or result_tile.get_type() == TileType.BLOCKED:
            return -5
        elif result_tile.get_type() == TileType.START:
            return -1
        elif result_tile.get_type() == TileType.EMPTY:
            return -1
        elif result_tile.get_type() == TileType.TARGET:
            return 100


class MoveForwardAction(Action):
    """Class representing the action to move the agent in a given direction"""

    def __init__(self, id, game):
        super().__init__(id, game)

    def execute(self) -> int:
        result = self.game.move_forward()
        if result == TileType.BLOCKED:
            return -1
        elif result == TileType.EMPTY:
            return 0
        elif result == TileType.TARGET:
            return 50


class ChangeDirectionAction(Action):
    """Class representing the action to move the agent in a given direction"""

    def __init__(self, id, game, direction):
        super().__init__(id, game)
        self.direction = direction

    def execute(self) -> int:
        self.game.set_current_direction(self.direction)
        return -2
