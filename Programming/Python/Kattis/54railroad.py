from sys import stdin

nums = [int(x) for x in stdin.readline().split()]
junctions = nums[0]
switches = nums[1]

if switches % 2 == 0:
    print "possible"
else:
    print "impossible"
