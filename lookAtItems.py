# Look at an item
import time
import random
import pickle
import shelve
import gameItems

inventory = ['short sword', 'padded armour', 'small shield']

print("You are standing in the middle of a well-lit, quiet room. You have some equipment on you.")
print("Your inventory includes:")
print('\n'.join(inventory))

while True:
    print("What do you do?")
    action = input().lower().split()
    action.append("")
    if action[0] == 'look':
        if action[1] == '':
            print("You look around you.")
        elif action[1] == 'at':
            action.remove("look")
            action.remove("at")
            action = ' '.join(action)
            action = action[:-1]
            print(action)
            if action in inventory:
                print(gameItems.itemDescriptions[action])
            elif action == 'inventory':
                print('\n'.join(inventory))
            else:
                print("That item is not in your inventory. Please try again.")


