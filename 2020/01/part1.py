with open("data.txt") as data:
    nums = [int(i) for i in data.read().split()]
    print(nums)
    for i0 in range(len(nums)):
        for i1 in range(i0, len(nums)):
            if nums[i0]+nums[i1] == 2020:
                print(f"{nums[i0]} + {nums[i1]} = 2020, {nums[i0]} * {nums[i1]} = {nums[i0] * nums[i1]}")