# unsorted_list = [27, 7, 5, 14, 2, 3, 3, 3, 9, 8, 6]
import random

# unsorted_list = [27, 7, 3, 4, 12]

# unsorted_list = [random.randint(1, 1000) for x in range(10)]

unsorted_list = [7, 1, 1, 6, 5, 4, 3, 2, 1]


def quick_sort(list_):
    if len(list_) <= 1:
        return list_
    # pivot = list_[4]
    pivot = list_[len(list_) // 2]

    left_list = list(filter(lambda x: x < pivot, list_))
    center_list = [elem for elem in list_ if elem == pivot]
    right_list = list(filter(lambda x: x > pivot, list_))
    return quick_sort(left_list) + center_list + quick_sort(right_list)


print(unsorted_list[0])
# unsorted_list[0] = 3
# unsorted_list[0], unsorted_list[1] = unsorted_list[1], unsorted_list[0]
print(unsorted_list[0])
print(unsorted_list[1])

print(quick_sort(unsorted_list))
sorted_ = 0
while True:

    for i in range(len(unsorted_list) - 1 - sorted_):
        print(f'Compare {unsorted_list[i]} and {unsorted_list[i + 1]}')
        if unsorted_list[i] > unsorted_list[i + 1]:
            unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
    sorted_ += 1
    print(unsorted_list)
    if sorted_ == len(unsorted_list) - 1:
        break


def bubble_sort(list_):
    while True:
        sorted_ = 0
        for i in range(len(list_) - 1):
            print(f'Compare {list_[i]} and {list_[i + 1]}')
            if list_[i] > list_[i + 1]:
                list_[i], list_[i + 1] = list_[i + 1], list_[i]
                sorted_ += 1
                print(list_)
        if sorted_ == 0:
            break
    return list_

# print(bubble_sort(unsorted_list))
# print(random.randint(0, 100), [random.randint(1, 100) for x in range(10)])
