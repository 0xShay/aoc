with open("data.txt") as f:
# with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    res = 0

    for line in lines:
        levels = [int(v) for v in line.split(" ")]
        broken2 = False

        for to_ignore in range(len(levels)):
            a, b = None, None
            for (k,val) in enumerate(levels):
                if k == to_ignore:
                    continue
                if a == None:
                    a = val
                elif b == None:
                    b = val
                else:
                    break
            increasing = b > a

            broken = False
            prev = 0 if to_ignore != 0 else 1
            for i in range(1 if to_ignore != 0 else 2, len(levels)):
                if prev == to_ignore:
                    prev += 1
                if i == to_ignore:
                    continue
                if increasing and (levels[i] - levels[prev] < 1 or levels[i] - levels[prev] > 3):
                    broken = True
                    break
                if (not increasing) and (levels[i] - levels[prev] > -1 or levels[i] - levels[prev] < -3):
                    broken = True
                    break
                prev = i
            if not broken:
                broken2 = True
                break
        
        if broken2:
            res += 1

    print(res)