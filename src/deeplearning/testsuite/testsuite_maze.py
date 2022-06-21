import json
from pathlib import Path

from deeplearning.games.labyrinth import EnvLabyrinth, LabyrinthGame
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter, PlotWriter
from deeplearning.testsuite.testsuite_base import TestSuiteBase


class TestSuiteMaze(TestSuiteBase):

    def __init__(self, name, agent, train_epochs, number_of_plays, plot_names, batch_size):
        super().__init__(name, agent, train_epochs, number_of_plays, plot_names, batch_size)

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
    def get_plot_name(agent_type, game, is_training=True):
        """ Return a readable name for the plot """
        mode = is_training and "Training" or "Playing"
        return "" + agent_type + ", " + str(mode) + ", " + str(game.get_labyrinth().width) + " x " + str(
            game.get_labyrinth().height) + " Maze with " + str(len(game.get_labyrinth().get_targets())) + " Targets"

    @staticmethod
    def get_agent_information(agent):
        """ Helper method to output QLearning parameters on plot """
        plot_information = "Epsilon: " + str(agent.epsilon) + ", Gamma: " + str(agent.gamma)

        # distinguish QTable from QNetwork
        if hasattr(agent, "timesteps_per_episode"):
            plot_information += ", Timesteps per Episode: " + str(agent.timesteps_per_episode)
        if hasattr(agent, "alpha"):
            plot_information += ", Learning rate: " + str(agent.alpha)
        return plot_information

    @staticmethod
    def from_dict(config):
        testsuite_name = config.get("testsuite_name")
        result_path = config.get("result_path")
        Path(result_path).mkdir(parents=True, exist_ok=True)

        agent_conf = config.get("agent")
        agent_type = agent_conf.get("type")
        game_conf = config.get("maze")
        play_conf = config.get("play")
        number_of_plays = play_conf.get("number_of_plays", 1)

        batch_size = agent_conf.get("batch_size")
        train_epochs = agent_conf.get("train_epochs")

        game = TestSuiteMaze.__create_maze(game_conf)
        agent = TestSuiteMaze._create_agent(agent_conf, EnvLabyrinth(game))

        plot_name_training = TestSuiteMaze.get_plot_name(agent_type=agent_type, game=game, is_training=True)
        plot_name_playing = TestSuiteMaze.get_plot_name(agent_type=agent_type, game=game, is_training=False)

        train_plot = PlotWriter(name=plot_name_training, plot_information=TestSuiteMaze.get_agent_information(agent),
                                should_render=False)
        play_plot = PlotWriter(name=plot_name_playing, plot_information=TestSuiteMaze.get_agent_information(agent),
                               should_render=False)

        agent.register_writer_training(train_plot)
        agent.register_writer_play(play_plot)

        return TestSuiteMaze(testsuite_name, agent, train_epochs, number_of_plays,
                             plot_names=[plot_name_training, plot_name_playing], batch_size=batch_size)


# ---- Sample Config ----- #

sample_suite = {
    "result_path": "./var/results/",
    "testsuite_name": "test",
    "agent": {
        "type": "QTable",  # QNetworkAgent, QNetworkAgentOptimizd, QTable
        "learning_rate": 0.2,
        "train_epochs": 20,
        "timesteps_per_episode": 100,
        "gamma": 0.6,
        "epsilon": 0.1,
        # "batch_size": 100, # Should be removed when type is QTable
        "optimizer": "Adam"
    },
    "play": {
        "number_of_plays": 10  # Number of Plays after every train round
    },
    "maze": {
        "height": 4,
        "width": 4,
        "targets": 2,
        "seed": 10
    }
}

#test = TestSuiteMaze.from_dict(sample_suite)
#test.run()
