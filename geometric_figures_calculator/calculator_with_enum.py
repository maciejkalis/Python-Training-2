"""
A program that calculates the area of a figure selected from the menu made to exercise creation of the own functions.

"""

import figures

from enum import IntEnum

Figures_Menu = IntEnum("Figures_Menu", {
                       "Rectangle": 1, "Square": 2, "Triangle": 3, "Trapeze": 4, "Circle": 5, "Exit": 6})

print("""Select the figure for which you want to calculate the area:
Rectangle - 1
Square - 2
Triangle - 3
Trapeze - 4
Circle - 5
Exit the program - 6""")

i = 0

while i < 1:
    menu = int(input(
        "Choose number corresponding to the figure, which area you want to calculate: "))
    print()

    if menu == Figures_Menu.Rectangle:
        sideA = int(
            input("Enter the length of the longer side of the rectangle: "))
        sideB = int(
            input("Enter the length of the shorter side of the rectangle: "))

        print("The area of the rectangle is equal to:",
              figures.rectangle_area(sideA, sideB), "\n")

    elif menu == Figures_Menu.Square:
        side = int(input("Enter the side length of the square: "))

        print("The area of the square is equal to:",
              figures.square_area(side), "\n")

    elif menu == Figures_Menu.Triangle:
        base = int(input("Enter the length of the base of the triangle: "))
        height = int(input("Enter the height of the triangle: "))

        print("The area of the triangle is equal to:",
              figures.triangle_area(base, height), "\n")

    elif menu == Figures_Menu.Trapeze:
        longBase = int(
            input("Enter the length of the longer base of the trapeze: "))
        shortBase = int(
            input("Enter the length of the shorter base of the trapeze: "))
        height = int(input("Enter the height of the trapeze: "))

        print("The area of the trapeze is equal to:",
              figures.trapeze_area(longBase, shortBase, height), "\n")

    elif menu == Figures_Menu.Circle:
        radius = int(input("Enter the radius of the circle: "))

        print("The area of the circle is equal to:",
              figures.circle_area(radius), "\n")

    elif menu == Figures_Menu.Exit:
        i += 1

    else:
        print("You didn't choose right operation. Try one more time.", "\n")
