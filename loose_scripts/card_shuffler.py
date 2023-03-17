import random


cardList = ["9", "9", "9", "9",
            "10", "10", "10", "10",
            "Jack", "Jack", "Jack", "Jack",
            "Queen", "Queen", "Queen", "Queen",
            "King", "King", "King", "King",
            "Ace", "Ace", "Ace", "Ace",
            "Joker", "Joker"]


def card_croupier(deck, player_1, player_2):
    random.shuffle(deck)
    player_1 = []
    player_2 = []
    n = 0

    while n < 5:
        card = deck.pop()
        player_1.append(card)

        card = deck.pop()
        player_2.append(card)
        n += 1
    return player_1, player_2


print(card_croupier(cardList, "Maciej", "Kamil"))
