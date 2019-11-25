from sys import stdin

name = stdin.readline()
ans = ""

pre_l = ""
for c in name:
    if c != pre_l:
        ans += c
    pre_l = c

print ans
