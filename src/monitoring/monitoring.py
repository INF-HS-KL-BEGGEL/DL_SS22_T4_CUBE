from abc import ABC, abstractmethod
from IPython.display import clear_output
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Writer(ABC):

    @abstractmethod
    def write(self, item):
        pass


class PlotWriter(Writer):

    def __init__(self, name=""):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(name)
        self.x = []
        self.y = []

    def set_label(self, x_label, y_label):
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)

    def show(self):
        self.fig.show()

    def write(self, item: tuple):
        x, y = item
        self.x.append(x)
        self.y.append(y)

        self.ax.plot(self.x, self.y, 'bo-')
        clear_output(wait=True)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
