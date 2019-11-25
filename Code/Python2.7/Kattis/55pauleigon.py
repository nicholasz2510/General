from sys import stdin

nums = [int(x) for x in stdin.readline().split()]
if (nums[1] + nums[2]) % (nums[0] * 2) < nums[0]:
    print "paul"
else:
    print "opponent"
