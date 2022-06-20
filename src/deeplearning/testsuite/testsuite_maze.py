import json
from pathlib import Path

from deeplearning.games.labyrinth import EnvLabyrinth, LabyrinthGame
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter, PlotWriter
from deeplearning.testsuite.testsuite_base import TestSuiteBase


class TestSuiteMaze(TestSuiteBase):

    def __init__(self, name, agent, train_epoches, number_of_plays, batch_size):
        super().__init__(name, agent, train_epoches, number_of_plays, batch_size)

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
        agent = TestSuiteMaze._create_agent(agent_conf, EnvLabyrinth(game))

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

        return TestSuiteMaze(testsuite_name, agent, train_epoches, number_of_plays, batch_size=batch_size)


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

test = TestSuiteMaze.from_dict(sample_suite)
test.run()
