import random

def rollDice(numDice, die):
    numDice = int(numDice)
    die = int(die)
    result = random.randint(numDice, die*numDice)
    return result

def ryansRollDice(sides, dice):  # Sides is the number of sides on the die
    rollingList = []
    for i in range(dice):
        rollingList.append(random.randint(1, sides))
    return rollingList

