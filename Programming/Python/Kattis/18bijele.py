import sys

correct_nums = [1, 1, 2, 2, 2, 8]
his_nums = [int(x) for x in sys.stdin.readline().split()]

for x in range(6):
    print correct_nums[x] - his_nums[x],
