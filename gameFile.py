# Complete game module
import random, time, pickle, shelve, gameItems, rooms, gameActions, checkRoom, dialogue, os
from loadCharacter import loadCharModule

currentLoc = os.getcwd

loadCharModule()
file = open(".\\temp\\tempCharName.pkl","rb")                #Load character name
name = pickle.load(file)
#print(name)
time.sleep(1)

print("\n\n\nGame Loading...\n\n\n")
saveFileName = ".\\charsaves\\" + name.lower().replace(" ", "") + "SaveFile"
charFile = shelve.open(saveFileName)                #Load character
location = charFile["location"]                     #Load character location
characterEquip = charFile["inventory"]              #Load character inventory
charGold = charFile["gold"]                         #Load character gold
health = charFile["health"]                         #Load character HP
magic = charFile["magic"]                           #Load character MP
fileEquipped = charFile["equipped"]                 #Load character equipped items
charXP = charFile["experience"]

####### Reload all values to clear unsaved pickle values #######
fileHP = open(".\\temp\\charHealthTemp.pkl","bw")                   #Load HP
pickle.dump(health, fileHP)
fileHP.close()
fileMP = open(".\\temp\\charMagicTemp.pkl","bw")                    #Load MP
pickle.dump(magic, fileMP)
fileMP.close()
tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","bw")   #Load equipped  
pickle.dump(fileEquipped,tempPickleEquipped)
tempPickleEquipped.close()
tempPickleXP = open(".\\temp\\tempPickleXP.pkl", "rb")              #Load XP
charXP = pickle.load(tempPickleXP)
tempPickleXP.close()
time.sleep(1)

print("You are standing in the " + rooms.roomNames[location])
time.sleep(1)
print(rooms.roomNames[location])
print(rooms.roomDescriptions[location])
fileLoc = open(".\\temp\\tempPickleLoc.pkl","bw")            #Save character location to pickle
pickle.dump(location,fileLoc)
fileLoc.close()
itemsBoolean = checkRoom.checkRoomItems()            
itemsBoolPlk = open(".\\temp\\itemsBoolPlk.pkl","bw")        #Save boolean for existence of items
pickle.dump(itemsBoolean,itemsBoolPlk)
itemsBoolPlk.close()
charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")
pickle.dump(characterEquip,charInvTemp)
charInvTemp.close()

tempPickleItems = open(".\\temp\\tempPickleItems.pkl","rb")  #Get current items in rooms for character
roomItems = pickle.load(tempPickleItems)
tempPickleItems.close()
tempRoomItems = open(".\\temp\\tempPickleItems.pkl","bw")    
pickle.dump(roomItems,tempRoomItems)
tempRoomItems.close()

tempRoomMonsters = charFile["roomMonsters"]     #Get current live monsters
tempPickleMonsters = open(".\\temp\\tempPickleMonsters.pkl","bw")    
pickle.dump(tempRoomMonsters,tempPickleMonsters)
tempPickleMonsters.close()

tempDeadMonsters = charFile["deadMonsters"]     #Get current dead monsters
tempPickleDeadMon = open(".\\temp\\tempPickleDeadMon.pkl","bw")
pickle.dump(tempDeadMonsters,tempPickleDeadMon)
tempPickleDeadMon.close()

tempPickleLootedMon = open(".\\temp\\tempPickleLootedMon.pkl","rb")  #Get current looted monsters
tempLootedMonsters = pickle.load(tempPickleLootedMon) 
tempPickleLootedMon.close()

tempPickleGold = open(".\\temp\\tempPickleGold.pkl","bw")
pickle.dump(charGold, tempPickleGold)
tempPickleGold.close()

charFile.close()
time.sleep(1)
checkRoom.checkRoomMonsters()
checkRoom.checkRoomNPCs()

print("")

while True:
    gameActions.checkAction(name)

