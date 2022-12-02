inputFile = open("/Users/djohnson/git/advent-of-code-2022/input-02.txt", "r")
moves = []
for item in inputFile:
    moves.append(item)

myMoves = []
elfMoves = []    
for move in moves:
    temp = move.split()
    elfMoves.append(temp[0])
    myMoves.append(temp[1])

# Part 1    
totalScore = 0
for i in range(0,len(elfMoves)):
    if myMoves[i] == "X": #Rock
        totalScore += 1
        if elfMoves[i] == "A": #Rock represents a tie
            totalScore += 3
        elif elfMoves[i] == "C": #Scissors represents a win
            totalScore += 6
        #Else it's paper and a loss, which is 0 points
    elif myMoves[i] == "Y": #Paper
        totalScore += 2
        if elfMoves[i] == "A": #Rock represents a win
            totalScore += 6
        elif elfMoves[i] == "B": #Paper represents a tie
            totalScore += 3
        #Else it's scissors and a loss, which is 0 points
    else: #Scissors
        totalScore += 3
        if elfMoves[i] == "B": #Paper represents a win
            totalScore += 6
        elif elfMoves[i] == "C": #Scissors represents a tie
            totalScore += 3
        #Else it's rock and a loss, which is 0 points

print("Total score:", totalScore)

# Part 2
totalScore = 0
for i in range(0,len(elfMoves)):
    if myMoves[i] == "X": #Loss
        totalScore += 0
        if elfMoves[i] == "A": #Rock
            totalScore += 3
        elif elfMoves[i] == "B": #Paper
            totalScore += 1
        elif elfMoves[i] == "C": #Scissors
            totalScore += 2
    elif myMoves[i] == "Y": #Tie
        totalScore += 3
        if elfMoves[i] == "A": #Rock
            totalScore += 1
        elif elfMoves[i] == "B": #Paper
            totalScore += 2
        elif elfMoves[i] == "C": #Scissors
            totalScore += 3
    else: #Win
        totalScore += 6
        if elfMoves[i] == "A": #Rock
            totalScore += 2
        elif elfMoves[i] == "B": #Paper
            totalScore += 3
        elif elfMoves[i] == "C": #Scissors
            totalScore += 1

print("Total score:", totalScore)