import re

print()
inputString = input().lower().split()
print(inputString)

if inputString[0] == 'look':
    print("You look ", end="")
    if inputString[1] == 'at':
        for c in range(len(inputString)):
            if c != 0:
                print(inputString[c], end=" ")        
else:
    print("I don't understand.")
