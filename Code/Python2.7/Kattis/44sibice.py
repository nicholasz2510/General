from sys import stdin
from math import sqrt

n, w, h = [int(x) for x in stdin.readline().split()]
d = sqrt(w ** 2 + h ** 2)

for x in range(n):
    l = float(stdin.readline())
    if l <= d:
        print "DA"
    else:
        print "NE"
