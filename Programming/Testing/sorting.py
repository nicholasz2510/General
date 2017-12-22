def swap(i1, i2, list):
    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp

def selection_sort(list):
    unsorted = 0

    while unsorted < len(list) - 1:
        min = unsorted
        for num in range(unsorted + 1, len(list)):
            if list[num] < list[min]:
                min = num

        swap(unsorted, min, list)

        unsorted += 1

    return list

def insertion_sort(list):
    new_list = []



print selection_sort([3, 2, 4, 1, 22, 343, 4534, 23423, 462543254235423, 0, -1, -3432, 1, 1, 1, 1, 1, 3])