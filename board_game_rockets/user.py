"""


"""


class User:

    NextId = 1  # static / class variable

    def __init__(self, name):

        self.name = name
        self.id = User.NextId
        User.NextId += 1

    def __str__(self) -> str:
        return "User name: " + self.name + "\nHis id: " + str(self.id) + "\n"
