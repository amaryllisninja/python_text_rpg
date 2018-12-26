import time, gameItems, cmdList, pickle, shelve

def isEquippable(globalItem, action):
    equippedType = []
    equipBool = ''
    itemType = gameItems.itemType[globalItem]
    tempPickleEquipped = open("tempPickleEquipped.pkl","rb")  
    fileEquipped = pickle.load(tempPickleEquipped)
    tempPickleEquipped.close()
    #print(fileEquipped)

    if len(fileEquipped) != 0 or fileEquipped != [] or fileEquipped != ():
        c = 0
        while c < len(fileEquipped):
            localEquip = fileEquipped[c]
            localType = gameItems.itemType[localEquip]
            equippedType.append(localType)
            c += 1
            
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        
        if globalItem in characterEquip:
            print("A " + globalItem + " is in your inventory.")
            globalType = gameItems.itemType[globalItem]
            if globalType in equippedType:
                if globalItem[:1] == ['a', 'e', 'i', 'o', 'u']:
                    print("You are already " + action + "ing an " + globalItem)
                else:
                    print("You are already " + action + "ing a " + globalItem)
            elif globalType not in equippedType:
                characterEquip.remove(globalItem)               #Remove equipped item from inventory pickle
                if characterEquip == [] or characterEquip == ():
                    characterEquip.append("")
                else:
                    pass
                charInvTemp = open("charInvTemp.pkl","bw")      #Dump inventory list to pickle
                pickle.dump(characterEquip, charInvTemp)        
                charInvTemp.close()

                tempPickleEquipped = open("tempPickleEquipped.pkl","rb")    #Dump equipped list to pickle 
                tempEquippedItems = pickle.load(tempPickleEquipped)
                tempPickleEquipped.close()
                tempEquippedItems.append(globalItem)                        #Add equipped item to equip list
                tempPickleEquipped = open("tempPickleEquipped.pkl","bw")    #Dump equipped list to pickle 
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
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        if globalItem in characterEquip:
            characterEquip.remove(globalItem)               #Remove equipped item from inventory pickle
            charInvTemp = open("charInvTemp.pkl","bw")      #Dump inventory list to pickle
            pickle.dump(characterEquip, charInvTemp)        
            charInvTemp.close()
            
            tempPickleEquipped = open("tempPickleEquipped.pkl","rb")        #Dump equipped list to pickle 
            tempEquippedItems = pickle.load(tempPickleEquipped)
            tempPickleEquipped.close()
            tempEquippedItems.append(globalItem)                            #Add equipped item to equip list
            tempPickleEquipped = open("tempPickleEquipped.pkl","bw")        #Dump equipped list to pickle 
            pickle.dump(tempEquippedItems,tempPickleEquipped)
            tempPickleEquipped.close()
            
            print("You " + action + " the " + globalItem + ".")
            time.sleep(2)
        elif globalItem not in characterEquip:
            print("You do not have that in your inventory.")
            print("Your inventory:\n" + '\n'.join(characterEquip))
        else:
            print("There was a problem with equipping an item from your inventory.")

