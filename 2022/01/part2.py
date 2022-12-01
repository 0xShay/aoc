with open("data.txt") as f:
    lines = f.read().split("\n")
    current_sum = 0
    current_line = 0
    elf_totals = []
    while current_line < len(lines):
        if lines[current_line] == "":
            elf_totals.append(current_sum)
            current_sum = 0
        elif current_line == len(lines) - 1:
            current_sum += int(lines[current_line])
            elf_totals.append(current_sum)
            current_sum = 0
        else:
            current_sum += int(lines[current_line])
        current_line += 1
    r1 = max(elf_totals)
    elf_totals.remove(r1)
    r2 = max(elf_totals)
    elf_totals.remove(r2)
    r3 = max(elf_totals)
    elf_totals.remove(r3)
    print(r1 + r2 + r3)