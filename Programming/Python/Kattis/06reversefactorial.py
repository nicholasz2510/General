import sys

factorial = int(sys.stdin.readline())
num = 2

while factorial != 1:
    factorial /= num
    num += 1

print num - 1