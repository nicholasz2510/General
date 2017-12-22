find_largest_list = [2, 53, 123, 122, 1, 567, 5, 8, 9, 53]
flip_list = [7, 4.5747, "fgjkj", 3.445584864568574, 78.582, 6, 21, "testing, i repeat, testing"]
check_elem_occurrence_list = [23, 5, "883002jfkd", 50.38, 848572, "null null null null null null null null", "None None None", 854378]
find_odd_positions_list = [43, "387483", 8320, 293949848.948942, 9429204.3949895, "kdkdkdkddkdkdkdkvjdjd"]
find_total_value_list = [1, 2, 3, 4, 3, 4]


def find_largest(list_to_iterate=find_largest_list):
    pre_x = 0
    for x in list_to_iterate:
        if x > pre_x:
            pre_x = x
    return pre_x

def flip(list_to_flip=flip_list):
    max_index = (len(list_to_flip) - 1)
    for x in range(max_index, -1, -1):
        list_to_flip.append(list_to_flip[x])
    for x in range(0, (max_index + 1)):
        list_to_flip.remove(list_to_flip[x])


def check_elem_occurrence(elem, list_to_check=check_elem_occurrence_list):
    for x in list_to_check:
        if x == elem:
            return True
    return False


# I assumed position meant index. If not, just += 1 to the index found.
def find_odd_positions(list_to_find=find_odd_positions_list):
    odds = []
    for x in list_to_find:
        if list_to_find.index(x) % 2 == 1:
            odds.append(x)
    return odds


def find_total_value(list_to_find=find_total_value_list):
    total = 0
    for x in list_to_find:
        total += x
    return total


print find_largest()
flip()
print flip_list
print check_elem_occurrence(50.38)
print check_elem_occurrence(678)
print find_odd_positions()
print find_total_value()
