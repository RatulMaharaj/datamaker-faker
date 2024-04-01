from src.faker import Faker, Person, Geo
import pytest


def test_generate_single():
    person = Person()
    data = person.sex.generate()

    # check the length
    assert len(data) == 1

    # check the values
    for item in data:
        assert item in ["male", "female"]

    assert len(person.sex.generate(10)) == 10


@pytest.mark.parametrize("n", [1, 1_000, 100_000, 1_000_00])
def test_generate_from_model(n):
    model = {
        "name": Person().first_name,
        "surname": Person().last_name,
        "sex": Person().sex,
        "country": Geo().country,
        "city": Geo().city,
    }

    faker = Faker(seed=123, model=model)
    data = faker.generate(n)
    assert len(data) == n


