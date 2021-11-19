from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    @abstractmethod
    def method_one(self):
        pass

    @abstractmethod
    def method_two(self):
        pass


class Concrete(Base):

    def method_one(self):
        print('Do something')


    def method_two(self):
        print('Do something')


instance = Concrete()
