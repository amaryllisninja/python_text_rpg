directionsOpen = ['n', 'e', 's', 'w']

print("Enter a direction:")
moveDirection = input()

if moveDirection == 'n' and moveDirection == directionsOpen[0]:
    print("You go North.")
elif moveDirection == 'e' and moveDirection == directionsOpen[1]:
    print("You go East.")
elif moveDirection == 's' and moveDirection == directionsOpen[2]:
    print("You go South.")
elif moveDirection == 'w' and moveDirection == directionsOpen[3]:
    print("You go West.")
else:
    print("You cannot go that way.")
