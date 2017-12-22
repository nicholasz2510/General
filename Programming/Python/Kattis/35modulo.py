from sys import stdin

lines = []
for x in range(10):
    lines.append(int(stdin.readline()))
nums = [x % 42 for x in lines]

distinct_nums = []
ans = 0
for n in nums:
    if not n in distinct_nums:
        distinct_nums.append(n)
        ans += 1

print ans
