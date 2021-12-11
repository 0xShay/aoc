lines = open("realInput.txt", "r").read().split("\n")
nums = []

for l in lines:
    nums.append(list(map(int, l)))

def printNums(ns):
    for l in ns:
        print(l)
    print()

def getAsides(ns, y, x):
    asides = []
    asides.append([y-1, x-1])
    asides.append([y, x-1])
    asides.append([y+1, x-1])
    asides.append([y-1, x])
    asides.append([y, x])
    asides.append([y+1, x])
    asides.append([y-1, x+1])
    asides.append([y, x+1])
    asides.append([y+1, x+1])
    newAsides = []
    for a in asides:
        if a[0] < len(ns) and a[0] >= 0 and a[1] < len(ns[0]) and a[1] >= 0:
            newAsides.append(a)
    return newAsides

octopusCount = len(nums) * len(nums[0])
totalFlashCount = 0
result = 0
i = 0

while result == 0:

    i += 1

    printNums(nums)

    flashCount = 0
    alreadyFlashed = []

    for i2 in range(50):

        for y, row in enumerate(nums):
            for x in range(len(nums[0])):
                if nums[y][x] >= 9 and [y, x] not in alreadyFlashed:
                    alreadyFlashed.append([y, x])
                    flashCount += 1
                    for cod in getAsides(nums, y, x):
                        nums[cod[0]][cod[1]] += 1
    
    for y, row in enumerate(nums):
        for x in range(len(nums[0])):
            if nums[y][x] >= 9 and [y, x] not in alreadyFlashed:
                alreadyFlashed.append([y, x])
                flashCount += 1
            else:
                nums[y][x] += 1

    for fd in alreadyFlashed:
        nums[fd[0]][fd[1]] = 0

    # print(flashCount)
    if flashCount == octopusCount:
        result = i
    totalFlashCount += flashCount

print("result")
print(result)

# set all alreadyFlashed to 0

# printNums(nums)