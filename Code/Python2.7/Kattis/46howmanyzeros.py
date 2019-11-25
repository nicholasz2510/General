from sys import stdin

while True:
    start, stop = [int(x) for x in stdin.readline().split()]
    if start < 0:
        break
    zeros = 0
    for x in range(start, stop + 1):
        for c in str(x):
            if c == "0":
                zeros += 1
    print zeros
