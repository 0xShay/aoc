lines = open("realInput.txt", "r").read().split("\n")
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

lowercaseOnes = []

for d in routes:
    if d.islower() and d not in lowercaseOnes and d not in ["start", "end"]:
        lowercaseOnes.append(d)

routeCount = 0

paths = [
    # {
    #     stops: ["", ""],
    #     visited: ["", ""]
    # }
]

# for destI, dest in enumerate(routes["start"]):
#     for lc in lowercaseOnes:
#         paths.append({
#             "stops": ["start", dest],
#             "visited": ["start"],
#             "visitTwiceChar": lc,
#             "visitedTwice": False
#         })
#         if paths[destI]["visitTwiceChar"] == dest:
#             if paths[destI]["visitedTwice"] == True:
#                 paths[destI]["visited"].append(dest)
#             else:
#                 paths[destI]["visitedTwice"] = True
#         else:
#             if dest not in paths[destI]["visited"] and dest.islower():
#                 paths[destI]["visited"].append(dest)
                
for lc in lowercaseOnes:
    paths.append({
        "stops": ["start"],
        "visited": ["start"],
        "visitTwiceChar": lc,
        "visitedTwice": False
    })

# for p in paths:
#     print(p["stops"], p["visited"])
# print()

for i in range(20):

    newPaths = []

    for p in paths:
        # get last stop
        lastStop = p["stops"][-1]
        # if len(p["stops"]) == 3 and [p["stops"][1], p["stops"][2]] == ["A", "c"]:
            # print(p)
            # print(routes[lastStop])
        for r in routes[lastStop]:
            if r not in p["visited"]:
                if r == p["visitTwiceChar"]:
                    if p["visitedTwice"] == False:
                        newPaths.append({
                            "stops": p["stops"] + [r],
                            "visited": p["visited"],
                            "visitTwiceChar": p["visitTwiceChar"],
                            "visitedTwice": True
                        })
                    else:
                        newPaths.append({
                            "stops": p["stops"] + [r],
                            "visited": p["visited"] + [r],
                            "visitTwiceChar": p["visitTwiceChar"],
                            "visitedTwice": True
                        })
                else:
                    if r.islower():
                        newPaths.append({
                            "stops": p["stops"] + [r],
                            "visited": p["visited"] + [r],
                            "visitTwiceChar": p["visitTwiceChar"],
                            "visitedTwice": p["visitedTwice"]
                        })
                    else:
                        newPaths.append({
                            "stops": p["stops"] + [r],
                            "visited": p["visited"],
                            "visitTwiceChar": p["visitTwiceChar"],
                            "visitedTwice": p["visitedTwice"]
                        })

    paths = list(newPaths)
    newPaths = []

    counted = []
    for p in paths:
        if p["stops"].count(p["visitTwiceChar"]) <= 2 and p["stops"] not in counted and p["stops"][-1] == "end" and p["stops"].count("end") == 1:
            routeCount += 1
            counted.append(p["stops"])
            # print(p["stops"], p["visited"])
        elif p["stops"].count(p["visitTwiceChar"]) <= 2:
            newPaths.append(p)
    print(f"{i} / 20")
    print(routeCount)
    print()

print(routeCount)