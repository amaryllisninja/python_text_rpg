import pickle, random, time, shelve, dialogue, rooms, checkRoom, roll, rooms, os
import gameItems as gI
import gameMonsters as gMon

def lootMon(charName, monster):
    #Load current room
    tempPickleLoc = open("tempPickleLoc.pkl","rb")      
    room = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    
    #Get current dead monsters in room for character
    tempPickleDeadMon = open("tempPickleDeadMon.pkl","rb")
    tempDeadMonsters = pickle.load(tempPickleDeadMon)
    tempPickleDeadMon.close()

    if os.path.isfile('tempPickleLootedMon.pkl') == True:
        #Get current looted monsters in room for character
        tempPickleLootedMon = open("tempPickleLootedMon.pkl","rb")
        tempLootedMonsters = pickle.load(tempPickleLootedMon) 
        tempPickleLootedMon.close()
        #print("Pickle exists!", tempLootedMonsters)
    else:
        #Create pickle for looted monsters
        tempLootedMonsters = []
        for c in range(0, len(rooms.roomNames)):
            tempLootedMonsters.append('')
            tempLootedMonsters[c] = list(tempLootedMonsters[c])
            c += 1
        tempPickleLootedMon = open("tempPickleLootedMon.pkl", 'bw')
        pickle.dump(tempLootedMonsters,tempPickleLootedMon)
        tempPickleLootedMon.close()
        #print("Pickle didn't exist.", tempLootedMonsters)

    
    if monster in tempDeadMonsters[room] and monster not in tempLootedMonsters[room]:
        percent = gMon.monsterDropPercentage[monster]
        percent = int(percent[0])
        percentRoll = roll.rollDice(1, 100)
        droppedList = []        
        
        if percentRoll <= percent:
            #print("You get an item!")
            monItems = gMon.monsterItems[monster]
            numMonItems = len(monItems)
            chanceOfEachItem = int((1/numMonItems)*100)
            
            for c in range(0, numMonItems):
                chanceToGetItem = roll.rollDice(1, 100)
                #print(monItems, numMonItems, chanceOfEachItem, chanceToGetItem)
                if chanceToGetItem >= chanceOfEachItem*c and chanceToGetItem <= chanceOfEachItem*(c+1):
                    itemObtained = monItems[c]
                    droppedList.append(itemObtained)
                else:
                    #print("Didn't get item number " + str(c))
                    pass
                c += 1
            print("On " + monster + ", you found:")
            print('/n'.join(droppedList))
            #print(tempLootedMonsters, room, len(tempLootedMonsters))
            #print(tempLootedMonsters)
        else:
            print("You found nothing on the " + monster + ".")
        tempLootedMonsters[room].append(monster)
        tempPickleLootedMon = open("tempPickleLootedMon.pkl", 'bw') #Add monster to 'looted' list
        pickle.dump(tempLootedMonsters,tempPickleLootedMon)
        tempPickleLootedMon.close()

        charInvTemp = open("charInvTemp.pkl","rb")
        inventory = pickle.load(charInvTemp)
        charInvTemp.close()

        for item in droppedList:
            inventory.append(item)
        #print(inventory)
        charInvTemp = open("charInvTemp.pkl","bw")
        pickle.dump(inventory,charInvTemp)
        charInvTemp.close()

    elif monster not in tempDeadMonsters[room]:
        print("There is no dead " + monster + " here.")

    elif monster in gI.itemNames:
        print("Why don\'t you try \'getting\' and item?")
        time.sleep(1)
        
    elif monster in tempLootedMonsters[room]:
        print("You have already looted the " + monster + ".")

    else:
        print("There was an error finding a monster to loot.")
            



