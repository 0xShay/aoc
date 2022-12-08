with open("data.txt") as f:
    lines = f.read().split("\n")
    base_time = int(lines[0])
    bus_ids = []
    for i in lines[1].split(","):
        if i != "x":
            bus_ids.append(int(i))
    departure_times = { b: [0] for b in bus_ids }
    bus_time_diff = {}
    for b in bus_ids:
        while departure_times[b][-1] < base_time:
            departure_times[b].append(departure_times[b][-1]+b)
        bus_time_diff[b] = max(departure_times[b])-base_time
    print(min(bus_time_diff, key=bus_time_diff.get) * min(bus_time_diff.values()))