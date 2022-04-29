from IPython.core.display_functions import clear_output

from agent.agent_base import Agent
import random
import numpy as np


class QTableAgent(Agent):

    def __init__(self, env):
        super().__init__(env)

        self.num_of_episodes = 10000
        self.q_table = np.zeros([self.environment.observation_space.n, self.environment.action_space.n])
        self.epsilon = 0.1
        self.alpha = 0.1
        self.gamma = 0.6

    def set_num_of_episodes(self, count):

        self.num_of_episodes = count

    def act(self, state):
        pass

    def retrain(self, batch_size):
        for episode in range(0, self.num_of_episodes):
            # Reset the enviroment
            state = self.environment.reset()

            # Initialize variables
            reward = 0
            terminated = False

            while not terminated:
                # Take learned path or explore new actions based on the epsilon
                if random.uniform(0, 1) < self.epsilon:
                    action = self.environment.action_space.sample()
                else:
                    print(self.q_table)
                    print(state)

                    action = np.argmax(self.q_table[state.number])

                # Take action
                next_state, reward, info = self.environment.step(action)

                # Recalculate
                q_value = self.q_table[state, action]
                max_value = np.max(self.q_table[next_state])
                new_q_value = (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * max_value)

                # Update Q-table
                self.q_table[state, action] = new_q_value
                state = next_state

            if (episode + 1) % 100 == 0:
                clear_output(wait=True)
                print("Episode: {}".format(episode + 1))
                self.environment.render()

        print("**********************************")
        print("Training is done!\n")
        print("**********************************")
