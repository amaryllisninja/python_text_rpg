import pickle, random, time, shelve, dialogue, rooms, checkRoom, roll
import gameItems as gI
import gameMonsters as gMon
import useItems as uI
import leveling as lvl
global inCombat

statMod = {1:-5, 2:-3, 3:-3, 4:-2, 5:-2, 6:-1, 7:-1, 8:0,
              9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0,
              17:1, 18:2, 19:3, 20:3, 21:4, 22:4, 23:5, 24:6,
              25:7}

def attack(action, charName):
    #Load character save file
    saveFileName = ".\\charsaves\\" + charName.lower().replace(" ", "") + "SaveFile"
    charFile = shelve.open(saveFileName)    #Load character      
    name = charFile["name"]                 #Load character name
    health = charFile["health"]             #Load character HP
    health[0] = int(health[0])
    health[2] = int(health[2])
    magic = charFile["magic"]               #Load character MP
    magic[0] = int(magic[0])
    magic[2] = int(magic[2])
    deathCnt = charFile["deathCount"]       #Load death count
    profession = charFile["profession"]     #Load character profession
    charFile.close()                        #Close save flie 
    
    #Load current room
    tempPickleLoc = open(".\\temp\\tempPickleLoc.pkl","rb")      
    room = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    
    #Get current live monsters in rooms for character
    tempPickleMonsters = open(".\\temp\\tempPickleMonsters.pkl","rb")
    tempRoomMonsters = pickle.load(tempPickleMonsters)
    tempPickleMonsters.close()
    roomMonsters = tempRoomMonsters[room]

    #Get current dead monsters in room for character
    tempPickleDeadMon = open(".\\temp\\tempPickleDeadMon.pkl","rb")
    deadMonsters = pickle.load(tempPickleDeadMon)
    tempPickleDeadMon.close()
    deadMonsters = deadMonsters[room]

    if action[1] == '':
        print(action[0].title() + " what?")
    else:
        victim = []
        c = 1

        #Creating 'victim' string
        while c <= len(action): 
            if action[c] != '':
                victim.append(action[c])
                c += 1
            elif action[c] == '':
                break
        victim = ' '.join(victim)
        if victim in roomMonsters:            
            #Player attack stats
            aDaC = checkEquipped(charName, victim)
            #aDaC = [number of dice, sides on dice, armor class]
            
            charStr = getCharStat('strength')
            charDex = getCharStat('dexterity')
            charInt = getCharStat('intelligence')
            charThaco = thacoCalc(aDaC[2], charDex)
            mainStat = checkProfession(profession)
            charHitStat = {
                'strength':charStr,
                'dexterity':charDex,
                'intelligence':charInt
            }
                
            #Monster attack stats###################################           
            monAtkDice = monsterWeaponCheck(victim)
            monStr = getMonStat(victim, 'strength')
            monDex = getMonStat(victim, 'dexterity')
            monInt = getMonStat(victim, 'intelligence')
            monMainStat = findMonMainStat(victim)
            monAC = getMonStat(victim, 'AC')
            monThaco = thacoCalc(monAC, monDex)
            monsterHP = int(getMonStat(victim, 'HP'))
            permMonHP = int(getMonStat(victim, 'HP'))
            monHitStat = {
                'strength':monStr,
                'dexterity':monDex,
                'intelligence':monInt
            }
            
            #Start main combat code###################################
            print("You are engaged in combat with " + victim.title() + ".")
            inCombat = True

            while inCombat == True:
                #Character attack phase####################
                print("\nDo you ATTACK, use an ITEM, or FLEE?", end='  ')
                atkAction = input()

                while True:
                    #If attacking ###########################
                    if atkAction.lower() == 'attack':
                        time.sleep(1)
                        charToHit = rollToHit(charHitStat[mainStat])
                        time.sleep(1)
                        damageDealt = atkRoll(aDaC[0], aDaC[1], monThaco, charToHit, name)
                        monsterHP -= damageDealt
                        checkMonHP(monsterHP, permMonHP, victim)
                        time.sleep(1)
                        if monsterHP <= 0:
                            print("You have killed " + victim.title() + ".")
                            removeMonster(charName, victim, room)
                            lvl.addXP(charName, victim)
                            inCombat == False
                            break
                        elif monsterHP > 0:
                            pass
                        else:
                            print("There was an error with player combat.")
                            break
                        break
                    
                    #If using item ###########################
                    elif atkAction.lower() == 'item':
                        charInvTemp = open(".\\temp\\charInvTemp.pkl","rb")  #Get items in char. inventory
                        inventory = pickle.load(charInvTemp)
                        charInvTemp.close()
                        print('\n'.join(inventory))                 #Print char inventory
                        print("Which item in your inventory do you use? (Or CANCEL)")
                        itemChoose = input()
                        if itemChoose in inventory:
                            if gI.itemType[itemChoose] in gI.useTypes:
                                uI.useItem(itemChoose, charName)
                                inventory.remove(itemChoose)
                                charInvTemp = open(".\\temp\\charInvTemp.pkl","bw")
                                pickle.dump(inventory, charInvTemp)
                                charInvTemp.close()
                                saveFileName = ".\\charsaves\\" + charName.lower().replace(" ", "") + "SaveFile"
                                charFile = shelve.open(saveFileName)                #Load character
                                fileHealth = charFile["health"]                     #Load character HP
                                health[0] = int(fileHealth[0])                      #Set health after item use
                                fileMagic = charFile["magic"]                       #Load character MP
                                magic[0] = int(fileMagic[0])                        #Set health after item use
                                charFile.close()
                                break
                            else:
                                print("You cannot use " + itemChoose + " right now.\n")
                        elif itemChoose.lower() == 'cancel':
                            print("Okay.")
                            time.sleep(1)
                            print("\nDo you ATTACK, use an ITEM, or FLEE?  ", end='')
                            atkAction = input()
                        else:
                            print(itemChoose.title() + " is not in your inventory. Please choose another item.\n")
                        
                    
                    #If fleeing ##############################
                    elif atkAction.lower() == 'flee':
                        print("You flee.")
                        fileLoc = open(".\\temp\\tempPickleLoc.pkl","rb")
                        location = pickle.load(fileLoc)
                        fileLoc.close()
                        
                        while True:
                            roomFlee = random.randint(0, 3)
                            fleeOpts = rooms.roomsConnectedTo[location]
                            fleeOpts = fleeOpts.split(' ')
                            
                            if fleeOpts[roomFlee] != 'x':
                                location = int(fleeOpts[roomFlee])
                                fileLoc = open(".\\temp\\tempPickleLoc.pkl","bw")
                                pickle.dump(location,fileLoc)
                                fileLoc.close()
                                break
                            else:
                                pass
                        time.sleep(1)
                        print("You run to...")
                        time.sleep(1)
                        print(rooms.roomNames[int(location)] + "\n" + rooms.roomDescriptions[int(location)])
                        checkRoom.checkRoomItems()
                        checkRoom.checkRoomMonsters()
                        break

                    #If not valid response ###################    
                    else:
                        print("That's not a valid option. Please choose \'attack\', \'item\', or \'flee\'.")
                        time.sleep(1)
                        print("\nDo you ATTACK, use an ITEM, or FLEE?  ", end='')
                        atkAction = input()
                if atkAction.lower() == 'flee':
                    break
                else:
                    pass
                        
                #Monster/victim attack phase###############
                if monsterHP <= 0:
                    break
                else:
                    time.sleep(2)
                    monToHit = rollToHit(monHitStat[monMainStat])
                    time.sleep(1)
                    monDamage = atkRoll(monAtkDice[0], monAtkDice[1], monThaco, monToHit, victim)
                    time.sleep(1)
                    health[0] -= monDamage
                    inCombat = checkHP(name, health, magic)

            #Eliminate negative numbers
            if health[0] < 0:
                health[0] = '0'
            else:
                pass
            if magic[0] < 0:
                magic[0] = '0'
            else:
                pass

            saveFileName = ".\\charsaves\\" + charName.lower().replace(" ", "") + "SaveFile"
            charFile = shelve.open(saveFileName)                #Load character
            fileHealth = charFile["health"]                     #Load character HP
            fileHealth[0] = str(health[0])
            charFile["health"] = fileHealth
            fileMagic = charFile["magic"]                       #Load character MP
            fileMagic[0] = str(magic[0])
            charFile["magic"] = fileMagic
            charFile.close()
            
        else:
            print("There is no " + victim + " in this room.")
            time.sleep(1)
            
def thacoCalc(totalAC, dex):
    #10 + armor bonus + shield bonus + Dexterity modifier + size modifier
    thaco = 10 + int(totalAC) + statMod[int(dex)]
    return thaco

def rollToHit(stat):                                            #Profession dominant stat
    toHit = (random.randint(1, 20) - statMod[int(stat)])
    return toHit

def atkRoll(numDice, atkDice, thaco, toHit, attacker):
    if thaco < toHit:
        print(attacker.title() + " missed.")
        damage = 0
    elif thaco >= toHit:
        damage = roll.rollDice(numDice, atkDice)
        print(attacker.title() + " hit for " + str(damage) + " points of damage!")
    else:
        pass
    return damage

def checkEquipped(charName, victim):
    equippedPickle = open(".\\temp\\tempPickleEquipped.pkl", "rb")
    equipped = pickle.load(equippedPickle)
    equippedPickle.close()
    aC = 0
    atkDice = [1, 3]
    for c in range(0,len(equipped)):                            #Find which items equipped are weapons
        itemType = gI.itemType[equipped[c]]        
        if itemType == 'weapon':
            atkDice = gI.weaponHitDice[equipped[c]]
            atkDice = atkDice.split()
            atkDice = (int(atkDice[0]), int(atkDice[1]))
        elif itemType == 'shield' or itemType == 'armor':
            aC += int(gI.armorClass[equipped[c]])
        else:
            pass
            time.sleep(2)
    if equipped == None or equipped == ['']:
        print("You have nothing equipped! You're fighting with your bare fists.")
    else:
        pass
    aDaC = []
    aDaC.append(atkDice[0])
    aDaC.append(atkDice[1])
    aDaC.append(aC)
    return aDaC                                                 #aDaC = [number of dice, sides on dice, armor class]

def monsterWeaponCheck(monster):
    monItems = gMon.monsterItems[monster]
    monWeapons = []
    for item in range(0, len(monItems)):
        a = monItems[item]
        itemType = gI.itemType[a]
        if itemType == 'weapon':
            monWeapons.append(monItems[item])
            #print(monster + " has got a " + monItems[item] + ".")
        else:
            pass
    if monWeapons == []:
        atkDice = [1, 3]
    else:
        randWeapon = roll.rollDice(0, len(monWeapons)-1)
        atkDice = gI.weaponHitDice[monWeapons[randWeapon]]
        atkDice = atkDice.split()
        del atkDice[2:]
    return atkDice
    
def monsterAtk(charName, victim):
    pass

def checkHP(person, health, magic):
    print("You are down to " + str(health[0]) + " health points.")
    if health[0] == 0 or health[0] <= 0:
        print("\n\nYou are dead. You feel nothing.\n\n")
        health[0] = health[2]                                   #Reset Health to full
        saveFileName = ".\\charsaves\\" + person.lower().replace(" ", "") + "SaveFile"
        charFile = shelve.open(saveFileName)                #Load character
        oldDeathCnt = int(charFile["deathCount"])               #Update death count
        newDeathCnt = oldDeathCnt + 1
        charFile["deathCount"] = newDeathCnt
        charIsDead(person, newDeathCnt, health, magic)
        charFile.close()
        time.sleep(3)
        inCombat = False
    elif health[0] <= (health[2])/4:
        print("You are covered with lacerations and blood. You feel awful.")
        inCombat = True
    elif health[0] <= (health[2])/2:
        print("You have cuts and bruises everywhere. You do not feel good.")
        inCombat = True
    elif health[0] < health[2]:
        print("You have a few scrapes. You feel fine.")
        inCombat = True
    elif health[0] == health[2]:
        print("Your body is unharmed. You feel great!")
        inCombat = True
    return inCombat

def checkMonHP(monsterHP, permMonHP, victim):
    if monsterHP == 0 or monsterHP <= 0:
        print(victim.title() + " has died.")
    elif monsterHP <= permMonHP/4:
        print(victim.title() + " is covered with lacerations and blood.")
    elif monsterHP <= permMonHP/2:
        print(victim.title() + " has cuts and bruises everywhere.")
    elif monsterHP < permMonHP:
        print(victim.title() + " has a few scrapes.")
    elif monsterHP == permMonHP:
        print(victim.title() + " is unharmed.")
    else:
        print("There was a problem with checking " + victim.title() + "\'s HP.")

# Character stat grab
def getCharStat(statFullName):
    statNum = {
        'strength': 0,
        'intelligence': 1,
        'dexterity': 2}
    
    charStatsTemp = open(".\\temp\\charStatsTemp.pkl","rb")
    fileStats = pickle.load(charStatsTemp)
    charStatsTemp.close()
    
    statLocNum = statNum[statFullName]
    statValue = fileStats[statLocNum]
    return statValue

# Monster stat grab
def getMonStat(monster, statFullName):
    statNum = {
        'strength': 0,
        'intelligence': 1,
        'dexterity': 2,
        'HP': 3,
        'MP': 4,
        'AC': 5}
    
    statDict = gMon.monsterStats[monster]
    statList = statDict.split()
    statLocNum = statNum[statFullName]
    statValue = statList[statLocNum]
    #print(statList)
    return statValue

def checkProfession(profession):
    if profession == 'mercenary':
        mainStat = 'strength'
    elif profession == 'thief':
        mainStat = 'dexterity'
    elif profession == 'thaumaturge':
        mainStat = 'intelligence'
    else:
        print("There was a problem. Could not find profession.")
        mainStat = 'None'
    return mainStat

def charIsDead(person, deathCnt, health, magic):
    time.sleep(3)
    print("You stand up and look around. You see a tall, dark-haired woman standing")
    print("nearby with an Ankh hanging around her neck. She smiles at you.")
    time.sleep(3)
    print("\'Hi, there, " + person + ".\' she says.")
    if int(deathCnt) == 0:
        print("\'I'm sure you're pretty confused right now, but let me clear things")
        print("up for you: You're dead. It's nothing to be alarmed by. It happens")
        print("to everyone. \nShall we go for a walk?\'")
    elif int(deathCnt) <= 5:
        response = roll.rollDice(0, len(dialogue.deathLess5)-1)
        print(dialogue.deathLess5[response])
    elif int(deathCnt) <= 10:
        response = roll.rollDice(0, len(dialogue.deathLess10)-1)
        print(dialogue.deathLess10[response])
    elif int(deathCnt) <= 15:
        response = roll.rollDice(0, len(dialogue.deathLess15)-1)
        print(dialogue.deathLess15[response])
    elif int(deathCnt) > 15:
        response = roll.rollDice(0, len(dialogue.deathGreater15)-1)
        print(dialogue.deathGreater15[response])
    else:
        print("You sure die a lot, huh?")

    #Set location to Dojo (later, underworld)
    location = 0
    fileLoc = open(".\\temp\\tempPickleLoc.pkl","bw")            #Save character location to pickle
    pickle.dump(location,fileLoc)
    fileLoc.close()
    print(deathCnt)

    time.sleep(3)
    
    print("\nYou stand up. You feel queasy and dizzy. As your eyes adjust, you find yourself in...\n")
    time.sleep(2)
    print(rooms.roomNames[int(location)] + "\n" + rooms.roomDescriptions[int(location)])
    checkRoom.checkRoomItems()
    checkRoom.checkRoomMonsters()
    
    time.sleep(3)

def removeMonster(charName, monster, room):
    #Get current live monsters in rooms for character
    tempPickleMonsters = open(".\\temp\\tempPickleMonsters.pkl","rb")
    tempRoomMonsters = pickle.load(tempPickleMonsters)
    tempPickleMonsters.close()
    roomMonsters = tempRoomMonsters[room]

    #Get current dead monsters in room for character
    tempPickleDeadMon = open(".\\temp\\tempPickleDeadMon.pkl","rb")
    tempDeadMonsters = pickle.load(tempPickleDeadMon)
    tempPickleDeadMon.close()
    deadMonsters = tempDeadMonsters[room]
    
    #Load room monsters
    #print(roomMonsters, deadMonsters)
    roomMonsters.remove(monster)
    if roomMonsters == []:
        roomMonsters.append('')
    else:
        pass
    
    deadMonsters.append(monster)
    if deadMonsters[0] == '':
        del deadMonsters[0]
    else:
        pass
    #print(roomMonsters, deadMonsters)

    tempRoomMonsters = list(tempRoomMonsters)
    tempDeadMonsters = list(tempDeadMonsters)
    tempRoomMonsters[room] = roomMonsters
    tempDeadMonsters[room] = deadMonsters
   

    tempPickleMonsters = open(".\\temp\\tempPickleMonsters.pkl","bw")
    pickle.dump(tempRoomMonsters,tempPickleMonsters) 
    tempPickleMonsters.close()

    tempPickleDeadMon = open(".\\temp\\tempPickleDeadMon.pkl","bw")
    pickle.dump(tempDeadMonsters,tempPickleDeadMon) 
    tempPickleDeadMon.close()
    #print(tempDeadMonsters)

def findMonMainStat(monster):
    mainStat = gMon.monsterMainStat[monster]
    return mainStat

    
    





        


