from dataclasses import dataclass, astuple, asdict


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str


ivan = Person('Ivan', 'Ivanov', 45, 'programmer')

print(ivan)

print(astuple(ivan))
print(asdict(ivan))
