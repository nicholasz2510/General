from sys import stdin

bottom = int(stdin.readline())
top = stdin.readline().split()
first = 0

for n in top:
    if n != "-1":
        first += int(n)
    else:
        bottom -= 1

print float(first) / float(bottom)
