inputFile = open("/Users/djohnson/git/advent-of-code-2022/input-01.txt", "r")
calories = []
for item in inputFile:
    try:
        calories.append(int(item))
    except ValueError:
        calories.append(-1)

# PART 1
calorieCounts = []
totalCalories = 0
for calorie in calories:
    if calorie == -1:
        calorieCounts.append(totalCalories)
        totalCalories = 0
    else:
        totalCalories += calorie
        
print("Largest calorie count:", max(calorieCounts))

# Part 2
topThree = 0
calorieCounts.sort(reverse = True)
for i in range(0,3):
    topThree += calorieCounts[i]
    
print("Top three elves have", topThree, "calories")