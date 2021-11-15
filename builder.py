class Computer:
    def __init__(self):
        self.name = 'Computer'
        self.cpu = None
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = (f'Product name: {self.name}',
                f'CPU: {self.cpu} Hhz',
                f'Memory: {self.memory} GB',
                f'Hard Disk: {self.hdd} GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._product = Computer()
        self._product.gpu = 'external'

    def max_cpu_and_memory(self):
        self._product.cpu = 4
        self._product.memory = 64

    def min_cpu_and_memory(self):
        self._product.cpu = 1
        self._product.memory = 8

    def custom_hdd(self, hdd):
        self._product.hdd = hdd

    def max_hdd(self):
        self._product.hdd = 3000

    def min_hdd(self):
        self._product.hdd = 500

    @property
    def product(self):
        product = self._product
        self.reset()
        return product


class Director:
    def __init__(self, _builder):
        self.builder = _builder

    def make_max_config(self):
        builder.max_cpu_and_memory()
        builder.max_hdd()
        return self.builder

    def make_min_config(self):
        builder.min_cpu_and_memory()
        builder.min_hdd()
        return self.builder

    def make_max_config_custom_hdd(self):
        builder.max_cpu_and_memory()
        builder.custom_hdd(2000)
        return self.builder


if __name__ == "__main__":
    # computer_max = Computer()
    # computer_max.memory = 32
    # computer_max.cpu = 4
    # computer_max.hdd = 3000
    # computer_max.gpu = 'external'
    # print(computer_max)

    builder = ComputerBuilder()

    builder.max_cpu_and_memory()
    builder.max_hdd()
    computer_max = builder.product
    print(computer_max)
    print()

    builder.min_cpu_and_memory()
    builder.min_hdd()
    computer_min = builder.product
    print(computer_min)
    print()

    builder = ComputerBuilder()
    director = Director(builder)
    # director.make_max_config()
    director.make_min_config()
    computer = builder.product
    print(computer) # #
# builder
# bbbbbb
