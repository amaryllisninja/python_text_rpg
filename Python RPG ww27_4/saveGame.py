import shelve
import pickle
import time

def save(name):
    print("Saving your game...")

    file = shelve.open(name + "SaveFile")
    tempPickleLoc = open("tempPickleLoc.pkl","bw")
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
    tempLocFile = open("tempLoc.pkl","bw")
