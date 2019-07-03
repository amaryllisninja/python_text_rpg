# Character file loading module
import shelve, time, rooms, pickle, os, string
currentLoc = os.getcwd()

def checkSaved(loadCharName):
    fileList = os.listdir(currentLoc + "\\charsaves\\")
    charSaved = []
    savedNames = []
    for file in range(len(fileList)):
        a = fileList[file]
        if a[-4:] == '.dat':
            charSaved.append(a)
        else:
            pass
    for file in range(len(charSaved)):
        b = charSaved[file]
        name = b.replace('SaveFile.dat', '')
        savedNames.append(name)
    if loadCharName not in savedNames:
        print("I don't have that character in my records.")
        print("Here are the characters I have saved:")
        print("\n".join(savedNames))
        loadCharModule()

def loadCharModule():
    print("Would you like to load a previously saved character? (y/n)")
    load = input()
    
    if load == 'y':
        print("What is the name of the character you wish to load?")
        loadCharName = input().lower()
        loadCharName = loadCharName.replace(" ","")

        fileList = os.listdir(currentLoc + "\\charsaves\\")
        charSaved = []
        savedNames = []
        for file in range(len(fileList)):
            a = fileList[file]
            if a[-4:] == '.dat':
                charSaved.append(a)
            else:
                pass
        for file in range(len(charSaved)):
            b = charSaved[file]
            name = b.replace('SaveFile.dat', '')
            savedNames.append(name)
            
        if loadCharName not in savedNames:
            print("I don't have that character in my records.")
            print("Here are the characters I have saved:")
            print("\n".join(savedNames))
            loadCharModule()
        
        else:
            print("Loading character...")
            time.sleep(1)

            saveFileName = ".\\charsaves\\" + loadCharName.lower().replace(" ", "") + "SaveFile"
            characterLoaded = shelve.open(saveFileName)                #Load character

            name = characterLoaded["name"]
            strength = characterLoaded["strength"]
            intelligence = characterLoaded["intelligence"]
            dexterity = characterLoaded["dexterity"]
            characterStats = [strength, intelligence, dexterity]
            profession = characterLoaded["profession"]
            inventory = characterLoaded["inventory"]
            gold = characterLoaded["gold"]
            location = characterLoaded["location"]
            stats = [strength, intelligence, dexterity]
            health = characterLoaded["health"]
            magic = characterLoaded["magic"]
            characterEquipped = characterLoaded["equipped"]

            fileStats = open(".\\temp\\charStatsTemp.pkl","bw")
            pickle.dump(stats,fileStats)
            fileStats.close()
            fileInv = open(".\\temp\\charInvTemp.pkl","bw")
            pickle.dump(inventory,fileInv)
            fileInv.close()

            print("Your character's name is " + name)
            print("Your character's stats are:")
            print("Strength: " + strength)
            print("Intelligence: " + intelligence)
            print("Dexterity: " + dexterity)
            print("Health Points: " + ''.join(health))
            print("Magic Points: " + ''.join(magic))
            print("Your character's profession is " + profession)
            print(name + "'s inventory: ")
            print('\n'.join(inventory))
            print(str(gold) + " gold")
            print("Equipped Items: ")
            print('\n'.join(characterEquipped))
            print("Current location: " + rooms.roomNames[location])

            file = open(".\\temp\\tempCharName.pkl","bw")
            pickle.dump(loadCharName,file)
            file.close()

    elif load == 'n':
        print("Loading character creation module...\n")
        time.sleep(1)
        import createCharacter

    else:
        print("I'm sorry. I didn't recognize that input. Please try again.")
        loadCharModule()
