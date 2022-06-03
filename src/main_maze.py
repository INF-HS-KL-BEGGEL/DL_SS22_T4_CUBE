from agent.agent_qtable import QTableAgent
from games.labyrinth.env_labyrinth import EnvLabyrinth
from games.labyrinth.labyrinth_game import LabyrinthGame


def run_qtable_agent(env):
    agent = QTableAgent(env)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


def run_qnetwork_agent(env):
    from agent.agent_qnetwork import QNetworkAgent
    agent = QNetworkAgent(env)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)


print('--- Start ---')
env = EnvLabyrinth(LabyrinthGame.setup_game(6, 6, 5, 123))

#run_qtable_agent(env)
#run_qnetwork_agent(env)

# Use this as a breakpoint to keep the plots open
print('--- END ---')
print("Input any key to exit...")
input()
