def isValid(x, y, map):
    return x > -1 and y > -1 and y < len(map) and x < len(map[0])

def getSurrounding(x, y, map):
    points = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), 
        (x, y - 1), (x, y + 1), 
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
    return [point for point in points if isValid(point[0], point[1], map)]

def printMap(map):
    for row in map:
        print("".join([str(i) for i in row]))

def simulateStep(octopi):
    # Increase all energy levels by one
    nines = set()
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            octopi[y][x] += 1
            if octopi[y][x] > 9:
                nines.add((x, y))
    
    flashed = set()
    while len(nines) > 0:
        nextNines = set()
        flashed = flashed.union(nines)
        for nine in nines:
            for o in getSurrounding(nine[0], nine[1], octopi):
                octopi[o[1]][o[0]] += 1
                if o not in flashed and octopi[o[1]][o[0]] > 9:
                    nextNines.add(o)
        nines = nextNines

    for o in flashed:
        octopi[o[1]][o[0]] = 0

    return len(flashed)

def part1(input):
    octopi = []
    for line in input:
        row = []
        for c in line.strip():
            row.append(int(c))
        octopi.append(row)

    total = 0
    for i in range(100):
        total += simulateStep(octopi)
    print(total)
    
    

def part2(input):
    octopi = []
    for line in input:
        row = []
        for c in line.strip():
            row.append(int(c))
        octopi.append(row)
    count = len(octopi) * len(octopi[0])

    total = 0
    step = 1
    while True:
        if simulateStep(octopi) == count:
            print(step)
            exit()
        step += 1

with open("input.txt") as input:
    #part1(input)
    part2(input)
