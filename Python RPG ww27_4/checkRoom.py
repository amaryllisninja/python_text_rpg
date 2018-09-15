#Room check
import time
import random
import pickle
import shelve
import rooms
from gameItems import itemNames

def checkRoomItems():
    #Get current location
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    room = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    tempPickleItems = open("tempPickleItems.pkl","rb")  #Get current items in rooms for character
    tempRoomItems = pickle.load(tempPickleItems)
    tempPickleItems.close()
    roomItems = tempRoomItems[room]
    
    if len(roomItems) != 0:
        if roomItems[0] != '':
            print("There is a ", end="")
            for c in range(len(roomItems)):
                if c == 0:
                    print(roomItems[0], end="")
                elif c > 0 and roomItems[c] != '':
                    print(" and a " + roomItems[c], end="")
            print(" here.")            
        else:
            pass
        return True
    else:
        return False

#Check room for monsters
def checkRoomMonsters():
    #Get current location
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    room = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    #Get current monsters in rooms for character
    tempPickleMonsters = open("tempPickleMonsters.pkl","rb")  
    tempRoomMonsters = pickle.load(tempPickleMonsters)
    tempPickleMonsters.close()
    roomMonsters = tempRoomMonsters[room]
    #Get current dead monsters in rooms for character
    tempPickleDeadMon = open("tempPickleDeadMon.pkl","rb")
    tempDeadMonsters = pickle.load(tempPickleDeadMon)
    tempPickleDeadMon.close()
    deadMonsters = tempDeadMonsters[room]

    #Display live monsters
    if len(roomMonsters) != 0:
        if roomMonsters[0] != '':
            print("There is a ", end="")
            for c in range(len(roomMonsters)):
                if c == 0:
                    print(roomMonsters[0], end="")
                elif c > 0:
                    print(" and a " + roomMonsters[c], end="")
            print(" here.")
        else:
            pass
    else:
        pass

    #Display dead monsters
    if len(deadMonsters) != 0:
        if deadMonsters[0] != '':
            print("There is a dead ", end="")
            for c in range(len(deadMonsters)):
                if c == 0:
                    print(deadMonsters[0], end="")
                elif c > 0:
                    print(" and a dead " + deadMonsters[c], end="")
            print(" rotting here.")
        else:
            pass
    else:
        pass

def checkRoomNPCs():
    #Get current location
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    room = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    tempPickleNPCs = open("tempPickleNPCs.pkl","rb")
    tempNPCs = pickle.load(tempPickleNPCs)
    tempPickleNPCs.close()
    roomNPCs = tempNPCs[room]
    if len(roomNPCs) != 0:
        if roomNPCs[0] != '':
            for person in range(len(roomNPCs)):
                if person == 0:
                    print(roomNPCs[person].title(), end="")
                elif person >= 0:
                    print(" and " + roomNPCs[person], end="")
            if len(roomNPCs) == 1:
                print(" is standing here.")
            else:
                print(" are standing here.")
    else:
        pass
