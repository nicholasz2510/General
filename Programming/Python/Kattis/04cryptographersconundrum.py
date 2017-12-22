import sys

ans = 0

for first_line in sys.stdin:
    for char in first_line:
        if first_line.index(char) == 0 and char != "P":
            ans += 1
            continue
        if first_line.index(char) == 1 and char != "E":
            ans += 1
            continue
        if first_line.index(char) == 2 and char != "R":
            ans += 1
            continue
        if first_line.index(char) % 3 == 0 and char != "P":
            ans += 1
            continue
        if first_line.index(char) % 3 == 1 and char != "E":
            ans += 1
            continue
        if first_line.index(char) % 3 == 2 and char != "R":
            ans += 1
            continue
    break

print ans
