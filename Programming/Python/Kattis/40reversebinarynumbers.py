from sys import stdin

num = int(stdin.readline())
num_in_binary = int(bin(num)[2:])
ans_in_binary = str(num_in_binary)[::-1]
ans = int(ans_in_binary, 2)

print ans
