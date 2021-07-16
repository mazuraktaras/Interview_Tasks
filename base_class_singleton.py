class Singleton:
    """The Singleton Class"""
    value = []

    def __new__(cls):
        return cls

    # def __init__(self):
    #     print("in init")

    @staticmethod
    def static_method():
        """Use @staticmethod if no inner variables required"""

    @classmethod
    def class_method(cls):
        """Use @classmethod to access class level variables"""
        print(cls.value)


if __name__ == "__main__":
    # The Client
    # All uses of singleton point to the same memory address (id)
    print(f"id(Singleton)\t= {id(Singleton)}")

    object_1 = Singleton()
    object_2 = Singleton()
    print(f"id(object_1)\t= {id(object_1)}")
    print(f"id(object_2)\t= {id(object_2)}")
    print(object_1 is object_2)
