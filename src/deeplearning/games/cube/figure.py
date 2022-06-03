from enum import Enum


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class Figure:
    """Class representing the figures that can be used in the game"""

    def __init__(self, name, direction: Direction):
        """
        Initializes the figure with the given name
            :param name: The name of the figure
        """
        self.name = name
        self.direction = direction
        self.points = [(), (), ()]

    def get_name(self):
        """Returns the name of the figure"""
        return self.name

    def rotate(self):
        """Rotates the figure"""
        directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
        current_index = directions.index(self.direction)
        if (current_index + 1) == len(directions):
            self.direction = directions[0]
        else:
            self.direction = directions[current_index + 1]

    def __eq__(self, other) -> bool:
        return self.name == other.name and self.direction == other.direction

    def __ne__(self, other) -> bool:
        return self.name != other.name or self.direction != other.direction

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
