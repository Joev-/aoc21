from functools import reduce

f = open('./inputs/day9.txt')
data = [[int(x) for x in line.strip()] for line in f.readlines()]

def neighbours(x, y):
    n = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    return [(x, y) for (x, y) in n if 0 <= x < len(data) and 0 <= y < len(data[x])]

lows = []
for x in range(len(data)):
    for y in range (len(data[0])):
        if all(data[x][y] < data[xx][yy] for xx, yy in neighbours(x, y)):
            lows.append((x, y))

r = sum(data[x][y] + 1 for x, y in lows)
print(f"Part 1: {r}")

def basin_length(x, y):
    visited = set()
    current_basin = []
    unexplored = [(x, y)]

    while unexplored:
        cx, cy = unexplored.pop()

        if (cx, cy) in visited:
            continue
        
        visited.add((cx,cy))

        if data[cx][cy] != 9 and (cx, cy) not in current_basin:
            current_basin.append((cx, cy))
            for nx,ny in neighbours(cx, cy):
                unexplored.append((nx, ny))
        
    return len(current_basin)

basin_lengths = [basin_length(x, y) for x,y in lows]
highests = sorted(basin_lengths, reverse=True)

r2 = reduce(lambda x,y: x*y, highests[:3])

print(f"Part 2: {r2}")