with open("data.txt") as f:
# with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    res = 0

    for line in lines:
        i = 0
        j = 0
        n1, n2 = 0, 0
        while i < len(line):

            if j == 0:
                n1, n2 = 0, 0

            if j == 4 and not (line[i].isdigit()):
                i += 1
                j = 0
                continue

            while (j == 4 or j == 5) and line[i].isdigit():
                if j == 4:
                    n1 *= 10
                    n1 += int(line[i])
                elif j == 5:
                    n2 *= 10
                    n2 += int(line[i])
                i += 1
            
            if j == 4:
                if line[i] == ',':
                    i += 1
                    j += 1
                    continue
                else:
                    i += 1
                    j = 0
                    continue
                    
            if j == 5:
                if line[i] == ')':
                    i += 1
                    j = 0
                    res += n1 * n2
                    n1, n2 = 0, 0
                    continue
                else:
                    i += 1
                    j = 0
                    continue

            if line[i] == "mul("[j]:
                j += 1
            else:
                j = 0
            i += 1

    print(res)