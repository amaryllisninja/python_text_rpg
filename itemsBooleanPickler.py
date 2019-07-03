import pickle

itemsBoolean = False

itemsBoolPlk = open(".\\temp\\itemsBoolPlk.pkl","bw")
pickle.dump(itemsBoolean,itemsBoolPlk)
fileLoc.close()
