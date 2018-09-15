# Allowable game actions
import rooms, random, time, pickle, shelve, gameItems
import checkRoom, dialogue, cmdList, equipFuncs, gameMonsters
import atk

def save(name):
    print("Saving...")
    charSaveFile = shelve.open(name + "SaveFile")
    
    charStatsTemp = open("charStatsTemp.pkl","rb")
    fileStats = pickle.load(charStatsTemp)
    #print(fileStats)
    charSaveFile["strength"] = fileStats[0]
    charSaveFile["intelligence"] = fileStats[1]
    charSaveFile["dexterity"] = fileStats[2]
    charStatsTemp.close()
    
    charInvTemp = open("charInvTemp.pkl","rb")
    fileInv = pickle.load(charInvTemp)
    charSaveFile["inventory"] = fileInv
    #print(fileInv)
    charInvTemp.close()
    
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    fileLoc = pickle.load(tempPickleLoc)
    charSaveFile["location"] = fileLoc
    tempPickleLoc.close()

    tempPickleItems = open("tempPickleItems.pkl","rb")
    fileItems = pickle.load(tempPickleItems)
    charSaveFile["roomItems"] = fileItems
    tempPickleItems.close()

    tempPickleEquipped = open("tempPickleEquipped.pkl","rb")  
    fileEquipped = pickle.load(tempPickleEquipped)
    charSaveFile["equipped"] = fileEquipped
    tempPickleEquipped.close()
    #print(fileEquipped)

    tempPickleDC = open("tempPickleDC.pkl","rb")
    fileDC = pickle.load(tempPickleDC)
    charSaveFile["deathCount"] = fileDC
    tempPickleDC.close()

    #Get current live monsters in room for character
    tempPickleMonsters = open("tempPickleMonsters.pkl","rb")    
    tempRoomMonsters = pickle.load(tempPickleMonsters)
    charSaveFile["roomMonsters"] = tempRoomMonsters
    tempPickleMonsters.close()

    #Get current dead monsters in room for character
    tempPickleDeadMon = open("tempPickleDeadMon.pkl","rb")
    tempDeadMonsters = pickle.load(tempPickleDeadMon)
    charSaveFile["deadMonsters"] = tempDeadMonsters
    tempPickleDeadMon.close()
    
    charSaveFile.close()    #Close character save file

    print("Saved.")
    print("Oh, boy! Are we gonna do something dangerous?")
    time.sleep(1)
    
# Moving from room to room
def canMove(moveDirection, directionsOpen, roomsConnectedTo, name):
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    location = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    if moveDirection == 'n' and moveDirection == directionsOpen[0]:
        print("You go North.")
        location = roomsConnectedTo[0]
        print("After moving, you are now in " + rooms.roomNames[int(location)] + ".")
    elif moveDirection == 'e' and moveDirection == directionsOpen[1]:
        print("You go East.")
        location = roomsConnectedTo[1]
        print("After moving, you are now in " + rooms.roomNames[int(location)] + ".")
    elif moveDirection == 's' and moveDirection == directionsOpen[2]:
        print("You go South.")
        location = roomsConnectedTo[2]
        print("After moving, you are now in " + rooms.roomNames[int(location)] + ".")
    elif moveDirection == 'w' and moveDirection == directionsOpen[3]:
        print("You go West.")
        location = roomsConnectedTo[3]
        print("After moving, you are now in " + rooms.roomNames[int(location)] + ".")
    else:
        print("You cannot go that way.")
        print(moveDirection)
    time.sleep(1)
    return location


# Start of moving code
def move(name):
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    location = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[location].split()

    print("Which direction do you go?")
    moveDirection = input().lower()
    moveDirection = moveDirection[:1]
    time.sleep(1)
    #print(str(location) + moveDirection)
    location = canMove(moveDirection, directionsOpen, roomsConnectedTo, name)

    print(rooms.roomNames[int(location)] + "\n" + rooms.roomDescriptions[int(location)])
    
    time.sleep(1)
    location = int(location)
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[int(location)].split()
    tempPickleLoc = open("tempPickleLoc.pkl","bw") #Temporary file to store location in
    pickle.dump(location,tempPickleLoc) #Save location to pickle
    tempPickleLoc.close()
    return


def moveTo(name,moveDirection):
    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    location = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[location].split()

    location = canMove(moveDirection, directionsOpen, roomsConnectedTo, name)

    print(rooms.roomNames[int(location)] + "\n" + rooms.roomDescriptions[int(location)])
    
    location = int(location)
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[int(location)].split()
    tempPickleLoc = open("tempPickleLoc.pkl","bw") #Temporary file to store location in
    pickle.dump(location,tempPickleLoc) #Save location to pickle
    tempPickleLoc.close()
    
    itemsBoolean = checkRoom.checkRoomItems()       #Display room items, if any
    itemsBoolPlk = open("itemsBoolPlk.pkl","bw")    #Save boolean for existence of items
    pickle.dump(itemsBoolean,itemsBoolPlk)
    itemsBoolPlk.close()

    checkRoom.checkRoomMonsters()     #Display room monsters, if any

    time.sleep(1)
    return


def checkAction(name):
    print("\nWhat do you do?")                  #Asks for initial input
    action = input().lower().split()
    action.append("")
    tempPickleItems = open("tempPickleItems.pkl","rb")  #Get current items in rooms for character
    tempRoomItems = pickle.load(tempPickleItems)
    tempPickleItems.close()
    tempPickleMonsters = open("tempPickleMonsters.pkl","rb")  #Get current monsters in rooms for character
    tempRoomMonsters = pickle.load(tempPickleMonsters)
    tempPickleMonsters.close()

    #Process to follow for 'look' action
    if action[0] == 'look':                     
        if action[1] == '':
            print("You look around you.\n")
            time.sleep(1)
            tempPickleLoc = open("tempPickleLoc.pkl","rb")
            location = pickle.load(tempPickleLoc)
            tempPickleLoc.close()
            print(rooms.roomNames[int(location)] + "\n" + rooms.roomDescriptions[int(location)])
            checkRoom.checkRoomItems()
            checkRoom.checkRoomMonsters()
        elif action[1] == 'at':
            del action[0]
            del action[0]
            action = ' '.join(action)
            action = action[:-1]
            tempPickleInv = open("charInvTemp.pkl","rb")
            inventory = pickle.load(tempPickleInv)
            tempPickleInv.close()
            tempPickleLoc = open("tempPickleLoc.pkl","rb")
            location = pickle.load(tempPickleLoc)
            tempPickleLoc.close()
            if action in inventory:
                print(gameItems.itemDescriptions[action])
                time.sleep(1)
            elif action in tempRoomMonsters[location]:
                print(gameMonsters.monsterDescriptions[action])
                time.sleep(1)
            elif action == 'inventory':
                print('\n'.join(inventory))
                time.sleep(1)
            elif action == '' or action == ' ':
                print("Please tell me what you want to look at.")
            elif action == 'self':
                charSaveFile = shelve.open(name + "SaveFile")
                fileName = charSaveFile["name"]
                fileStrength = charSaveFile["strength"]
                fileIntelligence = charSaveFile["intelligence"]
                fileDexterity = charSaveFile["dexterity"]
                fileHealth = charSaveFile["health"]
                fileMagic = charSaveFile["magic"]
                fileProfession = charSaveFile["profession"]

                tempPickleEquipped = open("tempPickleEquipped.pkl","rb")    #Load equipped list 
                tempEquipped = pickle.load(tempPickleEquipped)
                tempPickleEquipped.close()

                tempHealthFile = open("tempHealthFile.pkl","rb")    #Load temp health
                tempHP = pickle.load(tempHealthFile)
                tempHealthFile.close()
                tempMagicFile = open("tempMagicFile.pkl","rb")      #Load temp magic
                tempMP = pickle.load(tempMagicFile)
                tempMagicFile.close()
                
                charSaveFile.close()
                print("You look at yourself.")
                time.sleep(1)
                print("\nYour strength is " + fileStrength)
                print("Your intelligence is " + fileIntelligence)
                print("Your dexterity is " + fileDexterity)
                print("Your health points are ", ''.join(fileHealth))
                print("Your magic points are ", ''.join(fileMagic))
                print("You are a " + fileProfession)
                print("You are are equipped with:\n" + '\n'.join(tempEquipped) + "\n")
            else:
                print("That isn't here. Try typing the full name of what you're looking at.")
                dialogue.narrator()
                time.sleep(1)

    #Process to follow for 'save' action
    elif action[0] == 'save':                     
        save(name)

    #Process to follow for 'quit' action
    elif action[0] == 'quit':                     
        print("Would you like to save? (y/n)")
        choice = input()
        if choice == 'y':
            save(name)
            quit()
        else:
            quit()
            
    #Process to follow for 'go' action
    elif action[0] in cmdList.moveCmdList:
        if action[1] == '':
            move(name)
        elif action[1] == 'north' or action[1] == 'n':
                direction = action[1][:1]
                moveTo(name,direction)
        elif action[1] == 'east' or action[1] == 'e':
                direction = action[1][:1]
                moveTo(name,direction)
        elif action[1] == 'south' or action[1] == 's':
                direction = action[1][:1]
                moveTo(name,direction)
        elif action[1] == 'west' or action[1] == 'w':
                direction = action[1][:1]
                moveTo(name,direction)
        else:
            print("I don't understand what you mean.")
            dialogue.narrator()

    #Process to follow for 'help'
    elif action[0] == 'help':
        import helpMe

    #Process to follow for 'get'
    elif action[0] in cmdList.getCmdList:
        itemsBoolPlk = open("itemsBoolPlk.pkl","rb")    #Boolean to see if items are in room
        itemsBoolean = pickle.load(itemsBoolPlk)
        itemsBoolPlk.close()
        tempPickleItems = open("tempPickleItems.pkl","rb")  #Get current items in rooms for character
        tempRoomItems = pickle.load(tempPickleItems)
        tempPickleItems.close()
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        

        if itemsBoolean == True:
            if action[1] == '':
                print(action[0].title() + " what?")
            else:
                tempPickleLoc = open("tempPickleLoc.pkl","rb")
                location = pickle.load(tempPickleLoc)
                tempPickleLoc.close()
                item = []
                c = 1

                while c <= len(action):
                    if action[c] != '':
                        item.append(action[c])
                        #print(item, action)
                        c += 1
                    elif action[c] == '':
                        break
                item = ' '.join(item) 
                
                if item in rooms.roomItems[location] and item in tempRoomItems[location]:
                    print("You " + action[0] + " the " + item + ".")
                    characterEquip.append(item)
                    charInvTemp = open("charInvTemp.pkl","bw")
                    pickle.dump(characterEquip, charInvTemp)
                    charInvTemp.close()
                    tempRoomItems[location].remove(item)
                    tempPickleItems = open("tempPickleItems.pkl","bw")  
                    pickle.dump(tempRoomItems,tempPickleItems)
                    tempPickleItems.close()
                    time.sleep(2)
                else:
                    print("A " + item + " is not in this room.")
                    time.sleep(2)

        else:
            print("There are no items in this room.")

    #Process to follow for 'drop'
    elif action[0] in cmdList.dropCmdList:      
        tempPickleItems = open("tempPickleItems.pkl","rb")  #Get current items in rooms for character
        tempRoomItems = pickle.load(tempPickleItems)
        tempPickleItems.close()
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()

        if action[1] == '':
            print(action[0].title() + " what?")
        else:
            tempPickleLoc = open("tempPickleLoc.pkl","rb")
            location = pickle.load(tempPickleLoc)
            tempPickleLoc.close()
            item = []
            c = 1

            while c <= len(action):
                if action[c] != '':
                    item.append(action[c])
                    #print(item, action)
                    c += 1
                elif action[c] == '':
                    break
            item = ' '.join(item) 
            
            if item in characterEquip:
                print("You " + action[0] + " the " + item + ".")
                characterEquip.remove(item)
                charInvTemp = open("charInvTemp.pkl","bw")
                pickle.dump(characterEquip, charInvTemp)
                charInvTemp.close()
                tempRoomItems[location].append(item)
                tempPickleItems = open("tempPickleItems.pkl","bw")  
                pickle.dump(tempRoomItems,tempPickleItems)
                tempPickleItems.close()
                time.sleep(2)
            else:
                print("A " + item + " is not in your inventory.")
                time.sleep(2)

    #Process to follow for 'equip'            
    elif action[0] in cmdList.equipCmdList:
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        tempPickleEquipped = open("tempPickleEquipped.pkl","rb")    #Load items equipped
        tempEquippedItems = pickle.load(tempPickleEquipped)
        tempPickleEquipped.close()
        #print(tempEquippedItems)

        if action[1] == '':
            print(action[0].title() + " what?")
            item = ''
        else:
            item = []
            c = 1

            while c <= len(action): #Creating 'item' string
                if action[c] != '':
                    item.append(action[c])
                    #print(item, action)
                    c += 1
                elif action[c] == '':
                    break
            item = ' '.join(item)
            act0 = action[0]
        if item in gameItems.itemNames and item != '':
            equipFuncs.isEquippable(item, act0)
        elif item == '':
            pass
        else:
            print(item.title() + " isn't a valid item.")

    #Process to follow for 'unequip'
    elif action[0] in cmdList.unequipCmdList:
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        tempPickleEquipped = open("tempPickleEquipped.pkl","rb")    #Load items equipped
        tempEquippedItems = pickle.load(tempPickleEquipped)
        tempPickleEquipped.close()
        #print(tempEquippedItems)

        if action[1] == '':
            print(action[0].title() + " what?")
        else:
            item = []
            c = 1

            while c <= len(action): #Creating 'item' string
                if action[c] != '':
                    item.append(action[c])
                    #print(item, action)
                    c += 1
                elif action[c] == '':
                    break
            item = ' '.join(item) 
            
            if item in tempEquippedItems:  #If item is in character inventory
                print("You " + action[0] + " the " + item + ".")
                characterEquip.append(item)                     #Add equipped item to inventory pickle
                charInvTemp = open("charInvTemp.pkl","bw")      
                pickle.dump(characterEquip, charInvTemp)
                charInvTemp.close()

                tempEquippedItems.remove(item)                              #Remove equipped item from equip list
                tempPickleEquipped = open("tempPickleEquipped.pkl","bw")    #Dump equipped list to pickle 
                pickle.dump(tempEquippedItems,tempPickleEquipped)
                tempPickleEquipped.close()
                time.sleep(2)
            else:
                print("A " + item + " is not equipped.")
                time.sleep(2)

    #Process to follow for 'attack'
    elif action[0] in cmdList.attackCmdList:
        atk.attack(action, name)
            

    #Funny dialogue actions
    elif action[0] == 'snark':
        dialogue.narrator()
    elif action[0] == 'advice':
        dialogue.advice()
    elif action[0] == 'fortune':
        dialogue.fortune()
    else:
        print("That's not a command I recognize.\n\n")
        dialogue.narrator()
