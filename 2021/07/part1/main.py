crabPos = list(map(int, (open("realInput.txt", "r")).read().split(",")))

fuelUsed = []

for target in range(min(crabPos), max(crabPos)):
    totalFuelUsed = 0
    for crab in crabPos:
        totalFuelUsed += abs(crab - target)
    fuelUsed.append(totalFuelUsed)

print(min(fuelUsed))
# print(fuelUsed)