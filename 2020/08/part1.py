with open("data.txt") as f:
    
    cmd = f.read().split("\n")
    cmd_index = 0
    acc = 0

    visited_indexes = []

    while cmd_index not in visited_indexes:
        visited_indexes.append(cmd_index)
        _cmd = cmd[cmd_index].split(" ")[0]
        _arg = int(cmd[cmd_index].split(" ")[1])
        if _cmd == "nop":
            cmd_index += 1
        elif _cmd == "acc":
            acc += _arg
            cmd_index += 1
        elif _cmd == "jmp":
            cmd_index += _arg

    print(acc)