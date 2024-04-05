# DataFaker

[![PyPI - Version](https://img.shields.io/pypi/v/faker.svg)](https://pypi.org/project/faker)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/faker.svg)](https://pypi.org/project/faker)

---

**Table of Contents**

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [License](#license)

## Installation

```console
pip install datamaker-faker
```

## Features

This package:

- Aims to be a replacement for the `faker` package in Python but **NOT** a drop-in replacement.
- Fast: Generate data quickly at large scales.
- Reproducible: Set a seed to generate the same data over and over.
- Relational: Generate data that is related to each other.
- Extensible: Swop out the data for your own, or bring your own generators.

## Usage

```python
import json
from datamaker_faker import Faker

# define your data model
model = {
    "first": "first_name",
    "last": "last_name",
    "sex": "sex",
    "city": "city",
    "country": "country",
}

# create a new faker instance
faker = Faker(model, seed=9)

# generate some fake data
df = faker.generate(10)

# write the data to a csv file
df.to_csv("datafaker.csv")

# or leverage pandas to convert the data to json
data = df.to_dict("records")
print(json.dumps(data, indent=2))
```

Output:

```json
[
  {
    "first": "sophia",
    "last": "weber",
    "sex": "female",
    "city": "munich",
    "country": "germany"
  },
  {
    "first": "aiden",
    "last": "brown",
    "sex": "male",
    "city": "toronto",
    "country": "canada"
  },
  {
    "first": "sophia",
    "last": "weber",
    "sex": "female",
    "city": "munich",
    "country": "germany"
  },
  {
    "first": "aaradhya",
    "last": "singh",
    "sex": "female",
    "city": "delhi",
    "country": "india"
  },
  {
    "first": "liam",
    "last": "brown",
    "sex": "male",
    "city": "chicago",
    "country": "united states"
  },
  {
    "first": "daniel",
    "last": "kamau",
    "sex": "male",
    "city": "nairobi",
    "country": "kenya"
  },
  {
    "first": "alexander",
    "last": "smirnov",
    "sex": "male",
    "city": "nizhny novgorod",
    "country": "russia"
  },
  {
    "first": "johann",
    "last": "weber",
    "sex": "male",
    "city": "munich",
    "country": "germany"
  },
  {
    "first": "arjun",
    "last": "singh",
    "sex": "male",
    "city": "delhi",
    "country": "india"
  },
  {
    "first": "leonardo",
    "last": "ferrari",
    "sex": "male",
    "city": "naples",
    "country": "italy"
  }
]
```

## Disclaimer

This package is a work in progress and is not yet ready for production use.

## License

`faker` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
