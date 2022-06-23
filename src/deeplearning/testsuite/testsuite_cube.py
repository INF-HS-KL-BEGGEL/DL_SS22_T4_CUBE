import json
from pathlib import Path
from tensorflow.keras.optimizers import Adam

from deeplearning.games.cube import EnvCube, CubeGame
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter, PlotWriter
from deeplearning.testsuite.testsuite_base import TestSuiteBase


class TestSuiteCube(TestSuiteBase):

    def __init__(self, name, agent, train_epochs, number_of_plays, plot_names, batch_size, deactivated):
        super().__init__(name, agent, train_epochs, number_of_plays, plot_names, batch_size, deactivated)

    @staticmethod
    def from_json_file(filename):
        json_data = json.load(open(filename, "r"))
        if json_data.get("cube"):
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
    def get_plot_name(agent_type, game, is_training=True):
        """ Return a readable name for the plot """
        mode = is_training and "Training" or "Playing"
        return "" + str(agent_type) + ", " + str(mode) + ",  Cube with " + str(len(game.get_cube().get_faces())) + " faces"

    @staticmethod
    def from_dict(config):
        testsuite_name = config.get("testsuite_name")
        result_path = config.get("result_path")
        Path(result_path).mkdir(parents=True, exist_ok=True)

        deactivated = config.get("deactivated", False)

        agent_conf = config.get("agent")
        agent_type = agent_conf.get("type")
        game_conf = config.get("cube")
        play_conf = config.get("play")
        number_of_plays = play_conf.get("number_of_plays", 1)

        batch_size = agent_conf.get("batch_size")
        train_epochs = agent_conf.get("train_epochs")

        game = TestSuiteCube.__create_cube(game_conf)
        agent = TestSuiteCube._create_agent(agent_conf, EnvCube(game))

        plot_name_training = TestSuiteCube.get_plot_name(agent_type=agent_type, game=game, is_training=True)
        plot_name_playing = TestSuiteCube.get_plot_name(agent_type=agent_type, game=game, is_training=False)

        train_plot = PlotWriter(name=plot_name_training, plot_information=TestSuiteCube.get_agent_information(agent),
                                should_render=False)
        play_plot = PlotWriter(name=plot_name_playing, plot_information=TestSuiteCube.get_agent_information(agent),
                               should_render=False)

        train_console_writer = ConsoleWriter("Cube Writer")

        agent.register_writer_training(train_plot)
        agent.register_writer_training(train_console_writer)
        agent.register_writer_play(play_plot)

        return TestSuiteCube(testsuite_name, agent, train_epochs, number_of_plays,
                             plot_names=[plot_name_training, plot_name_playing], batch_size=batch_size, deactivated=deactivated)


### Sample Config ###

sample_suite = {
    "result_path": "./var/results/",
    "testsuite_name": "test",
    "agent": {
        "type": "QNetworkAgentOptimizd",  # QNetworkAgent, QTable
        "learning_rate": 0.05,
        "train_epochs": 10,
        "timesteps_per_episode": 100,
        "gamma": 0.9,
        "epsilon": 0.2,
        "batch_size": 100,
        "optimizer": "Adam"
    },
    "play": {
        "number_of_plays": 1  # Number of Plays after every train round
    },
    "cube": {
        "facesize": 4
    }
}

#test = TestSuiteCube.from_dict(sample_suite)
#test.run()
