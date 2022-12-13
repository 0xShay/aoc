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
    lists = [
        [[2]],
        [[6]]
    ]
    current_pair = []
    for l in (lines + [""]):
        if l != "":
            lists.append(eval(l))

    change_made = True

    while change_made:

        change_made = False

        for i in range(len(lists)-1):

            cmp = compare_lists(lists[i], lists[i+1])

            if cmp == False:
                lists[i], lists[i+1] = lists[i+1], lists[i]
                change_made = True

    print((lists.index([[6]])+1)*(lists.index([[2]])+1))