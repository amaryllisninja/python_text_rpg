# Moving from room to room
import rooms
import random
import time
import pickle
import shelve
from saveGame import save

def checkLocation():
    file = shelve.open("solaireSaveFile")  #Change to character name string later
    location = file["location"]
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[location].split()

    print("You are in room " + str(location))
    print(directionsOpen)
    print(roomsConnectedTo)
    return directionsOpen, roomsConnectedTo

def canMove(moveDirection, directionsOpen):
    if moveDirection == 'n' and moveDirection == directionsOpen[0]:
        print("You go North.")
        location = roomsConnectedTo[0]
    elif moveDirection == 'e' and moveDirection == directionsOpen[1]:
        print("You go East.")
        location = roomsConnectedTo[1]
    '''elif moveDirection == 's' and moveDirection == directionsOpen[2]:
        print("You go South.")
        location = roomsConnectedTo[2]
    elif moveDirection == 'w' and moveDirection == directionsOpen[3]:
        print("You go West.")
        location = roomsConnectedTo[0]
    else:
        print("You cannot go that way.")'''
    checkLocation()
    time.sleep(1)
    return location

# Start of moving code *******************************************************   
file = shelve.open("solaireSaveFile")  #Change to character name string later
location = file["location"]
tempPickleLoc = open("tempPickleLoc.pkl","bw") #Temporary file to store location in
directionsOpen = rooms.directionsOpen[location].split()
roomsConnectedTo = rooms.roomsConnectedTo[location].split()

print("You are in room " + str(location))
time.sleep(1)
print("You can move North, East, South, or West.")
time.sleep(1)
print(directionsOpen)
time.sleep(1)
print(roomsConnectedTo)

while True:
    tempPickleLoc = open("tempPickleLoc.pkl","bw")

    print("Which direction do you go?")
    moveDirection = input().lower()
    moveDirection = moveDirection[:1]
    time.sleep(1)
    location = canMove(moveDirection, directionsOpen[location])
    pickle.dump(location, tempPickleLoc)
    print("After moving, you are now in room " + str(location))

    tempPickleLoc = open("tempPickleLoc.pkl","rb")
    location = pickle.load(tempPickleLoc)
    tempPickleLoc = open("tempPickleLoc.pkl","bw")
    pickle.dump(location,tempPickleLoc)

    location = int(location)
    directionsOpen = rooms.directionsOpen[location].split()
    roomsConnectedTo = rooms.roomsConnectedTo[location].split()
    
    print("You are in room " + str(location))
    time.sleep(1)
    print(directionsOpen)
    time.sleep(1)
    print(roomsConnectedTo)


