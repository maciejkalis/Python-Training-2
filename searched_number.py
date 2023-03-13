"""
A program that allows you to find the hidden number inside it.

"""

hiddenNumber = 128

i = 0

while i == 0:
    givenNumber = int(input("There is a hidden number inside this program. Try to guess the hidden number: "))

    if givenNumber == hiddenNumber:
        print("Congratulations, you guessed the hidden number! The hidden number is equal to:", hiddenNumber)
        i += 1

    elif givenNumber >= (hiddenNumber - 10) and givenNumber < hiddenNumber:
        print("You are close to guess the number, but you still gave slightly too little number. Try a little higher!")
        continue

    elif givenNumber <= (hiddenNumber + 10) and givenNumber > hiddenNumber:
        print("You are close to guess the number, but you still gave slightly too higher number. Try a little lower!")
        continue

    elif givenNumber < (hiddenNumber - 10):
        print("The number you provided is too small! Try a little higher!")
        continue

    elif givenNumber > (hiddenNumber + 10):
        print("The number you provided is too high! Try a little lower!")
        continue
