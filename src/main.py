from agent.agent_qtable import QTableAgent
from environment.environment import Environment

env = Environment.create_sample()

agent = QTableAgent(env)

agent.retrain(10)

agent.q_table.to_csv("test.csv")

agent.q_table.to_json("test.json")
