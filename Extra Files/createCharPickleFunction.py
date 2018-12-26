
def createCharPickle(charStats):
    file = open("charData.pkl","bw")
    pickle.dump(characterStats,file)
    file.close()

    print("Exporting/importing file...")
    time.sleep(1)

    newFile = open("charData.pkl","rb")
    recoveredNumbers = pickle.load(newFile)
    print(recoveredNumbers)

    numberList = str(recoveredNumbers)

    print('\n'.join(numberList))

    file.close()
