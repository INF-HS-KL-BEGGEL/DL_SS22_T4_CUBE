import numpy as np
import random
from IPython.display import clear_output
import collections
from tensorflow.keras.optimizers import Adam
from agent.qnetwork import QNetwork

class QNetworkAgent:

    def __init__(self, environment, optimizer=Adam(learning_rate=0.01)):

        self.environment = environment
        # Initialize attributes
        self._state_size = len(environment.observation_space)
        self._action_size = len(environment.action_space)

        self.experience_replay = collections.deque(maxlen=2000)

        # Initialize discount and exploration rate
        self.gamma = 0.6
        self.epsilon = 0.1

        # Build networks
        self.target_network = QNetwork(self._action_size, self._state_size, optimizer)
        self.q_network = QNetwork(self._action_size, self._state_size, optimizer)

        self.target_network.algin_model(self.q_network)


    def store(self, state, action, reward, next_state, terminated):
        self.experience_replay.append((state, action, reward, next_state, terminated))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return self.environment.get_random_action().id

        q_values = self.q_network.predict(state)
        return np.argmax(q_values[0])

    def retrain(self, batch_size):
        minibatch = random.sample(self.experience_replay, batch_size)

        for state, action, reward, next_state, terminated in minibatch:

            target = self.q_network.predict(state)

            if terminated:
                target[0][action] = reward
            else:
                t = self.target_network.predict(next_state)
                target[0][action] = reward + self.gamma * np.amax(t)

            self.q_network.fit(state, target, epochs=1, verbose=0)

    def train(self, num_of_episodes, batch_size=10):
        for e in range(0, num_of_episodes):
            # Reset the enviroment
            state = self.environment.reset_state()
            state = np.reshape(state.get_number(), [1, 1])

            # Initialize variables
            reward = 0
            terminated = False

            #bar = progressbar.ProgressBar(maxval=timesteps_per_episode / 10, widgets= \
            #    [progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            #bar.start()

            self.timesteps_per_episode = 1
            for timestep in range(self.timesteps_per_episode):
                # Run Action
                action_index = self.act(state)
                print(action_index)

                action = self.environment.action_space[action_index]

                # Take action
                next_state, reward, terminated, info = self.environment.step(action)
                next_state = np.reshape(next_state, [1, 1])
                self.store(state, action.id, reward, next_state, terminated)

                state = next_state

                if terminated:
                    self.target_network.algin_model(self.q_network)
                    break

                if len(self.experience_replay) > batch_size:
                    self.retrain(batch_size)


            if (e + 1) % 10 == 0:
                print("**********************************")
                print("Episode: {}".format(e + 1))
                print("**********************************")