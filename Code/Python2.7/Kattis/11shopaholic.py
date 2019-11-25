from sys import stdin

n_of_items = int(stdin.readline())
sorted_amounts = sorted([int(n) for n in stdin.readline().split()])
list_of_lists = []
inner_list = []

for n in range((len(sorted_amounts) / 3) - 1):
    for a in sorted_amounts:
        if len(inner_list) < 3:
            inner_list.append(a)
        elif len(inner_list) == 3:
            list_of_lists.append(inner_list)
            inner_list = []
print n_of_items
print sorted_amounts
print list_of_lists
