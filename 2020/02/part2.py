with open("data.txt") as f:
    lines = f.read().split("\n")
    valid = 0
    for l in lines:
        i0, i1 = map(int, l.split()[0].split("-"))
        i0, i1 = i0-1, i1-1
        letter = l.split()[1][0]
        password = l.split()[2]
        if (password[i0] == letter and password[i1] != letter) or (password[i0] != letter and password[i1] == letter):
            valid += 1
    print(f"{valid} valid passwords")