twenty = []

for x in range(1, 21):
    twenty.append(x)

def on_all(l):
    nums = []
    for x in l:
        def square_nums(x):
            return x * x
        nums.append(square_nums(x))
    return nums

print on_all(twenty)
