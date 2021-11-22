from dataclasses import dataclass


@dataclass
class Person:
    number: int
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "data scientist"



ahmed = Person()
print(ahmed)
