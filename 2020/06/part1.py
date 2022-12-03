with open("data.txt") as f:
    
    groups = []
    group = []

    for line in f.read().split("\n") + [""]:
        if line == "":
            groups.append(group)
            group = []
        else:
            for char in line:
                if char not in group:
                    group.append(char)

    result = 0
    for g in groups:
        result += len(g)

    print(result)