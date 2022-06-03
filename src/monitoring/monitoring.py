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

    def __init__(self, name=""):
        super().__init__(name)

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_title(name)
        self.x = []
        self.y = []
        self.show()

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
        #clear_output(wait=True)
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
