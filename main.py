import json
from faker import Faker


model = {
    "first": "first_name",
    "last": "last_name",
    "sex": "sex",
    "city": "city",
    "country": "country",
}

faker = Faker(model, seed=43)
print(json.dumps(faker.generate(10), indent=2))
