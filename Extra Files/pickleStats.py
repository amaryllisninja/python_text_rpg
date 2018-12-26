import pickle
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

file = open("charData.pkl","bw")
pickle.dump(characterStats,file)
file.close()

print("Exporting/importing file...")
time.sleep(1)

newFile = open("charData.pkl","rb")
recoveredNumbers = pickle.load(newFile)
print(recoveredNumbers)

numberList = str(recoveredNumbers)

print('\n'.join(numberList))

file.close()
