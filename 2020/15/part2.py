# seemingly inefficient, took a few minutes to compute, but it works I guess...

with open("data.txt") as f:
    nums = list(map(int, f.read().split(",")))
    last_said = {
        n:[nums.index(n)] for n in nums
    }

    while len(nums) < 30000000:
        if nums[-1] in last_said.keys():
            nums.append(len(nums)-1-(last_said[nums[-1]][0]))
        else:
            nums.append(0)
        
        if nums[-1] in last_said.keys():
            last_said[nums[-1]].append(len(nums)-1)
            last_said[nums[-1]] = last_said[nums[-1]][-2:]
        else:
            last_said[nums[-1]] = [len(nums)-1]

    print(nums[-1])