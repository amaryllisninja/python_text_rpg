import pickle
import time

numbers = [3, 9, 27]

file = open("data.pkl","bw")
pickle.dump(numbers,file)
file.close()

print("Exporting/importing file...")
time.sleep(1)

newFile = open("data.pkl","rb")
recoveredNumbers = pickle.load(newFile)
print(recoveredNumbers)

numberList = dict(recoveredNumbers)

print('\n'.join(numberList))

file.close()
