from abc import ABC, abstractmethod
from tensorflow.keras.optimizers import Adam
from deeplearning.agent import QNetworkAgent, QTableAgent, QNetworkAgentOptimizd


class TestSuiteBase(ABC):

    def __init__(self, name, agent, train_epoches, number_of_plays, batch_size):
        self.agent = agent
        self.train_epoches = train_epoches
        self.number_of_plays = number_of_plays  # Number of Plays after every train round
        self.batch_size = batch_size
        self.name = name

    def run(self):
        for i in range(self.number_of_plays):
            self.agent.train(self.train_epoches, self.batch_size)
            self.agent.play(i)

    def get_name(self):
        return self.name


    @staticmethod
    def _get_optimizer(name, learning_rate):
        opimizers = {
            "Adam": Adam(learning_rate=learning_rate),
        }
        return opimizers[name]

    @staticmethod
    def _create_agent(agent_conf: dict, env_game):
        agent_type = agent_conf.get("type")

        learning_rate = agent_conf.get("learning_rate")
        timesteps_per_epoches = agent_conf.get("timesteps_per_epoches")
        gamma = agent_conf.get("gamma")
        epsilon = agent_conf.get("epsilon")

        if agent_type == "QNetworkAgentOptimizd":
            optimizer = TestSuiteBase._get_optimizer(agent_conf.get("optimizer", "Adam"), learning_rate)
            agent = QNetworkAgentOptimizd(env_game,
                                          optimizer,
                                          epsilon=epsilon,
                                          gamma=gamma,
                                          timesteps_per_episode=timesteps_per_epoches)

        elif agent_type == "QTable":
            agent = QTableAgent(env_game, epsilon=epsilon, gamma=gamma, alpha=learning_rate)
        else:
            optimizer = TestSuiteBase._get_optimizer(agent_conf.get("optimizer", "Adam"))
            agent = QNetworkAgent(env_game,
                                  optimizer,
                                  epsilon=epsilon,
                                  gamma=gamma,
                                  timesteps_per_episode=timesteps_per_epoches)

        return agent

