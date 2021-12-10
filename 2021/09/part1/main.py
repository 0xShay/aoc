lines = open("realInput.txt", "r").read().split("\n")
numbers = []

for l in lines:
    numbers.append(list(map(int, list(l))))

lilNums = []

for rowI, row in enumerate(numbers):
    for numI, num in enumerate(row):
        if (rowI == 0 or rowI == (len(lines)-1)) and (numI == 0 or numI == (len(lines[0])-1)):
            # corner, two next to
            print("e")
            if rowI == 0:
                if numI == 0:
                    # top left, one to right, one below
                    if num < min(row[numI+1], numbers[rowI+1][numI]):
                        lilNums.append(num)
                else:
                    # bot left, one to right, one above
                    if num < min(row[numI-1], numbers[rowI+1][numI]):
                        lilNums.append(num)
            else:
                if numI == 0:
                    # top right, one to left, one below
                    if num < min(row[numI+1], numbers[rowI-1][numI]):
                        lilNums.append(num)
                else:
                    # bot right, one to left, one above
                    if num < min(row[numI-1], numbers[rowI-1][numI]):
                        lilNums.append(num)
        elif (rowI == 0 or rowI == (len(lines)-1)) or (numI == 0 or numI == (len(lines[0])-1)):
            # edge, one up, one down, one side
            if rowI == 0:
                # top, one below, one left, one right
                if num < min(numbers[rowI+1][numI], row[numI-1], row[numI+1]):
                    lilNums.append(num)
            elif rowI == len(lines)-1:
                # bot, one above, one left, one right
                if num < min(numbers[rowI-1][numI], row[numI-1], row[numI+1]):
                    lilNums.append(num)
            elif numI == 0:
                # left, one to right, one above, one below
                if num < min(row[numI+1], numbers[rowI-1][numI], numbers[rowI+1][numI]):
                    lilNums.append(num)
            elif numI == len(lines[0])-1:
                # right, one to left, one above, one below
                if num < min(row[numI-1], numbers[rowI-1][numI], numbers[rowI+1][numI]):
                    lilNums.append(num)
        else:
            # normal, four next to
            if num < min(numbers[rowI-1][numI], numbers[rowI+1][numI], row[numI-1], row[numI+1]):
                lilNums.append(num)

print(lilNums)

print(sum(lilNums) + len(lilNums))