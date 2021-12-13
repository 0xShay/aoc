lines = open("realInput.txt", "r").read().split("\n")

coords = []
instructions = []

coordQuery = True

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
            grid.append([False])
        else:
            grid[i].append(False)

for cod in coords:
    grid[cod[1]][cod[0]] = True

for ins in instructions:
    # ins[0] says x or y
    # ins[1] says where    
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if y > 0 and x > 0:
                if ins[0] == "x":
                    if x > (len(grid[0]) // 2):
                        # right
                        if grid[y][x] == True or grid[y][x-((x-ins[1]) * 2)] == True:
                            grid[y][x] = True
                            grid[y][x-((x-ins[1]) * 2)] = True
                    else:
                        # left
                        if grid[y][x] == True or grid[y][x+((ins[1]-x) * 2)] == True:
                            grid[y][x] = True
                            grid[y][x+((ins[1]-x) * 2)] = True
                else:
                    if y > (len(grid) // 2):
                        # bot
                        if grid[y][x] == True or grid[y-((y-ins[1]) * 2)][x] == True:
                            grid[y][x] = True
                            grid[y-((y-ins[1]) * 2)][x] = True
                    else:
                        # top
                        if grid[y][x] == True or grid[y+((ins[1]-y) * 2)][x] == True:
                            grid[y][x] = True
                            grid[y+((ins[1]-y) * 2)][x] = True
    
    newGrd = []
    if ins[0] == "x":
        for y in range(len(grid)):
            newGrd.append([])
            cnt = 0
            while cnt < (len(grid[0]) // 2):
                newGrd[y].append(grid[y][cnt])
                cnt += 1
    else:
        cnt = 0
        while cnt < (len(grid) // 2):
            newGrd.append(grid[cnt])
            cnt += 1
    grid = newGrd

dotCount = 0

for row in grid:
    for n in row:
        if n == True:
            print("#", end="")
            dotCount += 1
        else:
            print("-", end="")
    print("\n", end="")

print()
print(dotCount)