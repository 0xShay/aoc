def simulate_acc(cmd):

        cmd_index = 0
        acc = 0

        visited_indexes = []

        while cmd_index not in visited_indexes and cmd_index < len(cmd):
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

        if (cmd_index not in visited_indexes):
            print(acc)

with open("data.txt") as f:
    
    orig_file = f.read().split("\n")

    for ln in range(len(orig_file)):
        cmd = list(orig_file)
        cmd[ln] = cmd[ln].replace("jmp", "NOP").replace("nop", "jmp").replace("NOP", "nop")
        simulate_acc(cmd)