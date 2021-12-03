from functools import reduce 

f = open('inputs/day3.txt')
data = f.readlines()

s = [list(x) for x in data]

# Transpose to column major lists
# [111100000101, 001110100010] => [[1, 0], [1, 0], [1, 1], [1, 1],...]
m = list(map(list, zip(*s)))

r = list(map(lambda c: '1' if c.count('1') > c.count('0') else '0', m))

gamma = int(''.join(r), 2)
epsilon = gamma ^ 0xFFF
print(f"γ: {gamma} ε: {epsilon} P1: {epsilon * gamma}")

