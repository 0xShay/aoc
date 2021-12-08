crabPos = list(map(int, (open("realInput.txt", "r")).read().split(",")))

tNums = []
lastOneSum = 0
lastAdded = 0
for i in range(max(crabPos) - min(crabPos)):
    lastAdded += 1
    tNums.append(lastOneSum + lastAdded)
    lastOneSum += lastAdded

print(tNums)

fuelUsed = []

for target in range(min(crabPos), max(crabPos)):
    totalFuelUsed = 0
    for crab in crabPos:
        totalFuelUsed += tNums[abs(crab - target)-1]
    fuelUsed.append(totalFuelUsed)

print(min(fuelUsed))