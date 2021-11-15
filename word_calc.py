import string


def letters_calc(input_string):
    alphabet = string.ascii_lowercase
    count = 0
    for letter in input_string:
        count += alphabet.index(letter) + 1
    return count


st = 'zebra'
print(letters_calc(st))
# dev commit
# dev commit
# dev commit
