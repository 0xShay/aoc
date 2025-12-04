with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]
    
    ptr = 50
    res = 0
        
    for step in lines:
        val = int(step[1:])
        
        for _ in range(val):
            if step[0] == 'L':
                ptr -= 1
            else:
                ptr += 1
            ptr = ptr % 100
            if ptr == 0:
                res += 1

    print(res)