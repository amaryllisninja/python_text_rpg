# Character file loading module
import shelve, time, rooms, pickle

def checkSaved(loadCharName):
    newFile = open("charactersSaved.pkl","rb")
    nameList = pickle.load(newFile)
    newFile.close()
    if loadCharName not in nameList:
        print("I don't have that character in my records.")
        print("Here are the characters I have saved:")
        print("\n".join(nameList))
        loadCharModule()

def loadCharModule():
    print("Would you like to load a previously saved character? (y/n)")
    load = input()
    
    if load == 'y':
        print("What is the name of the character you wish to load?")
        loadCharName = input().lower()
        loadCharName = loadCharName.replace(" ","")

        newFile = open("charactersSaved.pkl","rb")
        nameList = pickle.load(newFile)
        newFile.close()
        if loadCharName not in nameList:
            print("I don't have that character in my records.")
            print("Here are the characters I have saved:")
            print("\n".join(nameList))
            loadCharModule()        
        else:
            print("Loading character...")
            time.sleep(1)

            characterLoaded = shelve.open(loadCharName + "SaveFile")

            name = characterLoaded["name"]
            strength = characterLoaded["strength"]
            intelligence = characterLoaded["intelligence"]
            dexterity = characterLoaded["dexterity"]
            characterStats = [strength, intelligence, dexterity]
            profession = characterLoaded["profession"]
            inventory = characterLoaded["inventory"]
            location = characterLoaded["location"]
            stats = [strength, intelligence, dexterity]
            health = characterLoaded["health"]
            magic = characterLoaded["magic"]
            characterEquipped = characterLoaded["equipped"]

            fileStats = open("charStatsTemp.pkl","bw")
            pickle.dump(stats,fileStats)
            fileStats.close()
            fileInv = open("charInvTemp.pkl","bw")
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
            print("Equipped Items: ")
            print('\n'.join(characterEquipped))
            print("Current location: " + rooms.roomNames[location])

            file = open("tempCharName.pkl","bw")
            pickle.dump(loadCharName,file)
            file.close()

    elif load == 'n':
        print("Loading character creation module...\n")
        time.sleep(1)
        import createCharacter

    else:
        print("I'm sorry. I didn't recognize that input. Please try again.")
        loadCharModule()
