lines = open("realInput.txt", "r").read().split("\n")
numbers = []

for l in lines:
    numbers.append(list(map(int, list(l))))

lilNums = []

for rowI, row in enumerate(numbers):
    for numI, num in enumerate(row):
        if (rowI == 0 or rowI == (len(lines)-1)) and (numI == 0 or numI == (len(lines[0])-1)):
            # corner, two next to
            if rowI == 0:
                if numI == 0:
                    # top left, one to right, one below
                    if num < min(row[numI+1], numbers[rowI+1][numI]):
                        lilNums.append(((numI, rowI), num))
                else:
                    # bot left, one to right, one above
                    if num < min(row[numI-1], numbers[rowI+1][numI]):
                        lilNums.append(((numI, rowI), num))
            else:
                if numI == 0:
                    # top right, one to left, one below
                    if num < min(row[numI+1], numbers[rowI-1][numI]):
                        lilNums.append(((numI, rowI), num))
                else:
                    # bot right, one to left, one above
                    if num < min(row[numI-1], numbers[rowI-1][numI]):
                        lilNums.append(((numI, rowI), num))
        elif (rowI == 0 or rowI == (len(lines)-1)) or (numI == 0 or numI == (len(lines[0])-1)):
            # edge, three next to
            if rowI == 0:
                # top, one below, one left, one right
                if num < min(numbers[rowI+1][numI], row[numI-1], row[numI+1]):
                    lilNums.append(((numI, rowI), num))
            elif rowI == len(lines)-1:
                # bot, one above, one left, one right
                if num < min(numbers[rowI-1][numI], row[numI-1], row[numI+1]):
                    lilNums.append(((numI, rowI), num))
            elif numI == 0:
                # left, one to right, one above, one below
                if num < min(row[numI+1], numbers[rowI-1][numI], numbers[rowI+1][numI]):
                    lilNums.append(((numI, rowI), num))
            elif numI == len(lines[0])-1:
                # right, one to left, one above, one below
                if num < min(row[numI-1], numbers[rowI-1][numI], numbers[rowI+1][numI]):
                    lilNums.append(((numI, rowI), num))
        else:
            # normal, four next to
            if num < min(numbers[rowI-1][numI], numbers[rowI+1][numI], row[numI-1], row[numI+1]):
                lilNums.append(((numI, rowI), num))

print(lilNums)

totSizes = []
productResult = 1

for n in lilNums:
    countedCoords = []
    totalSize = 0

    def checkSur(coords):

        # coords = n[0]
        surrounding = []

        if coords[0] == 0:
            if coords[1] == 0:
                # top left corner
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0], coords[1]+1))
            elif coords[1] == len(numbers)-1:
                # bot left corner
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0], coords[1]-1))
            else:
                # left side
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0], coords[1]+1))
                surrounding.append((coords[0], coords[1]-1))
        elif coords[0] == len(numbers[0])-1:
            if coords[1] == 0:
                # top right corner
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0], coords[1]+1))
            elif coords[1] == len(numbers)-1:
                # bot right corner
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0], coords[1]-1))
            else:
                # right side
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0], coords[1]+1))
                surrounding.append((coords[0], coords[1]-1))
        else:
            if coords[1] == 0:
                # top row
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0], coords[1]+1))
            elif coords[1] == len(numbers)-1:
                # bot row
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0], coords[1]-1))
            else:
                # mid row
                surrounding.append((coords[0]-1, coords[1]))
                surrounding.append((coords[0]+1, coords[1]))
                surrounding.append((coords[0], coords[1]-1))
                surrounding.append((coords[0], coords[1]+1))

        basinSize = 0

        for cod in surrounding:
            if numbers[cod[1]][cod[0]] < 9 and cod not in countedCoords:
                countedCoords.append(cod)
                basinSize += 1
                basinSize += checkSur(cod)

        return basinSize

    totalSize += checkSur(n[0])
    totSizes.append(totalSize)
    print(totalSize)

totSizes.sort(reverse=True)

print(totSizes)
print(totSizes[0] * totSizes[1] * totSizes[2])