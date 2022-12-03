with open("data.txt") as f:
    lines = f.read().split("\n")

    duplicates = []
    score = 0
    
    for line_number in range(len(lines)):
        tri_duplicates = []
        if line_number % 3 == 0:
            fl = lines[line_number]
            sl = lines[line_number+1]
            tl = lines[line_number+2]
            for char in fl:
                if char in sl and char in tl and char not in tri_duplicates:
                    tri_duplicates.append(char)
            duplicates += tri_duplicates  

    for char in duplicates:
        if (char.islower()):
            score += ord(char)-96
            print(char, ord(char)-96)
        else:
            score += ord(char)-38
            print(char, ord(char)-38)
    print(duplicates)
    print(score)