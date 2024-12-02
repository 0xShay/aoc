with open("data.txt") as f:
# with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    res = 0

    for line in lines:
        levels = [int(v) for v in line.split(" ")]
        increasing = levels[1] > levels[0]
        broken = False
        for i in range(len(levels)-1):
            if increasing and (levels[i+1] - levels[i] < 1 or levels[i+1] - levels[i] > 3):
                broken = True
                break
            if (not increasing) and (levels[i+1] - levels[i] > -1 or levels[i+1] - levels[i] < -3):
                broken = True
                break
        if not broken:
            res += 1

    print(res)