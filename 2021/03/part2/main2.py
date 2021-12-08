lines = (open("realInput.txt", "r")).read().split("\n")

print(lines)

def colSum(ls, col):
    cumulSum = 0
    for line in ls:
        if line[col] == "1":
            cumulSum += 1
        else:
            cumulSum -= 1
    return cumulSum

def elim(ls, val, col):
    ls_res = []
    for line in ls:
        if line[col] == str(val):
            ls_res.append(line)
    return ls_res

trueResO2 = lines
winnerO2 = ""

for colNum in range(len(lines[0])):
    if (colSum(trueResO2, colNum) >= 0):
        trueResO2 = elim(trueResO2, 1, colNum)
    else:
        trueResO2 = elim(trueResO2, 0, colNum)
    if len(trueResO2) == 1:
        winnerO2 = trueResO2[0]
    print(colSum(lines, colNum))
    print(trueResO2)

trueResCO2 = lines
winnerCO2 = ""

for colNum in range(len(lines[0])):
    if (colSum(trueResCO2, colNum) < 0):
        trueResCO2 = elim(trueResCO2, 1, colNum)
    else:
        trueResCO2 = elim(trueResCO2, 0, colNum)
    if len(trueResCO2) == 1:
        winnerCO2 = trueResCO2[0]

print(f"O2: {winnerO2} ({int(winnerO2, 2)})")
print(f"CO2: {winnerCO2} ({int(winnerCO2, 2)})")
print(f"{int(winnerO2, 2)} * {int(winnerCO2, 2)} = {int(winnerO2, 2) * int(winnerCO2, 2)}")
