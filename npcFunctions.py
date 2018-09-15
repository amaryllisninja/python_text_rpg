#NPC functions and actions
import gameNPCs as gN
import gameItems as gI
import rooms, random, time, pickle, shelve

def getNPCType(npcName):
    npcType = gN.npcType[npcName]
    return npcType

def talk(npcName):
    talkList = gN.npcTalk[npcName]
    randNum = random.randint(0, len(talkList))
    print(talkList[randNum])

def farewell(npcName):
    farewellList = gN.npcFarewell[npcName]
    randNum = random.randint(0, len(farewellList))
    print(farewellList[randNum])

def buy(npcName):
    shopkeepInventory = gN.shopkeepInventory[npcName]
    for c in range(len(shopkeepInventory)):
        itemToBuy = shopkeepInventory[c]
        print(itemToBuy + ' - ' + str(gI.itemPrices[itemToBuy]) + 'G')
    print("What do you want to buy?")
    buy = input()
    if buy in shopkeepInventory and buy != '':
        price = gI.itemPrices[buy]
        print("You buy the " + buy + ".")
        tempPickleGold = open("tempPickleGold.pkl","rb")
        charGold = pickle.load(tempPickleGold)
        tempPickleGold.close()
        for i in range(len(shopkeepInventory)):
            if buy == shopkeepInventory[i]:
                invNum = i
                break
            else:
                pass
        charGold = charGold - price
        tempPickleGold = open("tempPickleGold.pkl","bw")
        pickle.dump(charGold, tempPickleGold)
        tempPickleGold.close()
        charInvTemp = open("charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        characterEquip.append(buy)
        charInvTemp = open("charInvTemp.pkl","bw")
        pickle.dump(characterEquip, charInvTemp)
        charInvTemp.close()
    elif buy == '':
        print("I didn\'t get that. Please try again.")
    else:
        print("\'I\'m sorry, but I don\'t sell that,\' " + npcName + " says.")

def sell(npcName):
    pass
    
def interaction(npcName):
    npcType = getNPCType(npcName)
    greetStr = gN.npcGreeting[npcName]
    print(greetStr)

    #NPC interaction loop
    while True:
        print(gN.npcOptPrompt[npcType], end='  ')
        choice = input()
        choice = choice.lower()
        
        if choice in gN.npcOptions[npcType]:
            if choice == 'directions':
                print("\'I can/'t give you directions, yet. You/'re on your own.\'")
            elif choice == 'talk':
                talk(npcName)
            elif choice == 'leave':
                farewell(npcName)
                time.sleep(1)
                break
            elif choice == 'buy':
                buy(npcName)
            elif choice == 'sell':
                sell(npcName)
            
        else:
            print("You can\'t " + choice + " with " + npcName + ".")
            time.sleep(1)
