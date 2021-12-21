def part1(input):
    values = [int(i) for i in input.readline().split(',')]
    maxPos = max(values)
    cost = [0] * maxPos
    minCost = -1
    minCostIndex = -1
    for i in range(maxPos):
        for v in values:
            cost[i] += abs(v - i)
        if minCost == -1 or cost[i] < minCost:
            minCost = cost[i]
            minCostIndex = i
    print(minCostIndex)
    print(minCost)


def part2(input):
    values = [int(i) for i in input.readline().split(',')]
    maxPos = max(values)
    cost = [0] * maxPos
    minCost = -1
    minCostIndex = -1
    for i in range(maxPos):
        for v in values:
            dist = abs(v - i)
            cost[i] += dist * (dist + 1) / 2
        if minCost == -1 or cost[i] < minCost:
            minCost = cost[i]
            minCostIndex = i
    print(minCostIndex)
    print(minCost)

with open("input.txt") as input:
    #part1(input)
    part2(input)
