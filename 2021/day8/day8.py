#  0:      1:      2:      3:      4:
# aaaa    ....    aaaa    aaaa    ....
#b    c  .    c  .    c  .    c  b    c
#b    c  .    c  .    c  .    c  b    c
# ....    ....    dddd    dddd    dddd
#e    f  .    f  e    .  .    f  .    f
#e    f  .    f  e    .  .    f  .    f
# gggg    ....    gggg    gggg    ....
#
#  5:      6:      7:      8:      9:
# aaaa    aaaa    aaaa    aaaa    aaaa
#b    .  b    .  .    c  b    c  b    c
#b    .  b    .  .    c  b    c  b    c
# dddd    dddd    ....    dddd    dddd
#.    f  e    f  .    f  e    f  .    f
#.    f  e    f  .    f  e    f  .    f
# gggg    gggg    ....    gggg    gggg
def part1(input):
    count = 0
    for line in input:
        pieces = line.split('|')
        patterns = pieces[0].strip().split()
        digits = pieces[1].strip().split()
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                count += 1
    print(count)

def isSolved(possiblities):
    for _, segments in possiblities.items():
        if len(segments) > 1:
            return False
    return True

def part2(input):
    sum = 0
    allSegments = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
    # Actual display values for digits 0-9
    displayValues = [
        {'a', 'b', 'c', 'e', 'f', 'g'},
        {'c', 'f'}, 
        {'a', 'c', 'd', 'e', 'g'}, 
        {'a', 'c', 'd', 'f', 'g'},
        {'b', 'c', 'd', 'f'},
        {'a', 'b', 'd', 'f', 'g'},
        {'a', 'b', 'd', 'e', 'f', 'g'},
        {'a', 'c', 'f'},
        {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        {'a', 'b', 'c', 'd', 'f', 'g'}]
    for line in input:
        possibilities = { 
            'a': set(allSegments), 
            'b': set(allSegments), 
            'c': set(allSegments), 
            'd': set(allSegments), 
            'e': set(allSegments), 
            'f': set(allSegments), 
            'g': set(allSegments) }
        pieces = line.split('|')
        patterns = set(pieces[0].strip().split())
        digits = pieces[1].strip().split()
        for i in range(2):
            for pattern in patterns:
                # 1
                if len(pattern) == 2:
                    for digit in pattern:
                        possibilities[digit] = possibilities[digit].intersection(displayValues[1])
                # 7
                elif len(pattern) == 3:
                    for digit in pattern:
                        possibilities[digit] = possibilities[digit].intersection(displayValues[7])
                    # If a 1 has been found already
                # 4
                elif len(pattern) == 4:
                    for digit in pattern:
                        possibilities[digit] = possibilities[digit].intersection(displayValues[4])
                # 2, 3, 5
                elif len(pattern) == 5:
                    # The missing values for 2, 3, 5 must be in 'b', 'c', 'e', 'f'
                    others = displayValues[8].difference(pattern)
                    for digit in others:
                        possibilities[digit] = possibilities[digit].intersection({'b', 'c', 'e', 'f'})
                # 0, 6, 9
                elif len(pattern) == 6:
                    # The missing value for 0, 6, 9 must be one of 'c', 'd', 'e'
                    others = displayValues[8].difference(pattern)
                    for digit in others:
                        possibilities[digit] = possibilities[digit].intersection({'c', 'd', 'e'})
        # Do 5 iterations, I guess?
        for i in range(5):
            for origKey, val in possibilities.items():
                if len(val) == 1:
                    #if i > 0:
                    #    print("before removing " + origKey + ", " + str(val))
                    #    print(str(possibilities))
                    for key, _ in possibilities.items():
                        if origKey != key:
                            possibilities[key].difference_update(val)
                    #if i > 0:
                    #    print("after removing " + origKey + ", " + str(val))
                    #    print(str(possibilities))
        if not isSolved(possibilities):
            print("Error: line is not solved")
            print(line)
            print(str(possibilities))
            exit()
        #print(str(possibilities))
        finalValue = ''
        for digit in digits:
            actualDigit = []
            for segment in digit:
                actualDigit.append(list(possibilities[segment])[0])
            #print(digit + str(actualDigit))
            for i in range(len(displayValues)):
                if set(actualDigit) == displayValues[i]:
                    finalValue += str(i)
                    break
        sum += int(finalValue)
    print(sum)

with open("input.txt") as input:
    #part1(input)
    part2(input)
