with open("input.txt") as f:
    lines = f.read().split(',')
    
    res = 0
    
    for l in lines:
        print("line", l)
        start, end = map(int, l.strip().split('-'))
        
        considered = set()
        for solo in range(1, int(str(end)[:(len(str(end)) // 2)+1])):
            num = int(str(solo) + str(solo))
            while num <= end:
                if num not in considered and num >= start:
                    print(num)
                    considered.add(num)
                    res += num
                num = int(str(num) + str(solo))
        print()
    print("===")
    print(res)