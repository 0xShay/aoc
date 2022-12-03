with open("data.txt") as f:
    duplicates = []
    score = 0
    for line in f.read().split("\n"):
        line_duplicates = []
        fh, sh = line[0:len(line)//2], line[len(line)//2:]
        for char in fh:
            if char in sh and char not in line_duplicates:
                line_duplicates.append(char)
        duplicates += line_duplicates
    for char in duplicates:
        if (char.islower()):
            score += ord(char)-96
            print(char, ord(char)-96)
        else:
            score += ord(char)-38
            print(char, ord(char)-38)
    print(duplicates)
    print(score)