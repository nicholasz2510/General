from sys import stdin

nums = [int(n) for n in stdin.readline().split()]

if nums[0] < nums[1]:
    if nums[1] - nums[0] == 1:
        print "Dr. Chaz will have 1 piece of chicken left over!"
    else:
        print "Dr. Chaz will have %s pieces of chicken left over!" % (str(nums[1] - nums[0]))
elif nums[0] > nums[1]:
    if nums[0] - nums[1] == 1:
        print "Dr. Chaz needs 1 more piece of chicken!"
    else:
        print "Dr. Chaz needs %s more pieces of chicken!" % (str(nums[0] - nums[1]))
