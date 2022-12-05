with open("data.txt") as f:
    lines = f.read().split("\n")
    line_index = 0

    num_stacks = int((1 + len(lines[0])) / 4)
    stacks = [[] for n in range(num_stacks)]
    int_positions = [(4*x)+1 for x in range(num_stacks)]

    while lines[line_index+1] != "":
        for i in range(num_stacks):
            if lines[line_index][int_positions[i]] != " ":
                stacks[i].append(lines[line_index][int_positions[i]])
        line_index += 1
    
    print(stacks)

    instructions = []
    line_index += 2
    for l in lines[line_index:]:
        q = int(l.split(" ")[1])
        src = int(l.split(" ")[3])-1
        dest = int(l.split(" ")[5])-1
        instructions.append([q, src, dest])
    
    # GOT HERE
    for ins in instructions:
        for i in range(ins[0]):
            elem = stacks[ins[1]].pop(0)
            stacks[ins[2]].insert(0, elem)
    
    for s in stacks:
        print(s[0], end="")