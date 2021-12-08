daFile = (open("realInput.txt", "r")).read()

depth = 0
aim = 0
horiPos = 0

for instruction in daFile.split("\n"):
    direction = instruction.split(" ")[0]
    weight = int(instruction.split(" ")[1])
    
    if direction == "up":
        aim -= weight
        
    if direction == "down":
        aim += weight
        
    if direction == "forward":
        horiPos += weight
        depth += (aim * weight)

print(f"depth: {str(depth)}")
print(f"aim: {str(aim)}")
print(f"horiPos: {str(horiPos)}")
print()
print(f"{str(depth)} * {str(horiPos)} = {str(depth * horiPos)}")