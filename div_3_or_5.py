
def div_3_or_5_(low, high):
    for number in range(low, high + 1):

        if number % 3 == 0 and number % 5 == 0:
            print(number)
            print('by 3 and 5')
            continue
        if number % 3 == 0:
            print(number)
            print('by 3')
        if number % 5 == 0:
            print(number)
            print('by 5')


div_3_or_5_(1, 60)
