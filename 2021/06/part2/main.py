fishAges = list(map(int, (open("realInput.txt", "r")).read().split(",")))
# print(fishAges)

ages = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for age in fishAges:
    ages[age] += 1

print(ages)

dayCount = 256
mostRecent = []

for dayNum in range(dayCount):
    newAges = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ageLevel, fishes in enumerate(ages):
        if ageLevel == 0:
            newAges[8] = fishes
            newAges[6] += fishes
        if ageLevel >= 1 and ageLevel <= 8:
            newAges[ageLevel - 1] += fishes
    ages = newAges
    print(f"day {dayNum} | {newAges}")
    mostRecent = list(newAges)

# print(len(mostRecent))

print(sum(ages))