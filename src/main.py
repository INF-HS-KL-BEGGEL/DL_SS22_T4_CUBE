from agent.agent_qtable import QTableAgent
from agent.agent_qnetwork import QNetworkAgent
from games.cube.cube_game import CubeGame
from games.cube.env_cube import EnvCube


env = EnvCube(CubeGame.setup_game(6))
agent = QTableAgent(env)
#agent = QNetworkAgent(env)

for i in range(0, 10):
    
    agent.train(50)
    agent.play(i)

# Use this as a breakpoint to keep the plots open
print('--- END ---')
#agent.q_table.to_csv("test.csv")

#agent.q_table.to_json("test.json")
