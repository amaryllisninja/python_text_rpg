import time, gameItems, cmdList, pickle, shelve

def isEquippable(globalItem, action):
    equippedType = []
    equipBool = ''
    itemType = gameItems.itemType[globalItem]
    tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","rb")  
    fileEquipped = pickle.load(tempPickleEquipped)
    tempPickleEquipped.close()
    canEquip = checkMinReqs(globalItem)
    
    if canEquip == True: 
        if len(fileEquipped) != 0 or fileEquipped != [] or fileEquipped != ():
            c = 0
            while c < len(fileEquipped):
                localEquip = fileEquipped[c]
                localType = gameItems.itemType[localEquip]
                equippedType.append(localType)
                c += 1
                
            charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")                          #Get items in char. inventory
            characterEquip = pickle.load(charInvTemp)
            charInvTemp.close()
            
            if globalItem in characterEquip:
                print("A " + globalItem + " is in your inventory.")
                
                globalType = gameItems.itemType[globalItem]
                if globalType in equippedType:
                    if globalItem[:1] == ['a', 'e', 'i', 'o', 'u']:
                        print("You are already have an " + globalType + " equipped.")
                    else:
                        print("You are already have a " + globalType + " equipped.")
                elif globalType not in equippedType:
                    characterEquip.remove(globalItem)                                   #Remove equipped item from inventory pickle
                    if characterEquip == [] or characterEquip == ():
                        characterEquip.append("")
                    else:
                        pass
                    charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")                  #Dump inventory list to pickle
                    pickle.dump(characterEquip, charInvTemp)        
                    charInvTemp.close()

                    tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","rb")    #Dump equipped list to pickle 
                    tempEquippedItems = pickle.load(tempPickleEquipped)
                    tempPickleEquipped.close()
                    tempEquippedItems.append(globalItem)                                 #Add equipped item to equip list
                    tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","bw")    #Dump equipped list to pickle 
                    pickle.dump(tempEquippedItems,tempPickleEquipped)
                    tempPickleEquipped.close()
                    print("You " + action + " the " + globalItem + ".")
                    time.sleep(2)
                else:
                    print("There was a problem with finding if that item was a valid equippable item.")
                
            elif globalItem not in characterEquip:
                print("You do not have that in your inventory.")
                print("Your inventory:\n" + '\n'.join(characterEquip))
            else:
                print("There was a problem with finding that item in your inventory.")
        else:
            print("Nothing is equipped.")
            charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")                             #Get items in char. inventory
            characterEquip = pickle.load(charInvTemp)
            charInvTemp.close()
            if globalItem in characterEquip:
                characterEquip.remove(globalItem)                                           #Remove equipped item from inventory pickle
                charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")                         #Dump inventory list to pickle
                pickle.dump(characterEquip, charInvTemp)        
                charInvTemp.close()
                
                tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","rb")           #Dump equipped list to pickle 
                tempEquippedItems = pickle.load(tempPickleEquipped)
                tempPickleEquipped.close()
                tempEquippedItems.append(globalItem)                                        #Add equipped item to equip list
                tempPickleEquipped = open(".\\temp\\tempPickleEquipped.pkl","bw")           #Dump equipped list to pickle 
                pickle.dump(tempEquippedItems,tempPickleEquipped)
                tempPickleEquipped.close()
                
                print("You " + action + " the " + globalItem + ".")
                time.sleep(2)
            elif globalItem not in characterEquip:
                print("You do not have that in your inventory.")
                print("Your inventory:\n" + '\n'.join(characterEquip))
            else:
                print("There was a problem with equipping an item from your inventory.")
    else:
        itemReqs = gameItems.minReqs[globalItem]
        print("You can not use " + globalItem + " yet. Your Strenth, Intelligence, and Dexterity must be ")
        print(str(itemReqs[0]) + ", " + str(itemReqs[1]) + ", and " + str(itemReqs[2]) + ".\n")

def checkMinReqs(item):
    charStatsTemp = open(".\\temp\\charStatsTemp.pkl","rb")
    charStats = pickle.load(charStatsTemp)
    charStatsTemp.close()
    itemStats = gameItems.minReqs[item]
    if int(itemStats[0]) > int(charStats[0]):
        return False
    elif int(itemStats[1]) > int(charStats[1]):
        return False
    elif int(itemStats[2]) > int(charStats[2]):
        return False
    else:
        return True