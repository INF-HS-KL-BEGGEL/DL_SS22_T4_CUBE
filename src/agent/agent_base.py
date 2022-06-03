from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, environment):
        self.environment = environment
        self.writer_training = {}
        self.writer_play = {}

    @abstractmethod
    def train(self, batch_size):
        pass

    def register_writer_training(self, writer):
        self.writer_training[writer.get_name()] = writer

    def register_writer_play(self, writer):
        self.writer_play[writer.get_name()] = writer

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