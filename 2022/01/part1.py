with open("data.txt") as f:
    lines = f.read().split("\n")
    max_sum = 0
    current_sum = 0
    current_line = 0
    while current_line < len(lines):
        if lines[current_line] == "":
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        elif current_line == len(lines) - 1:
            current_sum += int(lines[current_line])
            max_sum = max(max_sum, current_sum)
            current_sum = 0
        else:
            current_sum += int(lines[current_line])
        current_line += 1
    print(max_sum)