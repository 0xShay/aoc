with open("data.txt") as f:
    grid = []
    for l in f.read().split("\n"):
        row = []
        for c in l:
            row.append(int(c))
        grid.append(row)
    print(grid)

    max_scenic_score = -1

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[0])-1):
            # print(row, col)
            
            # up score
            temp_row = row-1
            current_val = grid[row][col]
            while (temp_row > 0 and grid[temp_row][col] < current_val):
                temp_row -= 1
            up_score = row-temp_row

            # down score
            temp_row = row+1
            current_val = grid[row][col]
            while (temp_row < len(grid)-1 and grid[temp_row][col] < current_val):
                temp_row += 1
            down_score = temp_row-row

            # left score
            temp_col = col-1
            current_val = grid[row][col]
            while (temp_col > 0 and grid[row][temp_col] < current_val):
                temp_col -= 1
            left_score = col-temp_col

            # right score
            temp_col = col+1
            current_val = grid[row][col]
            while (temp_col < len(grid[0])-1 and grid[row][temp_col] < current_val):
                temp_col += 1
            right_score = temp_col-col

            scenic_score = up_score * down_score * left_score * right_score
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print(max_scenic_score)