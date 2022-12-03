import re
with open("data.txt") as f:
    valid_passports = 0
    pp = {}
    for d in "|".join("|".join(f.read().split(" ")).split("\n")).split("|") + [""]:
        if d == "":
            if all(k in pp.keys() for k in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]):
                byr, iyr, eyr, hgt, hcl, ecl, pid = pp["byr"], pp["iyr"], pp["eyr"], pp["hgt"], pp["hcl"], pp["ecl"], pp["pid"]
                pp_valid = True
                if not (1920 <= int(byr) <= 2002):
                    pp_valid = False
                    print("invalid byr", pp)
                if not (2010 <= int(iyr) <= 2020):
                    pp_valid = False
                    print("invalid iyr", pp)
                if not (2020 <= int(eyr) <= 2030):
                    pp_valid = False
                    print("invalid eyr", pp)
                if not (hgt.endswith("cm") or hgt.endswith("in")):
                    pp_valid = False
                    print("invalid hgt", pp)
                else:
                    if hgt.endswith("cm"):
                        if not (150 <= int(hgt[:-2]) <= 193):
                            pp_valid = False
                            print("invalid hgt cm")
                    else:
                        if not (59 <= int(hgt[:-2]) <= 76):
                            pp_valid = False
                            print("invalid hgt in")
                if not re.fullmatch("\#[0-9a-zA-Z]{6}", hcl):
                    pp_valid = False
                    print("invalid hcl", pp)
                if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    pp_valid = False
                    print("invalid ecl", pp)
                if not re.fullmatch("[0-9]{9}", pid):
                    pp_valid = False
                    print("invalid pid", pp)
                if pp_valid:
                    valid_passports += 1
            pp = {}
        else:
            pp[d.split(":")[0]] = d.split(":")[1]
    print(valid_passports, "valid passports")