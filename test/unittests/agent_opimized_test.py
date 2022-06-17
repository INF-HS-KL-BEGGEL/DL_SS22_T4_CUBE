import unittest
from deeplearning.agent.agent_qnetwork_optimized import QNetworkAgentOptimizd
from deeplearning.monitoring.monitoring import PlotWriter
from deeplearning.games.labyrinth.labyrinth_game import LabyrinthGame
from deeplearning.games.labyrinth.maze_game_gui_adapter import LabyrinthGameGuiAdapter

from deeplearning.games.labyrinth.env_labyrinth import EnvLabyrinth
from tensorflow.keras.optimizers import Adam

class TestQNetworkAgentOptimizd(unittest.TestCase):

    def test(self):
        maze_game = LabyrinthGameGuiAdapter(LabyrinthGame.setup_game(7, 7, 4, 12))
        #maze_game = LabyrinthGame.setup_game(7, 7, 4, 12)

        env = EnvLabyrinth(maze_game)
        agent = QNetworkAgentOptimizd(env, optimizer=Adam(learning_rate=0.05), timesteps_per_episode=80, epsilon=0.3, gamma=0.9)

        train_plot = PlotWriter("Training")
        train_plot.set_label("Epoche", "Reward")

        play_plot = PlotWriter("Play")
        play_plot.set_label("Epoche", "Reward")

        agent.register_writer_training(train_plot)
        agent.register_writer_play(play_plot)

        for i in range(0, 50):
            agent.train(10, batch_size=80)
            agent.play(i)


if __name__ == '__main__':
    unittest.main()
