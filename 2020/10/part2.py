prev = {}
res = 0
paths_from = {}

def check_paths_from(n):
    global prev
    global res
    for p in prev[n]:
        if p in paths_from.keys():
            res += paths_from[p]
        else:
            check_paths_from(p)

        if p == 0:
            res += 1
    paths_from[n] = res
    return res

with open("data.txt") as f:

    adapter_ratings = list(map(int, f.read().split("\n"))) + [0]
    target = max(adapter_ratings) + 3

    prev[0] = []

    for ar in sorted(adapter_ratings, reverse=True):
        prev[ar] = []
        for i in range(1, 4):
            if ar-i in adapter_ratings:
                prev[ar].append(ar-i)

    print(check_paths_from(max(adapter_ratings)))

    # print(res)