def is_pal(l):
    reversed = []
    max_index = (len(l) - 1)
    for x in range(max_index, -1, -1):
        reversed.append(l[x])
    for x in range(0, len(l)):
        if l[x] != reversed[x]:
            return False
    return True

print is_pal([1, 2, 4, 7])
print is_pal(['r', 'a', 'c', 'e', 'c', 'a', 'r'])
