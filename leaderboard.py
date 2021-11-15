from abstract import ABCMeta, abstractmethod


class Leaderboard:
    """The Leaderboard as a Singleton"""
    _table = {}

    def __new__(cls):
        return cls

    @classmethod
    def print(cls):
        """A class level method"""
        print('-----------Leaderboard-----------')
        for key, value in sorted(cls._table.items()):
            print(f'|\t{key}\t|\t{value}\t|')
        print()

    @classmethod
    def add_winner(cls, position, name):
        """A class level method"""
        cls._table[position] = name


class IGame(metaclass=ABCMeta):
    """A Game Interface"""

    @staticmethod
    @abstractmethod
    def add_winner(position, name):
        """Must implement add_winner"""


class Game1(IGame):
    """Game1 implements IGame"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)


class Game2(IGame):
    """Game2 implements IGame"""

    def __init__(self):
        self.leaderboard = Leaderboard()

    def add_winner(self, position, name):
        self.leaderboard.add_winner(position, name)


if __name__ == "__main__":
    game_one = Game1()
    game_one.add_winner(2, 'Artem')
    game_one.add_winner(1, 'Gennadiy')

    game_two = Game2()
    game_two.add_winner(3, 'Taras')

    game_one.leaderboard.print()
    game_two.leaderboard.print()
