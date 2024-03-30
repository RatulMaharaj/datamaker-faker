from src.faker import Faker


def test_without_seed():
    faker = Faker()
    assert faker.seed is None
    assert faker.random_state is not None


def test_set_seed():
    faker = Faker(seed=42)
    assert faker.seed == 42
    assert faker.random_state is not None


def test_set_multiple_seeds():
    f1 = Faker(seed=42)
    f2 = Faker(seed=52)

    assert f1.seed == 42
    assert f2.seed == 52
