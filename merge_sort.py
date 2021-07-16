# Merge two lists

# first_list    [2, 3, 7, 7, 9, 11, 12]
# first_index                       ^
#                0  1  2  3  4  5   6
#
# second_list   [4, 5, 6, 10, 11, 12]
# second_index                     ^
#                0  1  2   3   4   5


# first_list = [2, 3, 7, 7, 9, 11, 12]
# # first_list = [2, 3, 14, 27]
# second_list = [4, 5, 6, 10, 11, 12]
# first_index = second_index = 0
#
# merged_list = []
#
# print(len(first_list), len(second_list))
#
# while first_index < len(first_list) and second_index < len(second_list):
#     if first_list[first_index] < second_list[second_index]:
#         merged_list.append(first_list[first_index])
#         first_index += 1
#     else:
#         merged_list.append(second_list[second_index])
#         second_index += 1
#
# if first_index < len(first_list):
#     print(first_index)
#     merged_list += first_list[first_index:]
#
# if second_index < len(second_list):
#     print(second_index)
#     merged_list += second_list[second_index:]
#
# print(merged_list, first_index, second_index)
# from typing import List


def merge_sorted_lists(first_list, second_list):
    first_index = second_index = 0

    merged_list = []

    # print(len(first_list), len(second_list))

    while first_index < len(first_list) and second_index < len(second_list):
        if first_list[first_index] < second_list[second_index]:
            merged_list.append(first_list[first_index])
            first_index += 1
        else:
            merged_list.append(second_list[second_index])
            second_index += 1

    if first_index < len(first_list):
        # print(first_index)
        merged_list += first_list[first_index:]

    if second_index < len(second_list):
        # print(second_index)
        merged_list += second_list[second_index:]

    # print(merged_list, first_index, second_index)
    return merged_list


# unsorted_list = [7, 5, 2, 3, 9, 8, 6]
# unsorted_list = [27, 7, 5, 14, 2, 3, 9, 8, 6]
unsorted_list: list[int] = [6, 2, 7]


def merge_sort(list_):
    if len(list_) == 1:
        return list_

    middle = len(list_) // 2
    left_list = merge_sort(list_[:middle])
    right_list = merge_sort(list_[middle:])
    print(left_list, right_list)

    return merge_sorted_lists(left_list, right_list)


# merge_sorted_lists([7],[5, 11])
print(merge_sort(unsorted_list))

# print(div_list([1]))

# print(div_list(unsorted_list))
