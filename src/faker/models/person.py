from .field import Field


class Person:
    def __init__(self, seed: int | None = None) -> None:
        self.first_name = Field("first_name", "person", seed=seed)
        self.last_name = Field("last_name", "person", seed=seed)
        self.sex = Field("sex", "person", seed=seed)
