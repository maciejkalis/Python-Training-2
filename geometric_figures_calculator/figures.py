import math


def rectangle_area(a, b):
    return a * b


def square_area(a):
    return a ** 2


def triangle_area(a, h):
    return int(0.5 * a * h)


def trapeze_area(a, b, h):
    return int(0.5 * (a + b) * h)


def circle_area(r):
    return math.pi * r ** 2
