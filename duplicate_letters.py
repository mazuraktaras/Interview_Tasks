def remove_duplicates(input_string):
    result_string = ''
    for letter in input_string:
        if letter not in result_string:
            result_string += letter
    return result_string


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # _string = 'aabcdfeffccm'
    _string = 'abdabccdde'
    print(remove_duplicates(_string))
