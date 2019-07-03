import gameMonsters as gMon
import pickle
from math import trunc

def addXP(name, monster):
    tempPickleXP = open(".\\temp\\tempPickleXP.pkl", "rb")
    charXP = pickle.load(tempPickleXP)
    tempPickleXP.close()
    oldLevel = checkLevel(charXP)

    if monster != '':
        monXP = gMon.monsterXP[monster]                     #Get Monster's experience points
        newCharXP = charXP + monXP                          #Add XP to character's xp total
        tempPickleXP = open(".\\temp\\tempPickleXP.pkl", "bw")
        pickle.dump(newCharXP, tempPickleXP)                #Save XP to pickle 
        tempPickleXP.close()
        newLevel = checkLevel(newCharXP)
        checkLevelUp(name, oldLevel, newLevel)
    else:
        print("Could not obtain monster name and info.")


def checkLevel(xp):
    if xp == 0:
        level = 0
    else:
        level = trunc((xp/2000) + 1)
    return level


def checkLevelUp(name, oldLevel, newLevel):
    if newLevel > oldLevel:
        print("You have leveled up!\nYou are now level " + newLevel + "\n\n")
        time.sleep(1)
        levelChar(name, newLevel)
    else:
        pass


def levelChar(name, newLevel):
    pass