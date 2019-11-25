from sys import stdin

nums = [int(n) for n in stdin.readline().split()]

if nums[0] + nums[1] == 0:
    print "Not a moose"
elif nums[0] == nums[1]:
    print "Even " + str(nums[0] + nums[1])
elif nums[0] > nums[1]:
    print "Odd " + str(nums[0] * 2)
elif nums[0] < nums[1]:
    print "Odd " + str(nums[1] * 2)
