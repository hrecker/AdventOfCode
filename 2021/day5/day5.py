def part1(input):
    map = []
    for line in input:
        pieces = line.strip().split('-')
        coord1Str = pieces[0][:len(pieces[0]) - 1].split(',')
        coord2Str = pieces[1][2:].split(',')
        #print(coord1Str)
        #print(coord2Str)
        coord1 = (int(coord1Str[0]), int(coord1Str[1]))
        coord2 = (int(coord2Str[0]), int(coord2Str[1]))
        maxCoord = max([coord1[0], coord1[1], coord2[0], coord2[1]]) + 1
        mapLen = len(map)
        if maxCoord > mapLen:
            for row in map:
                row.extend([0] * (maxCoord - mapLen))
            for _ in range(mapLen, maxCoord):
                map.append([0] * maxCoord)

        # Horizontal
        if coord1[0] != coord2[0] and coord1[1] == coord2[1]:
            #print("horiz")
            minX = min(coord1[0], coord2[0])
            maxX = max(coord1[0], coord2[0])
            y = coord1[1]
            for x in range(minX, maxX + 1):
                map[y][x] += 1
        # Vertical
        elif coord1[0] == coord2[0] and coord1[1] != coord2[1]:
            #print("vert")
            minY = min(coord1[1], coord2[1])
            maxY = max(coord1[1], coord2[1])
            x = coord1[0]
            for y in range(minY, maxY + 1):
                map[y][x] += 1

    count = 0
    for row in map:
        print(str(row))
        for val in row:
            if val > 1:
                count += 1
    print(count)

def part2(input):
    map = []
    for line in input:
        pieces = line.strip().split('-')
        coord1Str = pieces[0][:len(pieces[0]) - 1].split(',')
        coord2Str = pieces[1][2:].split(',')
        #print(coord1Str)
        #print(coord2Str)
        coord1 = (int(coord1Str[0]), int(coord1Str[1]))
        coord2 = (int(coord2Str[0]), int(coord2Str[1]))
        maxCoord = max([coord1[0], coord1[1], coord2[0], coord2[1]]) + 1
        mapLen = len(map)
        if maxCoord > mapLen:
            for row in map:
                row.extend([0] * (maxCoord - mapLen))
            for _ in range(mapLen, maxCoord):
                map.append([0] * maxCoord)

        minX = min(coord1[0], coord2[0])
        maxX = max(coord1[0], coord2[0])
        minY = min(coord1[1], coord2[1])
        maxY = max(coord1[1], coord2[1])
        # Horizontal
        if coord1[0] != coord2[0] and coord1[1] == coord2[1]:
            #print("horiz")
            y = coord1[1]
            for x in range(minX, maxX + 1):
                map[y][x] += 1
        # Vertical
        elif coord1[0] == coord2[0] and coord1[1] != coord2[1]:
            #print("vert")
            x = coord1[0]
            for y in range(minY, maxY + 1):
                map[y][x] += 1
        # Diagonal
        else:
            #print("diag: " + str)
            startY = coord1[1]
            endY = coord2[1]
            if minX != coord1[0]:
                startY = coord2[1]
                endY = coord1[1]
            #print("Starty: " + str(startY))
            increment = 1 if endY > startY else -1
            #print("Inc: " + str(increment))
            diff = 0
            for x in range(minX, maxX + 1):
                map[startY + diff][x] += 1
                diff += increment

    count = 0
    for row in map:
        #print(str(row))
        for val in row:
            if val > 1:
                count += 1
    print(count)

with open("input.txt") as input:
    #part1(input)
    part2(input)
