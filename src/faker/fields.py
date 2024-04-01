from enum import Enum


class Fields(Enum):
    class Person(Enum):
        first_name = "first_name"
        last_name = "last_name"
        sex = "sex"

    class Geo(Enum):
        country = "country"
        city = "city"
