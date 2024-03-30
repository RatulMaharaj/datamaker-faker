from pydantic import dataclasses
from . import data_folder


@dataclasses.dataclass
class Geo:
    city = data_folder / "geo" / "city"
    country = data_folder / "geo" / "country"
