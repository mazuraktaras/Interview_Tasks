import random

list_ = [1, 2, 3, 4, 5, 6]


while len(list_) > 0:
    print(list_.pop(random.randint(1, len(list_))-1))

