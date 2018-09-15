import shelve

newNames = ["corinth", "steven", "crystal", "bob", "joetheplumber", "morty", "rick", "solaire"]

file = shelve.open("charactersSaved")

#file["names"] = newNames
file.append("greg")
print(dict(file))
file.close()
