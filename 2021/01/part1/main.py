depths = (open("realInput.txt", "r")).read()

lastDepth = int(depths.split()[0]) * 2
increasedCount = 0

for depth in depths.split():
    if int(depth) > lastDepth:
        increasedCount += 1
    lastDepth = int(depth)

print(increasedCount)