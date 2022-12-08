with open("data.txt") as f:
    grid = []
    for l in f.read().split("\n"):
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row)
    print(grid)

    seeable = []

    # check all top downwards
    for i in range(len(grid[0])):
        ct = -1
        for cti in range(len(grid)):
            if ct < grid[cti][i]:
                seeable.append([cti, i])
                ct = grid[cti][i]
                cti += 1

    # check all down upwards
    for i in range(len(grid[0])):
        ct = -1
        for cti in range(len(grid)-1, -1, -1):
            if ct < grid[cti][i]:
                seeable.append([cti, i])
                ct = grid[cti][i]
                cti -= 1

    # check all left rightwards
    for i in range(len(grid)):
        ct = -1
        for cti in range(len(grid[0])):
            if ct < grid[i][cti]:
                seeable.append([i, cti])
                ct = grid[i][cti]
                cti += 1

    # check all right leftwards
    for i in range(len(grid)):
        ct = -1
        for cti in range(len(grid)-1, -1, -1):
            if ct < grid[i][cti]:
                seeable.append([i, cti])
                ct = grid[i][cti]
                cti -= 1

    counted = []

    for tree_loc in seeable:
        if tree_loc not in counted:
            counted.append(tree_loc)
    
    print(counted)
    print(len(counted))