#Room check
import time, random, pickle, shelve, rooms
from gameItems import itemNames
from collections import Counter

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
        combineDups(roomItems, '')
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
        combineDups(roomMonsters, '')
    else:
        pass

    #Display dead monsters
    if len(deadMonsters) != 0:
        combineDups(deadMonsters, 'dead ')
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
        combineDups(roomNPCs, '')
    else:
        pass


def combineDups(roomContents, adjective):
    if len(roomContents) == 1 and roomContents[0] == '':
        pass
    else:
        roomDupsCnt = Counter(roomContents)
        if len(roomDupsCnt) > 1:
            print("There are ", end='')
        else:
            print("There is ", end='')
        for item in roomDupsCnt:
            if roomDupsCnt[item] > 1: 
                print(str(roomDupsCnt[item]) + " " + adjective + item + "s, ", end='')
            elif item == '':
                pass
            else:
                print(str(roomDupsCnt[item]) + " " + adjective + item + ", ", end='')
        print("here.")

