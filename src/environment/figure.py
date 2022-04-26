

class Figure:
    """Class representing the figures that can be used in the game"""
    def __init__(self, name):
        """
        Initializes the figure with the given name
            :param name: The name of the figure
        """
        self.name = name
        self.points = [(), (), ()]

    def get_name(self):
        """Returns the name of the figure"""
        return self.name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)
