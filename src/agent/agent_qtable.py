import random

from IPython.core.display_functions import clear_output
from agent.agent_base import Agent
from agent.qtable import QTable


class QTableAgent(Agent):

    def __init__(self, environment, episodes=100):
        super().__init__(environment)

        self.env = environment
        self.num_of_episodes = episodes
        self.q_table = QTable(self.env, len(self.env.observation_space), len(self.env.action_space))
        self.epsilon = 0.1
        self.alpha = 0.1
        self.gamma = 0.6

    def act(self, state):
        pass

    def retrain(self, batch_size):

        for episode in range(0, self.num_of_episodes):
            # Reset the environment
            state = self.environment.reset()

            # Initialize variables
            reward = 0
            terminated = False

            while not terminated:

                # Take learned path or explore new actions based on the epsilon
                if random.uniform(0, 1) < self.epsilon:
                    action = self.get_random_action()
                else:
                    action = self.q_table.get_action_with_max_reward(state)

                # Take action
                next_state, reward, terminated, info = self.environment.step(action)

                if terminated:
                    self.q_table.print()
                    print(self.env.action_space)
                    print(self.env.observation_space)
                    break

                q_value = self.q_table.get_reward(state, action)
                max_value = self.q_table.get_max_reward(next_state)
                new_q_value = self.recalculate(q_value, max_value, reward)

                self.q_table.update(state, action, new_q_value)
                state = next_state

            if (episode + 1) % 100 == 0:
                clear_output(wait=True)
                print("Episode: {}".format(episode + 1))
                # self.environment.render()

        print("**********************************")
        print("Training is done!\n")
        print("**********************************")

    def recalculate(self, q_value, max_value, reward):

        return (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * max_value)

    def get_random_action(self):
        return random.choice(self.env.action_space)
