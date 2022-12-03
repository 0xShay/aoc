with open("data.txt") as f:
    valid_passports = 0
    current_passport = {}
    for d in "|".join("|".join(f.read().split(" ")).split("\n")).split("|") + [""]:
        if d == "":
            if all(k in current_passport.keys() for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
                valid_passports += 1
            current_passport = {}
        else:
            current_passport[d.split(":")[0]] = d.split(":")[1]
    print(valid_passports, "valid passports")