"""
A simple calculator written in Python to recall conditional statements.

"""

print("Welcome to Simple Calculator!")

choice = int(input("""Select the operation: 1 - multiplication, 2 - division, 3 - addition, 4 - subtraction, 5 - exponentiation
Choice: """))

print("Enter the numbers you want to operate on.")

a = int(input("a = "))
b = int(input("b = "))

if (choice == 1):
    print("The result of multiplying numbers a =",
          a, "and b =", b, "is equal to:", a * b)

elif (choice == 2):
    if (b == 0):
        print("You cannot divide by zero. Choose a different number b!")

    else:
        print("The result of dividing numbers a =", a,
              "and b =", b, "is equal to:", int(a / b))

elif (choice == 3):
    print("The result of adding numbers a =", a,
          "and b =", b, "is equal to:", a + b)

elif (choice == 4):
    print("The result of subtracting numbers a =",
          a, "and b =", b, "is equal to:", a - b)

elif (choice == 5):
    print("The result of exponentiation of numbers a =",
          a, "and b =", b, "is equal to:", a ** b)

else:
    print("You have not made a valid operation selection.")
