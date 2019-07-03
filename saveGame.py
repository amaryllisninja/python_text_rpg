import shelve
import pickle
import time

def save(name):
    print("Saving your game...")

    saveFileName = ".\\charsaves\\" + name.lower().replace(" ", "") + "SaveFile"
    file = shelve.open(saveFileName)                #Load character
    tempPickleLoc = open(".\\temp\\tempPickleLoc.pkl","bw")
    '''characterStats[0] = file["strength"]
    characterStats[1] = file["intelligence"]
    characterStats[2] = file["dexterity"]
    characterEquip = file["inventory"]'''
    location = tempPickleLoc
    file.close()
    time.sleep(1)

    print("Saved.")
    time.sleep(1)

def pickleLocation():
    tempLocFile = open(".\\temp\\tempLoc.pkl","bw")
