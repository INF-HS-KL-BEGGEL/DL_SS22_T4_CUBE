from IPython.core.display_functions import clear_output

from agent.agent_base import Agent
import random
import numpy as np

from logger import LogItem


class QTable:

    def __init__(self, obvservation_space_n, action_space_n):

        self.q_table = np.zeros([obvservation_space_n, action_space_n])
        self.logger = []

    def get_actions_from_state(self, state):
        # TODO returning available action from given state

        return []

    def get_action_with_max_reward(self, state):
        # TODO return action with maximal reward from given state
        return None

    def add_logger(self, logger):
        """
        add logger
        :param logger:
        :return:
        """
        self.logger.append(logger)

    def notify(self, logstring):
        """
        notofy all logger
        :param logstring:
        :return:
        """
        for logger in self.logger:
            logger.log(LogItem(logstring))


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

                    action = self.environment.action_space.get(np.argmax(self.q_table[state.number]))
                    #action = qt.get_action_with_max_reward(state)
                    #qt = QTable(1,2)

                print(action)

                # Take action
                next_state, reward, info = self.environment.step(action)

                # Update Q-table
                self.q_table[state.number, action] = self.recalculate(action, reward, state, next_state)
                state = next_state

            if (episode + 1) % 100 == 0:
                clear_output(wait=True)
                print("Episode: {}".format(episode + 1))
                self.environment.render()

        print("**********************************")
        print("Training is done!\n")
        print("**********************************")


    def recalculate(self,action, reward, state, next_state):
        """"""

        # Recalculate
        q_value = self.q_table[state.number, action]
        max_value = np.max(self.q_table[next_state.number])
        new_q_value = (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * max_value)

        return new_q_value