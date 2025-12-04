with open("input.txt") as f:
    lines = f.readlines()
    
    res = 0
    
    for l in lines:
        vals = [int(ch) for ch in l.strip()]
        
        max_after = [0]
        for i in range(len(vals)-1, -1, -1):
            max_after.append(max(max_after[-1], vals[i]))
        max_after.pop()
        max_after.reverse()
        print(vals)
        print(max_after)
        print()
        
        jolts = 0
        for i in range(len(vals)-1):
            jolts = max(jolts, (vals[i]*10) + max_after[i])
        
        res += jolts
        
    print(res)