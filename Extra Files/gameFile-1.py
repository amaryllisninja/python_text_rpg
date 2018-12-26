# Complete game module
import random
import time
import pickle
import shelve
from loadCharacter import loadCharModule
import gameItems
import rooms
import gameActions

loadCharModule()
time.sleep(2)

print("\n\n\nGame Loading...\n\n\n")
charFile = shelve.open(name + "SaveFile")
location = charFile["location"]
time.sleep(2)
print(location)

print("You are standing in the" + room.roomNames[location])
time.sleep(1)
print("You feel like your feet are glued to the floor.\n")
time.sleep(1)

print(rooms.roomNames[0])
print(rooms.roomDescriptions[0])

gameActions.checkAction()
