def try_slope(grid, right, down):

    pos = [0, 0]
    tree_count = 0

    while pos[0] < len(grid):
        if (grid[pos[0]][pos[1]] == "#"):
            tree_count += 1
        new_y = pos[0]+down
        new_x = (pos[1]+right)%len(grid[0])
        pos = [new_y, new_x]
    
    print(f"{tree_count} trees encountered with {right}r {down}d")
    return tree_count

with open("data.txt") as f:
    
    grid = []
    for l in f.read().split("\n"):
        row = []
        for c in l:
            row.append(c)
        grid.append(row)

    result = 1
    result *= try_slope(grid, 1, 1)
    result *= try_slope(grid, 3, 1)
    result *= try_slope(grid, 5, 1)
    result *= try_slope(grid, 7, 1)
    result *= try_slope(grid, 1, 2)
    print(result)