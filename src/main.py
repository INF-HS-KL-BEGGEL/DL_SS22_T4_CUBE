from agent.agent_qtable import QTableAgent
from agent.agent_qnetwork import QNetworkAgent

from environment.environment import Environment


env = Environment.create_sample()


agent = QTableAgent(env)
#agent = QNetworkAgent(env)

for i in range(0, 10):
    
    agent.train(50)

    agent.play(i)

# Use this as a breakpoint to keep the plots open
print('--- END ---')
#agent.q_table.to_csv("test.csv")

#agent.q_table.to_json("test.json")
