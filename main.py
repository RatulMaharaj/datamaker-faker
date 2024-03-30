class FirstName:
    def __init__(self) -> None:
        self.path = "first name path"
        self.seed = ""

        def generate():
            print("Generating data")

        self.generate = generate


class Person:
    def __init__(self) -> None:
        self.location = "some_location"
        self.first_name = FirstName()


person = Person()
print(person.first_name.path)
