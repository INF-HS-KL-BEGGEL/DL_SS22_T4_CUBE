from abc import ABC, abstractmethod


class Agent(ABC):

    def __init__(self, environment):

        self.environment = environment


    @abstractmethod
    def retrain(self, batch_size):
        pass