from statistics import median
import statistics
import math

f = open('./inputs/day7.txt')
data = list(map(int, f.readline().split(',')))
m = int(statistics.median(data))
dh = [abs(x-m) for x in data]
r = sum(dh)
print(f"P1: {r}")

m2 = math.floor(sum(data) / len(data))
m3 = [abs(x-m2) for x in data]
dhp = [(((x*x) + x) / 2) for x in m3]
rp = sum(dhp)
print(f"P2: {rp}")