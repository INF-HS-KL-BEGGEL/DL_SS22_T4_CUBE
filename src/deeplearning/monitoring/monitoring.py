import time
from abc import ABC, abstractmethod

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

class Writer(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def write(self, item):
        pass

    def get_name(self):
        return self.name


class PlotWriter(Writer):

    def __init__(self, name="", plot_information="", should_render=False):
        super().__init__(name)
        self.name = name
        self.should_render = should_render

        self.fig = plt.figure()
        self.fig.canvas.set_window_title(name)

        self.ax = self.fig.add_subplot(111)
        self.ax.grid(axis='y')
        self.ax.set_title(plot_information + '\n' + name,  loc='center')

        self.x = []
        self.y = []
        self.showed = False

        self.ax.set_xlabel("Epoch")
        self.ax.set_ylabel("Reward")

    def set_label(self, x_label, y_label):
        """
        Change the Axis Label
        :param x_label: Label of the x-axis
        :param y_label: Label of the y-axis
        :return:
        """
        self.ax.set_xlabel(x_label)
        self.ax.set_ylabel(y_label)

    def save(self, path=""):
        self.fig.savefig(path + self.name + "@" + str(time.time()) + '.png')

    def set_title(self, title):
        self.ax.set_title(self.name + '\n' + title,  loc='center')

    def show(self):
        if self.should_render:
            self.fig.show()

    def write(self, item: tuple):
        x, y = item
        self.x.append(x)
        self.y.append(y)

        self.ax.plot(self.x, self.y, 'bo-')

        if not self.showed:
            self.showed = True
            self.show()

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()


class CsvWriter(Writer):

    def __init__(self, name, filename=""):
        super().__init__(name)
        self.filename = filename
        self.file = open(self.filename, "w")
        self.delimiter = ";"

    def set_label(self, x_label, y_label):
        self.file.write("%s%s%s\n" % (x_label, self.delimiter ,y_label))

    def write(self, item: tuple):
        x, y = item
        self.file.write("%s%s%s\n" % (x, self.delimiter, y))
        self.file.flush()

    def __del__(self):
        self.file.close()


class ConsoleWriter(Writer):

    def __init__(self, name):
        super().__init__(name)
        self.label = ("x", "y")

    def set_label(self, x_label, y_label):
        self.label = (x_label, y_label)

    def write(self, item: tuple):
        x, y = item
        print("%s: %s, %s: %s" % (self.label[0], x, self.label[1], y))
