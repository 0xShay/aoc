DIRECTIONS = ["N", "E", "S", "W"]

with open("data.txt") as f:
    direction = "E"
    ns = 0
    ew = 0
    for l in f.read().split("\n"):
        action = l[0]
        value = int(l[1:])
        print(action, value)
        if action == "N":
            ns += value
        elif action == "S":
            ns -= value
        elif action == "E":
            ew += value
        elif action == "W":
            ew -= value
        elif action == "L":
            direction = DIRECTIONS[(DIRECTIONS.index(direction) - int((value/90))) % 4]
        elif action == "R":
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + int((value/90))) % 4]
        elif action == "F":
            if direction == "N":
                ns += value
            elif direction == "S":
                ns -= value
            elif direction == "E":
                ew += value
            elif direction == "W":
                ew -= value
    print(abs(ns) + abs(ew))