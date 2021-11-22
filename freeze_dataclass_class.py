from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    first_name: str = "Ahmed"
    last_name: str = "Besbes"
    age: int = 30
    job: str = "data scientist"


ahmed = Person()
print(ahmed)

ahmed.age = 45

print(ahmed)
