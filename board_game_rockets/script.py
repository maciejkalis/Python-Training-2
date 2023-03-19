from user import User
from rocket import Rocket

users = [
    User("John")
    for _ in range(8)
]

rockets = [
    Rocket()
    for _ in range(5)
]

for user in users:
    print(user.id)

for rocket in rockets:
    print(rocket.id)

print("The next id will be equal to:", User.NextId)
