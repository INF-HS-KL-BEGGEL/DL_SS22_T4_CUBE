from IPython.core.display_functions import clear_output
import json
import pandas as pd
from agent.agent_base import Agent
import random
import numpy as np

from environment.action import Action

class QTable:

    def __init__(self, env, observation_space_size, action_space_size):
        self.q_table = np.zeros((observation_space_size, action_space_size))
        self.env = env

    def write_value(self, state, action, value):

        self.q_table[state.get_number(), action.id()] = value

    def get_actions_from_state(self, state):
        return self.env.action_space

    def get_action_with_max_reward(self, state):
        print(state)
        index = np.argmax(self.q_table[state.get_number()])
        return self.env.action_space[index]

    def get_reward(self, state, action):
        return self.q_table[state.get_number(), action.id()]

    def get_max_reward(self, state):
        print("state nr", state.number )
        return np.max(self.q_table[state.get_number()])

    def update(self, state, action, new_q_value):
        print("update:", state.number, action.id())
        self.q_table[state.get_number(), action.id()] = new_q_value

    def print(self):
        print(self.q_table)

    def to_csv(self, filename):
        pd.DataFrame(self.q_table).to_csv(filename)

    def to_json(self, filename):
        json.dump({"table": self.q_table.tolist()}, open(filename, "w"))

    def load_csv(self, filename):
        self.q_table = pd.read_csv(filename).to_numpy()

    def load_json(self, filename):
        self.q_table = np.array(json.load(open(filename, "r"))["table"])


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

                if self.environment.game.is_done():
                    break

                # Take learned path or explore new actions based on the epsilon
                if random.uniform(0, 1) < self.epsilon:
                    action = self.get_random_action()
                else:
                    action = self.q_table.get_action_with_max_reward(state)

                print("Action", action)
                # Take action
                next_state, reward, terminated, info = self.environment.step(action)

                print("Reward", reward)
                print("Action", action)
                self.q_table.print()

                # Recalculate
                q_value = self.q_table.get_reward(state, action)
                max_value = self.q_table.get_max_reward(next_state)
                new_q_value = self.recalculate(q_value, max_value, reward)

                # Update Q-table
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
