"""
A program that adds three even, positive numbers.

"""

result = 0

i = 0

while i < 3:
    givenNumber = int(input("Enter a positive, even number: "))
    if (givenNumber > 0) and (givenNumber % 2 == 0):
        result += givenNumber
        i += 1

    else:
        print("You were supposed to enter an even, positive number. Try again!")
        continue
print("The sum of the given numbers is", result)
