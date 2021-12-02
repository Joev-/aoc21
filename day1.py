f = open('inputs/day1.txt')
data = [int(x) for x in f.readlines()]

# (171, 154), (154, 155), (155, 170) ...
p1: int = sum([1 for x, y in zip(data, data[1:]) if x < y])
print(f"Part 1: {p1}")
# a+b+c < b+c+d if a < d
# (171, 170), (154, 167), ...
p2: int = sum([1 for x, y in zip(data, data[3:]) if x < y])
print(f"Part 2: {p2}")
