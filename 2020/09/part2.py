with open("data.txt") as f:

    preamble = int(input("Enter preamble size: "))

    lines = list(map(int, f.read().split("\n")))
    prev = lines[:preamble]
    first_index = 0

    res = -1

    while first_index < len(lines) and res == -1:

        prev = lines[first_index:first_index+preamble]        
        target = lines[first_index+preamble]
        
        # check if two unique values in prev can sum to target

        possible_sums = []

        for i1 in prev:
            for i2 in prev:
                possible_sums.append(i1 + i2)

        if target not in possible_sums:
            res = target

        first_index += 1

    # print(res)

    start_index = 0
    res2 = -1
    while start_index < len(lines) and res2 == -1:
        acc = 0
        current_index = start_index
        while acc < res:
            acc += lines[current_index]
            current_index += 1
        if acc == res:
            res2 = min(lines[start_index:current_index]) + max(lines[start_index:current_index])
        start_index += 1

    print(res2)