with open("input.txt") as f:
    lines = f.readlines()
    
    ranges = []
    ingredients = []
    ranges_over = False
    
    for l in lines:
        line = l.strip()
        if line == '':
            ranges_over = True
            continue
        if not ranges_over:
            [a, b] = line.split('-')
            ranges.append((int(a), int(b)))
        else:
            ingredients.append(int(line))
    
    ranges.sort()
    
    final_ranges = []
    start = ranges[0][0]
    end = ranges[0][1]
    for (i,r) in enumerate(ranges):
        if i == 0:
            continue
        if r[0] <= end:
            end = max(ranges[i-1][1], r[1])
        else:
            final_ranges.append((start, end))
            start, end = r[0], r[1]
    final_ranges.append((start, end))
    
    print(final_ranges)

    res = 0
    for fr in final_ranges:
        res += fr[1] - fr[0] + 1
        
    print(res)