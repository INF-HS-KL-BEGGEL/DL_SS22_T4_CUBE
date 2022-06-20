from abc import ABC, abstractmethod
from tensorflow.keras.optimizers import Adam
from deeplearning.agent import QNetworkAgent, QTableAgent, QNetworkAgentOptimizd


class TestSuiteBase(ABC):

    def __init__(self, name, agent, train_epochs, number_of_plays, plot_names, batch_size):
        self.agent = agent
        self.train_epochs = train_epochs
        self.number_of_plays = number_of_plays  # Number of Plays after every train round
        self.batch_size = batch_size
        self.name = name
        self.plot_names = plot_names  # array of plot names

    def run(self):
        for i in range(self.number_of_plays):
            # QNetwork Agent
            if self.batch_size is not None:
                self.agent.train(self.train_epochs, self.batch_size)
            # QTable Agent
            else:
                self.agent.train(self.train_epochs)
            self.agent.play(i)
        # If we have registered plots, save them
        if len(self.plot_names) > 0:
            self.agent.save_plots(self.plot_names)

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
        timesteps_per_episode = agent_conf.get("timesteps_per_episode")
        gamma = agent_conf.get("gamma")
        epsilon = agent_conf.get("epsilon")

        if agent_type == "QNetworkAgentOptimizd":
            optimizer = TestSuiteBase._get_optimizer(agent_conf.get("optimizer", "Adam"), learning_rate)
            agent = QNetworkAgentOptimizd(env_game,
                                          optimizer,
                                          epsilon=epsilon,
                                          gamma=gamma,
                                          timesteps_per_episode=timesteps_per_episode)

        elif agent_type == "QTable":
            agent = QTableAgent(env_game, epsilon=epsilon, gamma=gamma, alpha=learning_rate)
        else:
            optimizer = TestSuiteBase._get_optimizer(agent_conf.get("optimizer", "Adam"), learning_rate)
            agent = QNetworkAgent(env_game,
                                  optimizer,
                                  epsilon=epsilon,
                                  gamma=gamma,
                                  timesteps_per_episode=timesteps_per_episode)

        return agent
