with open("data.txt") as f:
    pos = [0, 0]

    direction = "E"
    ns = 1
    ew = 10

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
            if value == 90:
                ns, ew = ew, -ns
            elif value == 180:
                ns, ew = -ns, -ew
            elif value == 270:
                ns, ew = -ew, ns
        elif action == "R":
            if value == 90:
                ns, ew = -ew, ns
            elif value == 180:
                ns, ew = -ns, -ew
            elif value == 270:
                ns, ew = ew, -ns
        elif action == "F":
            pos[0] += (ns*value)
            pos[1] += (ew*value)
    print(abs(pos[0]) + abs(pos[1]))