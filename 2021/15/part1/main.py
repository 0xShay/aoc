lines = open("testInput.txt", "r").read().split("\n")
ints = []
for l in lines:
    ints.append(list(map(int, [ch for ch in l])))

# print(ints)

# start at 0,0

allCoords = []

def getNeighbours(coords):
    tempCoords = []
    for cod in [
        (coords[0], coords[1]+1),
        (coords[0]+1, coords[1]),
        (coords[0]-1, coords[1]),
        (coords[0], coords[1]-1),
    ]:
        if cod[0] < len(ints[0]) and cod[0] >= 0 and cod[1] < len(ints) and cod[1] >= 0:
            tempCoords.append(cod)
    return tempCoords

def smallestKnown(tData, uVtd):
    minVal = 99999999999999999
    minCod = ()
    for c in uVtd:
        if tData[c]["dist"] < minVal and c in uVtd:
            minVal = tData[c]["dist"]
            minCod = c
    return minCod

for y in range(len(ints)):
    for x in range(len(ints[0])):
        allCoords.append((x, y))

td = {v: {"dist": 99999999999999999} for v in allCoords}
# visited = []
unvisited = list(allCoords)

td[(0,0)]["dist"] = 0

while len(unvisited) > 0:

    subjectVertex = smallestKnown(td, unvisited)
    for nb in getNeighbours(subjectVertex):
        tempDist = td[subjectVertex]["dist"] + ints[nb[1]][nb[0]]
        if tempDist < td[nb]["dist"]:
            td[nb]["dist"] = tempDist
            td[nb]["prev"] = subjectVertex
    # visited.append(subjectVertex)
    unvisited.remove(subjectVertex)

# for e in td:
    # if "prev" in td[e]:
        # print(td[e]["prev"], "=>", e, td[e]["dist"])

print()
print(td[(len(ints)-1, len(ints[0])-1)])