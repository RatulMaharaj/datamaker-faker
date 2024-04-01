from .field import Field


class Geo:
    def __init__(self, seed: int | None = None) -> None:
        self.country = Field("country", "geo", seed=seed)
        self.city = Field("city", "geo", seed=seed)
