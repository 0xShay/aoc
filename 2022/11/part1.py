monkeys = {}

with open("data.txt") as f:
    lines = f.read().split("\n")
    curr_monkey = -1
    for i,l in enumerate(lines):
        if i%7 == 0:
            curr_monkey = int(l[6:-1])
            monkeys[curr_monkey] = {
                "inspect_count": 0
            }
        if i%7 == 1:
            monkeys[curr_monkey]["items"] = list(map(int, l[18:].split(", ")))
        if i%7 == 2:
            monkeys[curr_monkey]["operation"] = l[19:].replace("old", "worry_level")
        if i%7 == 3:
            monkeys[curr_monkey]["test_divisible_by"] = int(l[21:])
        if i%7 == 4:
            monkeys[curr_monkey]["if_true"] = int(l[29:])
        if i%7 == 5:
            monkeys[curr_monkey]["if_false"] = int(l[30:])

    for round_num in range(20):

        for i in monkeys.keys():
            while len(monkeys[i]["items"]) > 0:
                item = monkeys[i]["items"].pop(0)
                monkeys[i]["inspect_count"] += 1
                worry_level = int(item)
                worry_level = eval(monkeys[i]["operation"])
                worry_level = worry_level // 3
                if worry_level % monkeys[i]["test_divisible_by"] == 0:
                    monkeys[monkeys[i]["if_true"]]["items"].append(worry_level)
                else:
                    monkeys[monkeys[i]["if_false"]]["items"].append(worry_level)
        
    inspect_counts = []
    for i in monkeys.keys():
        inspect_counts.append(monkeys[i]["inspect_count"])
    
    first = max(inspect_counts)
    inspect_counts.remove(max(inspect_counts))
    second = max(inspect_counts)

    print(first * second)