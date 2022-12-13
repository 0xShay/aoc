def compare_lists(p1, p2):

    if type(p1) == int and type(p2) == int:
        if p1 < p2:
            return True
        elif p1 > p2:
            return False
        else:
            return None

    if type(p1) == list and type(p2) == int:
        return compare_lists(p1, [p2])

    if type(p1) == int and type(p2) == list:
        return compare_lists([p1], p2)
    
    if type(p1) == list and type(p2) == list:
        i = 0
        while True:
            if i == len(p1) == len(p2):
                return None # all same length
            elif i == len(p1):
                return True # p1 is shorter
            elif i == len(p2):
                return False # p2 is shorter
            ordered = compare_lists(p1[i], p2[i])
            if ordered != None:
                return ordered
            i += 1

with open("data.txt") as f:

    lines = f.read().split("\n")
    pairs = []
    current_pair = []
    for l in (lines + [""]):
        if l == "":
            pairs.append(current_pair)
            current_pair = []
        else:
            current_pair.append(eval(l))

    res = 0

    for i,p in enumerate(pairs):
        if compare_lists(p[0], p[1]):
            res += i+1
    
    print(res)