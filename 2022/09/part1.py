head_pos = [0, 0]
tail_pos = [0, 0]
tail_covered = []

with open("data.txt") as f:

    for l in f.read().split("\n"):

        direction = l.split(" ")[0]
        weight = int(l.split(" ")[1])

        for i in range(weight):

            if direction == "L":
                head_pos[0] -= 1
            elif direction == "R":
                head_pos[0] += 1
            elif direction == "U":
                head_pos[1] -= 1
            elif direction == "D":
                head_pos[1] += 1

            if abs(head_pos[0]-tail_pos[0]) == 2:
                tail_pos[0] = (head_pos[0]+tail_pos[0]) // 2
                if (head_pos[1] != tail_pos[1]):
                    tail_pos[1] = head_pos[1]
            elif abs(head_pos[1]-tail_pos[1]) == 2:
                tail_pos[1] = (head_pos[1]+tail_pos[1]) // 2
                if (head_pos[0] != tail_pos[0]):
                    tail_pos[0] = head_pos[0]
            
            if [tail_pos[0], tail_pos[1]] not in tail_covered:
                tail_covered.append([tail_pos[0], tail_pos[1]])

    print(len(tail_covered))