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
