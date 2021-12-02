f = open('inputs/day2.txt')
data = f.readlines()

h = d = a = 0
for c in data:
    dir, value = c.split(' ')
    value = int(value)

    match dir:
        case 'forward':
            h += value
            d += a * value
        case 'down':
            a += value
        case 'up':
            a -= value
            
print(f"P1: {h*a}")
print(f"P2: {d*h}")