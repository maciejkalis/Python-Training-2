"""
It's a simple, theoretical board game made to practice object-oriented paradigm of programming.
In this module there are two classes defined.
The based one - Rocket, there is constructor which defines attributes such as:
- altitude
- speed
- x coordinate of "rocket object"

Second class RocketBoard creates board object with list of Rocket objects inside.

There are methods such as moveUp() or get_distance() to move objects on board randomly,
based on defined attributes and calculates the distance between them accordingly.

The get_distance() method has been defined in the Rocket class
(in which can be called from object created based on that class), as well as in the RocketBoard
in which it was defined as static method so it is possible to call the function
directly from the class.

"""
from __future__ import annotations
from random import randint, randrange
from math import sqrt


class Rocket:
    id = 0

    def __init__(self, speed: float = 1, altitude: float = 0, x: float = 0):
        self.altitude = altitude
        self.speed = speed
        self.x = x
        Rocket.id += 1
        self.id = Rocket.id

    def moveUp(self):
        self.altitude += self.speed

    def __str__(self):
        return "The altitude of the rocket is " + str(self.altitude) + " and rocket x = " + str(self.x)

    def get_distance(self, rocket: Rocket) -> float:
        ac = (rocket.x - self.x) ** 2
        bc = (rocket.altitude - self.altitude) ** 2
        return sqrt(ac + bc)


class RocketBoard:
    def __init__(self, amountOfRockets: int = 5, altitude: float = 0, x: float = 0):
        self.rockets = [
            Rocket(randint(1, 6), altitude, x)
            for _ in range(amountOfRockets)
        ]

        for _ in range(10):
            rocketIndexToMove = randrange(len(self.rockets))
            self.rockets[rocketIndexToMove].moveUp()

        for rocket in self.rockets:
            print(rocket)

    def __getitem__(self, key: int) -> Rocket:
        return self.rockets[key]

    def __setitem__(self, key, value):
        self.rockets[key].altitude = value

    def get_amount_of_rockets(self):
        return len(self.rockets)

    def __len__(self):
        return self.get_amount_of_rockets()

    @staticmethod
    def get_distance(rocket1: Rocket, rocket2: Rocket) -> float:
        ac = (rocket2.x - rocket1.x) ** 2
        bc = (rocket2.altitude - rocket1.altitude) ** 2
        return sqrt(ac + bc)
