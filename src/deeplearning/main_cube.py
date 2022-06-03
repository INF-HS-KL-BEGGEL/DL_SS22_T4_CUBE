from agent.agent_qtable import QTableAgent
from agent.agent_qnetwork import QNetworkAgent
from games.cube.cube_game import CubeGame
from games.cube.env_cube import EnvCube

def run_qtable_agent(env):
    agent = QTableAgent(env)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)

def run_qnetwork_agent(env):
    agent = QNetworkAgent(env)

    for i in range(0, 20):
        agent.train(50)
        agent.play(i)

print('--- Start ---')
env = EnvCube(CubeGame.setup_game(6))

#run_qtable_agent(env)
run_qnetwork_agent(env)

# Use this as a breakpoint to keep the plots open
print('--- END ---')
