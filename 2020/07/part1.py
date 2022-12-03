with open("data.txt") as f:

    bags = {}

    for line in f.read().split("\n"):
        container = line.split(" bags contain ")[0]
        contents = []
        if "no other bags" not in line:
            for c in line.split(" bags contain ")[1].split(", "):
                contents.append(c.split(" ")[1] + " " + c.split(" ")[2])
        bags[container] = contents

    parent_bags = ["shiny gold"]
    prev_length = -1

    while len(parent_bags) != prev_length:
        prev_length = len(parent_bags)

        for b in bags.keys():
            for p in parent_bags:
                if p in bags[b]:
                    if b not in parent_bags:
                        parent_bags.append(b)

    print(len(parent_bags)-1)