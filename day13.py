import functools

f = open("./inputs/day13.txt")
data = f.read().splitlines()
coordinates = {(int(x),int(y)) for x,y in [line.strip().split(',') for line in data if ',' in line]}
fold_ops = [(d, int(n)) for d,n in [line.split()[-1].split('=') for line in data if '=' in line]]

def fold(points, op):
    match op:
        case ('x', along):
            func = lambda p, a=along: (a - abs(a - p[0]), p[1])
        case ('y', along):
            func = lambda p, a=along: (p[0], a - abs(a - p[1]))
    return set(map(func, points))

r1 = fold(coordinates, fold_ops[0])
print(f"Part 1: {len(r1)}")

completed = functools.reduce(fold, fold_ops, coordinates)

w = max(x for x, _ in completed)
h = max(y for _, y in completed)

digits = [['  '] * (w + 1) for _ in range(h + 1)]

for x, y in completed:
    digits[y][x] = '##'

print("Part 2:")
print('\n'.join(''.join(r) for r in digits))
