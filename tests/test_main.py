from src.faker import Faker, Person
import json


def test_generate_single():
    person = Person()
    data = person.sex.generate()

    # check the length
    assert len(data) == 1

    # check the values
    for item in data:
        assert item in ["male", "female"]

    assert len(person.sex.generate(10)) == 10


def test_generate_from_dict():
    model = {
        "first_name": Person().first_name,
        "last_name": Person().last_name,
        "sex": Person().sex,
    }

    faker = Faker(seed=123, model=model)
    data = faker.generate(n=2)
    # TODO: use pandas to manage orientation
    print(json.dumps(data, indent=4))
