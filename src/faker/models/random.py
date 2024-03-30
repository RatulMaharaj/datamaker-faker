import numpy as np


class Integer:
    def __init__(self, random_state: np.random.RandomState):
        self.random_state = random_state

    def generate(self, n=1):
        return self.random_state.randint(0, 100, size=n)
