import json
from pathlib import Path
from tensorflow.keras.optimizers import Adam

from deeplearning.games.cube import EnvCube, CubeGame
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter, PlotWriter
from deeplearning.testsuite.testsuite_base import TestSuiteBase


class TestSuiteCube(TestSuiteBase):

    def __init__(self, name, agent, train_epoches, number_of_plays, batch_size):
        super().__init__(name, agent, train_epoches, number_of_plays, batch_size)

    @staticmethod
    def from_json_file(filename):
        json_data = json.load(open(filename, "r"))
        return TestSuiteCube.from_dict(json_data)

    @staticmethod
    def __create_cube(cube_conf: dict):
        facesize = cube_conf.get("facesize", 6)
        return CubeGame.setup_game(facesize)

    @staticmethod
    def __get_optimizer(name, learning_rate):
        opimizers = {
            "Adam": Adam(learning_rate=learning_rate),
        }
        return opimizers[name]

    @staticmethod
    def from_dict(config):
        testsuite_name = config.get("testsuite_name")
        result_path = config.get("result_path")
        Path(result_path).mkdir(parents=True, exist_ok=True)

        game_conf = config.get("maze")
        agent_conf = config.get("agent")
        play_conf = config.get("play")
        number_of_plays = play_conf.get("number_of_plays", 1)

        batch_size = agent_conf.get("batch_size", 1000)
        train_epoches = agent_conf.get("train_epoches")

        game = TestSuiteCube.__create_cube(game_conf)
        agent = TestSuiteCube.__create_agent(agent_conf, EnvCube(game))

        csv_train_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_training.csv")
        csv_train_writer.set_label("Epoches", "Reward")
        csv_play_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_play.csv")
        csv_play_writer.set_label("Index", "Reward")

        # plot_train_writer = PlotWriter(name=testsuite_name + "Plot")
        # plot_train_writer.set_label("Epoche", "Reward")
        # agent.register_writer_training(plot_train_writer)

        agent.register_writer_training(csv_train_writer)
        agent.register_writer_play(csv_play_writer)
        agent.register_writer_training(ConsoleWriter("Console Training"))

        return TestSuiteCube(testsuite_name, agent, train_epoches, number_of_plays, batch_size=batch_size)


### Sample Config ###

sample_suite = {
    "result_path": "./var/results/",
    "testsuite_name": "test",
    "agent": {
        "type": "QNetworkAgentOptimizd",  # QNetworkAgent, QTable
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

test = TestSuiteCube.from_dict(sample_suite)
test.run()
