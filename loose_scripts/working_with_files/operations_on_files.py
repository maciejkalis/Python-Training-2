"""
Load names and surnames from a file named:
namesSurnames.txt

1) split them up to make a list of tuples, where the inner tuples are
first/last pairs
2) save the names to the file names.txt
3) save the names to the file surnames.txt

"""

namesAndSurnames = []

with open("namesSurnames.txt", "r", encoding="UTF-8") as file:
    for line in file:
        namesAndSurnames.append(tuple(line.replace("\n", "").split(" ")))


with open("names.txt", "w", encoding="UTF-8") as file:
    for item in namesAndSurnames:
        file.write(item[0] + "\n")

with open("surnames.txt", "w", encoding="UTF-8") as file:
    for item in namesAndSurnames:
        try:
            file.write(item[1] + "\n")
        except IndexError:
            file.write("\n")
