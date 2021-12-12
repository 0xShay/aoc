lines = open("testInput.txt", "r").read().split("\n")
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

def findAvailable(node, path, visited):

    for dst in routes[node]:

        if dst not in visited:

            if dst.islower():
                if dst == "end":
                    print(path+["end"])
                else:
                    findAvailable(dst, path+[dst], visited+[dst])
            else:
                if dst == "end":
                    print(path+["end"])
                else:
                    findAvailable(dst, path+[dst], visited)

findAvailable("start", ["start"], ["start"])