with open("data.txt") as f:
    grid = []
    for l in f.read().split("\n"):
        row = []
        for c in l:
            row.append(c)
        grid.append(row)

    pos = [0, 0]
    tree_count = 0

    while pos[0] < len(grid):
        if (grid[pos[0]][pos[1]] == "#"):
            tree_count += 1
        new_y = pos[0]+1
        new_x = (pos[1]+3)%len(grid[0])
        pos = [new_y, new_x]
    
    print(tree_count, "trees encountered")