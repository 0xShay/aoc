fishAges = list(map(int, (open("realInput.txt", "r")).read().split(",")))
# print(fishAges)

dayCount = 256
mostRecent = []

for dayNum in range(dayCount):
    newFishAges = []
    for fishAge in fishAges:
        if fishAge == 0:
            newFishAges.append(6)
            newFishAges.append(8)
        else:
            newFishAges.append(fishAge - 1)
    fishAges = list(newFishAges)
    print(f"day {dayNum+1} | {len(newFishAges)}")
    mostRecent = list(newFishAges)

# print(len(mostRecent))