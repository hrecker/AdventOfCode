def day1(input):
    count = 0
    last = -1
    for line in input:
        next = int(line)
        if last != -1 and next > last:
            count += 1
        last = next
    print(count)

def day2(input):
    count = 0
    d1 = -1
    d2 = -1
    d3 = -1
    lastSum = -1
    sum = -1
    iter = -1
    for line in input:
        iter += 1
        d1 = d2
        d2 = d3
        d3 = int(line)
        lastSum = sum
        sum = d1 + d2 + d3
        if iter > 2 and sum > lastSum:
            count += 1
    print(count)

with open("input.txt") as input:
    day2(input)