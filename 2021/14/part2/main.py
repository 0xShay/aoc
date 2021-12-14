import math

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

print(polymer)

pairCount = {}

for chI in range(len(polymer)-1):
    if polymer[chI] + polymer[chI+1] in pairCount:
        pairCount[polymer[chI] + polymer[chI+1]] += 1
    else:
        pairCount[polymer[chI] + polymer[chI+1]] = 1

# print(pairCount)

for i in range(40):

    lastPair = ""
    newPairCount = {}

    for pair in pairCount:
        newChar = insertionRules[pair]
        if pair == lastPair:
            addVal = 2
        else:
            addVal = 1
        if (pair[0] + newChar) in newPairCount:
            newPairCount[pair[0] + newChar] += (pairCount[pair] * addVal)
        else:
            newPairCount[pair[0] + newChar] = (pairCount[pair] * addVal)
        if (newChar + pair[1]) in newPairCount:
            newPairCount[newChar + pair[1]] += (pairCount[pair] * addVal)
        else:
            newPairCount[newChar + pair[1]] = (pairCount[pair] * addVal)
    
    pairCount = newPairCount

# print(newPairCount)

letterFreq = {}

for pr in newPairCount:
    if pr[0] in letterFreq:
        letterFreq[pr[0]] += newPairCount[pr]
    else:
        letterFreq[pr[0]] = newPairCount[pr]
    if pr[1] in letterFreq:
        letterFreq[pr[1]] += newPairCount[pr]
    else:
        letterFreq[pr[1]] = newPairCount[pr]

lfList = []

for l in letterFreq:
    lfList.append(int(math.ceil(letterFreq[l] / 2)))
    letterFreq[l] = int(math.ceil(letterFreq[l] / 2))

print(max(lfList) - min(lfList))