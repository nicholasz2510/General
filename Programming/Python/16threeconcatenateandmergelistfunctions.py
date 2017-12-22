concatenate_list_1_1 = [1, 2, 3]
concatenate_list_1_2 = [4, 5, 6]

concatenate_list_2_1 = [6, 5, 4]
concatenate_list_2_2 = [3, 2, 1]

concatenate_list_3_1 = ["a", "b", "c"]
concatenate_list_3_2 = ["d", "e", "f"]

alternate_list_1_1 = [1, 3, 5]
alternate_list_1_2 = [2, 4, 6]

alternate_list_2_1 = [6, 4, 2]
alternate_list_2_2 = [5, 3, 1]

alternate_list_3_1 = ["a", "c", "e"]
alternate_list_3_2 = ["b", "d", "f"]

merge_list_1_1 = [1, 2, 3]
merge_list_1_2 = [1, 2, 3]

merge_list_2_1 = [1, 3, 5]
merge_list_2_2 = [2, 4, 6]

merge_list_3_1 = [5, 67, 397]
merge_list_3_2 = [54, 273, 654, 999]


def concatenate_lists(list_1, list_2):
    concatenated_list = []
    for x in list_1:
        concatenated_list.append(x)
    for x in list_2:
        concatenated_list.append(x)
    return concatenated_list


# list_1 and list_2 must be of equal length
def alternate_list(list_1, list_2):
    concatenated_list = []
    for x in range(0, len(list_1)):
        concatenated_list.append(list_1[x])
        concatenated_list.append(list_2[x])
    return concatenated_list


def merge_lists(list_1, list_2):
    merged_list = []
    while len(list_1) != 0 and len(list_2) != 0:
        if list_1[0] < list_2[0]:
            merged_list.append(list_1[0])
            list_1.pop(0)
        elif list_1[0] > list_2[0]:
            merged_list.append(list_2[0])
            list_2.pop(0)
        else:
            merged_list.append(list_1[0])
            merged_list.append(list_2[0])
            list_1.pop(0)
            list_2.pop(0)
    if len(list_1) > 0:
        for x in list_1:
            merged_list.append(x)
    elif len(list_2) > 0:
        for x in list_2:
            merged_list.append(x)
    return merged_list


print "1."
print concatenate_lists(concatenate_list_1_1, concatenate_list_1_2)
print concatenate_lists(concatenate_list_2_1, concatenate_list_2_2)
print concatenate_lists(concatenate_list_3_1, concatenate_list_3_2)
print ""
print "2."
print alternate_list(alternate_list_1_1, alternate_list_1_2)
print alternate_list(alternate_list_2_1, alternate_list_2_2)
print alternate_list(alternate_list_3_1, alternate_list_3_2)
print ""
print "3."
print merge_lists(merge_list_1_1, merge_list_1_2)
print merge_lists(merge_list_2_1, merge_list_2_2)
print merge_lists(merge_list_3_1, merge_list_3_2)
