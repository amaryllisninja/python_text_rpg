# Character roll up program
import random

characterStats = ['strength', 'intelligence', 'dexterity']
playState = 'y'

def welcomePlayer():
    print("Welcome to the Character Roll Up game!\n")

def displayStats(characterStats):
    print("Your character's stats are:")
    print("Strength: " + characterStats[0])
    print("Intelligence: " + characterStats[1])
    print("Dexterity: " + characterStats[2])

def rollDice(chatacterStats):
    print("Rolling 3d6...")
    input()
    
    characterStats[0] = random.randint(1, 18)
    characterStats[1] = random.randint(1, 18)
    characterStats[2] = random.randint(1, 18)

    characterStats[0] = str(characterStats[0])
    characterStats[1] = str(characterStats[1])
    characterStats[2] = str(characterStats[2])

    displayStats(characterStats)
    
def playAgain():
    print("Would you like to play again? (y/n)")
    playState = input()
    return playState

def whatToDo():
    print("You can 'display' at your current stats, 'roll' new stats, or ask for 'help'.")
    print("What would you like to do?")
    response = input()
    if response == 'display':
        displayStats(characterStats)
    elif response == 'roll':
        rollDice(characterStats)
    elif response == 'help':
        print("Type 'display' to see your current stats, 'roll' to roll up new stats.\n")
    else:
        print("I'm sorry. I didn't understand your response.\n")
        
welcomePlayer()
    
while playState == 'y':
    whatToDo()
    playState = playAgain()

