from agent.agent_qtable import QTableAgent
from environment.environment import Environment

env = Environment()

agent = QTableAgent(env)

agent.retrain(10)

