file_system = {
    "": {
        "_size": 0
    }
}

dir_sizes = []

with open("data.txt") as f:

    current_dir = ""
    for line in f.read().split("\n"):
        if line.startswith("$"):
            if line.split(" ")[1] == "cd":
                location = line.split(" ")[2]
                if location == "..":
                    current_dir = "/".join(current_dir.split("/")[:-1])
                elif location == "/":
                    current_dir = ""
                else:
                    current_dir += "/" + location
        else:
            _fs = file_system
            _pl = current_dir.split("/")
            if "" not in _pl:
                _pl.insert(0, "")
            for ps in _pl:
                _fs = _fs[ps]
            if line.split(" ")[0] == "dir":
                dir_name = line.split(" ")[1]
                if dir_name not in _fs.keys():
                    _fs[dir_name] = {}
                _fs[dir_name] = { "_size": 0 }
            else:
                file_size = int(line.split(" ")[0])
                _fs["_size"] += file_size
    
    def check_size(directory):
        global dir_sizes
        size = 0
        size += directory["_size"]
        for sd in directory.keys():
            if sd != "_size":
                size += check_size(directory[sd])
        directory["_size"] = size
        dir_sizes.append(size)
        return size

    for d in file_system.values():
        global space_needed
        space_needed = 30000000 - (70000000 - check_size(d))

    result = 0
    i = 0

    while result == 0:
        if dir_sizes[i] > space_needed:
            result = dir_sizes[i]
        i += 1

    print(result)