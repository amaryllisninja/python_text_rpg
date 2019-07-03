# Moving from room to room
def canMove(moveDirection, directionsOpen, roomsConnectedTo, name):
    tempPickleLoc = open(".\\temp\\tempPickleLoc.pkl","rb")
    location = pickle.load(tempPickleLoc)
    tempPickleLoc.close()
    if moveDirection == 'n' and moveDirection == directionsOpen[0]:
        print("You go North.")
        location = roomsConnectedTo[0]
    elif moveDirection == 'e' and moveDirection == directionsOpen[1]:
        print("You go East.")
        location = roomsConnectedTo[1]
    elif moveDirection == 's' and moveDirection == directionsOpen[2]:
        print("You go South.")
        location = roomsConnectedTo[2]
    elif moveDirection == 'w' and moveDirection == directionsOpen[3]:
        print("You go West.")
        location = roomsConnectedTo[3]
    else:
        print("You cannot go that way.")
        print(moveDirection)
    print("After moving, you are now in " + rooms.roomNames[int(location)] + ".")
    time.sleep(1)
    return location
