with open("data.txt") as f:
    res = 0
    for line in f.read().split("\n"):
        p1_min = int(line.split(",")[0].split("-")[0])
        p1_max = int(line.split(",")[0].split("-")[1])
        p2_min = int(line.split(",")[1].split("-")[0])
        p2_max = int(line.split(",")[1].split("-")[1])
        if p1_min >= p2_min and p1_max <= p2_max:
            res += 1
        elif p2_min >= p1_min and p2_max <= p1_max:
            res += 1
    print(res)