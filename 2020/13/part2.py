with open("data.txt") as f:
    lines = f.read().split("\n")
    base_time = int(lines[0])
    bus_ids = []
    bus_ixes = []
    for i in range(len(lines[1].split(","))):
        if lines[1].split(",")[i] != "x":
            bus_ids.append(int(lines[1].split(",")[i]))
            bus_ixes.append(i)
    print(bus_ids, bus_ixes)
    b = []
    N = []
    x = []
    bNx = []
    for i in range(len(bus_ids)):
        b.append(bus_ids[i]-bus_ixes[i])
        _product = 1
        for i2 in range(len(bus_ids)):
            if i2 != i:
                _product *= bus_ids[i2]
        N.append(_product)
        
        _x = _product % bus_ids[i]
        if _x == 1:
            x.append(_x)
        else:
            next_try = 0
            found = False
            while not found:
                next_try += 1
                if (next_try*_x) % bus_ids[i] == 1:
                    found = True
            x.append(next_try)

        bNx.append(b[i] * N[i] * x[i])
    print(b)
    print(N)
    print(x)
    mod_prod = 1
    for n in bus_ids:
        mod_prod *= n
    print(sum(bNx) % mod_prod)