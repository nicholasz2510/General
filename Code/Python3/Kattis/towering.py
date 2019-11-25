from sys import stdin

inputs = [int(x) for x in stdin.readline().split()]
box_heights = inputs[:6]
tower_heights = inputs[6:]


def has_three_adding(nums, k):
    possibilities = []
    for x in range(len(nums) - 3):
        for y in range(x + 1, len(nums)):
            for z in range(y + 1, len(nums)):
                if nums[x] + nums[y] + nums[z] == k:
                    possibilities.append([nums[x], nums[y], nums[z]])
    return possibilities[0]


stack_1 = sorted(has_three_adding(box_heights, tower_heights[0]), reverse=True)
stack_2 = sorted(has_three_adding(box_heights, tower_heights[1]), reverse=True)

print(str(stack_1[0]) + " " + str(stack_1[1]) + " " + str(stack_1[2]) + " " + str(stack_2[0]) + " " + str(stack_2[1]) + " " + str(stack_2[2]))
