class StateBase:

    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def __hash__(self) -> int:
        return super().__hash__()

    def __eq__(self, other):
        return self.number == other.number

    def __ne__(self, other):
        print("ACHTUNG HIER WURDE __ne__ aufgerufen")
        return not self == other
