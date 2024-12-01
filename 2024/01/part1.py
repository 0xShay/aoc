with open("data.txt") as f:
    lines = f.read().split("\n")
    current_line = 0
    l1, l2 = [], []
    while current_line < len(lines):
        l, r = [int(v) for v in lines[current_line].split("   ")]
        l1.append(l)
        l2.append(r)
        current_line += 1
    l1.sort()
    l2.sort()
    print(sum([abs(l - r) for (l, r) in zip(l1, l2)]))