from collections import deque

chunkEndings = set([")", "}", "]", ">"])

chunkPairs = {
    ")": "(",
    "}": "{",
    "]": "[",
    ">": "<",
    "(": ")",
    "{": "}",
    "[": "]",
    "<": ">"
}

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

incompletePoints = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def part1(input):
    score = 0
    for line in input:
        stack = deque()
        for c in line.strip():
            if c in chunkEndings:
                last = stack.pop()
                if last != chunkPairs[c]:
                    print("Expected " + chunkPairs[last] + ", found " + c)
                    score += points[c]
                    break
            else:
                stack.append(c)
    print(score)

def part2(input):
    scores = []
    for line in input:
        stack = deque()
        incomplete = True
        for c in line.strip():
            if c in chunkEndings:
                last = stack.pop()
                if last != chunkPairs[c]:
                    incomplete = False
            else:
                stack.append(c)
        score = 0
        while incomplete and len(stack) > 0:
            # Incomplete line
            score *= 5
            expected = chunkPairs[stack.pop()]
            score += incompletePoints[expected]
        if score > 0:
            scores.append(score)
    
    scores.sort()
    print(scores[int(len(scores) / 2)])

with open("input.txt") as input:
    #part1(input)
    part2(input)
