from tensorflow.keras import Model, Sequential
from tensorflow.keras.layers import Dense, Embedding, Reshape
from tensorflow.keras.optimizers import Adam
from environment.state import StateBase
import numpy as np


class QNetwork:

    def __init__(self, action_size, state_size, optimizer, env):
        self._state_size = state_size
        self._action_size = action_size
        self._optimizer = optimizer
        self.model = self._build_compile_model()
        self.environment = env

    def _build_compile_model(self):
        model = Sequential()
        model.add(Embedding(self._state_size, 10, input_length=1))
        model.add(Reshape((10,)))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(self._action_size, activation='linear'))

        model.compile(loss='mse', optimizer=self._optimizer)
        return model

    def get_weights(self):
        return self.model.get_weights()

    def algin_model(self, qnetwork):
        self.model.set_weights(qnetwork.get_weights())

    def predict(self, state: StateBase) -> tuple:
        state = np.reshape(state.get_number(), [1, 1])
        q_values = self.model.predict(state)
        action_index = np.argmax(q_values[0])
        action = self.environment.action_space[action_index]

        return action, q_values

    def fit(self, state, target, epochs=1, verbose=0):
        state = np.reshape(state.get_number(), [1, 1])
        self.model.fit(state, target, epochs=1, verbose=0)
        return