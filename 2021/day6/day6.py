def simulateDay(state):
    newState = []
    newFish = 0
    for f in state:
        f -= 1
        if f < 0:
            newFish += 1
            f = 6
        newState.append(f)
    newState.extend([8] * newFish)
    return newState

memo = {}

def countDescendants(currentVal, currentDay, maxDays):
    first = currentDay + currentVal + 1
    if first > maxDays:
        return 0
    key = str(first)
    if key in memo:
        return memo[key]
    directDescendants = []
    current = first
    while current <= maxDays:
        directDescendants.append(current)
        current += 7
    #print(str(directDescendants))
    result = len(directDescendants)
    for desc in directDescendants:
        result += countDescendants(8, desc, maxDays)
    memo[key] = result
    return result

def part1(input):
    state = [int(i) for i in input.readline().split(',')]
    for i in range(80):
        state = simulateDay(state)
    #print(str(state))
    print(len(state))

def part2(input):
    state = [int(i) for i in input.readline().split(',')]
    totalFish = len(state)
    for starter in state:
        desc = countDescendants(starter, 0, 256)
        totalFish += desc
        #print("Total for " + str(starter) + ": " + str(desc))
    print(totalFish)
    #print(str(countDescendants(2, 0, 3)))

with open("input.txt") as input:
    #part1(input)
    part2(input)
