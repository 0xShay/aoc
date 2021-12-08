lines = open("realInput.txt", "r").read().split("\n")

def sort_string(st):
    sorted_str = sorted(st)
    return "".join(sorted_str)

resultSum = 0

for line in lines:
    nums = ["","","","","","","","","",""]
    patterns = line.split(" | ")[0].split(" ")
    outputs = line.split(" | ")[1].split(" ")

    or235 = []
    or069 = []
    midRow = ""

    for p in patterns:
        if len(p) == 2:
            nums[1] = p
        if len(p) == 3:
            nums[7] = p
        if len(p) == 4:
            nums[4] = p
        if len(p) == 5:
            # 2 or 3 or 5
            or235.append(p)
        if len(p) == 6:
            # 0 or 6 or 9
            or069.append(p)
        if len(p) == 7:
            nums[8] = p

    if len(or235) == 3:
        # find common letter, that's the middle row
        midRow = "".join(set("".join(set(or235[0]).intersection(or235[1]))).intersection(or235[2]))

    if len(or069) == 3 and len(midRow) == 3:
        for nam in or069:
            cnt = 0
            for ltr in midRow:
                if ltr in nam:
                    cnt += 1
            if cnt == 2:
                nums[0] = nam

    for nam in or235:
        cnt = 0
        for ltr in nums[4]:
            if ltr in nam:
                    cnt += 1
        if cnt == 2:
            nums[2] = nam

    or35 = []
    for nam in or235:
        if nam != nums[2]:
            or35.append(nam)

    dupeLetters35 = []
    for l in or35[0]:
        if l not in dupeLetters35:
            dupeLetters35.append(l)
    for l in or35[1]:
        if l not in dupeLetters35:
            dupeLetters35.append(l)

    for ltr in nums[8]:
        if (ltr not in dupeLetters35):
            string6 = ""
            for l in nums[8]:
                if l != ltr:
                    string6 += l
            nums[9] = string6
        if (ltr in nums[1]) and (ltr in nums[2]):
            string6 = ""
            for l in nums[8]:
                if l != ltr:
                    string6 += l
            nums[6] = string6
        
    ct6 = 0
    for ltr in nums[6]:
        if ltr in or35[0]:
            ct6 += 1
    if ct6 == 5:
        nums[3] = or35[1]
        nums[5] = or35[0]
    if ct6 == 4:
        nums[3] = or35[0]
        nums[5] = or35[1]

    nums = list(map(sort_string, nums))
    print(nums)
    print(list(map(sort_string, outputs)))

    resultOne = ""

    for o in list(map(sort_string, outputs)):
        resultOne += str(nums.index(sort_string(o)))

    print(resultOne)
    print("----------------")
    resultSum += int(resultOne)

print(resultSum)

# if seg not in 3 and 5, it's the missing one in 9 /
# if seg in 1 and 2, it's the missing one in 6 /
# 5 shares 5 with 6, 3 shares 4 with 6 /