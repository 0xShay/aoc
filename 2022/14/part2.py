with open("data.txt") as f:
    
    rocks = []
    maximum_y = 0

    for l in f.read().split("\n"):
        points = l.split(" -> ")
        last_point = list(map(int, points[0].split(",")))
        for pt in points[1:]:
            x, y = list(map(int, pt.split(",")))
            if x != last_point[0]:
                for _x in range(min(x, last_point[0]), max(x+1, last_point[0]+1)):
                    if [_x, y] not in rocks:
                        rocks.append([_x, y])
                        if y > maximum_y:
                            maximum_y = y
            elif y != last_point[1]:
                for _y in range(min(y, last_point[1]), max(y+1, last_point[1]+1)):
                    if [x, _y] not in rocks:
                        rocks.append([x, _y])
                        if _y > maximum_y:
                            maximum_y = _y
            last_point = [x, y]
    
    print(len(rocks), maximum_y)

    sand_grains = []
    to_check = [[500,0]]

    while len(to_check) > 0:

        c = to_check.pop()

        if c[1]+1 < maximum_y+2:
            
            # check below
            if [c[0], c[1]+1] not in rocks:
                if [c[0], c[1]+1] not in sand_grains:
                    sand_grains.append([c[0], c[1]+1])
                    to_check.append([c[0], c[1]+1])
            # check bottom left
            if [c[0]-1, c[1]+1] not in rocks:
                if [c[0]-1, c[1]+1] not in sand_grains:
                    sand_grains.append([c[0]-1, c[1]+1])
                    to_check.append([c[0]-1, c[1]+1])
            # check bottom right
            if [c[0]+1, c[1]+1] not in rocks:
                if [c[0]+1, c[1]+1] not in sand_grains:
                    sand_grains.append([c[0]+1, c[1]+1])
                    to_check.append([c[0]+1, c[1]+1])

    print(len(sand_grains)+1)