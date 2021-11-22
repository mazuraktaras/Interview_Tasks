from dataclasses import dataclass, field
from typing import Any


@dataclass
class Person:
    first_name: Any = "Ivan"
    last_name: str = "Ivanov"
    age: int = 45
    job: str = "programmer"
    full_name: str = field(init=False, repr=False)

    def __post_init__(self):
        self.full_name = self.first_name + " " + self.last_name

    def make_somth(self):
        self.test = 10


ivan = Person()
print(ivan)
# Person(first_name='Ahmed', last_name='Besbes', age=30, job='Data Scientist', full_name='Ahmed Besbes')

print(ivan.full_name, ivan.make_somth(), ivan.__dict__)
