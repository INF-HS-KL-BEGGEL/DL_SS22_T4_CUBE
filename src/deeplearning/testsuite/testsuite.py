import json
from deeplearning.agent.agent_qnetwork import QNetworkAgent
from deeplearning.games.labyrinth.env_labyrinth import EnvLabyrinth
from deeplearning.games.labyrinth.labyrinth_game import LabyrinthGame
from tensorflow.keras.optimizers import Adam
from deeplearning.monitoring.monitoring import CsvWriter, ConsoleWriter
from pathlib import Path

class TestSuiteMaze:

    def __init__(self, agent, train_epoches, number_of_plays, batch_size):
        self.agent = agent
        self.train_epoches = train_epoches
        self.number_of_plays = number_of_plays # Number of Plays after every train round
        self.batch_size = batch_size

    def run(self):
        for i in range(self.number_of_plays):
            self.agent.train(self.train_epoches, self.batch_size)
            self.agent.play(i)

    @staticmethod
    def __create_maze(maze_conf: dict):

        height = maze_conf.get("height")
        width = maze_conf.get("width")
        targets = maze_conf.get("targets")
        seed = maze_conf.get("seed")
        return LabyrinthGame.setup_game(height, width, targets, seed=seed)

    @staticmethod
    def from_json_file(filename):
        json_data = json.load(open(filename, "r"))
        return TestSuiteMaze.from_dict(json_data)

    @staticmethod
    def from_dict(config):

        testsuite_name = config.get("testsuite_name")
        result_path =config.get("result_path")
        agent_conf = config.get("agent")
        game_conf = config.get("maze")
        play_conf = config.get("play")

        number_of_plays = play_conf.get("number_of_plays", 1)

        learning_rate = agent_conf.get("learning_rate")
        timesteps_per_epoches = agent_conf.get("timesteps_per_epoches")
        gamma = agent_conf.get("gamma")
        epsilon = agent_conf.get("epsilon")
        batch_size = agent_conf.get("batch_size", 1000)

        train_epoches = agent_conf.get("train_epoches")

        game = TestSuiteMaze.__create_maze(game_conf)
        agent = QNetworkAgent(EnvLabyrinth(game),
                              Adam(learning_rate=learning_rate),
                              epsilon=epsilon,
                              gamma=gamma,
                              timesteps_per_episode=timesteps_per_epoches)

        Path(result_path).mkdir(parents=True, exist_ok=True)

        csv_train_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_training.csv")
        csv_train_writer.set_label("Epoches", "Reward")
        csv_play_writer = CsvWriter(name=testsuite_name, filename=result_path + testsuite_name + "_play.csv")
        csv_play_writer.set_label("Index", "Reward")

        #plot_train_writer = PlotWriter(name=testsuite_name)
        #plot_train_writer.set_label("Epoche", "Reward")
        #agent.register_writer_training(plot_train_writer)

        agent.register_writer_training(csv_train_writer)

        agent.register_writer_play(csv_play_writer)
        agent.register_writer_training(ConsoleWriter("Console Training"))

        return TestSuiteMaze(agent, train_epoches, number_of_plays, batch_size=batch_size)

sample_suite = {
    "result_path": "./var/results/",
    "testsuite_name": "test",
    "agent": {
        "learning_rate": 0.05,
        "train_epoches": 10,
        "timesteps_per_epoches": 100,
        "gamma": 0.9,
        "epsilon": 0.2,
        "batch_size": 100
    },
    "play": {
        "number_of_plays": 1 # Number of Plays after every train round
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
