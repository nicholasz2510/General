from sys import stdin

nums = [float(n) for n in stdin.readline().split()]
ans = (nums[1] * 2) - nums[0]
if ans == int(ans):
    print int(ans)
    quit()
print ans
