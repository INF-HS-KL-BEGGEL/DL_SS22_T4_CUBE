import random
import time
from IPython.core.display_functions import clear_output
from agent.agent_base import Agent
from agent.qtable import QTable
from logger.logger import PlotWriter

class QTableAgent(Agent):

    def __init__(self, environment):
        super().__init__(environment)

        self.environment = environment
        self.q_table = QTable(self.environment, len(self.environment.observation_space), len(self.environment.action_space))
        self.epsilon = 0.001
        self.alpha = 0.05
        self.gamma = 0.5

        self.plotwriter = PlotWriter()
        self.plotwriter.show()

    def play(self, game_run_index):
        self.plotwriter.show()

        sum_reward = 0
        state = self.environment.reset_state()
        terminated = False
        while not terminated:

            action = self.q_table.get_action_with_max_reward(state)
            print(action.__class__)
            # Take action
            next_state, reward, terminated, info = self.environment.step(action)

            sum_reward += reward
            if terminated:
                self.q_table.print("TERMINATED")
                #print(self.env.action_space)
                #print(self.env.observation_space)
                break

            print("################################ SUM", sum_reward)
            state = next_state

        #self.plotwriter.write((game_run_index, sum_reward))
        self.environment.reset_environment()

    def train(self, num_of_episodes=100):

        for episode in range(0, num_of_episodes):
            # Reset the environment
            state = self.environment.reset_state()

            # Initialize variables
            reward = 0
            terminated = False

            start_t = time.time()
            sum_reward = 0

            while not terminated:

                # Take learned path or explore new actions based on the epsilon
                if random.uniform(0, 1) < self.epsilon:
                    action = self.environment.get_random_action()
                else:
                    action = self.q_table.get_action_with_max_reward(state)

                # Take action
                next_state, reward, terminated, info = self.environment.step(action)
                sum_reward += reward

                if terminated:
                    #print(self.environment.action_space)
                    #print(self.env.observation_space)
                    #self.q_table.print("Episode %s" % episode)
                    break

                q_value = self.q_table.get_reward(state, action)
                max_value = self.q_table.get_max_reward(next_state)
                new_q_value = self.recalculate(q_value, max_value, reward)

                self.q_table.update(state, action, new_q_value)
                state = next_state

            end_t = time.time()
            self.q_table.print("Episode %s Time: %s" % (episode, end_t - start_t))
            #self.plotwriter.write((episode, end_t - start_t))
            self.plotwriter.write((episode, sum_reward))
            #self.epsilon -= (self.epsilon/100)*1
            start_t = end_t
            sum_reward = 0
            self.environment.reset_environment()

        print("**********************************")
        print("Training is done!\n")
        print("**********************************")
        self.environment.reset_environment()

    def recalculate(self, q_value, max_value, reward):

        return (1 - self.alpha) * q_value + self.alpha * (reward + self.gamma * max_value)
