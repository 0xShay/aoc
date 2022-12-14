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
                        if _y > maximum_y:
                            maximum_y = _y
            elif y != last_point[1]:
                for _y in range(min(y, last_point[1]), max(y+1, last_point[1]+1)):
                    if [x, _y] not in rocks:
                        rocks.append([x, _y])
                        if _y > maximum_y:
                            maximum_y = _y
            last_point = [x, y]

    print(len(rocks), maximum_y)

    sand_grains = []
    max_grains_placed = False

    while not max_grains_placed:

        _current_x, _current_y = 500, 0
        _grain_complete = False

        while not _grain_complete:

            if _current_y+1 >= (maximum_y+2):
                _grain_complete = True
            elif [_current_x, _current_y+1] not in rocks and [_current_x, _current_y+1] not in sand_grains:
                # bottom sq is not taken
                _current_y += 1
            elif [_current_x-1, _current_y+1] not in rocks and [_current_x-1, _current_y+1] not in sand_grains:
                # bottom left sq is not taken
                _current_x -= 1
                _current_y += 1
            elif [_current_x+1, _current_y+1] not in rocks and [_current_x+1, _current_y+1] not in sand_grains:
                # bottom right sq is not taken
                _current_x += 1
                _current_y += 1
            else:
                # no squares available
                _grain_complete = True
        
        if [_current_x, _current_y] == [500, 0]:
            max_grains_placed = True

        if _current_y < maximum_y+2:
            sand_grains.append([_current_x, _current_y])

        # print(_current_x, _current_y)
    
    print(len(sand_grains))