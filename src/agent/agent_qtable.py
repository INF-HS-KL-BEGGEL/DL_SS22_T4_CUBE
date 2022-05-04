from IPython.core.display_functions import clear_output

from agent.agent_base import Agent
import random
import numpy as np

from environment.action import Action


class QTable:

    def __init__(self, observation_space_size, action_space_size):
        self.q_table = np.zeros((observation_space_size, action_space_size))

    def write_value(self, state, action, value):
        self.q_table[state, action] = value
        
    def get_max(self, state):
        return np.argmax(self.q_table[state])

    def get_item(self, state, action):
        return self.q_table[state, action]

    def get_actions_from_state(self, state):
        # TODO returning available action from given state
        return []

    def get_action_with_max_reward(self, state):
        # TODO return action with maximal reward from given state
        return None


class QTableAgent(Agent):

    def __init__(self, environment, episodes=10000):
        super().__init__(environment)

        self.env = environment
        self.num_of_episodes = episodes
        self.q_table = QTable(self.env.observation_space.n, self.env.action_space.n)
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
                    action = self.environment.action_space.sample()
                else:
                    action = self.q_table.get_max(state.state_position)

                # Take action
                next_state, reward, terminated, info = self.environment.step(action)

                print(reward)
                print(action)
                print(self.q_table.q_table)

                # Recalculate
                q_value = self.q_table.q_table[state.state_position, action]
                max_value = np.max(self.q_table.q_table[next_state.state_position])
                new_q_value = (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * max_value)
                
                # Update Q-table
                self.q_table.q_table[state.state_position, action] = new_q_value
                state = next_state

            if (episode + 1) % 100 == 0:
                clear_output(wait=True)
                print("Episode: {}".format(episode + 1))
                # self.environment.render()

        print("**********************************")
        print("Training is done!\n")
        print("**********************************")

