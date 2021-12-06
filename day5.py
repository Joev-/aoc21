f = open('./inputs/day5.txt')
data = f.readlines()

points = [[tuple([int(v) for v in l.split(',')]) for l in line.strip().split(' -> ')] for line in data]

the_grid_a_digital_frontier = {}
for start,end in points:
    x1, y1 = start
    x2, y2 = end

    # only horizontals or verticals (or all - pt2)
    if x1 == x2 or y1 == y2 or True:
        dx = x2 - x1
        dy = y2 - y1
        xdir = (dx > 0) - (dx < 0)
        ydir = (dy > 0) - (dy < 0)

        while x1 != x2 + xdir or y1 != y2 + ydir:
            k = (x1, y1)
            v = the_grid_a_digital_frontier.get(k, 0)
            the_grid_a_digital_frontier[k] = v + 1
            x1 += xdir
            y1 += ydir

print(sum(v > 1 for v in the_grid_a_digital_frontier.values()))


