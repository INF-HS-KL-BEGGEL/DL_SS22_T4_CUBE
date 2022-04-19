

class Figure():

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __ne__(self, other) -> bool:
        return self.name != other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)