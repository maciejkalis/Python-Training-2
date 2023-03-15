"""
Write a function that takes a list of numbers as an argument and returns the sum of all the positive numbers in the list.
The function should ignore all negative numbers or zeros in the list.

"""

# ver. 1

x = [1, 3, -4, 0, -5, 6, 8]


def list_numbers_sum(list):
    sum = 0
    for number in list:
        if number > 0:
            sum += number
    return sum


function = list_numbers_sum(x)

print(function)


# ver. 2

"""
The version with list expression.

"""


def sum_positives(list):
    return sum([number for number in list if number > 0])


function2 = sum_positives(x)

print(function2)
