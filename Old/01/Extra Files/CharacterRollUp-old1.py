# Character roll up program
import random

characterStats = [strength, intelligence, dexterity]

def welcomePlayer():
    print("Welcome to the Character Roll Up game!/n")

def whatToDo():
    print("What would you like to do?")
    print("You can 'display' at your current stats, 'roll' new stats, or ask for 'help'.")
    response = input()
    if response == 'display':
        displayStats()
    elif response == 'roll':
        rollDice(characterStats)
    elif response == 'help':
        print("Type 'display' to see your current stats, 'roll' to roll up new stats.")
    else:
        print("I'm sorry. I didn't understand your response.")
        break
  
def rollDice(chatacterStats):
    print(Rolling 3d6...)
    input()
    
    characterStats[0] = random.randint(1, 18)
    characterStats[1] = random.randint(1, 18)
    characterStats[2] = random.randint(1, 18)
    
    return characterStats

def displayStats(characterStats):
    print("Your character's stats are:")
    print("\nStrength: " + characterStats[0])
    print("\nIntelligence: " + characterStats[1])
    print("\nDexterity: " + characterStats[2])
    
def playAgain():
    print("Would you like to play again? (y/n)")
    playState = input()
    return playState
    
while playState != 'n':
    welcomePlayer()
    whatToDo()
    playAgain()