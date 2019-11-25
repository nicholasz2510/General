import sys

nums = sorted([int(n) for n in sys.stdin.readline().split()])
order = list(sys.stdin.readline())[0:3]

for l in order:
    if l == "A":
        print str(nums[0]),
    elif l == "B":
        print str(nums[1]),
    elif l == "C":
        print str(nums[2]),
