import unittest
from deeplearning.agent.agent_qnetwork_optimized import QNetworkAgentOptimizd
from deeplearning.agent.agent_qtable import QTableAgent

from deeplearning.monitoring.monitoring import PlotWriter
from deeplearning.games.labyrinth.labyrinth_game import LabyrinthGame
from deeplearning.games.labyrinth.maze_game_gui_adapter import LabyrinthGameGuiAdapter
from deeplearning.games.cube import EnvCube, CubeGame

from deeplearning.games.labyrinth.env_labyrinth import EnvLabyrinth
from tensorflow.keras.optimizers import Adam

class TestQNetworkAgentOptimizd(unittest.TestCase):

    def test(self):
        maze_game = LabyrinthGameGuiAdapter(LabyrinthGame.setup_game(6, 6, 3, 12))
        #maze_game = LabyrinthGame.setup_game(7, 7, 4, 12)

        env = EnvLabyrinth(maze_game)

        eps = 0.2
        timesteps_per_episode = 1000
        learning_rate = 0.01
        agent = QNetworkAgentOptimizd(env, optimizer=Adam(learning_rate=learning_rate), timesteps_per_episode=timesteps_per_episode, epsilon=eps, gamma=0.95)

        train_plot = PlotWriter("Training", plot_information="LearningRate: %s, TimeStepsPerEpisode:%s, Epsilon: %s" % (learning_rate, timesteps_per_episode, eps),
                                should_render=True)
        play_plot = PlotWriter("Play", plot_information="LearningRate: %s, TimeStepsPerEpisode:%s, Epsilon: %s" % (learning_rate, timesteps_per_episode, eps),
                                should_render=True)


        agent.register_writer_training(train_plot)
        agent.register_writer_play(play_plot)

        for i in range(0, 50):
            agent.train(100, batch_size=40)
            agent.play(i)
            agent.set_epsilon(eps)

    def test_cube(self):

        env = EnvCube(CubeGame.setup_game(3))

        eps = 0.2
        timesteps_per_episode = 2000
        learning_rate = 0.01
        agent = QNetworkAgentOptimizd(env, optimizer=Adam(learning_rate=learning_rate),
                                      timesteps_per_episode=timesteps_per_episode, epsilon=eps, gamma=0.95)

        train_plot = PlotWriter("Training", plot_information="LearningRate: %s, TimeStepsPerEpisode:%s, Epsilon: %s" % (
        learning_rate, timesteps_per_episode, eps),
                                should_render=True)
        play_plot = PlotWriter("Play", plot_information="LearningRate: %s, TimeStepsPerEpisode:%s, Epsilon: %s" % (
        learning_rate, timesteps_per_episode, eps),
                               should_render=True)

        agent.register_writer_training(train_plot)
        agent.register_writer_play(play_plot)

        for i in range(0, 50):
            agent.train(100, batch_size=40)
            agent.play(i)
            agent.set_epsilon(eps)


if __name__ == '__main__':
    unittest.main()
