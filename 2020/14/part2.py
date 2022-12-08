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
            x_indexes = []

            for i in range(len(mask)):
                if mask[i] == "1":
                    location = set_bit(location, i, 1)
                if mask[i] == "X":
                    x_indexes.append(i)

            for v in range(2**len(x_indexes)):
                char_stack = f'{v:0{len(x_indexes)}b}'
                _location = location
                for i, x_i in enumerate(x_indexes):
                    _location = set_bit(_location, int(x_i), int(char_stack[i]))
                memory[_location] = value

    print(sum(memory.values()))