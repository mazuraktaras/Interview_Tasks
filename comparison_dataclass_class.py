class Person:
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.first_name,
                self.last_name,
                self.age,
                self.job) == (other.first_name,
                              other.last_name,
                              other.age,
                              other.job)


ivan = Person('Ivan', 'Ivanov', 45, 'programmer')

print(ivan.first_name, ivan.age, ivan.last_name, ivan.job)
print(ivan)

ivan_other = Person('Ivan', 'Ivanov', 45, 'programmer')

print(ivan == ivan_other)

