lines = (open("realInput.txt", "r")).read().split("\n")

drawNumbers = list(map(int, lines[0].split(",")))

boards = []

def isValidNumber(num):
    return num.isnumeric()

for boardStart in range(2, len(lines), 6):
    boards.append(
        list(map(int, list(filter(isValidNumber, lines[boardStart+0].split(" "))))) +
        list(map(int, list(filter(isValidNumber, lines[boardStart+1].split(" "))))) +
        list(map(int, list(filter(isValidNumber, lines[boardStart+2].split(" "))))) +
        list(map(int, list(filter(isValidNumber, lines[boardStart+3].split(" "))))) +
        list(map(int, list(filter(isValidNumber, lines[boardStart+4].split(" "))))) 
    )

# print(boards)

calledNumbers = []

def hasWon(bd):

    won = False

    for row in range(5):
        totalInRow = 0
        for i in range(5):
            if bd[(row * 5) + i] in calledNumbers:
                totalInRow += 1
        if totalInRow == 5:
            won = True

    for col in range(5):
        totalInCol = 0
        for i in range(5):
            if bd[col + (i * 5)] in calledNumbers:
                totalInCol += 1
        if totalInCol == 5:
            won = True

    return won

winner = ""
winnerList = []

lastCalled = []

for toDraw in drawNumbers:
    calledNumbers.append(toDraw)
    for bd in boards:
        if hasWon(bd) and bd not in winnerList:
            winnerList.append(bd)
            winner = bd
            lastCalled = calledNumbers.copy()
            lastDrawn = toDraw

print("=================")

print(winner)
print(lastCalled)

sumOfUncalled = 0

for num in winner:
    if not num in lastCalled:
        sumOfUncalled += num

print(sumOfUncalled)
print(lastDrawn)
print(f"{str(sumOfUncalled)} * {str(lastDrawn)} = {str(sumOfUncalled * lastDrawn)}") 