from agent.agent_qtable import QTableAgent
from environment.environment import Environment

env = Environment.create_sample()

agent = QTableAgent(env)

for i in range(1, 20):

    agent.retrain(100)
    agent.play(i)


agent.q_table.to_csv("test.csv")

agent.q_table.to_json("test.json")
