# Character creation module

import random, time, pickle, shelve, characters, rooms, roll

def welcomePlayer():
    print("Welcome to Amaryllis' character generator!")
    print("In this generator, you can name a character, roll up his stats, and select his profession.")
    print("Press enter to begin.")
    input()

# Create character name
def characterName():
    correct = 'n'
    while correct != 'y':
        print("What would you like to call your character?")
        name = input()
        print("You've named your character " + name + ". Is this correct? (y/n)")
        correct = input()    
    
    return name

def displayName(name):
    print("Your character's name is:")
    print(name)

# Start of stat code
def displayStats(characterStats):
    print("Your character's stats are:")
    print("Strength: " + characterStats[0])
    print("Intelligence: " + characterStats[1])
    print("Dexterity: " + characterStats[2])
    print("Health Points: " + characterStats[3])
    print("Magic Points: " + characterStats[4])

def rollDice(chatacterStats):
    reroll = 'y'
    rerollAmt = 0
    while True:

        print("Rolling 3d6...")
        time.sleep(2)
        
        characterStats[0] = random.randint(3, 18)                       #Roll str
        characterStats[1] = random.randint(3, 18)                       #Roll int
        characterStats[2] = random.randint(3, 18)                       #Roll dex
        characterStats[3] = characterStats[0] + characterStats[2]       #Roll HP
        characterStats[4] = random.randint(1, 6) + characterStats[1]    #Roll MP

        characterStats[0] = str(characterStats[0])
        characterStats[1] = str(characterStats[1])
        characterStats[2] = str(characterStats[2])
        characterStats[3] = str(characterStats[3])
        characterStats[4] = str(characterStats[4])

        displayStats(characterStats)
        time.sleep(1)
        rerollAmt = rerollAmt + 1
        if rerollAmt <= 2:
            print("You may roll your stats up to 3 times. \nWould you like to reroll? (y/n) ")
            pass
        else:
            print("You can no longer reroll.")
            break

        reroll = input()
        if reroll == 'y':
            pass
        elif reroll == 'n':
            break
        else:
            print("Incorrect input.")
            time.sleep(1)
        
    tempHP = characterStats[3]      #Setting temporary hit points
    tempHealthFile = open("tempHealthFile.pkl","bw")
    pickle.dump(tempHP, tempHealthFile)
    tempHealthFile.close()
    tempMP = characterStats[4]      #Setting temporary magic points
    tempMagicFile = open("tempMagicFile.pkl","bw")
    pickle.dump(tempMP, tempMagicFile)
    tempMagicFile.close()
    time.sleep(2)
#End of stat code

# Start of profession code
def characterProf():
    print("\nYour character can be a 'fighter', 'wizard', or 'thief'.")
    print("Type 'info' for more information about professions.")
    print("What is your character's profession?")
    profession = input().lower()

    if profession == 'info':
        print("Fighter is a strength based profession. If you have a high \nstrength, fighter is a good profession to choose.")
        print("Wizard is a intelligence based profession. If you have a \nhigh intelligence, wizard is a good profession to choose.")
        print("Thief is a dexterity based profession. If you have a high \ndexterity, thief is a good profession to choose.")
        time.sleep(4)
        print("\nYour character can be a 'fighter', 'wizard', or 'thief'.")
        print("Type 'info' for more information about professions.")
        print("What is your character's profession?")
        profession = input().lower()

    print("You've selected " + profession + " as your profession. Is this correct? (y/n)")
    correct = input()

    while correct != 'y':
        print("\nYour character can be a 'fighter', 'wizard', or 'thief'.")
        print("What is your character's profession?")
        profession = input().lower()        
        print("You've selected " + profession + " as your profession. Is this correct? (y/n)")
        correct = input()

    return profession

def checkProfession(profession):
    if profession == 'fighter':
        print("\nFighters can use any weapon, shield, or armor. They cannot cast spells or use wands.")
        print("As a fighter, your strength will affect how much damage your weapons will deal \nand whether or not you can hit your opponent.")
        print("Your starting equipment will be a short sword, a small shield, and padded armor.\n")
        time.sleep(6)
    elif profession == 'wizard':
        print("\nWizards can cast any spell, but can only use small weapons and light armor.")
        print("As a wizard, intelligence will affect what spells you can cast and how many you can memorize.")
        print("Your starting equipment will be a dagger, a spell book, wizard robes, and a pointed hat.\n")
        time.sleep(6)
    elif profession == 'thief':
        print("\nThiefs can use any light or medium weapon, small and medium shields, and wear light or medium armor.")
        print("As a thief, your dexerity will affect your ability to pick locks, climb, sneak, etc.")
        print("Your starting equipment will be a dagger, a lock picking kit, and rope.\n")
        time.sleep(6)
    else:
        print("I'm afraid that " + profession + " isn't a valid profession. Please select again.")
        time.sleep(1)
        profession = 'invalid'
    return profession

def charProfSelect():
    profession = characterProf()
    profession = checkProfession(profession)
    while profession == 'invalid':
        profession = characterProf()
        profession = checkProfession(profession)
    return profession

def displayProf(profession):
    print("Your character's profession is:")
    print(profession)
# End of profession code

# Combination of character info
def character():
    displayName(name)
    displayStats(characterStats)
    displayProf(profession)
    displayGold()
    print("\nYou have nothing equipped.")

# Equipment assignment based on profession
def giveEquipment():
    if profession == 'fighter':
        characterEquip.append('short sword')
        characterEquip.append('small shield')
        characterEquip.append('padded armor')
        newGold = (roll.rollDice(5, 4))*10
    elif profession == 'wizard':
        characterEquip.append('dagger')
        characterEquip.append('spell book')
        characterEquip.append('wizard robes')
        characterEquip.append('pointed hat')
        newGold = ((roll.rollDice(1, 4))+1)*10
    elif profession == 'thief':
        characterEquip.append('dagger')
        characterEquip.append('lock picking kit')
        characterEquip.append('rope')
        newGold = (roll.rollDice(2, 6))*10
    file = shelve.open(name.lower().replace(" ", "") + "SaveFile")
    file["gold"] = newGold
    file.close()
    #Create gold pickle
    tempPickleGold = open("tempPickleGold.pkl","bw")
    pickle.dump(newGold, tempPickleGold)
    tempPickleGold.close()

# Show amount of gold
def displayGold():
    print("You have " + str(newGold) + " gold.")

# List inventory
def inventoryList():
    print("In your inventory, you have:")
    print('\n'.join(characterEquip))
    print()

# Places character in room 0
def setInitialLocation():
    location = 0
    return location
    
def playAgain():    #Create a new character
    print("Would you like to create another character? (y/n)")
    playState = input()
    return playState

def saveCharacter():
    print("Saving your character...")

    #Create room items
    tempPickleItems = open("tempPickleItems.pkl","bw")       
    pickle.dump(rooms.roomItems,tempPickleItems)
    tempPickleItems.close()
    tempPickleItems = open("tempPickleItems.pkl","rb")
    roomItems = pickle.load(tempPickleItems)
    tempPickleItems.close()
    #Create live room monsters
    tempPickleMonsters = open("tempPickleMonsters.pkl","bw")       
    pickle.dump(rooms.roomMonsters,tempPickleMonsters)
    tempPickleMonsters.close()
    tempPickleMonsters = open("tempPickleMonsters.pkl","rb")    
    roomMonsters = pickle.load(tempPickleMonsters)
    tempPickleMonsters.close()
    
    #Create dead room monsters
    tempPickleDeadMon = open("tempPickleDeadMon.pkl","bw")
    pickle.dump(rooms.deadMonsters,tempPickleDeadMon)
    tempPickleDeadMon.close()
    tempPickleDeadMon = open("tempPickleDeadMon.pkl","rb")
    deadMonsters = pickle.load(tempPickleDeadMon)
    tempPickleDeadMon.close()
    
    #Create looted monsters
    tempLootedMonsters = []
    for c in range(0, len(rooms.roomNames)):
        tempLootedMonsters.append('')
        tempLootedMonsters[c] = list(tempLootedMonsters[c])
        c += 1
    tempPickleLootedMon = open("tempPickleLootedMon.pkl","bw")
    pickle.dump(tempLootedMonsters,tempPickleLootedMon) 
    tempPickleLootedMon.close()

    #Create NPCs
    tempPickleNPCs = open("tempPickleNPCs.pkl","bw")
    pickle.dump(rooms.roomNPCs, tempPickleNPCs)
    tempPickleNPCs.close()
    tempPickleNPCs = open("tempPickleNPCs.pkl","rb")
    tempNPCs = pickle.load(tempPickleNPCs)
    tempPickleNPCs.close()
    
    file = shelve.open(name.lower().replace(" ", "") + "SaveFile")
    file["name"] = name
    file["strength"] = characterStats[0]
    file["intelligence"] = characterStats[1]
    file["dexterity"] = characterStats[2]
    file["health"] = [characterStats[3], '/', characterStats[3]]
    file["magic"] = [characterStats[4], '/', characterStats[4]]
    file["profession"] = profession
    file["inventory"] = characterEquip
    file["location"] = 0
    file["equipped"] = characterEquipped
    file["roomItems"] = roomItems
    file["roomMonsters"] = roomMonsters
    file["deadMonsters"] = deadMonsters
    file["lootedMonsters"] = tempLootedMonsters
    file["npcs"] = tempNPCs
    file["deathCount"] = 0
    file["experience"] = 0
    
    file.close()

    #Load name
    fileName = open("tempCharName.pkl","bw")                
    pickle.dump(name,fileName)
    file.close()
    #Load stats
    fileStats = open("charStatsTemp.pkl","bw")              
    pickle.dump(characterStats,fileStats)
    fileStats.close()
    #Load inventory
    fileInv = open("charInvTemp.pkl","bw")                  
    pickle.dump(characterEquip,fileInv)
    fileInv.close()
    #Load HP
    fileHP = open("charHealthTemp.pkl","bw")                
    pickle.dump(characterStats[3],fileHP)
    fileHP.close()
    #Load MP
    fileMP = open("charMagicTemp.pkl","bw")                 
    pickle.dump(characterStats[4],fileMP)
    fileMP.close()
    #Load equipped 
    tempPickleEquipped = open("tempPickleEquipped.pkl","bw") 
    pickle.dump(characterEquipped,tempPickleEquipped)
    tempPickleEquipped.close()
    #Load death count
    tempPickleDC = open("tempPickleDC.pkl","bw")           
    pickle.dump(0,tempPickleDC)
    tempPickleDC.close()
    #Load Experience
    tempPickleXP = open("tempPickleXP.pkl","bw")           
    pickle.dump(0,tempPickleXP)
    tempPickleXP.close()
    #Characters level up every 2000XP points. Ie, level 1 is 0-1999 xp. Level 2 is 2000-3999...

    print("Saved.\n")
    time.sleep(1)

# Start of actual character generation code
playState = 'y'
welcomePlayer()
    
while playState == 'y':   
    characterStats = ['strength', 'intelligence', 'dexterity', 'health', 'magic']
    characterEquip = []
    characterEquipped = []
    playState = 'y'
    name = 'name'
    newGold = 0
    name = characterName()
    rollDice(characterStats)
    profession = charProfSelect()

    print("You've completed your character!")
    time.sleep(1)
    character()
    giveEquipment()
    inventoryList()
    location = 0
    saveCharacter()
    
    playState = playAgain()

