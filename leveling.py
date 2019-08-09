import gameMonsters as gMon
import pickle, time, random, shelve
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
    strength = charFile["strength"]
    intelligence = charFile["intelligence"]
    dexterity = charFile["dexterity"]
    profession = charFile["profession"]  
    health = charFile["health"]                         
    magic = charFile["magic"]
    charFile.close()  
    attrPts = 4
    oldAttr = [strength, intelligence, dexterity, health, magic]

    print("Now that you are level " + str(newLevel) + ", you have 4 new attribute points that you \ncan assign to your stats as you see fit.")
    print("You current stats are:")
    print("Strength", strength)
    print("Intelligence", intelligence)
    print("Dexterity", dexterity, "\n")

    while attrPts != 0:
        while True:
            print("\nDo you want to add points to STRength, INTelligence, or DEXterity?", end='  ')
            attribute = input()
            if attribute not in ['str', 'int', 'dex']:
                print("You must choose STR for strength, INT for intelligence, or DEX for dexterity.")
            else:
                break
        while True:
            print("How many points do you want to add to " + attribute + "? (You have " + str(attrPts) + " points left.)", end=' ')
            numAttr = input()
            if int(numAttr) > attrPts or int(numAttr) <= 0:
                print("You have " + str(attrPts) + " points to assign.")
            else:
                break
        if attribute.lower() == 'str':
            strength += numAttr
            attrPts = numAttr - numAttr
        elif attribute.lower() == 'int':
            intelligence += numAttr
            attrPts = numAttr - numAttr
        elif attribute.lower() == 'dex':
            dexterity += numAttr
            attrPts = numAttr - numAttr
        else:
            print("There was a problem with assigning attribute points to that stat. Please try again.")
            errorLogFile = open('.\\temp\\errorLog.txt', 'a')
            errorLogFile.write('\n***************** Error while assigning attribute points in leveling *******************\n')
            errorLogFile.close()
    newHealth = strength + dexterity
    newMagic = (intelligence - oldAttr[1]) + oldAttr[4] + random.randint(1, 4)
    print("Your new health is " + newHealth + " and your new magic is " + newMagic + ".\n")