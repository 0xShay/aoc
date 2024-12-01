from collections import defaultdict

with open("data.txt") as f:
    lines = f.read().split("\n")
    current_line = 0
    l1, l2 = [], []
    counts = defaultdict(lambda: 0)
    ss = 0
    while current_line < len(lines):
        l, r = [int(v) for v in lines[current_line].split("   ")]
        l1.append(l)
        l2.append(r)
        current_line += 1
    for val in l2:
        counts[val] += 1
    for val in l1:
        ss += val * counts[val]
    print(ss)