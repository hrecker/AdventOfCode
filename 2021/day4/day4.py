def allIncluded(fullList, toInclude):
    return all(elem1 in fullList for elem1 in toInclude)

def checkWin(board, drawn):
    #print(str(board))
    for row in board:
        if allIncluded(drawn, row):
            #print("Row win found")
            #print(str(row))
            #print(str(drawn))
            return True
    for i in range(5):
        col = [row[i] for row in board]
        if allIncluded(drawn, col):
            return True
    return False

def getScore(board, drawn):
    sum = 0
    for row in board:
        for val in row:
            if val not in drawn:
                sum += int(val)
    return sum * int(drawn[len(drawn) - 1])

def part1(input):
    fullDrawn = input.readline().split(',')
    boards = []
    currentBoard = []
    for line in input:
        if line.strip():
            currentBoard.append(line.strip().split())
        elif currentBoard:
            boards.append(currentBoard)
            currentBoard = []
    boards.append(currentBoard)
    
    drawnBeforeWin = []
    minDrawn = len(fullDrawn)
    winningBoard = []
    for board in boards:
        winFound = False
        for i in range(len(fullDrawn)):
            if checkWin(board, fullDrawn[0:i + 1]):
                drawnBeforeWin.append(i + 1)
                winFound = True
                if (i + 1) < minDrawn:
                    minDrawn = i + 1
                    winningBoard = board
                #print("Win found")
                break
        if not winFound:
            drawnBeforeWin.append(-1)
    lastCalled = fullDrawn[minDrawn - 1]
    print("Last called: " + str(lastCalled))
    print("Score: " + str(getScore(winningBoard, fullDrawn[0:minDrawn])))
    


def part2(input):
    fullDrawn = input.readline().split(',')
    boards = []
    currentBoard = []
    for line in input:
        if line.strip():
            currentBoard.append(line.strip().split())
        elif currentBoard:
            boards.append(currentBoard)
            currentBoard = []
    boards.append(currentBoard)
    
    drawnBeforeWin = []
    maxDrawn = -1
    worstBoard = []
    for board in boards:
        winFound = False
        for i in range(len(fullDrawn)):
            if checkWin(board, fullDrawn[0:i + 1]):
                drawnBeforeWin.append(i + 1)
                winFound = True
                if (i + 1) > maxDrawn:
                    maxDrawn = i + 1
                    worstBoard = board
                #print("Win found")
                break
        if not winFound:
            drawnBeforeWin.append(-1)
    lastCalled = fullDrawn[maxDrawn - 1]
    print("Last called: " + str(lastCalled))
    print("Score: " + str(getScore(worstBoard, fullDrawn[0:maxDrawn])))

with open("input.txt") as input:
    #part1(input)
    part2(input)
