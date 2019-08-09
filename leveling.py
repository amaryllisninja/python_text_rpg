import gameMonsters as gMon
import pickle, time
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
        print("\nAdded " + str(monXP) + " experience points. You now have " + str(newCharXP) + " experience points.")
    else:
        print("Could not obtain monster name and info.")


def checkLevel(xp):
    if xp == 0:
        level = 0
    elif xp != 0:
        level = trunc((xp/2000) + 1)
    else:
        errorLogFile = open('.\\temp\\errorLog.txt', 'a')
        errorLogFile.write('\n***************** Error in leveling *******************\n')
        errorLogFile.write('An error occured while checking level.')
        errorLogFile.close()
    return level


def checkLevelUp(name, oldLevel, newLevel):
    if newLevel > oldLevel:
        print("You have leveled up!\nYou are now level " + str(newLevel) + "\n\n")
        time.sleep(1)
        levelChar(name, newLevel)
    else:
        pass


def levelChar(name, newLevel):
    saveFileName = ".\\charsaves\\" + name.lower().replace(" ", "") + "SaveFile"
    charFile = shelve.open(saveFileName)                #Load character
    profession = charFile["profession"]    
    if profession == 'mercenary':
        print("You are a mercenary. You ")
    if profession == 'thaumaturge':
        print("You are a thaumaturge. ")
    if profession == 'thief':
        print("You are a thief. ")
    else:
        errorLogFile = open('.\\temp\\errorLog.txt', 'a')
        errorLogFile.write('\n***************** Error in leveling *******************\n')
        errorLogFile.write('An error occured while checking profession.')
        errorLogFile.close()