with open("input.txt") as f:
    lines = f.readlines()
    
    res = 0
    
    for l in lines:
        vals = [int(ch) for ch in l.strip()]

        digits = []
        ptr = 0
        jolts = 0
        
        print(vals)
        
        for _ in range(12):
            # get the biggest digit in the next 12 digits (but before the final 12-len(digits))
            window = vals[ptr:len(vals)-11+len(digits)]
            print(f"{window=} {ptr=} {digits=}")
            
            max_ix = None
            max_val = 0
            for i in range(ptr, len(vals)-11+len(digits)):
                if vals[i] > max_val:
                    max_ix = i
                    max_val = vals[i]
            
            if max_ix != None:
                digits.append(max_val)
                ptr = max_ix + 1
            
        i = 0
        while digits:
            jolts += digits.pop() * 10**i
            i += 1
        
        print(jolts)
        
        res += jolts
        
    print(res)