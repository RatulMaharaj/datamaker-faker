from . import data_folder
import numpy as np
import pandas as pd


class Field:
    def __init__(
        self,
        name: str,
        category: str,
        seed: int | None = None,
        relations: list[str] | None = None,
    ) -> None:
        self.name = name
        self.category = category
        self.path = data_folder / category / name
        self.seed = seed
        self.random_state = np.random.RandomState(seed)
        self.relations = relations

    def __sample(self, arr: np.array, n: int = 1):
        return self.random_state.choice(arr, n, replace=True)

    def generate(self, n=1):
        data = pd.read_csv(f"{self.path}.csv")[self.name].to_numpy()
        return self.__sample(data, n).tolist()
