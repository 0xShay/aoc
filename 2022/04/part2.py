with open("data.txt") as f:
    res = 0
    for line in f.read().split("\n"):
        p1_min = int(line.split(",")[0].split("-")[0])
        p1_max = int(line.split(",")[0].split("-")[1])
        p2_min = int(line.split(",")[1].split("-")[0])
        p2_max = int(line.split(",")[1].split("-")[1])
        p1 = [i for i in range(p1_min, p1_max+1)]
        p2 = [i for i in range(p2_min, p2_max+1)]
        overlap = False
        for i in p1:
            if i in p2:
                overlap = True
        if overlap:
            res += 1
    print(res)