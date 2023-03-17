import random


cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


random.shuffle(cardList)

deckPlayerOne = []

deckPlayerTwo = []

n = 0

while n < 5:
    card = cardList.pop()
    deckPlayerOne.append(card)

    card = cardList.pop()
    deckPlayerTwo.append(card)

    n += 1

print(deckPlayerOne)

print(deckPlayerTwo)
