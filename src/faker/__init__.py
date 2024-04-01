import numpy as np
import pandas as pd
from enum import Enum
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
        # TODO: Improving typing
        self.seed = seed
        self.model = model
        self.random_state = np.random.RandomState(seed)

    def __sample(self, arr: np.array, n: int = 1):
        # TODO: Make the sampling algorithm swappable
        return self.random_state.choice(arr, n, replace=True)

    def __get_dataset(self, path: str, field: str, full: bool = False):
        df = pd.read_csv(f"{path}.csv")

        if full:
            return df
        else:
            return df[field].to_numpy()

    def __determine_relations(self, path: str | Path, name: str):
        df = pd.read_csv(f"{path}.csv")
        return [col for col in df.columns if col not in [name, "id"]]

    def __enforce_relations(self, generated: dict[str, list[Any]]):
        fields = [(field.name, field.path) for field in self.model.values()]
        generated_df = pd.DataFrame(generated)
        og_cols = generated_df.columns
        columns = [field[0] for field in fields]
        generated_df.columns = columns

        for name, path in fields:
            if self.__determine_relations(path, name) != []:
                df = self.__get_dataset(path, name, True)
                generated_df = pd.merge(
                    generated_df,
                    df,
                    on=name,
                    how="left",
                    suffixes=("_drop", ""),
                )[columns]

        generated_df.columns = og_cols
        return generated_df.to_dict(orient="records")

    def generate(self, n=1):
        generated = {}
        for k, v in self.model.items():
            data = self.__get_dataset(v.path, v.name)
            generated[k] = self.__sample(data, n).tolist()

        with_relations = self.__enforce_relations(generated)

        return with_relations

    # TODO: This is generation from csv, but we should also support generation from functions
