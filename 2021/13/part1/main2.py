lines = open("testInput.txt", "r").read().split("\n")

coords = []
instructions = []

coordQuery = True

def getAxis(cod, axis):
    return cod[axis]

def flipY(grd):
    newGrd = []
    for y in range(len(grd)):
        if y < (len(grd) // 2):
            newGrd.append(grd[y])
        else:
            for char in grd[y - (len(grd) // 2)]:
                newRow = []
                for char2 in grd[y]:
                    if (char == "#") or (char2 == "#"):
                        newRow.append("#")
                    else:
                        newRow.append("-")
                newGrd.append(newRow)
    return newGrd

def cut(grd, axis, val):
    newGrd = []
    if axis == "y":
        for i in range(val):
            newGrd.append(grd[i])
    else:
        for y, row in enumerate(grd):
            for i in range(val):
                if i == 0:
                    newGrd.append([row[i]])
                else:
                    newGrd[y].append(row[i])
    return newGrd

for l in lines:
    if coordQuery == True:
        if l == "":
            coordQuery = False
        else:
            coords.append((int(l.split(",")[0]), int(l.split(",")[1])))
    else:
        instructions.append((l.split("fold along ")[1].split("=")[0], int(l.split("fold along ")[1].split("=")[1])))

x_list = []
y_list = []
for cod in coords:
    x_list.append(cod[0])
    y_list.append(cod[1])

grid = []

for i in range(max(y_list)+1):
    for i2 in range(max(x_list)+1):
        if i2 == 0:
            grid.append(["-"])
        else:
            grid[i].append("-")

for cod in coords:
    grid[cod[1]][cod[0]] = "#"

grid = flipY(grid)

print()
for row in grid:
    print("".join(row))

