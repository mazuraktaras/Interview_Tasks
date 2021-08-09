from abc import ABC, abstractmethod


# ------------ Product Base Class ------------

class Shirt(ABC):

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_textile_amount(self):
        pass


class Cap:

    def __init__(self, size):
        self.size = size

    @abstractmethod
    def get_size(self):
        pass

    @abstractmethod
    def get_textile_amount(self):
        pass


# ------------ Concrete Product Classes ------------
# Shirts
class TShirt(Shirt):
    def get_size(self):
        return self.size

    def get_textile_amount(self):
        return 100


class ClassicShirt(Shirt):
    def get_size(self):
        return self.size

    def get_textile_amount(self):
        return 200


# Caps
class SportCap(Cap):
    def get_size(self):
        return self.size

    def get_textile_amount(self):
        return 50


class ClassicCap(Cap):
    def get_size(self):
        return self.size

    def get_textile_amount(self):
        return 70


# ------------ Fabric Base Class ------------


# ------------ Fabric Concrete (child) Classes ------------

class Fabric:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def make_shirt(self):
        if self.type == 1:
            return ClassicShirt(self.size)
        elif self.type == 2:
            return TShirt(self.size)

    def make_cup(self):
        if self.type == 1:
            return ClassicCap(self.size)
        elif self.type == 2:
            return SportCap(self.size)


product_line = ((1, 42), (1, 43), (2, 40), (2, 38), (2, 12))


# ------------ Main code ------------

def production(a):
    textile_quantity = 0

    for i in a:
        wear_collection = Fabric(i[0], i[1])

        textile_quantity += wear_collection.make_shirt().get_textile_amount()
        textile_quantity += wear_collection.make_cup().get_textile_amount()

    return textile_quantity


print(production(product_line))
