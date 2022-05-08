from agent.agent_qtable import QTableAgent
from agent.agent_qnetwork import QNetworkAgent

from environment.environment import Environment

env = Environment.create_sample()

# agent = QTableAgent(env)
agent = QNetworkAgent(env)

for i in range(1, 2):

    agent.retrain(10)

    #agent.play(i)


agent.q_table.to_csv("test.csv")

agent.q_table.to_json("test.json")
