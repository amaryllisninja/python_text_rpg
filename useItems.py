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
         if consumableAction[0] == 'health' or consumableAction[0] == 'magic':            
            if newStat > int(updateStat[2]):
               charFile[consumableAction[0]] = [updateStat[2], '/', updateStat[2]]
               newStat = updateStat[2]
               print("Your " + consumableAction[0] + " was maxed out.")
            elif newStat <= int(updateStat[2]):
               charFile[consumableAction[0]] = [str(newStat), '/', updateStat[2]]
            else:
               print("There was an error while updating your " + updateStat + ".")
         else:
            charFile[consumableAction[0]] = newStat
         print("Your " + consumableAction[0] + " is now " + str(newStat) + ".")
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

