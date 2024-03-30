from . import data_folder
import numpy as np


class Field:
    def __init__(
        self,
        name: str,
        seed: int | None = None,
    ) -> None:
        self.path = data_folder / "person" / name
        self.seed = seed
        self.random_state = np.random.RandomState(seed)

    def __sample(self, arr: np.array, n: int = 1):
        return self.random_state.choice(arr, n, replace=True)

    def generate(self, n=1):
        data = np.genfromtxt(
            f"{self.path}.csv",
            delimiter=",",
            dtype=str,  # TODO: Improve dtypes to match cols available
            skip_header=1,
            autostrip=True,
            usecols=(0,),
        )
        return self.__sample(data, n).tolist()


class Person:
    def __init__(self, seed: int | None = None) -> None:
        self.first_name = Field("first_name", seed=seed)
        self.last_name = Field("last_name", seed=seed)
        self.sex = Field("sex", seed=seed)
