"""
Few operations to test classes and functions made in rocket module.

"""

from rocket import RocketBoard, Rocket

board = RocketBoard(7, 10, 10)

print(board[0])

rocket = Rocket(speed=12, altitude=4, x=9)

print(rocket.altitude)

board[0].x = 4

print(board[0].get_distance(board[1]))

rocket1 = Rocket(speed=3, altitude=4, x=7)
rocket2 = Rocket(speed=8, altitude=2, x=5)

print(RocketBoard.get_distance(rocket1, rocket2))
