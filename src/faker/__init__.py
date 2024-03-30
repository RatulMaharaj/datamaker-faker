import numpy as np
from pathlib import Path
from .models.person import Person
from .models.geo import Geo
from .models.random import Integer
from typing import Any

# define the data folder
data_folder = Path(__file__).parent / "data"


class Faker:
    def __init__(
        self, seed: int | None = None, model: dict[str, dict[str, Any]] | None = None
    ):
        self.seed = seed
        self.model = model
        self.random_state = np.random.RandomState(seed)

    def __sample(self, arr: np.array, n: int = 1):
        return self.random_state.choice(arr, n, replace=True)

    def generate(self, n=1):
        generated = {}
        for k, v in self.model.items():
            data = np.genfromtxt(
                f"{v.path}.csv",
                delimiter=",",
                dtype=str,  # TODO: Improve dtypes to match cols available
                skip_header=1,
                autostrip=True,
                usecols=(0,),
            )
            generated[k] = self.__sample(data, n).tolist()

        return generated

    # TODO: This is generation from csv, but we should also support generation from functions
