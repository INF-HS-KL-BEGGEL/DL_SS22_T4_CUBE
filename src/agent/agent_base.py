from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, environment):

        self.environment = environment


    @abstractmethod
    def train(self, batch_size):
        pass