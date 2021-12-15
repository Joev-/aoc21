from statistics import median

f = open('./inputs/day10.txt')
data = f.read().splitlines()

complete = []

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,

    # Part 2
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

pairs = {
    '{': '}',
    '[': ']',
    '(': ')',
    '<': '>'
}

score = 0
part2_scores = []

for line in data:
    mismatch = None
    open = []
    autocomplete_score = 0

    for c in line:
        if c in pairs.keys():
            open.append(c)
            continue
        else:
            o = open.pop()
            if pairs[o] != c:
                mismatch = c
                break
    if mismatch:
        score += scores[mismatch]
    else:
        # Line is incomplete
        while open:
            o = open.pop()
            autocomplete_score = autocomplete_score * 5 + scores[o]
        part2_scores.append(autocomplete_score)

print(f"Part 1: {score}")
print(f"Part 2: {median(part2_scores)}")
