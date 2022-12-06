with open("data.txt") as f:
    
    signal = f.read()

    last_fourteen = []
    signal_index = 0
    found = False

    while not found:

        last_fourteen.append(signal[signal_index])

        if len(last_fourteen) > 14:
            last_fourteen.pop(0)

            found = True
            for i in range(14):
                for j in range(14):
                    if i != j and last_fourteen[i] == last_fourteen[j]:
                        found = False

        print(last_fourteen)
        signal_index += 1

    print(signal_index)