import numpy as np
import random
import collections
from deeplearning.agent.agent_base import Agent
from tensorflow.keras.optimizers import Adam
from deeplearning.agent.qnetwork import QNetwork

class QNetworkAgentOptimizd(Agent):

    def __init__(self, environment, optimizer=Adam(learning_rate=0.01), epsilon=0.2, gamma=0.9, timesteps_per_episode=10):

        super().__init__(environment)
        # Initialize attributes
        self._state_size = len(environment.observation_space)
        self._action_size = len(environment.action_space)

        self.experience_replay = collections.deque(maxlen=500)

        # Initialize discount and exploration rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.timesteps_per_episode = timesteps_per_episode

        self.total_episodes = 0

        # Build networks
        self.target_network = QNetwork(self._action_size, self._state_size, optimizer, self.environment)
        self.q_network = QNetwork(self._action_size, self._state_size, optimizer, self.environment)

        self.target_network.algin_model(self.q_network)

    def store(self, state, action, reward, next_state, terminated):
        """TODO"""
        self.experience_replay.append([state, action, reward, next_state, terminated])

    def act(self, state):

        if np.random.rand() <= self.epsilon:
            return self.environment.get_random_action()

        action, q_values = self.q_network.predict(state)
        return action

    def retrain(self, batch_size):
        """TODO"""

        minibatch = random.Random().sample(self.experience_replay, batch_size)
        #dt = np.dtype('int,int,float,int,bool')
        batch = np.array(minibatch)
        #print(batch)
        #print(batch[:, 0])

        q_model = self.q_network.get_model()
        t_model = self.target_network.get_model()
        # Generate predictions for samples
        states = batch[:, 0]
        target = q_model.predict(states, steps=len(states))

        rows_terminated = np.where(batch[:, 4] == True)
        rewards_terminated_states = batch[rows_terminated][:, 2]
        action_indizes = np.argmax(target[rows_terminated], axis=1)
        target[:, action_indizes] = rewards_terminated_states

        rows_not_terminated = np.where(batch[:, 4] == False)
        rewards_not_terminated_states = batch[rows_not_terminated][:, 2]
        next_states = batch[rows_not_terminated][:, 3]
        t = t_model.predict(next_states, steps=len(next_states))
        action_indizes = np.argmax(target[rows_not_terminated], axis=1)
        target[:, action_indizes] = rewards_not_terminated_states + self.gamma * np.amax(t)
        # Generate arg maxes for predictions
        q_model.fit(states, target, batch_size=batch_size, verbose=0)

    def play(self, index):
        """
        """
        state = self.environment.reset_environment()
        sum_reward = 0
        for timestep in range(self.timesteps_per_episode):
            # Run Action
            action = self.act(state)

            # Take action
            next_state, reward, terminated, info = self.environment.step(action)
            sum_reward += reward

            if terminated:
                self.target_network.algin_model(self.q_network)
                break

            next_state_number = next_state.get_number()

            self.store(state.get_number(), action.id, reward, next_state_number , terminated)
            state = next_state

        self.notify_writer_play((index, sum_reward))

    def train(self, num_of_episodes, batch_size=100):
        for e in range(0, num_of_episodes):
            # Reset the enviroment
            state = self.environment.reset_environment()
            print("After Reset", self.environment.game.get_targets())

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
                #print(action, reward)

                next_state_number = next_state.get_number()
                self.store(state.get_number(), action.id, reward, next_state_number, terminated)

                if terminated:
                    print("Terminated")
                    self.target_network.algin_model(self.q_network)
                    self.environment.reset_environment()
                    break

                state = next_state

                if len(self.experience_replay) > batch_size:
                    #print("Retrain")
                    self.retrain(batch_size)

            self.notify_writer_training((self.total_episodes, sum_reward))
            print("Episode: {}, Reward {}".format(self.total_episodes, sum_reward))
            self.total_episodes += 1