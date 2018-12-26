import createCharacter
import loadCharacter
import random
import time
import pickle
import shelve

characterStats = ['strength', 'intelligence', 'dexterity']
characterEquip = []
playState = 'y'
name = 'name'

createCharacter.welcomePlayer()
        
while playState == 'y':   
    name = createCharacter.characterName()
    createCharacter.rollDice(characterStats)
    profession = createCharacter.charProfSelect()

    print("You've completed your character!")
    time.sleep(1)
    createCharacter.character()
    createCharacter.giveEquipment()
    createCharacter.inventoryList()

    createCharacter.saveCharacter()
        
    playState = createCharacter.playAgain()
