three_list_add_to = 0
five_list_add_to = 0

three_list = []
five_list = []

solution_repeats = []
solution = []

for x in range(5):
    three_list.append(three_list_add_to)
    three_list_add_to += 3

for x in range(4):
    five_list.append(five_list_add_to)
    five_list_add_to += 5

for x in three_list:
    for y in five_list:
        solution_repeats.append(x + y)

for x in solution_repeats:
    if not solution.__contains__(x):
        solution.append(x)

# print len(solution_repeats)
print len(solution)
# print sorted(solution)
