def part1(input):
    f = 0
    d = 0
    for line in input:
        val = int(line.split()[1])
        if line[0] == 'f':
            f += val
        elif line[0] == 'u':
            d -= val
        elif line[0] == 'd':
            d += val
    print(f * d)
        

def part2(input):
    f = 0
    d = 0
    a = 0
    for line in input:
        val = int(line.split()[1])
        if line[0] == 'f':
            f += val
            d += (a * val)
        elif line[0] == 'u':
            a -= val
        elif line[0] == 'd':
            a += val
    print(f * d)

with open("input.txt") as input:
    #part1(input)
    part2(input)
