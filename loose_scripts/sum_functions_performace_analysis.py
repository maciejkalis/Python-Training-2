"""
A program that calculates the sum of numbers from 1 to a given number
using various methods and checking the efficiency of each method.

"""
import time

givenNumber = int(input("Enter the number: "))

# ver. 1 for loop


def sum_to_given_number1(number):
    result = 0
    for i in range(1, number + 1):
        result += i
    return result


# ver. 2 list comprehension


def sum_to_given_number2(finalNumber):
    return sum([number for number in range(1, finalNumber + 1)])


# ver. 3 set comprehension


def sum_to_given_number3(finalNumber):
    return sum({number for number in range(1, finalNumber + 1)})


# ver. 4 generator


def sum_to_given_number4(finalNumber):
    return sum((number for number in range(1, finalNumber + 1)))


# ver. 5 sum of the range function output alone


def sum_to_given_number5(finalNumber):
    return sum(range(1, finalNumber + 1))


# ver. 6 Using the formula for the sum of the n - first terms
# of the arithmetic sequence


def sum_to_given_number6(finalNumber):
    return int((1 + finalNumber) / 2 * finalNumber)


def finish_timer(start):
    end = time.perf_counter()
    return end - start


def function_performance(func, arg):
    start = time.perf_counter_ns()
    func(arg)
    end = time.perf_counter_ns()
    return end - start


print(function_performance(sum_to_given_number1, givenNumber))
print(function_performance(sum_to_given_number2, givenNumber))
print(function_performance(sum_to_given_number3, givenNumber))
print(function_performance(sum_to_given_number4, givenNumber))
print(function_performance(sum_to_given_number5, givenNumber))
print(function_performance(sum_to_given_number6, givenNumber))
