"""
A random game simulator that draws 6 unique numbers out of 49

"""
import random

# ver 1. - the correct probability of drawing the numbers is not maintained here
# just a training example


def choose_random_numbers(amount, total_amount):
    i = 0
    drawnNumbers = []

    while i < amount:
        randomNumber = random.randint(0, total_amount)
        if randomNumber in drawnNumbers:
            continue
        else:
            drawnNumbers.append(randomNumber)
            i += 1
    return drawnNumbers


print(choose_random_numbers(6, 49))

# ver 2. correct probability


def choose_random_numbers2(amount, total_amount):
    print(random.sample(range(total_amount + 1), amount))


choose_random_numbers2(6, 49)
