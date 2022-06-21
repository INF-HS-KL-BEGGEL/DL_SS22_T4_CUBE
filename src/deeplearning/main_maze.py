import time
from tkinter import mainloop

from agent import QTableAgent
from games.labyrinth import EnvLabyrinth, LabyrinthGame, LabyrinthGameGuiAdapter
from monitoring.monitoring import PlotWriter


def run_qtable_agent(env):
    agent = QTableAgent(env)

    train_plot = PlotWriter("QTable Training " + str(env.game.get_labyrinth().width) +
                            " x " + str(env.game.get_labyrinth().height) + " Maze with " +
                            str(len(env.game.get_labyrinth().get_targets())) + " Targets", "Test", True)

    play_plot = PlotWriter("QTable Playing " + str(env.game.get_labyrinth().width) +
                           " x " + str(env.game.get_labyrinth().height) + " Maze with " +
                           str(len(env.game.get_labyrinth().get_targets())) + " Targets", "Test", True)

    agent.register_writer_training(train_plot)
    agent.register_writer_play(play_plot)

    for i in range(0, 20):
        agent.train(100)
        agent.play(i)


def run_qnetwork_agent(env):
    from agent.agent_qnetwork import QNetworkAgent
    agent = QNetworkAgent(env)

    train_plot = PlotWriter("QNetwork Training " + str(env.game.get_labyrinth().width) +
                            " x " + str(env.game.get_labyrinth().height) + " Maze with " +
                            str(len(env.game.get_labyrinth().get_targets())) + " Targets")

    play_plot = PlotWriter("QNetwork Playing " + str(env.game.get_labyrinth().width) +
                           " x " + str(env.game.get_labyrinth().height) + " Maze with " +
                           str(len(env.game.get_labyrinth().get_targets())) + " Targets")

    agent.register_writer_training(train_plot)
    agent.register_writer_play(play_plot)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


print('--- Start ---')
render_maze = True

if render_maze:
    maze_game = LabyrinthGameGuiAdapter(LabyrinthGame.setup_game(10, 10, 4))
else:
    maze_game = LabyrinthGame.setup_game(10, 10, 4)

env = EnvLabyrinth(maze_game)
run_qtable_agent(env)
#run_qnetwork_agent(env)
mainloop()
# Use this as a breakpoint to keep the plots open
print('--- END ---')
print("Input any key to exit...")
input()
