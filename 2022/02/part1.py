WIN = [
    ["C", "X"],
    ["A", "Y"],
    ["B", "Z"]
]
LOSE = [
    ["A", "Z"],
    ["B", "X"],
    ["C", "Y"]
]
with open("data.txt") as f:
    score = 0
    for l in f.read().split("\n"):
        move1, move2 = l.split(" ")
        if [move1, move2] in WIN:
            score += 6
        elif [move1, move2] in LOSE:
            score += 0
        else:
            score += 3
        score += ["X", "Y", "Z"].index(move2) + 1
    print(score)