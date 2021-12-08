lines = (open("realInput.txt", "r")).read().split("\n")
colOcc = {}

for lineIndex, line in enumerate(lines):
    for i in range(len(lines[0])):
        if i not in colOcc:
            colOcc[i] = 0
        if line[i] == "1":
            colOcc[i] += 1
        else:
            colOcc[i] -= 1

gammaBinary = ""

for i in range(len(colOcc)):
    if colOcc[i] < 0:
        gammaBinary += "0"
    else:
        gammaBinary += "1"

print(f"Gamma binary: {gammaBinary} ({int(gammaBinary, 2)})")

epsilonBinary = ""

for char in gammaBinary:
    if char == "0":
        epsilonBinary += "1"
    else:
        epsilonBinary += "0"

print(f"Epilson binary: {epsilonBinary} ({int(epsilonBinary, 2)})")

print()
print(f"{int(gammaBinary, 2)} * {int(epsilonBinary, 2)} = {int(gammaBinary, 2) * int(epsilonBinary, 2)}")