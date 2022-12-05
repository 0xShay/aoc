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

    print(res)