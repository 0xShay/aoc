with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    
    ptr = 50
    res = 0
    
    for l in lines:
        val = int(l[1:])
        if l[0] == 'L':
            ptr = (ptr - val) % 100
        else:
            ptr = (ptr + val) % 100
        if ptr == 0:
            res += 1

    print(res)