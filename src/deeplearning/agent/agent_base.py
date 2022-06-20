from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, environment):
        self.environment = environment
        self.writer_training = {}
        self.writer_play = {}

    @abstractmethod
    def train(self, num_of_episodes, batch_size=1):
        pass

    @abstractmethod
    def play(self, index):
        pass

    def register_writer_training(self, writer):
        if self.writer_training.get(writer.get_name()):
            raise Exception("Writer %s schon vorhanden" % writer.get_name())
        self.writer_training[writer.get_name()] = writer

    def register_writer_play(self, writer):
        if self.writer_play.get(writer.get_name()):
            raise Exception("Writer %s schon vorhanden" % writer.get_name())
        self.writer_play[writer.get_name()] = writer

    def get_writer_play(self, name):
        return self.writer_play[name]

    def get_writer_training(self, name):
        return self.writer_training[name]

    def notify_writer_training(self, item, name=None):

        if not name:
            for w in self.writer_training.values():
                w.write(item)
        else:
            self.writer_training[name].write(item)

    def notify_writer_play(self, item, name=None):
        if not name:
            for w in self.writer_play.values():
                w.write(item)
        else:
            self.writer_play[name].write(item)