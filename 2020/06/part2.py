with open("data.txt") as f:

    lines = f.read().split("\n") + [""]

    result = 0

    line_no = 0

    groups = []
    current_group = []
    while line_no < len(lines):

        # print(lines[line_no])
        
        if lines[line_no] == "":
            groups.append(current_group)
            chars_in_all = []
            for c in current_group[0]:
                char_in_all = True
                for l in current_group:
                    if c not in l:
                        char_in_all = False
                if char_in_all:
                    chars_in_all.append(c)
            result += len(chars_in_all)
            current_group = []
        else:
            current_group += lines[line_no].split()
        
        line_no += 1
        
    print(result)