"""
A program that calculates the area of a figure selected from the menu.
Script was written to exercise functions usage.

"""

from figures import *

print("""Select the figure for which you want to calculate the area:
Rectangle - 'R'
Square - 'S'
Triangle - 'T'
Trapeze - 'TR'
Circle - 'C'
Exit the program - 'E'""")

i = 0

while i < 1:
    menu = input("Choose operation (R/S/T/TR/C/E): ")
    menuUpper = menu.upper()
    print()

    if menuUpper == "R":
        sideA = int(
            input("Enter the length of the longer side of the rectangle: "))
        sideB = int(
            input("Enter the length of the shorter side of the rectangle: "))

        print("The area of the rectangle is equal to:",
              rectangle_area(sideA, sideB), "\n")

    elif menuUpper == "S":
        side = int(input("Enter the side length of the square: "))

        print("The area of the square is equal to:", square_area(side), "\n")

    elif menuUpper == "T":
        base = int(input("Enter the length of the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))

        print("The area of the triangle is equal to:",
              triangle_area(base, height), "\n")

    elif menuUpper == "TR":
        longBase = int(
            input("Enter the length of the longer base of the trapeze: "))
        shortBase = int(
            input("Enter the length of the shorter base of the trapeze: "))
        height = int(input("Enter the height of the trapeze: "))

        print("The area of the trapeze is equal to:",
              trapeze_area(longBase, shortBase, height), "\n")

    elif menuUpper == "C":
        radius = int(input("Enter the radius of the circle: "))

        print("The area of the circle is equal to:", circle_area(radius), "\n")

    elif menuUpper == "E":
        i += 1

    else:
        print("You didn't choose right operation. Try one more time.", "\n")
