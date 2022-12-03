with open("data.txt") as f:
    lines = f.read().split("\n")
    valid = 0
    for l in lines:
        minimum, maximum = map(int, l.split()[0].split("-"))
        letter = l.split()[1][0]
        password = l.split()[2]
        if password.count(letter) >= minimum and password.count(letter) <= maximum:
            valid += 1
    print(f"{valid} valid passwords")