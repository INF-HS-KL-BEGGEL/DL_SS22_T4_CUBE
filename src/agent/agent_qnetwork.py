import numpy as np
import random
import collections
from agent.agent_base import Agent
from tensorflow.keras.optimizers import Adam
from agent.qnetwork import QNetwork
from monitoring.monitoring import PlotWriter


class QNetworkAgent(Agent):

    def __init__(self, environment, optimizer=Adam(learning_rate=0.05)):

        super().__init__(environment)
        # Initialize attributes
        self._state_size = len(environment.observation_space)
        self._action_size = len(environment.action_space)

        self.experience_replay = collections.deque(maxlen=2000)

        # Initialize discount and exploration rate
        self.gamma = 0.9
        self.epsilon = 0.2
        self.timesteps_per_episode = 10

        self.total_episodes = 0

        # Build networks
        self.target_network = QNetwork(self._action_size, self._state_size, optimizer, self.environment)
        self.q_network = QNetwork(self._action_size, self._state_size, optimizer, self.environment)

        self.target_network.algin_model(self.q_network)

        self.train_plot = PlotWriter("Training")
        self.train_plot.set_label("Epoche", "Reward")
        self.train_plot.show()

        self.play_plot = PlotWriter("Play")
        self.play_plot.set_label("Epoche", "Reward")
        self.play_plot.show()

    def store(self, state, action, reward, next_state, terminated):
        self.experience_replay.append((state, action, reward, next_state, terminated))

    def act(self, state):

        if np.random.rand() <= self.epsilon:
            return self.environment.get_random_action()

        action, q_values = self.q_network.predict(state)
        return action

    def retrain(self, batch_size):
        minibatch = random.sample(self.experience_replay, batch_size)

        for state, action, reward, next_state, terminated in minibatch:
            target_action, q_values = self.q_network.predict(state)

            if terminated:
                q_values[0][action.id] = reward
            else:
                t_action, t = self.target_network.predict(next_state)
                q_values[0][action.id] = reward + self.gamma * np.amax(t)

            self.q_network.fit(state, q_values, epochs=1, verbose=0)

    def play(self, index):
        """
        """
        state = self.environment.reset_state()
        sum_reward = 0
        for timestep in range(self.timesteps_per_episode):
            # Run Action
            action = self.act(state)

            # Take action
            next_state, reward, terminated, info = self.environment.step(action)
            self.store(state, action, reward, next_state, terminated)
            sum_reward += reward
            state = next_state

            if terminated:
                self.target_network.algin_model(self.q_network)
                break

        self.play_plot.write((index, sum_reward))

    def train(self, num_of_episodes, batch_size=100):
        for e in range(0, num_of_episodes):
            # Reset the enviroment
            state = self.environment.reset_state()
            # Initialize variables
            reward = 0
            terminated = False
            sum_reward = 0

            #self.timesteps_per_episode = 1
            for timestep in range(self.timesteps_per_episode):
                # Run Action
                action = self.act(state)
                # Take action
                next_state, reward, terminated, info = self.environment.step(action)
                sum_reward += reward
                self.store(state, action, reward, next_state, terminated)
                #print(action, reward)

                state = next_state

                if terminated:
                    self.target_network.algin_model(self.q_network)
                    break

                if len(self.experience_replay) > batch_size:
                    self.retrain(batch_size)

            self.train_plot.write((self.total_episodes, sum_reward))
            self.total_episodes += 1

            if (e + 1) % 10 == 0:
                print("**********************************")
                print("Episode: {}".format(e + 1))
                print("**********************************")
