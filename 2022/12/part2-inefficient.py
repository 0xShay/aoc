# it works but it took about 20 minutes to compute 😂

grid = []

E = None
prev = {}
dist = {} # from S
visited = {}
found = False

res_distances = []

def find_next_to_visit():
    not_visited_keys = []
    not_visited_values = []
    for k in visited.keys():
        if not visited[k]:
            not_visited_keys.append(k)
            not_visited_values.append(dist[k])
    return not_visited_keys[not_visited_values.index(min(not_visited_values))]

def all_visited():
    all_v = True
    for v in visited.values():
        if v == False:
            all_v = False
    return all_v

with open("data.txt") as f:
    
    a_positions = []

    lines = f.read().split("\n")
    grid = [list(l) for l in lines]
    for row in range(len(grid)):
        if "E" in list(grid[row]):
            E = (row, grid[row].index("E"))
        grid[row] = list(grid[row])
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "S":
                grid[row][col] = "a"
            elif grid[row][col] == "E":
                grid[row][col] = "z"            
            if grid[row][col] == "a":
                a_positions.append((row, col))

    for S in a_positions:
        
        prev = {}
        dist = {} # from S
        visited = {}
        found = False

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                dist[(row, col)] = float("inf")
                prev[(row, col)] = None
                visited[(row, col)] = False

        dist[S] = 0
        prev[S] = None

        while not all_visited():

            c = find_next_to_visit()

            for v in [
                (c[0]-1, c[1]),
                (c[0], c[1]-1),
                (c[0], c[1]+1),
                (c[0]+1, c[1]),
            ]:
                if v[0] >= 0 and v[0] < len(grid) and v[1] >= 0 and v[1] < len(grid[0]) and not visited[v]:
                    if ord(grid[v[0]][v[1]]) <= ord(grid[c[0]][c[1]])+1:
                        if (dist[c]+1) < dist[v]:
                            dist[v] = dist[c] + 1
                            prev[v] = c
            
            visited[c] = True
        
        route = [E]
        invalid_route = False
        while route[-1] != S:
            if route[-1] == None:
                invalid_route = True
                break
            route.append(prev[route[-1]])

        print(len(route)-1, route)
        if not invalid_route:
            res_distances.append(len(route)-1)

    print(min(res_distances))