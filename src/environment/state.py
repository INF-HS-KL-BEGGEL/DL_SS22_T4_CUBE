

class State:

    def __init__(self, number):
        self.number = number

        # Aktion die zu dem State gefuehrt hat
        # Aktuelle Position des Wuerfels
        # Figuren, die der Agent noch in den Wuerfel machen moechte
        # Eventuell Bepunktung? Oder gehoert die wo anders hin

    def get_prev(self):
        return self.prev

    def __hash__(self):
        return self.number

    def __eq__(self, other):
        return self.number

    def __ne__(self, other):
        return not self.number == other