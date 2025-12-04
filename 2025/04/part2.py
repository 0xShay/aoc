with open("input.txt") as f:
    lines = f.readlines()
    
    grid = []
    
    for line in lines:
        l = []
        for ch in line.strip():
            if ch == '.':
                l.append(0)
            else:
                l.append(1)
        grid.append(l)
    
    can_access = {}
    def check_can_access(i, j):
        # check the 8 adjacent positions
        adjacent_rolls = 0
        for pos in [
            (i-1, j-1),
            (i-1, j),
            (i-1, j+1),
            (i,   j-1),
            (i,   j+1),
            (i+1, j-1),
            (i+1, j),
            (i+1, j+1),
        ]:
            if pos[0] < 0 or pos[1] < 0 or pos[0] >= len(grid) or pos[1] >= len(grid[0]):
                continue
            if grid[pos[0]][pos[1]]:
                adjacent_rolls += 1
        
        can_access[(i, j)] = (adjacent_rolls < 4)
        return (adjacent_rolls < 4)


    change_made = True
    res = 0
    
    while change_made:
        change_made = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and check_can_access(i, j):
                    change_made = True
                    grid[i][j] = 0
                    res += 1

        print(res)
            
    print(res)