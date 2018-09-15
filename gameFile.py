# Complete game module
import random, time, pickle, shelve, gameItems, rooms, gameActions, checkRoom, dialogue, os
from loadCharacter import loadCharModule

loadCharModule()
file = open("tempCharName.pkl","rb")                #Load character name
name = pickle.load(file)
#print(name)
time.sleep(2)

print("\n\n\nGame Loading...\n\n\n")
charFile = shelve.open(name + "SaveFile")           #Load character
location = charFile["location"]                     #Load character location
characterEquip = charFile["inventory"]              #Load character inventory
charGold = charFile["gold"]                         #Load character gold
health = charFile["health"]                         #Load character HP
magic = charFile["magic"]                           #Load character MP
fileEquipped = charFile["equipped"]                 #Load equipped items
tempPickleEquipped = open("tempPickleEquipped.pkl","bw")  
pickle.dump(fileEquipped,tempPickleEquipped)
tempPickleEquipped.close()

print("Tip: Type HELP if this is your first time playing this game.")
time.sleep(1)

####### Reload all values to clear unsaved pickle values #######
fileHP = open("charHealthTemp.pkl","bw")            #Load HP
pickle.dump(health, fileHP)
fileHP.close()
fileMP = open("charMagicTemp.pkl","bw")             #Load MP
pickle.dump(magic, fileMP)
fileMP.close()

print("You are standing in the " + rooms.roomNames[location])
time.sleep(1)
print(rooms.roomNames[location])
print(rooms.roomDescriptions[location])
fileLoc = open("tempPickleLoc.pkl","bw")            #Save character location to pickle
pickle.dump(location,fileLoc)
fileLoc.close()
itemsBoolean = checkRoom.checkRoomItems()            
itemsBoolPlk = open("itemsBoolPlk.pkl","bw")        #Save boolean for existence of items
pickle.dump(itemsBoolean,itemsBoolPlk)
itemsBoolPlk.close()
charInvTemp = open("charInvTemp.pkl","bw")
pickle.dump(characterEquip,charInvTemp)
charInvTemp.close()

tempPickleItems = open("tempPickleItems.pkl","rb")  #Get current items in rooms for character
roomItems = pickle.load(tempPickleItems)
tempPickleItems.close()
tempRoomItems = open("tempPickleItems.pkl","bw")    
pickle.dump(roomItems,tempRoomItems)
tempRoomItems.close()

tempRoomMonsters = charFile["roomMonsters"]     #Get current live monsters
tempPickleMonsters = open("tempPickleMonsters.pkl","bw")    
pickle.dump(tempRoomMonsters,tempPickleMonsters)
tempPickleMonsters.close()

tempDeadMonsters = charFile["deadMonsters"]     #Get current dead monsters
tempPickleDeadMon = open("tempPickleDeadMon.pkl","bw")
pickle.dump(tempDeadMonsters,tempPickleDeadMon)
tempPickleDeadMon.close()

tempPickleLootedMon = open("tempPickleLootedMon.pkl","rb")  #Get current looted monsters
tempLootedMonsters = pickle.load(tempPickleLootedMon) 
tempPickleLootedMon.close()

tempPickleGold = open("tempPickleGold.pkl","bw")
pickle.dump(charGold, tempPickleGold)
tempPickleGold.close()

charFile.close()
time.sleep(1)
checkRoom.checkRoomMonsters()
checkRoom.checkRoomNPCs()

print("")

while True:
    gameActions.checkAction(name)

