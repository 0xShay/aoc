lines = open("realInput.txt", "r").read().split("\n")
openBrks = ["(", "[", "{", "<"]
closeBrks = [")", "]", "}", ">"]
pairs = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
score = {
    "": 0,
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

def matchingBrk(br):
    for p in pairs:
        if p[0] == br:
            return p[1]
        elif p[1] == br:
            return p[0]
    return ""

def findFirstIllegal(st):
    stack = []
    for char in st:
        if char in closeBrks:
            lastBrk = stack.pop()
            if closeBrks.index(char) == closeBrks.index(matchingBrk(lastBrk)):
                # all is well
                pass
            else:
                return char
        else:
            stack.append(char)
    return ""

resultSum = 0

for l in lines:
    resultSum += score[findFirstIllegal(l)]

print(resultSum)