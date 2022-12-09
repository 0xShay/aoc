knot_pos = [[0, 0] for x in range(10)]
tail_covered = []

# 2206 too low

with open("data.txt") as f:

    for l in f.read().split("\n"):

        direction = l.split(" ")[0]
        weight = int(l.split(" ")[1])

        for i in range(weight):

            if direction == "L":
                knot_pos[0][0] -= 1
            elif direction == "R":
                knot_pos[0][0] += 1
            elif direction == "U":
                knot_pos[0][1] -= 1
            elif direction == "D":
                knot_pos[0][1] += 1

            for k in range(1, 10):

                if abs(knot_pos[k-1][0]-knot_pos[k][0]) == 2 and abs(knot_pos[k-1][1]-knot_pos[k][1]) == 2:
                    knot_pos[k][0] = (knot_pos[k-1][0]+knot_pos[k][0]) // 2
                    knot_pos[k][1] = (knot_pos[k-1][1]+knot_pos[k][1]) // 2
                elif abs(knot_pos[k-1][0]-knot_pos[k][0]) == 2:
                    knot_pos[k][0] = (knot_pos[k-1][0]+knot_pos[k][0]) // 2
                    if (knot_pos[k-1][1] != knot_pos[k][1]):
                        knot_pos[k][1] = knot_pos[k-1][1]
                elif abs(knot_pos[k-1][1]-knot_pos[k][1]) == 2:
                    knot_pos[k][1] = (knot_pos[k-1][1]+knot_pos[k][1]) // 2
                    if (knot_pos[k-1][0] != knot_pos[k][0]):
                        knot_pos[k][0] = knot_pos[k-1][0]

                if [knot_pos[9][0], knot_pos[9][1]] not in tail_covered:
                    tail_covered.append([knot_pos[9][0], knot_pos[9][1]])

    print(len(tail_covered))