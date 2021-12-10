lines = open("realInput.txt", "r").read().split("\n")
openBrks = ["(", "[", "{", "<"]
closeBrks = [")", "]", "}", ">"]
pairs = [("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")]
score = {
    "": 0,
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
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
            if closeBrks.index(char) != closeBrks.index(matchingBrk(lastBrk)):
                return char
        else:
            stack.append(char)
    return ""
    
def cancelOutClose(st):
    stack = []
    for char in st:
        if char in closeBrks:
            stack.pop()            
        else:
            stack.append(char)
    return "".join(stack)

def flip(st):
    returnString = ""
    for ch in st[::-1]:
        returnString += matchingBrk(ch)
    return returnString

lineScores = []

for l in lines:
    lScore = 0
    # resultSum += score[findFirstIllegal(l)]
    if findFirstIllegal(l) == "":
        for char in flip(cancelOutClose(l)):
            lScore *= 5
            lScore += score[char]
        lineScores.append(lScore)

lineScores.sort()
print(lineScores)
print(lineScores[len(lineScores) // 2])