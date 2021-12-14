lines = open("realInput.txt", "r").read().split("\n")

letterBox = []

insertionRules = {}
polymer = ""

coordQuery = True

for l in lines:
    for char in l:
        if char not in letterBox and char not in " -> ":
            letterBox.append(char)
    if coordQuery == True:
        if l == "":
            coordQuery = False
        else:
            polymer = l
    else:
        insertionRules[l.split(" -> ")[0]] = l.split(" -> ")[1]

print("0)", polymer)

for i in range(10):

    toAdd = []
    for ltrI in range(len(polymer)-1):
        pair = (polymer[ltrI] + polymer[ltrI+1])
        toAdd.append(insertionRules[pair])

    newPolymer = ""
    # print(toAdd)
    for ltrI in range(len(polymer)-1):
        newPolymer += (polymer[ltrI] + toAdd[ltrI])
    newPolymer += (polymer[-1])

    polymer = newPolymer

    # print(str(i+1) + ")", polymer)

occurences = [polymer.count(c) for c in letterBox]
print(max(occurences) - min(occurences))