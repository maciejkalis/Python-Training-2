"""
Program which counts occurrence of given word in the loaded file.

"""

path = "text.txt"

wordToCount = "cat"

try:
    with open(path, "r") as file:
        text = file.read()

        numberOfOccurrence = text.count(wordToCount)

        print(
            f"Word '{wordToCount}' in the given file named '{path}' occurred {numberOfOccurrence} time/times")

except FileNotFoundError:
    print(f"There is not file '{path}' in the directory!")

except PermissionError:
    print(f"You do not have permission to read the file '{path}'!")
