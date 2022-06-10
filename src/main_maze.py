import time
from tkinter import mainloop

from agent.agent_qtable import QTableAgent
from games.labyrinth.env_labyrinth import EnvLabyrinth
from games.labyrinth.labyrinth_game import LabyrinthGame
from games.labyrinth.maze_game_gui_adapter import LabyrinthGameGuiAdapter

def run_qtable_agent(env):
    agent = QTableAgent(env)

    for i in range(0, 20):
        agent.train(100)
        agent.play(i)


def run_qnetwork_agent(env):
    from agent.agent_qnetwork import QNetworkAgent
    agent = QNetworkAgent(env)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


print('--- Start ---')
render_maze = True

if render_maze:
    maze_game = LabyrinthGameGuiAdapter(LabyrinthGame.setup_game(25, 25, 4))
else:
    maze_game = LabyrinthGame.setup_game(25, 25, 4)

env = EnvLabyrinth(maze_game)
run_qtable_agent(env)
# run_qnetwork_agent(env)
mainloop()
# Use this as a breakpoint to keep the plots open
print('--- END ---')
print("Input any key to exit...")
input()
