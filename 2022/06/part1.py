with open("data.txt") as f:
    
    signal = f.read()

    last_four = []
    signal_index = 0

    while len(last_four) != 4 or last_four.count(last_four[0]) * last_four.count(last_four[1]) * last_four.count(last_four[2]) * last_four.count(last_four[3]) != 1:
        last_four.append(signal[signal_index])
        if len(last_four) > 4:
            last_four.pop(0)
        print(last_four)
        signal_index += 1

    print(signal_index)