lines = (open("realInput.txt", "r")).read().split("\n")

# for lineIndex, line in enumerate(lines):
    
#     for i in range(len(lines[0])):
#         if i not in colOcc:
#             colOcc[i] = 0
#         if line[i] == "1":
#             colOcc[i] += 1
#         else:
#             colOcc[i] -= 1

def colOcc(ls):
    occs = {}
    for line in ls:
        for i in range(len(ls[0])):
            if i not in occs:
                occs[i] = 0
            if line[i] == "1":
                occs[i] += 1
            else:
                occs[i] -= 1
    return occs

resultsO2 = {}

for col in colOcc(lines):

    resultsO2[col] = []

    if col == 0:
        if colOcc(lines)[col] >= 0:
            for l in lines:
                    if l[col] == "1":
                        resultsO2[col].append(l)
        else:
            for l in lines:
                if l[col] == "0":
                    resultsO2[col].append(l)
    else:
        if colOcc(resultsO2[col-1])[col] >= 0:
            for l in resultsO2[col-1]:
                    if l[col] == "1":
                        resultsO2[col].append(l)
        else:
            for l in resultsO2[col-1]:
                if l[col] == "0":
                    resultsO2[col].append(l)
            
resultsCO2 = {}

for col in colOcc(lines):

    resultsCO2[col] = []

    if col == 0:
        if colOcc(lines)[col] < 0:
            for l in lines:
                    if l[col] == "1":
                        resultsCO2[col].append(l)
        else:
            for l in lines:
                if l[col] == "0":
                    resultsCO2[col].append(l)
    else:
        if colOcc(resultsCO2[col-1])[col-1] < 0:
            for l in resultsCO2[col-1]:
                    if l[col] == "1":
                        resultsCO2[col].append(l)
        else:
            for l in resultsCO2[col-1]:
                if l[col] == "0":
                    resultsCO2[col].append(l)

O2result = ""

for res in resultsO2:
    if len(resultsO2[res]) == 1:
        O2result = resultsO2[res][0]

CO2result = ""

for res in resultsCO2:
    if len(resultsCO2[res]) == 1:
        CO2result = resultsCO2[res][0]

print(f"O2 rating: {resultsO2[len(resultsO2)-1]}")
print(f"CO2 rating: {resultsCO2[len(resultsCO2)-1]}")

print(f"O2 rating: {O2result} ({int(O2result, 2)})")
print(f"CO2 rating: {CO2result} ({int(CO2result, 2)})")
print()
print(f"{int(O2result, 2)} * {int(CO2result, 2)} = {int(O2result, 2) * int(CO2result, 2)}")