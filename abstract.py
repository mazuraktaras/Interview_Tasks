class Base:
    def method_one(self):
        raise NotImplementedError()

    def method_two(self):
        raise NotImplementedError()


class Concrete(Base):
    def method_one(self):
        print('Do something')


instance = Concrete()

instance.method_one()
instance.method_two()
