# Open file from shelveTut.py

import shelve

importStats = ['stre', 'inte', 'dext']

stats = shelve.open("charShelve")

importStats = stats
stats = str(stats)
strength = importStats["strength"]
intelligence = importStats["intelligence"]
dexterity = importStats["dexterity"]

print("Your strength is: " + strength)
print("Your intelligence is: " + intelligence)
print("Your dexterity is: " + dexterity)
