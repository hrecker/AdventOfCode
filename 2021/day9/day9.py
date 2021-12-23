def isValid(x, y, map):
    return x > -1 and y > -1 and y < len(map) and x < len(map[0])

def getAdjacent(x, y, map):
    points = [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)]
    return [point for point in points if isValid(point[0], point[1], map)]

def isLowpoint(x, y, map):
    for adj in getAdjacent(x, y, map):
        if map[adj[1]][adj[0]] <= map[y][x]:
            return False
    return True

def part1(input):
    map = []
    for line in input:
        row = [int(c) for c in line.strip()]
        map.append(row)
    
    lows = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if isLowpoint(x, y, map):
                lows.append(map[y][x])
    print(sum(lows) + len(lows))

def getBasinMembers(x, y, map):
    start = (x, y)
    bounds = [start]
    found = set()
    found.add(start)
    lastFoundSize = -1
    while lastFoundSize != len(found):
        lastFoundSize = len(found)
        newBounds = []
        for point in bounds:
            neighbors = getAdjacent(point[0], point[1], map)
            for n in neighbors:
                if n not in found and map[n[1]][n[0]] < 9:
                    newBounds.append(n)
                    found.add(n)
        bounds = newBounds
    return found

def part2(input):
    map = []
    for line in input:
        row = [int(c) for c in line.strip()]
        map.append(row)
    
    lows = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if isLowpoint(x, y, map):
                lows.append((x, y))
    print(str(lows))

    largest = [-1, -1, -1]
    for low in lows:
        basinSize = len(getBasinMembers(low[0], low[1], map))
        print(basinSize)
        if basinSize > largest[0]:
            if basinSize > largest[1]:
                if basinSize > largest[2]:
                    largest[0] = largest[1]
                    largest[1] = largest[2]
                    largest[2] = basinSize
                else:
                    largest[0] = largest[1]
                    largest[1] = basinSize
            else:
                largest[0] = basinSize
    
    result = 1
    for size in largest:
        result = result * size
    print(result)


with open("input.txt") as input:
    #part1(input)
    part2(input)
