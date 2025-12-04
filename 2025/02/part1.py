with open("input.txt") as f:
    lines = f.read().split(',')
    
    res = 0
    
    for l in lines:
        start, end = map(int, l.strip().split('-'))
        
        for solo in range(1, end+1):
            num = int(str(solo) + str(solo))
            if num > end:
                break
            if num >= start:
                res += num
        
    print(res)