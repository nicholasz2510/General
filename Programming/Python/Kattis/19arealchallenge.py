import sys
import math

area = int(sys.stdin.readline())
one_side = math.sqrt(area)

if int(one_side) == one_side:
    one_side = int(one_side)

print one_side * 4
