f = open('./inputs/day8.txt')
readings = [tuple(x.strip().split(' | ')) for x in f.readlines()]
r = sum(len(d) in [2,4,3,7] for _,o in readings for d in o.split(' '))
print(f"P1: {r}")

def decode(input):
    values = input.split(' ')
    # 1: 'cf', 2: 'acdeg', ..etc..
    patterns = {}
    
    # Known lengths
    uniques = {2: 1, 3: 7, 4: 4, 7: 8}
    for v in list(filter(lambda x: len(x) in uniques, values)):
        l = len(v)
        patterns[uniques[l]] = ''.join(sorted(v))

    # 6 length - 0, 6, 9
    for v in list(filter(lambda x: len(x) == 6, values)):
        vs = ''.join(sorted(v))
        # 0 and 9 patterns overlap with known pattern for 1, so must be 6
        if not set(patterns[1]) <= set(vs) and not 6 in patterns:
            patterns[6] = vs
            continue
        
        # 9 overlaps with known pattern for 4, so must be 0
        if not set(patterns[4]) <= set(vs) and not 0 in patterns:
            patterns[0] = vs
            continue
        
        # Remaining value is 9
        patterns[9] = vs

    # 5 length - 2, 3, 5
    for v in list(filter(lambda x: len(x) == 5, values)):
        vs = ''.join(sorted(v))
        # 3 overlaps with known pattern for 1
        if set(patterns[1]) <= set(vs) and not 3 in patterns:
            patterns[3] = vs
            continue

        # Pattern 4 - Pattern 1 leaves an overlap of pattern for number 5
        negated = set(patterns[4]) - set(patterns[1])
        if negated <= set(vs) and 5 not in patterns:
            patterns[5] = vs
            continue

        # Which means 2 is the remaining pattern
        patterns[2] = vs

    return patterns

sum = 0
for signals,segments in readings:
    decoder = decode(signals)
    reveresed = {v: k for k,v in decoder.items()}

    digits = []
    for ov in segments.split(' '):
        s = ''.join(sorted(ov))
        digit = reveresed.get(s)
        if digit is not None:
            digits.append(str(digit))
    
    print(f"{segments}: {''.join(digits)}")
    sum += int(''.join(digits))

print(f"P2: {sum}")
