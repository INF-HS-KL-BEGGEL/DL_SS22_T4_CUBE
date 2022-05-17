import json

import numpy as np
import pandas as pd
from tabulate import tabulate


class QTable:

    def __init__(self, env, observation_space_size, action_space_size):
        self.q_table = np.zeros((observation_space_size, action_space_size))
        self.env = env
        self.print()

    def write_value(self, state, action, value):
        self.q_table[state.get_number(), action.id] = value

    def get_actions_from_state(self, state):
        return self.env.action_space

    def get_action_with_max_reward(self, state):
        index = np.argmax(self.q_table[state.get_number()])
        return self.env.action_space[index]

    def get_reward(self, state, action):
        return self.q_table[state.get_number(), action.id]

    def get_max_reward(self, state):
        return np.max(self.q_table[state.get_number()])

    def update(self, state, action, new_q_value):
        self.q_table[state.get_number(), action.id] = new_q_value

    def print(self, msg=""):
        print("******************** %s **********************" % msg)
        table = np.vstack((self.env.action_space, self.q_table))
        print(tabulate(table, headers='firstrow', tablefmt="fancy_grid"))

    def to_csv(self, filename):
        pd.DataFrame(self.q_table).to_csv(filename)

    def to_json(self, filename):
        json.dump({"table": self.q_table.tolist()}, open(filename, "w"))

    def load_csv(self, filename):
        self.q_table = pd.read_csv(filename).to_numpy()

    def load_json(self, filename):
        self.q_table = np.array(json.load(open(filename, "r"))["table"])
