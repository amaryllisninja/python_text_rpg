import pickle

itemsBoolean = False

itemsBoolPlk = open("itemsBoolPlk.pkl","bw")
pickle.dump(itemsBoolean,itemsBoolPlk)
fileLoc.close()
