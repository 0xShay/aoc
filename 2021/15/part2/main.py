import heapq

lines = open("realInput.txt", "r").read().split("\n")

ints = []
for l in lines:
    ints.append(list(map(int, [ch for ch in l])))
    
newInts = []

for i in range(5):
    for rowNum, row in enumerate(ints):
        thisRow = []
        for num in row:
            if (num+i) % 9 == 0:
                thisRow.append(9)
            else:
                thisRow.append((num+i) % 9)
        newInts.append(thisRow)

ints = []
for row in newInts:
    thisRow = []
    for i in range(5):        
        for num in row:
            if (num+i) % 9 == 0:
                thisRow.append(9)
            else:
                thisRow.append((num+i) % 9)
    ints.append(thisRow)




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

def smallestKnown(tData, tHeap):
    minKey = tHeap[0][1]
    heapq.heappop(tHeap)
    return minKey

for y in range(len(ints)):
    for x in range(len(ints[0])):
        allCoords.append((x, y))

td = {v: {"dist": 99999999999999999} for v in allCoords}

td[(0,0)]["dist"] = 0

tdHeap = [(value["dist"], key) for key,value in td.items()]

while len(tdHeap) > 0:

    subjectVertex = smallestKnown(td, tdHeap)
    for nb in getNeighbours(subjectVertex):
        tempDist = td[subjectVertex]["dist"] + ints[nb[1]][nb[0]]
        if tempDist < td[nb]["dist"]:
            td[nb]["dist"] = tempDist
            td[nb]["prev"] = subjectVertex
            heapq.heappush(tdHeap, ((tempDist, (nb))))
    # print(subjectVertex)

print()
print(td[(len(ints)-1, len(ints[0])-1)])