"""
Simple game created to practice "random" library functions.

In the game player is moving only forward through five steps
and at each step there is a chance to draw a chest or nothing along the way.

Depending on the color of the drawn chest,
the player gets a different amount of gold.

The boxes have different colors.

The color of the chest indicates how rare the chest is.

green - 75%
orange - 20%
violet - 4%
gold (legendary) - 1%

It's set there is a 40% chance you won't meet anything.
60% that there will be a chest.

The amount of gold that can be drop from different chests:

green - 1000,
orange - 4000,
violet - 9000,
gold - 16000

"""
import random

from enum import Enum


def findApproximateValue(value, percentRange):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)


Event = Enum("Event", ["CHEST", "EMPTY"])

eventDictionary = {
    Event.CHEST: 0.6,
    Event.EMPTY: 0.4
}

# Creates a list whose elements will be the keys taken from the eventDictionary
eventList = list(eventDictionary.keys())

# Creates a list whose elements will be the values (probability)
# taken from the eventDictionary
eventProbability = list(eventDictionary.values())

Colors = Enum(
    "Colors", {
        "Green": "green",
        "Orange": "orange",
        "Purple": "purple",
        "Gold": "gold"
    }
)

chestColorsDictionary = {
    Colors.Green: 0.75,
    Colors.Orange: 0.2,
    Colors.Purple: 0.04,
    Colors.Gold: 0.01
}

chestColorList = tuple(chestColorsDictionary.keys())
chestColorProbability = tuple(chestColorsDictionary.values())

rewardsForChest = {
    chestColorList[reward]: ((reward + 1) * (reward + 1)) * 1000
    for reward in range(len(chestColorList))
}

gameLength = 5

goldAcquired = 0

print("Welcome in my game called CHAMBER")
print("""You have only 5 steps to make,
see yourself how much gold you gonna acquire till the end!""")

while gameLength > 0:

    gameAnswer = input("Do you want to move forward?")
    if (gameAnswer == "yes" or gameAnswer == "Yes"):
        print("Great, let's see what you've got...")
        drawnEvent = random.choices(eventList, eventProbability)[0]

        if (drawnEvent == Event.CHEST):
            print("You've drown a CHEST!")
            drawnColor = random.choices(
                chestColorList, chestColorProbability)[0]
            print("The chest color is", drawnColor.value)

            gamerReward = findApproximateValue(
                rewardsForChest[drawnColor], 10)

            print("In the chest you've found there is:", gamerReward, "gold!")

            goldAcquired = goldAcquired + gamerReward

        elif (drawnEvent == Event.EMPTY):
            print("You've drown nothing, you are so unlucky!")

    else:
        print("You can go just straight man... nothing else, this game is dumb :P")
        continue

    gameLength -= 1


print("Congratulation, you have acquired:", goldAcquired, "gold!")
