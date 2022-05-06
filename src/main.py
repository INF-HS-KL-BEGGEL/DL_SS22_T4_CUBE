from agent.agent_qtable import QTableAgent
from environment.environment import Environment

env = Environment.create_sample()

agent = QTableAgent(env, 10000)

for i in range(1, 20):

    agent.retrain()
    agent.play(i)


agent.q_table.to_csv("test.csv")

agent.q_table.to_json("test.json")
