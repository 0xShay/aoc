interesting_values = []
interesting_cycles = [20, 60, 100, 140, 180, 220]

with open("data.txt") as f:

    next_cycle_job = 0
    current_cycle_index = 0
    X = 1

    for i, l in enumerate(f.read().split("\n")):
        X += next_cycle_job
        add_cycle_x = False
        if l.split(" ")[0] == "addx":
            next_cycle_job = int(l.split(" ")[1])
            current_cycle_index += 1
            if current_cycle_index in interesting_cycles:
                interesting_values.append(current_cycle_index*X)
            current_cycle_index += 1
        else:
            next_cycle_job = 0
            current_cycle_index += 1
        if current_cycle_index in interesting_cycles:
            interesting_values.append(current_cycle_index*X)    

    print(sum(interesting_values))

    #  cycles