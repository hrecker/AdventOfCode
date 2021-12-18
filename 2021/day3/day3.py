def part1(lines):
    digitCount = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                digitCount[i] += 1
            else:
                digitCount[i] -= 1
    gammaString = ''
    for digit in digitCount:
        if digit > 0:
            gammaString += '1'
        else:
            gammaString += '0'
    gamma = int(gammaString, 2)
    epsilon = pow(2, len(gammaString)) - gamma - 1
    print(gamma * epsilon)

def getLeastMostCommon(lines):
    digitCount = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == '1':
                digitCount[i] += 1
            else:
                digitCount[i] -= 1
    #print(str(digitCount))
    mostCommon = ''
    leastCommon = ''
    for digit in digitCount:
        if digit >= 0:
            mostCommon += '1'
            leastCommon += '0'
        else:
            mostCommon += '0'
            leastCommon += '1'
    return (leastCommon, mostCommon)

def part2(lines):
    validOxygen = lines
    nextValidOxygen = []
    validCo2 = lines
    nextValidCo2 = []
    oxygenIndex = 0
    co2Index = 0
    while len(validOxygen) > 1:
        nextValidOxygen = []
        mostCommon = getLeastMostCommon(validOxygen)[1]
        for line in validOxygen:
            if line[oxygenIndex] == mostCommon[oxygenIndex]:
                nextValidOxygen.append(line)
        validOxygen = list(nextValidOxygen)
        oxygenIndex += 1
    while len(validCo2) > 1:
        nextValidCo2 = []
        mostCommon = getLeastMostCommon(validCo2)[0]
        for line in validCo2:
            if line[co2Index] == mostCommon[co2Index]:
                nextValidCo2.append(line)
        validCo2 = list(nextValidCo2)
        co2Index += 1
    
    oxygen = int(validOxygen[0], 2)
    co2 = int(validCo2[0], 2)
    print("Oxy: " + validOxygen[0])
    print("co2: " + validCo2[0])
    print(oxygen * co2)

with open("input.txt") as input:
    lines = [line.rstrip('\n') for line in input]
    #part1(lines)
    part2(lines)
