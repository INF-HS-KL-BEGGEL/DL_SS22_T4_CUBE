import json
from deeplearning.agent.agent_qnetwork import QNetworkAgent
from deeplearning.agent.agent_qnetwork_optimized import QNetworkAgentOptimizd
from deeplearning.agent.agent_qtable import QTableAgent
from deeplearning.games.labyrinth.env_labyrinth import EnvLabyrinth
from deeplearning.games.labyrinth.labyrinth_game import LabyrinthGame
from tensorflow.keras.optimizers import Adam
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter, PlotWriter
from pathlib import Path


class TestSuiteMaze:

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
    def from_json_file(filename):
        json_data = json.load(open(filename, "r"))
        return TestSuiteMaze.from_dict(json_data)

    @staticmethod
    def __create_maze(maze_conf: dict):
        height = maze_conf.get("height")
        width = maze_conf.get("width")
        targets = maze_conf.get("targets")
        seed = maze_conf.get("seed")
        return LabyrinthGame.setup_game(height, width, targets, seed=seed)

    def __create_agent(agent_conf: dict, game):
        agent_type = agent_conf.get("type")

        learning_rate = agent_conf.get("learning_rate")
        timesteps_per_epoches = agent_conf.get("timesteps_per_epoches")
        gamma = agent_conf.get("gamma")
        epsilon = agent_conf.get("epsilon")

        if agent_type == "QNetworkAgentOptimizd":
            agent = QNetworkAgentOptimizd(EnvLabyrinth(game),
                              TestSuiteMaze.__get_optimizer(agent_conf.get("optimizer", "Adam"), learning_rate),
                              epsilon=epsilon,
                              gamma=gamma,
                              timesteps_per_episode=timesteps_per_epoches)

        elif agent_type == "QTable":
            agent = QTableAgent(EnvLabyrinth(game),
                              epsilon=epsilon,
                              gamma=gamma,
                              alpha=learning_rate)
        else:
            agent = QNetworkAgent(EnvLabyrinth(game),
                              TestSuiteMaze.__get_optimizer(agent_conf.get("optimizer", "Adam"), learning_rate),
                              epsilon=epsilon,
                              gamma=gamma,
                              timesteps_per_episode=timesteps_per_epoches)

        return agent

    @staticmethod
    def __get_optimizer(name, learning_rate):
        opimizers = {
            "Adam": Adam(learning_rate=learning_rate),
        }
        return  opimizers[name]

    @staticmethod
    def from_dict(config):
        testsuite_name = config.get("testsuite_name")
        result_path = config.get("result_path")
        Path(result_path).mkdir(parents=True, exist_ok=True)

        agent_conf = config.get("agent")
        game_conf = config.get("maze")
        play_conf = config.get("play")
        number_of_plays = play_conf.get("number_of_plays", 1)

        batch_size = agent_conf.get("batch_size", 1000)
        train_epoches = agent_conf.get("train_epoches")

        game = TestSuiteMaze.__create_maze(game_conf)
        agent = TestSuiteMaze.__create_agent(agent_conf, game)

        csv_train_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_training.csv")
        csv_train_writer.set_label("Epoches", "Reward")
        csv_play_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_play.csv")
        csv_play_writer.set_label("Index", "Reward")

        #plot_train_writer = PlotWriter(name=testsuite_name + "Plot")
        #plot_train_writer.set_label("Epoche", "Reward")
        #agent.register_writer_training(plot_train_writer)

        agent.register_writer_training(csv_train_writer)
        agent.register_writer_play(csv_play_writer)
        agent.register_writer_training(ConsoleWriter("Console Training"))

        return TestSuiteMaze(testsuite_name, agent, train_epoches, number_of_plays, batch_size=batch_size)

### Sample Config ###

sample_suite = {
    "result_path": "./var/results/",
    "testsuite_name": "test",
    "agent": {
        "type": "QNetworkAgentOptimizd", # QNetworkAgent, QTable
        "learning_rate": 0.05,
        "train_epoches": 10,
        "timesteps_per_epoches": 100,
        "gamma": 0.9,
        "epsilon": 0.2,
        "batch_size": 100,
        "optimizer": "Adam"
    },
    "play": {
        "number_of_plays": 1  # Number of Plays after every train round
    },
    "maze": {
        "height": 4,
        "width": 4,
        "targets": 2,
        "seed": 10
    }
}

test = TestSuiteMaze.from_dict(sample_suite)
test.run()
