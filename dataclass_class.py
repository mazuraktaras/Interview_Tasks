from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str


ivan = Person('Ivan', 'Ivanov', 45, 'programmer')

print(ivan.first_name, ivan.age, ivan.last_name, ivan.job)
print(ivan)

ivan_other = Person('Ivan', 'Ivanov', 45, 'programmer')

print(ivan == ivan_other)
