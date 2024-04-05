from src.datamaker_faker import Faker, Field
import pytest


def test_generate_single():
    sex = Field("sex")
    data = sex.generate()

    # check the length
    assert len(data) == 1

    # check the values
    for item in data:
        assert item in ["male", "female"]

    assert len(sex.generate(10)) == 10


@pytest.mark.parametrize("n", [10, 100_000, 1_000_00])
def test_generate_from_model(n):
    model = {
        "frstnm": "first_name",
        "srnm": "last_name",
        "sx": "sex",
        "ctry": "country",
        "cty": "city",
    }

    faker = Faker(model, seed=123)
    data = faker.generate(n)

    assert len(data) == n
