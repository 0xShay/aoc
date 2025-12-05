import bisect

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
    
    print([r[0] for r in final_ranges])
    print(final_ranges)

    print()
    
    print(ingredients)
    
    print()
    
    res = 0
    for val in ingredients[0:]:
        # binary search for the range just under the value
        range_ix = bisect.bisect_left([r[0] for r in final_ranges], val)-1
        if range_ix == -1:
            continue
        if val >= final_ranges[range_ix][0] and val <= final_ranges[range_ix][1]:
            res += 1
            
    print(res)