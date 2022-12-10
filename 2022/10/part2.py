drawing = []

def draw(ci, X):

    if ci % 40 == 0:
        drawing.append([])

    if ci%40 in [X-1, X, X+1]:
        drawing[ci // 40].append("#")
    else:
        drawing[ci // 40].append(".")

with open("data.txt") as f:

    next_cycle_job = 0
    current_cycle_index = 0
    X = 1

    for i, l in enumerate(f.read().split("\n")):
        X += next_cycle_job
        add_cycle_x = False
        if l.split(" ")[0] == "addx":
            next_cycle_job = int(l.split(" ")[1])
            draw(current_cycle_index, X)
            current_cycle_index += 1
            draw(current_cycle_index, X)
            current_cycle_index += 1

        else:
            next_cycle_job = 0
            draw(current_cycle_index, X)
            current_cycle_index += 1

        # print(current_cycle_index, "".join(drawing[current_cycle_index//40]))

# print(drawing)

    #  cycles

for row in drawing:
    print("".join(row))