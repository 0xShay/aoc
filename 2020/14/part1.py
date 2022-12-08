memory = {}
mask = ""

def set_bit(val, index, to):
    _mask = 1 << index
    val &= ~_mask
    if to == 1:
        val |= _mask
    return val

with open("data.txt") as f:
    for l in f.read().split("\n"):
        if l.split(" ")[0] == "mask":
            mask = list(reversed(l.split(" ")[2]))
        elif l.startswith("mem"):
            location = int(l.split(" ")[0][4:-1])
            value = int(l.split(" ")[2])
            for i in range(len(mask)):
                if mask[i] != "X":
                    value = set_bit(value, i, int(mask[i]))
            memory[location] = value
    print(sum(memory.values()))