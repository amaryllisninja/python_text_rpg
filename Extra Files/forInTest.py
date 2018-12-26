import shelve

aDict = {0:'cat', 1:'dog', 2:'racoon', 3:'moose'}
newDict = shelve.open("newDictShelf")

print(newDict)
newDict["0"] = 'moose'

for c in range(len(aDict)):
    newDict[str(c)] = aDict[c]

print(dict(newDict))
