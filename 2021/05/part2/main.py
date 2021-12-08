lines = (open("realInput.txt", "r")).read().split("\n")

coords = []

for l in lines:
    coord0 = l.split(" -> ")[0].split(",")
    coord1 = l.split(" -> ")[1].split(",")
    # if (coord0[0] == coord1[0] or coord0[1] == coord1[1]):
    coords.append(([int(coord0[0]), int(coord0[1])], [int(coord1[0]), int(coord1[1])]))

# print(coords)

lineOn = {}

for coordPair in coords:

    if coordPair[0][0] == coordPair[1][0]:
        # two x coords are same, loop y
        for y in range(
            min(coordPair[0][1], coordPair[1][1]), max(coordPair[0][1], coordPair[1][1])+1
        ):
            if (coordPair[0][0], y) in lineOn:
                lineOn[(coordPair[0][0], y)] += 1
            else:
                lineOn[(coordPair[0][0], y)] = 1
                
    if coordPair[0][1] == coordPair[1][1]:
        # two y coords are same, loop x
        for x in range(
            min(coordPair[0][0], coordPair[1][0]), max(coordPair[0][0], coordPair[1][0])+1
        ):
            if (x, coordPair[0][1]) in lineOn:
                lineOn[(x, coordPair[0][1])] += 1
            else:
                lineOn[(x, coordPair[0][1])] = 1

    # neither x nor y match on coords, diagonal
    if (coordPair[0][0] != coordPair[1][0]) and (coordPair[0][1] != coordPair[1][1]):
            
        # find gradient, 1 or -1?
        gradient = (coordPair[1][1] - coordPair[0][1]) / (coordPair[1][0] - coordPair[0][0])

        # find starting point (smallest x, furthest left)
        if gradient == -1:
            if coordPair[0][0] < coordPair[1][0]:
                # start at coordPair[0], it's furthest left,
                # and deduct -1 from both x and y in loop, appending points
                for i in range((coordPair[1][0]+1) - coordPair[0][0]):
                    if (coordPair[0][0]+i, coordPair[0][1]-i) in lineOn:
                        lineOn[(coordPair[0][0]+i, coordPair[0][1]-i)] += 1
                    else:
                        lineOn[(coordPair[0][0]+i, coordPair[0][1]-i)] = 1
            else:
                # start at coordPair[1], it's furthest left (going towards coordPair[0]),
                # and deduct -1 from x/y in loop, appending
                for i in range((coordPair[0][0]+1) - coordPair[1][0]):
                    if (coordPair[1][0]+i, coordPair[1][1]-i) in lineOn:
                        lineOn[(coordPair[1][0]+i, coordPair[1][1]-i)] += 1
                    else:
                        lineOn[(coordPair[1][0]+i, coordPair[1][1]-i)] = 1
        else:
            # gradient is positive
            if coordPair[0][0] < coordPair[1][0]:
                # start at coordPair[0], it's furthest left,
                for i in range((coordPair[1][0]+1) - coordPair[0][0]):
                    if (coordPair[0][0]+i, coordPair[0][1]+i) in lineOn:
                        lineOn[(coordPair[0][0]+i, coordPair[0][1]+i)] += 1
                    else:
                        lineOn[(coordPair[0][0]+i, coordPair[0][1]+i)] = 1
            else:
                # start at coordPair[1], it's furthest left (going towards coordPair[0]),
                for i in range((coordPair[0][0]+1) - coordPair[1][0]):
                    if (coordPair[1][0]+i, coordPair[1][1]+i) in lineOn:
                        lineOn[(coordPair[1][0]+i, coordPair[1][1]+i)] += 1
                    else:
                        lineOn[(coordPair[1][0]+i, coordPair[1][1]+i)] = 1

# print(lineOn)

dangerCount = 0

for cod in lineOn:
    if lineOn[cod] > 1:
        dangerCount += 1
    
print(dangerCount)