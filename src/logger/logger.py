from abc import ABC, abstractmethod
from IPython.display import clear_output
import matplotlib.pyplot as plt


class Writer(ABC):

    @abstractmethod
    def write(self, item):
        pass


class PlotWriter(Writer):

    def __init__(self):

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.x = []
        self.y = []
        self.fig.show()

    def write(self, item: tuple):
        x, y = item
        self.x.append(x)
        self.y.append(y)

        self.ax.plot(self.x, self.y , 'bo')
        clear_output(wait=True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()