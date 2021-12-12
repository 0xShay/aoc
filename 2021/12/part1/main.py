lines = open("testInput.txt", "r").read().split("\n")
routes = {}

for l in lines:
    if l.split("-")[0] in routes:
        routes[l.split("-")[0]].append(l.split("-")[1])
    else:
        routes[l.split("-")[0]] = [l.split("-")[1]]
        
    if l.split("-")[1] in routes:
        routes[l.split("-")[1]].append(l.split("-")[0])
    else:
        routes[l.split("-")[1]] = [l.split("-")[0]]
        
print(routes)
print()

routeCount = 0

paths = [
    # {
    #     stops: ["", ""],
    #     visited: ["", ""]
    # }
]

for destI, dest in enumerate(routes["start"]):
    paths.append({
        "stops": ["start", dest],
        "visited": ["start"]
    })
    if dest not in paths[destI]["visited"] and dest.islower():
        paths[destI]["visited"].append(dest)

for p in paths:
    print(p["stops"], p["visited"])
print()

for i in range(30):

    newPaths = []

    for p in paths:
        # get last stop
        lastStop = p["stops"][-1]
        for r in routes[lastStop]:
            if r not in p["visited"]:
                if r.islower():
                    newPaths.append({
                        "stops": p["stops"] + [r],
                        "visited": p["visited"] + [r]
                    })
                else:
                    newPaths.append({
                        "stops": p["stops"] + [r],
                        "visited": p["visited"]
                    })

    paths = newPaths

    for p in paths:
        if p["stops"][-1] == "end" and p["stops"].count("end") == 1:
            routeCount += 1
            print(p["stops"], p["visited"])
    print()

print(routeCount)