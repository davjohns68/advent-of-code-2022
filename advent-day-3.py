inputFile = open("/Users/djohnson/git/advent-of-code-2022/input-03.txt", "r")
rucksacks = []
matched = []
for item in inputFile:
    rucksacks.append(item)

# Part 1
for pair in rucksacks:
    found = False
    pair = pair.strip()
    rs1 = pair[:len(pair) // 2]
    rs2 = pair[len(pair) // 2:]
    for item in rs1:
        if rs2.find(item) >= 0:
            matched.append(item)
            break
prioritySum = 0
for item in matched:
    if item.isupper():
        prioritySum += ord(item) - 38
    else:
        prioritySum += ord(item) - 96
        
print("Part 1 priority sum:", prioritySum)

# Part 2
matched = []
for i in range(0,len(rucksacks), 3):
    rs1 = rucksacks[i]
    rs2 = rucksacks[i + 1]
    rs3 = rucksacks[i + 2]
    for item in rs1:
        if rs2.find(item) >= 0 and rs3.find(item) >= 0:
            matched.append(item)
            break
        
prioritySum = 0
for item in matched:
    if item.isupper():
        prioritySum += ord(item) - 38
    else:
        prioritySum += ord(item) - 96

print("Part 2 priority sum:", prioritySum)