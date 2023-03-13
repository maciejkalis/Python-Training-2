"""
Find numbers from 100 to 470 (included) that are:
- divisible by 7 but not divisible by 5

Use the methods below:
1) Generator
2) List comprehension
3) Set comprehension
4) Dictionary Comprehension

"""

# ver. 1 - generator

numbersGenerator = (
    number
    for number in range(100, 471)
    if (number % 7 == 0) and (number % 5 != 0)
)

# ver. 2 - List comprehension

numbers = [
    number
    for number in range(100, 471)
    if (number % 7 == 0) and (number % 5 != 0)
]

# print(numbers)

# ver. 3 - Set comprehension

numbers2 = {
    number
    for number in range(100, 471)
    if (number % 7 == 0) and (number % 5 != 0)
}

# print(numbers2)

# ver. 4 - Dictionary Comprehension

numbers3 = {
    number: number**2
    for number in range(100, 471)
    if (number % 7 == 0) and (number % 5 != 0)
}

print(numbers3)
