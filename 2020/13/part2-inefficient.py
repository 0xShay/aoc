with open("data-sample.txt") as f:
    lines = f.read().split("\n")
    base_time = int(lines[0])
    bus_ids = []
    bus_ixes = []
    for i in range(len(lines[1].split(","))):
        if lines[1].split(",")[i] != "x":
            bus_ids.append(int(lines[1].split(",")[i]))
            bus_ixes.append(i)
    print(bus_ids, bus_ixes)
    temp_timestamp = 0
    target_timestamp = 0
    

    while target_timestamp == 0:
        temp_timestamp += bus_ids[0]
        valid = True
        for ix in range(len(bus_ids)):
            if valid == True and (temp_timestamp + bus_ixes[ix]) % bus_ids[ix] != 0:
                valid = False
        if valid == True:
            target_timestamp = temp_timestamp
    print(target_timestamp)
