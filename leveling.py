import gameMonsters as gMon

def addXP(name, charXP, monXP):
    tempPickleXP = open("tempPickleXP.pkl", "rb")
    charXP = pickle.load(timePickleXP)
    tempPickleXP.close()

    if monster != '':
        monXP = gMon.monsterXP[monster]
        newCharXP = charXP + monXP
        tempPickleXP = open("tempPickleXP.pkl", "rb")
        pickle.dump(newCharXP, tempPickleXP)
        tempPickleXP.close()
    else:
        print("Could not obtain monster name and info.")