from sys import stdin

line = stdin.readline()
ans = ""
important = False

ans += line[0]
for ch in line:
    if important:
        ans += ch
        important = False
    else:
        if ch == "-":
            important = True

print ans
