depths = (open("realInput.txt", "r")).read().split()

lastSum = (int(depths[0]) + int(depths[1]) + int(depths[2])) * 2
increasedCount = 0

for i in range(len(depths) - 2):
    thisSum = int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2])
    if not i == 0:
        print(f"{depths[i]} {depths[i + 1]} {depths[i + 2]}")
        if thisSum > lastSum:
            increasedCount += 1
    lastSum = thisSum

print(increasedCount)