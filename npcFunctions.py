#NPC functions and actions
import gameNPCs as gN
import gameItems as gI
import rooms, random, time, pickle, shelve

def getNPCType(npcName):
    npcType = gN.npcType[npcName]
    return npcType

def talk(npcName):
    talkList = gN.npcTalk[npcName]
    randNum = random.randint(0, (len(talkList) - 1))
    print(talkList[randNum])

def farewell(npcName):
    farewellList = gN.npcFarewell[npcName]
    randNum = random.randint(0, len(farewellList) - 1)
    print(farewellList[randNum])

def buy(npcName):
    tempPickleGold = open(".\\temp\\tempPickleGold.pkl","rb")
    charGold = pickle.load(tempPickleGold)
    tempPickleGold.close()
    if getNPCType(npcName) == 'merchant':
        merchantInventory = gN.merchantInventory[npcName]
        for c in range(len(merchantInventory)):
            itemToBuy = merchantInventory[c]
            print(itemToBuy + ' - ' + str(gI.itemPrices[itemToBuy]) + 'G')
        print("What do you want to buy?")
        buy = input()
        if buy in merchantInventory and charGold != '':
            price = gI.itemPrices[buy]
            tempPickleGold = open(".\\temp\\tempPickleGold.pkl","rb")
            charGold = pickle.load(tempPickleGold)
            tempPickleGold.close()
            if price <= int(charGold):
                print("You buy the " + buy + ".")
                for i in range(len(merchantInventory)):
                    if buy == merchantInventory[i]:
                        invNum = i
                        break
                    else:
                        pass
                charGold = charGold - price
                tempPickleGold = open(".\\temp\\tempPickleGold.pkl","bw")
                pickle.dump(charGold, tempPickleGold)
                tempPickleGold.close()
                charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")  #Get items in char. inventory
                characterEquip = pickle.load(charInvTemp)
                charInvTemp.close()
                characterEquip.append(buy)
                charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")
                pickle.dump(characterEquip, charInvTemp)
                charInvTemp.close()
                print("You now have " + str(charGold) + " gold.")
            else:
                print("It is not wise to go into debt for a " + buy + ".")
        elif buy == '':
            print("I didn\'t get that. Please try again.")
        else:
            print("\'I\'m sorry, but I don\'t sell that,\' " + npcName + " says.")
    else:
        print("You may not buy from "  + str(npcName).title() + ".")

def sell(npcName):
    if getNPCType(npcName) == 'merchant':
        charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")  #Get items in char. inventory
        characterEquip = pickle.load(charInvTemp)
        charInvTemp.close()
        if len(characterEquip) > 0 and characterEquip[0] != '':
            for c in range(len(characterEquip)):
                itemToSell = characterEquip[c]
                print(itemToSell + ' - ' + str(gI.itemPrices[itemToSell]) + 'G')
            print("What do you want to sell?")
            sell = input()
            if sell in characterEquip and sell != '':
                price = gI.itemPrices[sell]
                print("You sell the " + sell + ".")
                tempPickleGold = open(".\\temp\\tempPickleGold.pkl","rb")
                charGold = pickle.load(tempPickleGold)
                tempPickleGold.close()
                for i in range(len(characterEquip)):
                    if sell == characterEquip[i]:
                        invNum = i
                        break
                    else:
                        pass
                charGold = charGold + price
                tempPickleGold = open(".\\temp\\tempPickleGold.pkl","bw")
                pickle.dump(charGold, tempPickleGold)
                tempPickleGold.close()
                charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")  #Get items in char. inventory
                characterEquip = pickle.load(charInvTemp)
                charInvTemp.close()
                characterEquip.remove(sell)
                charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")
                pickle.dump(characterEquip, charInvTemp)
                charInvTemp.close()
                print("You now have " + str(charGold) + " gold.")
            elif sell == '':
                print("I didn\'t get that. Please try again.")
            else:
                print("\'I\'m sorry, but I can\'t buy that,\' " + npcName + " says.")
        else:
            print("You have nothing to sell.")
    else:
        print("You may not sell to " + str(npcName).title() + ".")
    
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
                print("\'I can\'t give you directions, yet. You\'re on your own.\'")
            elif choice == 'talk':
                talk(npcName)
            elif choice == 'leave':
                farewell(npcName)
                break
            elif choice == 'buy':
                buy(npcName)
            elif choice == 'sell':
                sell(npcName)
            
        else:
            print("You can\'t \'" + choice + "\' with " + npcName + ".")
            time.sleep(1)
