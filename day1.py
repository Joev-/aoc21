f = open('inputs/day1.txt')
data = [int(x) for x in f.readlines()]

# (171, 154), (154, 155), (155, 170) ...
p1: int = sum([x < y for x, y in zip(data, data[1:])])
print(f"Part 1: {p1}")
# a+b+c < b+c+d if a < d
# (171, 170), (154, 167), ...
p2: int = sum([x < y for x, y in zip(data, data[3:])])
print(f"Part 2: {p2}")
