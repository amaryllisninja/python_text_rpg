import shelve
import time
import random

characterStats = ['strength', 'intelligence', 'dexterity']

print("Rolling 3d6...")
time.sleep(2)
    
characterStats[0] = random.randint(3, 18)
characterStats[1] = random.randint(3, 18)
characterStats[2] = random.randint(3, 18)

characterStats[0] = str(characterStats[0])
characterStats[1] = str(characterStats[1])
characterStats[2] = str(characterStats[2])

print(characterStats)
time.sleep(2)

# Save to shelve
file = shelve.open(characterStats[0] + "charShelve")

file["strength"] = characterStats[0]
file["intelligence"] = characterStats[1]
file["dexterity"] = characterStats[2]


print(file["strength"])
print(file["intelligence"])
print(file["dexterity"])

print(dict(file))
