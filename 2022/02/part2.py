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
        move1, outcome = l.split(" ")
        move2 = None
        if outcome == "X":
            for o in LOSE:
                if o[0] == move1:
                    move2 = o[1]
            score += 0
        if outcome == "Y":
            move2 = ["X", "Y", "Z"][["A", "B", "C"].index(move1)]
            score += 3
        if outcome == "Z":
            for o in WIN:
                if o[0] == move1:
                    move2 = o[1]
            score += 6
        score += ["X", "Y", "Z"].index(move2) + 1
    print(score)