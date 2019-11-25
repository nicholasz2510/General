import sys
import math

cals_per_day = []

for i in range(int(sys.stdin.readline())):
    cals_per_day.append(int(sys.stdin.readline()))

for d in cals_per_day:
    print int(math.ceil(d / 400.0))
