inputFile = open("/Users/djohnson/git/advent-of-code-2022/input-04.txt", "r")
partners = []
for item in inputFile:
    partners.append(item)

# Part 1
containedCount = 0
for pairs in partners:
    individuals = pairs.split(',')
    elf1 = individuals[0].split('-')
    elf2 = individuals[1].split('-')
    if (int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1])) or (int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1])):
        containedCount += 1

print("Part 1 completely contained pairs:", containedCount)

# Part 2
overlapCount = 0
for pairs in partners:
    individuals = pairs.split(',')
    elf1 = individuals[0].split('-')
    elf2 = individuals[1].split('-')
    if ((int(elf2[0]) <= int(elf1[0]) <= int(elf2[1])) or (int(elf2[0]) <= int(elf1[1]) <= int(elf2[1]))) or ((int(elf1[0]) <= int(elf2[0]) <= int(elf1[1])) or (int(elf1[0]) <= int(elf2[1]) <= int(elf1[1]))):
        overlapCount += 1

print("Part 2 overlapping pairs:", overlapCount)    