from abc import ABC, abstractmethod

import matplotlib.pyplot as plt


class Writer(ABC):

    @abstractmethod
    def write(self, item):
        pass


class PlotWriter(Writer):

    def __init__(self):

        self.plt = plt.figure()
        self.x = []
        self.y = []
        self.plt.show()

    def write(self, item: tuple):
        x, y = item
        self.x.append(x)
        self.y.append(y)

        plt.subplot()
        plt.plot(self.x, self.y , 'bo')
        plt.redraw()