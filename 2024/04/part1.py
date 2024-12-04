WORD = "XMAS"

NORTH     = (1, 0)
NORTHEAST = (1, 1)
EAST      = (0, 1)
SOUTHEAST = (-1, 1)
WEST      = (0, -1)
SOUTHWEST = (-1, -1)
SOUTH     = (-1, 0)
NORTHWEST = (1, -1)

directions = [NORTH, NORTHEAST, EAST, SOUTHEAST, WEST, SOUTHWEST, SOUTH, NORTHWEST]

with open("data.txt") as f:
# with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    res = 0
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            for direction in directions:
                a, b = i, j
                valid = True
                ltr = 0
                while ltr < len(WORD):
                    if a < 0 or b < 0 or a >= len(lines) or b >= len(lines[0]):
                        valid = False
                        break
                    if lines[a][b] != WORD[ltr]:
                        valid = False
                        break
                    a += direction[0]
                    b += direction[1]
                    ltr += 1
                if valid:
                    print((i, j, direction))
                    res += 1
    print(res)