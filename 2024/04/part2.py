with open("data.txt") as f:
# with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    res = 0
    for i in range(1, len(lines)-1):
        for j in range(1, len(lines[i])-1):
            tl = lines[i-1][j-1]
            bl = lines[i+1][j-1]
            tr = lines[i-1][j+1]
            br = lines[i+1][j+1]
            if lines[i][j] != 'A':
                continue
            if tl == 'M':
                if br == 'S':
                    if (tr, bl) in [('M', 'S'), ('S', 'M')]:
                        res += 1
                        continue
            if tr == 'M':
                if bl == 'S':
                    if (tl, br) in [('M', 'S'), ('S', 'M')]:
                        res += 1
                        continue
            if bl == 'M':
                if tr == 'S':
                    if (tl, br) in [('M', 'S'), ('S', 'M')]:
                        res += 1
                        continue
            if br == 'M':
                if tl == 'S':
                    if (tr, bl) in [('M', 'S'), ('S', 'M')]:
                        res += 1
                        continue
    print(res)