from sys import stdin

moves = stdin.readline()
cups = [1, 0, 0]

for m in moves:
    if m == "A":
        if cups[0] != cups[1]:
            if cups[0] == 1:
                cups[0] = 0
                cups[1] = 1
            else:
                cups[0] = 1
                cups[1] = 0
    if m == "B":
        if cups[1] != cups[2]:
            if cups[1] == 1:
                cups[1] = 0
                cups[2] = 1
            else:
                cups[1] = 1
                cups[2] = 0
    if m == "C":
        if cups[0] != cups[2]:
            if cups[0] == 1:
                cups[0] = 0
                cups[2] = 1
            else:
                cups[0] = 1
                cups[2] = 0

print cups.index(1) + 1
