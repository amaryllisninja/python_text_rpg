import random, time, pickle, shelve, rooms, gameActions
import gameItems as gI

def useItem(item, name):
   print(gI.itemType[item])
   if gI.itemType[item] in gI.useTypes:
      itemType = gI.itemType[item]
      charFile = shelve.open(name + "SaveFile")
      
      if itemType == 'item':
         pass
      elif itemType == 'tool':
         pass
      elif itemType == 'potion' or itemType == 'food': 
         print("You consume the " + item + ".\n")
         consumableAction = gI.consumableInfo[item]        #For potion and food.
         #Grab stat to be updated
         updateStat = charFile[consumableAction[0]]
         #Roll potion effect for stat
         effect = random.randint(1, consumableAction[1])
         newStat = int(updateStat[0]) + effect

         #Recover Health Points
         if consumableAction[0] == 'health':             
            if newStat >= int(updateStat[2]):
               updateHealth(name, updateStat[2], updateStat[2])
               print("Your health was maxed out.")
               print("Your health is now " + str(updateStat[2]) + ".")
            elif newStat < int(updateStat[2]):
               updateHealth(name, newStat, updateStat[2])
               print("Your health is now " + str(newStat) + ".")
            else:
               print("There was an error while updating your " + updateStat + ".")

         #Recover Magic Points
         elif consumableAction[0] == 'magic':
            if newStat >= int(updateStat[2]):
               updateMagic(name, updateStat[2], updateStat[2])
               print("Your magic was maxed out.")
               print("Your magic is now " + str(updateStat[2]) + ".")
               print("Your magic is now " + str(newStat) + ".")
            elif newStat < int(updateStat[2]):
               updateMagic(name, newStat, updateStat[2])
               print("Your magic is now " + str(newStat) + ".")
            else:
               print("There was an error while updating your " + updateStat + ".")
         else:
            charFile[consumableAction[0]] = newStat
      elif itemType == 'book':
         pass
      elif itemType == 'spell':
         pass
      elif itemType == 'climb':
         pass
      elif itemType == 'unlock':
         pass
      else:
         print("You cannot use " + item + " at this time.\n")
      charFile.close()
         
   else:
      print("You cannot use " + item + ".\n")
   pass


def updateHealth(name, updateStat1, updateStat2):
   charFile = shelve.open(name + "SaveFile")
   newHealth = [str(updateStat1), '/', str(updateStat2)]
   charFile["health"] = newHealth
   charFile.close()
   tempHealth = open("tempHealthFile.pkl","bw")
   pickle.dump(newHealth,tempHealth)
   tempHealth.close()


def updateMagic(name, updateStat1, updateStat2):
   charFile = shelve.open(name + "SaveFile")
   newMagic = [str(updateStat1), '/', str(updateStat2)]
   charFile["magic"] = newMagic
   charFile.close()
   tempMagic = open("tempMagicFile.pkl","bw")
   pickle.dump(newMagic,tempMagic)
   tempMagic.close()
   print("Your magic points were maxed out.")










