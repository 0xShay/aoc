lines = open("realInput.txt", "r").read().split("\n")
routes = {}

for l in lines:

    src = l.split("-")[0]
    dst = l.split("-")[1]

    if dst != "start":
        if src in routes:
            routes[src].append(dst)
        else:
            routes[src] = [dst]    

    if src != "start":
        if dst in routes:
            routes[dst].append(src)
        else:
            routes[dst] = [src]

print(routes)
print()

lowercaseOnes = []

for d in routes:
    if d.islower() and d not in lowercaseOnes and d not in ["start", "end"]:
        lowercaseOnes.append(d)

def findAvailable(node, path, visited, dupeChar, duped, reses):

    if dupeChar == "":
        for l in lowercaseOnes:
            findAvailable(node, path, visited, l, False, reses)

    for dst in routes[node]:
        if dst not in visited:
            if dst.islower():
                if dst == "end":
                    print(path+["end"])
                    reses.add(str(path+["end"]))
                else:
                    if dst == dupeChar:
                        if duped == False:
                            findAvailable(dst, path+[dst], visited, dupeChar, True, reses)
                        else:
                            findAvailable(dst, path+[dst], visited+[dst], dupeChar, duped, reses)
                    else:
                        findAvailable(dst, path+[dst], visited+[dst], dupeChar, duped, reses)
            else:
                if dst == "end":
                    print(path+["end"])
                    reses.add(str(path+["end"]))
                else:
                    findAvailable(dst, path+[dst], visited, dupeChar, duped, reses)

reses = set()
findAvailable("start", ["start"], ["start"], "", False, reses)

print()
print(len(reses))