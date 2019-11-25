from sys import stdin

a, b = [int(x) for x in stdin.readline().split()]

print (a * (b - 1)) + 1
